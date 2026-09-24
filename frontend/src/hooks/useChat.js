import { useState, useCallback, useRef } from "react";

const API_BASE = "http://localhost:8000/api";

export function useChat() {
  const [conversations, setConversations] = useState([]);
  const [currentConversation, setCurrentConversation] = useState(() => {
    try {
      const saved = localStorage.getItem("ailrac_current_conv");
      return saved ? JSON.parse(saved) : null;
    } catch {
      return null;
    }
  });
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [pendingExecution, setPendingExecution] = useState(null);
  const [isResolvingExecution, setIsResolvingExecution] = useState(false);
  const [settings, setSettings] = useState({
    blocked_domains: [],
    voice_output_enabled: false,
    voice_input_enabled: false,
    telegram_enabled: false,
    safe_search: true,
    ai_model: "gemini",
    theme_mode: "system",
    assistant_voice_profile: "default",
  });

  // Ref to current settings for use in polling callbacks without stale closure
  const settingsRef = useRef(settings);
  settingsRef.current = settings;

  // Polling interval refs
  const pollIntervalRef = useRef(null);
  const executionPollRef = useRef(null);

  // ─── VOICE POLLING ───

  const startVoicePolling = useCallback(() => {
    // Clear any existing interval
    if (pollIntervalRef.current) {
      clearInterval(pollIntervalRef.current);
    }

    pollIntervalRef.current = setInterval(async () => {
      try {
        const res = await fetch(`${API_BASE}/voice/status`);
        if (res.ok) {
          const data = await res.json();
          setIsSpeaking(data.is_speaking);
          // If done speaking, stop polling
          if (!data.is_speaking) {
            clearInterval(pollIntervalRef.current);
            pollIntervalRef.current = null;
          }
        }
      } catch {
        // backend may be momentarily unreachable; stop gracefully
        setIsSpeaking(false);
        clearInterval(pollIntervalRef.current);
        pollIntervalRef.current = null;
      }
    }, 300);
  }, []);

  const stopSpeaking = useCallback(async () => {
    try {
      await fetch(`${API_BASE}/voice/stop`, { method: "POST" });
    } catch {
      // ignore
    }
    setIsSpeaking(false);
    if (pollIntervalRef.current) {
      clearInterval(pollIntervalRef.current);
      pollIntervalRef.current = null;
    }
  }, []);

  // ─── CODE EXECUTION APPROVAL (while chat request is in flight) ───

  const stopExecutionPolling = useCallback(() => {
    if (executionPollRef.current) {
      clearInterval(executionPollRef.current);
      executionPollRef.current = null;
    }
  }, []);

  const startExecutionPolling = useCallback(() => {
    stopExecutionPolling();
    const poll = async () => {
      try {
        const res = await fetch(`${API_BASE}/execution/pending`);
        if (!res.ok) return;
        const data = await res.json();
        if (data.pending) {
          setPendingExecution(data);
        } else {
          setPendingExecution(null);
          stopExecutionPolling();
        }
      } catch {
        // backend busy or unreachable
      }
    };
    poll();
    executionPollRef.current = setInterval(poll, 700);
  }, [stopExecutionPolling]);

  const approveExecution = useCallback(async () => {
    if (!pendingExecution?.id) return;
    setIsResolvingExecution(true);
    try {
      const res = await fetch(
        `${API_BASE}/execution/${pendingExecution.id}/approve`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ confirm: "y" }),
        },
      );
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        console.error("Approve failed:", err.detail || res.status);
      }
    } catch (err) {
      console.error("Approve failed:", err);
    } finally {
      setIsResolvingExecution(false);
      setPendingExecution(null);
      stopExecutionPolling();
    }
  }, [pendingExecution, stopExecutionPolling]);

  const denyExecution = useCallback(async () => {
    if (!pendingExecution?.id) return;
    setIsResolvingExecution(true);
    try {
      await fetch(`${API_BASE}/execution/${pendingExecution.id}/deny`, {
        method: "POST",
      });
      setPendingExecution(null);
      stopExecutionPolling();
    } catch (err) {
      console.error("Deny failed:", err);
    } finally {
      setIsResolvingExecution(false);
    }
  }, [pendingExecution, stopExecutionPolling]);

  // ─── CONVERSATIONS ───

  const loadConversations = useCallback(async () => {
    try {
      const res = await fetch(`${API_BASE}/conversations`);
      if (!res.ok) return;
      setConversations(await res.json());
    } catch {
      // backend not running yet — fail silently
    }
  }, []);

  const selectConversation = useCallback(async (conv) => {
    setCurrentConversation(conv);
    try {
      localStorage.setItem("ailrac_current_conv", JSON.stringify(conv));
    } catch (e) {}
    try {
      const res = await fetch(`${API_BASE}/conversations/${conv.id}/messages`);
      if (res.ok) setMessages(await res.json());
    } catch {
      setMessages([]);
    }
  }, []);

  const newConversation = useCallback(() => {
    setCurrentConversation(null);
    try {
      localStorage.removeItem("ailrac_current_conv");
    } catch (e) {}
    setMessages([]);
  }, []);

  const deleteConversation = useCallback(
    async (convId) => {
      try {
        await fetch(`${API_BASE}/conversations/${convId}`, {
          method: "DELETE",
        });
        if (currentConversation?.id === convId) {
          setCurrentConversation(null);
          try {
            localStorage.removeItem("ailrac_current_conv");
          } catch (e) {}
          setMessages([]);
        }
        await loadConversations();
      } catch (err) {
        console.error("Delete failed:", err);
      }
    },
    [currentConversation, loadConversations],
  );

  const renameConversation = useCallback(
    async (convId, newTitle) => {
      try {
        await fetch(`${API_BASE}/conversations/${convId}`, {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ title: newTitle }),
        });
        await loadConversations();
        if (currentConversation?.id === convId) {
          setCurrentConversation((prev) => {
            const updated = { ...prev, title: newTitle };
            try {
              localStorage.setItem(
                "ailrac_current_conv",
                JSON.stringify(updated),
              );
            } catch (e) {}
            return updated;
          });
        }
      } catch (err) {
        console.error("Rename failed:", err);
      }
    },
    [currentConversation, loadConversations],
  );

  // ─── CHAT ───

  const sendMessage = useCallback(
    async (text) => {
      if (!text.trim() || isLoading) return;

      // Optimistic UI — show the user message immediately
      const optimisticId = `optimistic-${Date.now()}`;
      const optimisticMsg = {
        id: optimisticId,
        role: "user",
        content: text,
        timestamp: new Date().toISOString(),
      };
      setMessages((prev) => [...prev, optimisticMsg]);
      setIsLoading(true);
      setPendingExecution(null);
      startExecutionPolling();

      try {
        const res = await fetch(`${API_BASE}/chat`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            conversation_id: currentConversation?.id ?? null,
            message: text,
          }),
        });

        if (!res.ok) {
          const err = await res.json().catch(() => ({}));
          throw new Error(err.detail || `HTTP ${res.status}`);
        }

        const data = await res.json();

        if (data.is_new_conversation || !currentConversation) {
          setCurrentConversation(data.conversation);
          try {
            localStorage.setItem(
              "ailrac_current_conv",
              JSON.stringify(data.conversation),
            );
          } catch (e) {}
        }

        // FIX: Added safe validation filter logic before modifying array layout
        if (data.read_aloud_only) {
          setMessages((prev) =>
            [
              ...prev.filter((m) => m && m.id !== optimisticId),
              data.user_message,
            ].filter(Boolean),
          );
        } else {
          setMessages((prev) =>
            [
              ...prev.filter((m) => m && m.id !== optimisticId),
              data.user_message,
              data.assistant_message,
            ].filter(Boolean),
          );
        }

        await loadConversations();

        if (data.settings) {
          setSettings(data.settings);
          settingsRef.current = data.settings;
        }

        // Poll while backend is speaking (including auto-enabled voice)
        if (data.speak_started) {
          setTimeout(() => {
            setIsSpeaking(true);
            startVoicePolling();
          }, 400);
        }
      } catch (err) {
        console.error("Send failed:", err);
        setMessages((prev) => [
          ...prev.filter((m) => m.id !== optimisticId),
          {
            id: `error-${Date.now()}`,
            role: "assistant",
            content:
              `❌ **Could not reach Ailrac backend.**\n\n` +
              `Make sure the Python server is running:\n` +
              "```\ncd backend\npython main.py\n```",
            timestamp: new Date().toISOString(),
          },
        ]);
      } finally {
        setIsLoading(false);
        try {
          const res = await fetch(`${API_BASE}/execution/pending`);
          if (res.ok) {
            const data = await res.json();
            if (data.pending) {
              setPendingExecution(data);
              return;
            }
          }
        } catch {
          // ignore
        }
        stopExecutionPolling();
        setPendingExecution(null);
      }
    },
    [
      currentConversation,
      isLoading,
      loadConversations,
      startVoicePolling,
      startExecutionPolling,
      stopExecutionPolling,
    ],
  );

  // ─── SETTINGS ───

  const loadSettings = useCallback(async () => {
    try {
      const res = await fetch(`${API_BASE}/settings`);
      if (res.ok) {
        const loaded = await res.json();
        setSettings(loaded);
        settingsRef.current = loaded;
      }
    } catch {
      // ignore
    }
    await loadConversations();

    // Also load messages for the persisted conversation if it exists
    const savedConv = localStorage.getItem("ailrac_current_conv");
    if (savedConv) {
      try {
        const conv = JSON.parse(savedConv);
        const res = await fetch(
          `${API_BASE}/conversations/${conv.id}/messages`,
        );
        if (res.ok) setMessages(await res.json());
      } catch (err) {
        console.error("Failed to load persisted messages:", err);
      }
    }
  }, [loadConversations]);

  const saveSettings = useCallback(async (newSettings) => {
    try {
      const res = await fetch(`${API_BASE}/settings`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newSettings),
      });
      if (res.ok) {
        const saved = await res.json();
        setSettings(saved);
        settingsRef.current = saved;
      }
    } catch (err) {
      console.error("Save settings failed:", err);
    }
  }, []);

  return {
    conversations,
    currentConversation,
    messages,
    isLoading,
    isSpeaking,
    sendMessage,
    selectConversation,
    newConversation,
    deleteConversation,
    renameConversation,
    settings,
    saveSettings,
    loadSettings,
    stopSpeaking,
    pendingExecution,
    approveExecution,
    denyExecution,
    isResolvingExecution,
  };
}

import { useState, useEffect } from "react";
import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";
import MessageInput from "./components/MessageInput";
import SettingsPage from "./components/SettingsPage";
import CodeApprovalModal from "./components/CodeApprovalModal";
import { useChat } from "./hooks/useChat";

export default function App() {
  const [currentView, setCurrentView] = useState("chat"); // 'chat' or 'settings'
  const [sidebarOpen, setSidebarOpen] = useState(true);

  const {
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
  } = useChat();

  useEffect(() => {
    loadSettings();
  }, []);

  useEffect(() => {
    const mode = settings?.theme_mode ?? "system";
    const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
    const applyTheme = () => {
      const resolvedMode =
        mode === "system" ? (mediaQuery.matches ? "dark" : "light") : mode;
      document.documentElement.dataset.theme = resolvedMode;
    };

    applyTheme();
    if (mode === "system") {
      mediaQuery.addEventListener("change", applyTheme);
      return () => mediaQuery.removeEventListener("change", applyTheme);
    }
  }, [settings?.theme_mode]);

  return (
    <div className="app-container">
      {pendingExecution && (
        <CodeApprovalModal
          pending={pendingExecution}
          onApprove={approveExecution}
          onDeny={denyExecution}
          isResolving={isResolvingExecution}
        />
      )}
      <Sidebar
        conversations={conversations}
        currentConversation={currentConversation}
        currentView={currentView}
        onNewChat={() => {
          newConversation();
          setCurrentView("chat");
        }}
        onSelectConversation={(conv) => {
          selectConversation(conv);
          setCurrentView("chat");
        }}
        onDeleteConversation={deleteConversation}
        onRenameConversation={renameConversation}
        onOpenSettings={() => setCurrentView("settings")}
        isOpen={sidebarOpen}
        onToggle={() => setSidebarOpen((v) => !v)}
      />

      <main className={`main-area ${!sidebarOpen ? "sidebar-collapsed" : ""}`}>
        {currentView === "settings" ? (
          <SettingsPage
            settings={settings}
            onSave={saveSettings}
            onBack={() => setCurrentView("chat")}
          />
        ) : (
          <>
            <ChatWindow
              messages={messages}
              isLoading={isLoading}
              isSpeaking={isSpeaking}
              onStopSpeaking={stopSpeaking}
              currentConversation={currentConversation}
              onToggleSidebar={() => setSidebarOpen((v) => !v)}
              sidebarOpen={sidebarOpen}
              onSendSuggestion={sendMessage}
            />
            <MessageInput onSend={sendMessage} isLoading={isLoading} />
          </>
        )}
      </main>
    </div>
  );
}

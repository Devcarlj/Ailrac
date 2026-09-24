import { useState, useRef, useEffect } from "react";

export default function MessageInput({ onSend, isLoading }) {
  const [text, setText] = useState("");
  const [isListening, setIsListening] = useState(false);
  const textareaRef = useRef(null);
  const recognitionRef = useRef(null);

  // Auto-resize textarea as content grows
  useEffect(() => {
    const ta = textareaRef.current;
    if (ta) {
      ta.style.height = "auto";
      ta.style.height = Math.min(ta.scrollHeight, 180) + "px";
    }
  }, [text]);

  const handleSend = () => {
    const trimmed = text.trim();
    if (trimmed && !isLoading) {
      onSend(trimmed);
      setText("");
      if (textareaRef.current) textareaRef.current.style.height = "auto";
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const toggleVoice = () => {
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) {
      alert(
        "Voice input is not supported in this browser. Please use Chrome or Edge.",
      );
      return;
    }

    if (isListening) {
      recognitionRef.current?.stop();
      setIsListening(false);
      return;
    }

    const recognition = new SR();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";

    recognition.onresult = (e) => {
      const transcript = e.results[0][0].transcript;
      setText((prev) => (prev ? `${prev} ${transcript}` : transcript));
      setIsListening(false);
    };
    recognition.onerror = () => setIsListening(false);
    recognition.onend = () => setIsListening(false);

    recognitionRef.current = recognition;
    recognition.start();
    setIsListening(true);
  };

  return (
    <div className="input-area">
      <div className={`input-wrapper ${isListening ? "listening-ring" : ""}`}>
        <textarea
          ref={textareaRef}
          id="message-input"
          className="message-textarea"
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={
            isListening
              ? "Listening…"
              : "Message Ailrac…  (Enter to send, Shift+Enter for new line)"
          }
          rows={1}
          disabled={isLoading}
        />
        <div className="input-buttons">
          <button
            id="voice-btn"
            className={`icon-action-btn voice-btn ${isListening ? "listening" : ""}`}
            onClick={toggleVoice}
            title={isListening ? "Stop listening" : "Voice input"}
          >
            {isListening ? "■" : "◉"}
          </button>
          <button
            id="send-btn"
            className="icon-action-btn send-btn"
            onClick={handleSend}
            disabled={!text.trim() || isLoading}
            title="Send message"
          >
            {isLoading ? (
              <span className="spinner" />
            ) : (
              <span className="send-arrow">↑</span>
            )}
          </button>
        </div>
      </div>
      <p className="input-hint">
        Ailrac can make mistakes. Verify important information.
      </p>
    </div>
  );
}

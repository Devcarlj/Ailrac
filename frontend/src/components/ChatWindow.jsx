import { useEffect, useRef } from 'react'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism'

const SUGGESTIONS = [
  '🔍 Search for the latest AI news',
  '📺 Open YouTube for me',
  '🐍 Write a Python function to reverse a string',
  '💡 What can you help me with?',
]

function TypingIndicator() {
  return (
    <div className="message assistant">
      <div className="msg-avatar ailrac-avatar">⚡</div>
      <div className="msg-bubble ai-bubble">
        <div className="typing-indicator">
          <span /><span /><span />
        </div>
      </div>
    </div>
  )
}

function CodeBlock({ language, children }) {
  return (
    <SyntaxHighlighter
      style={oneDark}
      language={language}
      PreTag="div"
      customStyle={{ borderRadius: '8px', margin: '8px 0', fontSize: '13px' }}
    >
      {String(children).replace(/\n$/, '')}
    </SyntaxHighlighter>
  )
}

function Message({ msg }) {
  const isUser = msg.role === 'user'
  const time = new Date(msg.timestamp).toLocaleTimeString([], {
    hour: '2-digit', minute: '2-digit',
  })

  return (
    <div className={`message ${msg.role}`}>
      {!isUser && <div className="msg-avatar ailrac-avatar">⚡</div>}

      <div className="msg-body">
        <div className={`msg-bubble ${isUser ? 'user-bubble' : 'ai-bubble'}`}>
          {isUser ? (
            <p className="msg-text">{msg.content}</p>
          ) : (
            <div className="msg-text markdown">
              <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                components={{
                  code({ node, children, ...props }) {
                    const match = /language-(\w+)/.exec(props.className || '')
                    const isInline = node?.tagName === 'code' && !match
                    return !isInline && match ? (
                      <CodeBlock language={match[1]}>{children}</CodeBlock>
                    ) : (
                      <code className="inline-code" {...props}>{children}</code>
                    )
                  },
                }}
              >
                {msg.content}
              </ReactMarkdown>
            </div>
          )}
        </div>
        <span className="msg-time">{time}</span>
      </div>

      {isUser && <div className="msg-avatar user-avatar">U</div>}
    </div>
  )
}

// ─── VOICE VISUALIZER OVERLAY ───
function VoiceVisualizer({ onStop }) {
  const BARS = 28

  return (
    <div className="voice-visualizer-container" role="status" aria-label="AI is speaking">
      <div className="voice-visualizer-inner">
        {/* Glow orb behind the waveform */}
        <div className="voice-glow-orb" />

        {/* Label */}
        <div className="voice-label-row">
          <span className="voice-pulse-dot" />
          <span className="voice-label-text">Ailrac is speaking…</span>
        </div>

        {/* Waveform bars */}
        <div className="voice-waveform" aria-hidden="true">
          {Array.from({ length: BARS }).map((_, i) => (
            <div
              key={i}
              className="voice-bar"
              style={{ animationDelay: `${(i * 45) % 700}ms` }}
            />
          ))}
        </div>

        {/* Stop button */}
        <button
          id="voice-stop-btn"
          className="voice-stop-btn"
          onClick={onStop}
          aria-label="Stop AI from speaking"
        >
          <span className="voice-stop-icon">■</span>
          Stop Speaking
        </button>
      </div>
    </div>
  )
}

export default function ChatWindow({
  messages, isLoading, isSpeaking, onStopSpeaking,
  currentConversation, onToggleSidebar, sidebarOpen, onSendSuggestion,
}) {
  const bottomRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isLoading])

  return (
    <div className="chat-window">
      {/* Header */}
      <header className="chat-header">
        {!sidebarOpen && (
          <button className="icon-btn" onClick={onToggleSidebar} title="Open sidebar">
            ▶
          </button>
        )}
        <div className="chat-header-title">
          {currentConversation
            ? <h1 className="chat-title">{currentConversation.title}</h1>
            : <h1 className="chat-title">Ailrac</h1>}
        </div>
        <div className="status-badge">
          <span className="status-dot" />
          AI Online
        </div>
      </header>

      {/* Messages */}
      <div className="messages-area">
        {messages.length === 0 && !isLoading && (
          <div className="welcome-screen">
            <div className="welcome-logo">⚡</div>
            <h2 className="welcome-title">What can I help with?</h2>
            <p className="welcome-sub">
              Ask me anything — I can search the web, write code, answer questions,
              open apps, and more.
            </p>
            <div className="suggestions-grid">
              {SUGGESTIONS.map((s, i) => (
                <button
                  key={i}
                  className="suggestion-chip"
                  onClick={() => onSendSuggestion(s.replace(/^[^\s]+\s/, ''))}
                >
                  {s}
                </button>
              ))}
            </div>
          </div>
        )}

        {messages.map(msg => <Message key={msg.id} msg={msg} />)}
        {isLoading && <TypingIndicator />}
        <div ref={bottomRef} />
      </div>

      {/* Voice Visualizer Overlay */}
      {isSpeaking && <VoiceVisualizer onStop={onStopSpeaking} />}
    </div>
  )
}

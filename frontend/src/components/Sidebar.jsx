import { useState, useRef } from 'react'

function groupByDate(conversations) {
  const now = new Date()
  const startOfToday = new Date(now.getFullYear(), now.getMonth(), now.getDate())
  const startOfYesterday = new Date(startOfToday)
  startOfYesterday.setDate(startOfYesterday.getDate() - 1)
  const startOfWeek = new Date(startOfToday)
  startOfWeek.setDate(startOfWeek.getDate() - 7)

  const groups = { Today: [], Yesterday: [], 'Last 7 days': [], Older: [] }
  for (const conv of conversations) {
    const d = new Date(conv.updated_at)
    if (d >= startOfToday) groups['Today'].push(conv)
    else if (d >= startOfYesterday) groups['Yesterday'].push(conv)
    else if (d >= startOfWeek) groups['Last 7 days'].push(conv)
    else groups['Older'].push(conv)
  }
  return groups
}

function ConversationItem({ conv, isActive, onSelect, onDelete, onRename }) {
  const [menuOpen, setMenuOpen] = useState(false)
  const [isEditing, setIsEditing] = useState(false)
  const [editTitle, setEditTitle] = useState(conv.title)
  const inputRef = useRef(null)

  const openEdit = () => {
    setIsEditing(true)
    setMenuOpen(false)
    setTimeout(() => inputRef.current?.focus(), 40)
  }

  const submitEdit = () => {
    const trimmed = editTitle.trim()
    if (trimmed && trimmed !== conv.title) onRename(conv.id, trimmed)
    else setEditTitle(conv.title)
    setIsEditing(false)
  }

  return (
    <div
      className={`conv-item ${isActive ? 'active' : ''}`}
      onClick={() => !isEditing && !menuOpen && onSelect(conv)}
    >
      <span className="conv-icon">💬</span>

      {isEditing ? (
        <input
          ref={inputRef}
          className="conv-rename-input"
          value={editTitle}
          onChange={e => setEditTitle(e.target.value)}
          onBlur={submitEdit}
          onKeyDown={e => {
            if (e.key === 'Enter') submitEdit()
            if (e.key === 'Escape') { setEditTitle(conv.title); setIsEditing(false) }
          }}
          onClick={e => e.stopPropagation()}
        />
      ) : (
        <span className="conv-title">{conv.title}</span>
      )}

      <div className="conv-actions" onClick={e => e.stopPropagation()}>
        <button
          className="conv-menu-btn"
          onClick={() => setMenuOpen(v => !v)}
          title="Options"
        >
          ···
        </button>
        {menuOpen && (
          <>
            <div className="conv-menu-backdrop" onClick={() => setMenuOpen(false)} />
            <div className="conv-menu">
              <button onClick={openEdit}>✏️ Rename</button>
              <button
                className="danger"
                onClick={() => { setMenuOpen(false); onDelete(conv.id) }}
              >
                🗑️ Delete
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  )
}

export default function Sidebar({
  conversations, currentConversation, currentView,
  onNewChat, onSelectConversation, onDeleteConversation, onRenameConversation,
  onOpenSettings, isOpen, onToggle,
}) {
  const groups = groupByDate(conversations)

  return (
    <aside className={`sidebar ${isOpen ? 'open' : 'closed'}`}>
      {/* Header */}
      <div className="sidebar-header">
        <div className="logo">
          <span className="logo-icon">⚡</span>
          {isOpen && <span className="logo-text">Ailrac</span>}
        </div>
        <button className="icon-btn" onClick={onToggle} title="Toggle sidebar">
          {isOpen ? '◀' : '▶'}
        </button>
      </div>

      {isOpen && (
        <>
          {/* New Chat */}
          <button className="new-chat-btn" id="new-chat-btn" onClick={onNewChat}>
            <span className="new-chat-plus">✦</span>
            New Chat
          </button>

          {/* Conversation list */}
          <nav className="conv-list">
            {conversations.length === 0 ? (
              <div className="conv-empty">
                <span>💬</span>
                <p>No conversations yet.</p>
                <p>Start a new chat!</p>
              </div>
            ) : (
              Object.entries(groups)
                .filter(([, items]) => items.length > 0)
                .map(([label, items]) => (
                  <div key={label} className="conv-group">
                    <span className="conv-group-label">{label}</span>
                    {items.map(conv => (
                      <ConversationItem
                        key={conv.id}
                        conv={conv}
                        isActive={currentView === 'chat' && currentConversation?.id === conv.id}
                        onSelect={onSelectConversation}
                        onDelete={onDeleteConversation}
                        onRename={onRenameConversation}
                      />
                    ))}
                  </div>
                ))
            )}
          </nav>

          {/* Footer */}
          <div className="sidebar-footer">
            <button
              className={`settings-btn ${currentView === 'settings' ? 'active' : ''}`}
              id="settings-btn"
              onClick={onOpenSettings}
            >
              <span>⚙️</span>
              <span>Settings</span>
            </button>
          </div>
        </>
      )}
    </aside>
  )
}


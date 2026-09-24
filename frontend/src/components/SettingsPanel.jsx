import { useState, useEffect, useCallback } from 'react'

const API_BASE = 'http://localhost:8000/api'

const MODE_OPTIONS = [
  {
    value: 'search',
    label: 'Search Mode (Web Enabled, Local OS Automation Fully Locked)',
    icon: '🔍',
    accent: 'mode-accent-search',
  },
  {
    value: 'control',
    label: 'Control Mode (Local OS Access Enabled, Web Access Fully Blocked)',
    icon: '🎮',
    accent: 'mode-accent-control',
  },
]

function ModeToggle({ id, checked, onChange, label, description, accentClass }) {
  return (
    <div className={`mode-kill-switch-row ${accentClass}`}>
      <div className="mode-kill-switch-info">
        <span className="mode-kill-switch-label">{label}</span>
        <span className="mode-kill-switch-desc">{description}</span>
      </div>
      <label className="toggle-switch" htmlFor={id} aria-label={label}>
        <input
          id={id}
          type="checkbox"
          checked={checked}
          onChange={e => onChange(e.target.checked)}
        />
        <span className="toggle-track">
          <span className="toggle-thumb" />
        </span>
      </label>
    </div>
  )
}

export default function SettingsPanel({
  searchModeEnabled = true,
  controlModeEnabled = true,
  onToggleSearchMode,
  onToggleControlMode,
}) {
  const [currentMode, setCurrentMode] = useState('search')
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState(null)
  const [savedFlash, setSavedFlash] = useState(false)

  const loadMode = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const res = await fetch(`${API_BASE}/settings/mode`)
      if (!res.ok) throw new Error(`Failed to load mode (${res.status})`)
      const data = await res.json()
      setCurrentMode(data.current_mode ?? 'search')
    } catch (err) {
      setError(err.message || 'Could not load execution mode')
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    loadMode()
    const interval = setInterval(loadMode, 5000)
    return () => clearInterval(interval)
  }, [loadMode])

  const saveMode = async (mode) => {
    if (mode === currentMode || saving) return
    setSaving(true)
    setError(null)
    try {
      const res = await fetch(`${API_BASE}/settings/mode`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode }),
      })
      if (!res.ok) {
        const body = await res.json().catch(() => ({}))
        throw new Error(body.detail || `Failed to save mode (${res.status})`)
      }
      const data = await res.json()
      setCurrentMode(data.current_mode ?? mode)
      setSavedFlash(true)
      setTimeout(() => setSavedFlash(false), 1500)
    } catch (err) {
      setError(err.message || 'Could not update execution mode')
    } finally {
      setSaving(false)
    }
  }

  return (
    <section className="settings-card tab-content mode-panel" aria-labelledby="execution-mode-heading">
      <h3 id="execution-mode-heading">🛡️ Dual-Mode Execution</h3>
      <p className="settings-desc">
        Switch how Ailrac routes every request. All intents go through the LLM — mode only
        controls which tools are structurally available.
      </p>

      {loading && <p className="mode-status-line">Loading runtime mode…</p>}
      {error && <p className="mode-error" role="alert">{error}</p>}
      {savedFlash && <p className="mode-saved-flash">✓ Mode applied to runtime engine</p>}

      <div className="mode-selector" role="radiogroup" aria-label="Execution mode">
        {MODE_OPTIONS.map((opt) => {
          const selected = currentMode === opt.value
          return (
            <button
              key={opt.value}
              type="button"
              role="radio"
              aria-checked={selected}
              disabled={loading || saving}
              className={`mode-option ${opt.accent} ${selected ? 'selected' : ''}`}
              onClick={() => saveMode(opt.value)}
            >
              <span className="mode-option-icon">{opt.icon}</span>
              <span className="mode-option-body">
                <span className="mode-option-title">{opt.label}</span>
              </span>
              <span className={`mode-radio ${selected ? 'mode-radio-on' : ''}`} />
            </button>
          )
        })}
      </div>

      <div className="mode-boundary-legend">
        {MODE_OPTIONS.map((opt) => (
          <div
            key={opt.value}
            className={`mode-boundary-row mode-boundary-${opt.value}`}
          >
            <strong>{opt.label}</strong>
          </div>
        ))}
      </div>

      <p className="mode-telegram-hint">
        Telegram: <code>/search</code> · <code>/control</code> or use the persistent keyboard buttons.
        Changes sync with this dashboard within a few seconds.
      </p>

      {/* ── Mode Kill-Switches ────────────────────────────────────────────── */}
      <div className="mode-kill-switches">
        <h4 className="mode-kill-switches-heading">🔐 Mode Access Control</h4>
        <p className="settings-desc mode-kill-desc">
          Independently enable or disable each mode. A disabled mode refuses all requests
          regardless of the active mode switch above — useful for locking Ailrac to a
          single capability surface.
        </p>

        <ModeToggle
          id="search-mode-enabled-toggle"
          checked={searchModeEnabled}
          onChange={onToggleSearchMode}
          label="🔍 Search Mode Enabled"
          description={
            searchModeEnabled
              ? 'Web search & content summarization are active. Disable to block all web access.'
              : '⚠️ Disabled — Ailrac will refuse all web search and summarization requests.'
          }
          accentClass="mode-kill-search"
        />

        <div className="divider" />

        <ModeToggle
          id="control-mode-enabled-toggle"
          checked={controlModeEnabled}
          onChange={onToggleControlMode}
          label="🎮 Control Mode Enabled"
          description={
            controlModeEnabled
              ? 'Local OS automation (apps, mouse, scripts) is active. Disable to block all system access.'
              : '⚠️ Disabled — Ailrac will refuse all local OS automation and script execution.'
          }
          accentClass="mode-kill-control"
        />
      </div>
    </section>
  )
}

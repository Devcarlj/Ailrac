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

export default function SettingsPanel() {
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
    </section>
  )
}

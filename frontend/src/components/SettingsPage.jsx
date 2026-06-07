import { useState, useEffect } from 'react'
import SettingsPanel from './SettingsPanel'

const QUICK_BLOCKS = ['facebook.com', 'instagram.com', 'twitter.com', 'tiktok.com']

const MODEL_OPTIONS = [
  {
    id: 'gemini',
    icon: '☁️',
    name: 'Gemini 2.5 Flash',
    badge: 'Cloud',
    badgeClass: 'badge-cloud',
    description: 'Google\'s latest cloud model. Full tool-calling support — can open browser, run commands, and execute Python on your laptop.',
    pros: ['Tool use (browser, shell, Python)', 'Best reasoning & accuracy', 'Always up-to-date'],
    cons: ['Requires internet + API key', 'Data leaves your device'],
  },
  {
    id: 'gemma4',
    icon: '💎',
    name: 'Gemma 4 26B',
    badge: 'Cloud · Gemma',
    badgeClass: 'badge-cloud',
    description: 'Google\'s open Gemma 4 26B MoE model via the Gemini API (same API key). Fast native Google Search grounding for live news, weather, and scores.',
    pros: ['Native Google Search grounding', '256K context window', 'Tool use (browser, shell, Python)'],
    cons: ['Requires internet + API key', 'Data processed in the cloud'],
  },
  {
    id: 'ollama',
    icon: '🖥️',
    name: 'Qwen 2.5 Coder 7B',
    badge: 'Local · Ollama',
    badgeClass: 'badge-local',
    description: 'Runs 100% on your machine via Ollama. No internet needed, fully private. Optimized for coding tasks.',
    pros: ['100% private — data stays local', 'Works offline', 'Great for code tasks'],
    cons: ['No tool-calling (browser/shell)', 'Requires Ollama running locally'],
  },
]

const VOICE_PROFILE_OPTIONS = [
  {
    id: 'default',
    icon: '🔊',
    name: 'Default System Voice',
    description: 'Windows SAPI / pyttsx3 — the built-in assistant voice.',
  },
  {
    id: 'jarvis',
    icon: '🤖',
    name: 'J.A.R.V.I.S. (Local Engine)',
    description: 'Local Piper neural voice using jarvis-medium.onnx on this machine.',
  },
]

function Toggle({ id, checked, onChange, label, description }) {
  return (
    <div className="toggle-row">
      <div className="toggle-info">
        <span className="toggle-label">{label}</span>
        <span className="toggle-desc">{description}</span>
      </div>
      <label className="toggle-switch" htmlFor={id}>
        <input id={id} type="checkbox" checked={checked} onChange={e => onChange(e.target.checked)} />
        <span className="toggle-track">
          <span className="toggle-thumb" />
        </span>
      </label>
    </div>
  )
}

export default function SettingsPage({ settings, onSave, onBack }) {
  const [blockedDomains, setBlockedDomains] = useState([])
  const [newDomain, setNewDomain]           = useState('')
  const [voiceOutput, setVoiceOutput]       = useState(false)
  const [voiceInput, setVoiceInput]         = useState(false)
  const [telegram, setTelegram]             = useState(false)
  const [safeSearch, setSafeSearch]         = useState(true)
  const [aiModel, setAiModel]               = useState('gemini')
  const [assistantVoiceProfile, setAssistantVoiceProfile] = useState('default')
  const [saved, setSaved]                   = useState(false)
  const [activeTab, setActiveTab]           = useState('execution')

  useEffect(() => {
    if (settings) {
      setBlockedDomains(settings.blocked_domains ?? [])
      setVoiceOutput(settings.voice_output_enabled ?? false)
      setVoiceInput(settings.voice_input_enabled ?? false)
      setTelegram(settings.telegram_enabled ?? false)
      setSafeSearch(settings.safe_search !== false)
      setAiModel(settings.ai_model ?? 'gemini')
      setAssistantVoiceProfile(settings.assistant_voice_profile ?? 'default')
    }
  }, [settings])

  const updateSetting = async (key, val) => {
    setSaved(true)
    const newSettings = {
      blocked_domains:      key === 'blocked_domains'      ? val : blockedDomains,
      voice_output_enabled: key === 'voice_output_enabled' ? val : voiceOutput,
      voice_input_enabled:  key === 'voice_input_enabled'  ? val : voiceInput,
      telegram_enabled:     key === 'telegram_enabled'     ? val : telegram,
      safe_search:          key === 'safe_search'          ? val : safeSearch,
      ai_model:             key === 'ai_model'             ? val : aiModel,
      assistant_voice_profile:
        key === 'assistant_voice_profile' ? val : assistantVoiceProfile,
    }

    if (key === 'blocked_domains')      setBlockedDomains(val)
    if (key === 'voice_output_enabled') setVoiceOutput(val)
    if (key === 'voice_input_enabled')  setVoiceInput(val)
    if (key === 'telegram_enabled')     setTelegram(val)
    if (key === 'safe_search')          setSafeSearch(val)
    if (key === 'ai_model')             setAiModel(val)
    if (key === 'assistant_voice_profile') setAssistantVoiceProfile(val)

    await onSave(newSettings)
    setTimeout(() => setSaved(false), 1000)
  }

  const addDomain = () => {
    let d = newDomain.trim().toLowerCase()
    if (!d) return
    if (!d.includes('.')) d += '.com'
    if (!blockedDomains.includes(d)) {
      const updated = [...blockedDomains, d]
      updateSetting('blocked_domains', updated)
    }
    setNewDomain('')
  }

  const removeDomain = (d) => {
    const updated = blockedDomains.filter(x => x !== d)
    updateSetting('blocked_domains', updated)
  }

  const quickToggle = (domain) => {
    if (blockedDomains.includes(domain)) {
      removeDomain(domain)
    } else {
      const updated = [...blockedDomains, domain]
      updateSetting('blocked_domains', updated)
    }
  }

  return (
    <div className="settings-page">
      {/* ── Header ── */}
      <div className="settings-header">
        <div className="settings-header-left">
          <button className="back-btn" onClick={onBack} aria-label="Back to chat">
            ← Back to Chat
          </button>
          <h2>⚙️ Settings</h2>
        </div>
        <button
          className="btn-primary saved"
          id="save-settings-btn"
          disabled
          style={{ opacity: 0.85, cursor: 'default' }}
        >
          {saved ? '⚡ Saving...' : '✓ Auto-saved'}
        </button>
      </div>

      {/* ── Settings Content Container ── */}
      <div className="settings-container">
        {/* ── Tabs (Sidebar inside Settings) ── */}
        <aside className="settings-sidebar">
          <button
            className={`settings-tab-btn ${activeTab === 'execution' ? 'active' : ''}`}
            onClick={() => setActiveTab('execution')}
            id="tab-execution"
          >
            🛡️ Execution Mode
          </button>
          <button
            className={`settings-tab-btn ${activeTab === 'model' ? 'active' : ''}`}
            onClick={() => setActiveTab('model')}
            id="tab-model"
          >
            🤖 AI Model
          </button>
          <button
            className={`settings-tab-btn ${activeTab === 'security' ? 'active' : ''}`}
            onClick={() => setActiveTab('security')}
            id="tab-security"
          >
            🔒 Security &amp; Blocking
          </button>
          <button
            className={`settings-tab-btn ${activeTab === 'features' ? 'active' : ''}`}
            onClick={() => setActiveTab('features')}
            id="tab-features"
          >
            🎛️ Input &amp; Output Channels
          </button>
        </aside>

        {/* ── Body ── */}
        <main className="settings-body-content">

          {activeTab === 'execution' && <SettingsPanel />}

          {/* AI MODEL TAB */}
          {activeTab === 'model' && (
            <div className="settings-card tab-content">
              <h3>🤖 AI Model</h3>
              <p className="settings-desc">
                Choose which AI powers Ailrac. Switch anytime — the change takes effect on the next message.
              </p>

              <div className="model-picker">
                {MODEL_OPTIONS.map(opt => (
                  <button
                    key={opt.id}
                    id={`model-card-${opt.id}`}
                    className={`model-card ${aiModel === opt.id ? 'selected' : ''}`}
                    onClick={() => updateSetting('ai_model', opt.id)}
                  >
                    {/* Selection indicator */}
                    <span className={`model-radio ${aiModel === opt.id ? 'model-radio-on' : ''}`} />

                    <div className="model-card-header">
                      <span className="model-icon">{opt.icon}</span>
                      <div className="model-card-title-group">
                        <span className="model-name">{opt.name}</span>
                        <span className={`model-badge ${opt.badgeClass}`}>{opt.badge}</span>
                      </div>
                    </div>

                    <p className="model-description">{opt.description}</p>

                    <div className="model-pros-cons">
                      <ul className="model-pros">
                        {opt.pros.map(p => <li key={p}>✓ {p}</li>)}
                      </ul>
                      <ul className="model-cons">
                        {opt.cons.map(c => <li key={c}>✗ {c}</li>)}
                      </ul>
                    </div>

                    {aiModel === opt.id && (
                      <div className="model-active-banner">✓ Active</div>
                    )}
                  </button>
                ))}
              </div>

              {aiModel === 'ollama' && (
                <div className="ollama-notice">
                  <strong>🖥️ Ollama Setup Required</strong>
                  <p>Make sure Ollama is running and the model is downloaded:</p>
                  <pre className="ollama-code">ollama serve{'\n'}ollama pull qwen2.5-coder:7b</pre>
                  <p className="ollama-hint">Ollama default URL: <code>http://localhost:11434</code></p>
                </div>
              )}
            </div>
          )}

          {/* SECURITY TAB */}
          {activeTab === 'security' && (
            <div className="settings-card tab-content">
              <h3>🔒 Security &amp; Blocking</h3>
              <p className="settings-desc">
                Ailrac will <strong>refuse</strong> to open, access, or interact with any blocked platform — even if you ask it to.
              </p>

              {/* Quick-block chips */}
              <div className="quick-block-row">
                <span className="quick-block-label">Quick block:</span>
                <div className="quick-chips">
                  {QUICK_BLOCKS.map(d => (
                    <button
                      key={d}
                      className={`quick-chip ${blockedDomains.includes(d) ? 'blocked' : ''}`}
                      onClick={() => quickToggle(d)}
                      title={blockedDomains.includes(d) ? `Unblock ${d}` : `Block ${d}`}
                    >
                      {blockedDomains.includes(d) ? '🚫' : '＋'} {d}
                    </button>
                  ))}
                </div>
              </div>

              {/* Custom domain input */}
              <div className="domain-input-row">
                <input
                  id="domain-input"
                  type="text"
                  className="domain-input"
                  placeholder="e.g. snapchat.com"
                  value={newDomain}
                  onChange={e => setNewDomain(e.target.value)}
                  onKeyDown={e => e.key === 'Enter' && addDomain()}
                />
                <button className="add-domain-btn" id="add-domain-btn" onClick={addDomain}>
                  + Block
                </button>
              </div>

              {/* Active blocks */}
              <div className="domain-tags">
                {blockedDomains.length === 0
                  ? <span className="no-tags">No platforms blocked yet.</span>
                  : blockedDomains.map(d => (
                    <div key={d} className="domain-tag">
                      🚫 {d}
                      <button onClick={() => removeDomain(d)} title={`Remove ${d}`}>✕</button>
                    </div>
                  ))
                }
              </div>

              <div className="divider" />

              <Toggle
                id="safe-search-toggle"
                checked={safeSearch}
                onChange={(val) => updateSetting('safe_search', val)}
                label="🔍 Safe Search"
                description="Force SafeSearch on all Google searches opened by Ailrac"
              />
            </div>
          )}

          {/* FEATURES TAB */}
          {activeTab === 'features' && (
            <div className="settings-card tab-content">
              <h3>🎛️ Input &amp; Output Channels</h3>
              <p className="settings-desc">
                Control which Ailrac input/output channels are active. Changes take effect after restarting the Python backend.
              </p>
              <div className="toggle-list">
                <Toggle
                  id="voice-output-toggle"
                  checked={voiceOutput}
                  onChange={(val) => updateSetting('voice_output_enabled', val)}
                  label="🔊 Voice Output"
                  description="Ailrac speaks its responses aloud using text-to-speech"
                />
                <div className="divider" />
                <h4 className="settings-subheading">Assistant Voice Profile</h4>
                <p className="settings-desc voice-profile-desc">
                  Choose which voice reads assistant responses when voice output is enabled.
                </p>
                <div className="model-picker voice-profile-picker">
                  {VOICE_PROFILE_OPTIONS.map(opt => (
                    <button
                      key={opt.id}
                      id={`voice-profile-${opt.id}`}
                      type="button"
                      className={`model-card ${assistantVoiceProfile === opt.id ? 'selected' : ''}`}
                      onClick={() => updateSetting('assistant_voice_profile', opt.id)}
                    >
                      <span
                        className={`model-radio ${assistantVoiceProfile === opt.id ? 'model-radio-on' : ''}`}
                      />
                      <div className="model-card-header">
                        <span className="model-icon">{opt.icon}</span>
                        <div className="model-card-title-group">
                          <span className="model-name">{opt.name}</span>
                        </div>
                      </div>
                      <p className="model-description">{opt.description}</p>
                      {assistantVoiceProfile === opt.id && (
                        <div className="model-active-banner">✓ Active</div>
                      )}
                    </button>
                  ))}
                </div>
                <div className="divider" />
                <Toggle
                  id="voice-input-toggle"
                  checked={voiceInput}
                  onChange={(val) => updateSetting('voice_input_enabled', val)}
                  label="🎙️ Voice Input (Microphone)"
                  description="Enable continuous microphone listening mode on the backend"
                />
                <div className="divider" />
                <Toggle
                  id="telegram-toggle"
                  checked={telegram}
                  onChange={(val) => updateSetting('telegram_enabled', val)}
                  label="📱 Telegram Gateway"
                  description="Control Ailrac via your personal Telegram bot"
                />
              </div>
            </div>
          )}
        </main>
      </div>
    </div>
  )
}

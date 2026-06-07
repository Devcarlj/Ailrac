import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism'

export default function CodeApprovalModal({
  pending,
  onApprove,
  onDeny,
  isResolving,
}) {
  if (!pending?.code) return null

  return (
    <div className="code-approval-overlay" role="dialog" aria-modal="true" aria-labelledby="code-approval-title">
      <div className="code-approval-modal">
        <div className="code-approval-header">
          <span className="code-approval-icon" aria-hidden="true">🛡️</span>
          <div>
            <h2 id="code-approval-title">Code execution approval required</h2>
            <p className="code-approval-subtitle">
              Ailrac wants to run Python on your machine. Review the script below. Only approve if you trust this action.
            </p>
          </div>
        </div>

        <div className="code-approval-code-wrap">
          <SyntaxHighlighter
            language="python"
            style={oneDark}
            customStyle={{
              margin: 0,
              borderRadius: '10px',
              fontSize: '13px',
              maxHeight: '280px',
            }}
          >
            {pending.code}
          </SyntaxHighlighter>
        </div>

        <p className="code-approval-hint">
          Dangerous patterns (file deletion, <code>os</code>, <code>subprocess</code>, reading <code>.env</code>) are blocked automatically.
        </p>

        <div className="code-approval-actions">
          <button
            type="button"
            className="code-approval-btn deny"
            onClick={onDeny}
            disabled={isResolving}
          >
            Deny
          </button>
          <button
            type="button"
            className="code-approval-btn approve"
            onClick={onApprove}
            disabled={isResolving}
          >
            {isResolving ? 'Running…' : 'Approve & run'}
          </button>
        </div>
      </div>
    </div>
  )
}

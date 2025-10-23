export default function JsonViewer({ data }) {
  return (
    <div className="relative">
      <div className="absolute top-4 right-4">
        <button
          onClick={() => {
            navigator.clipboard.writeText(JSON.stringify(data, null, 2))
          }}
          className="px-3 py-1.5 bg-gray-100 hover:bg-gray-200 text-gray-700 text-sm font-medium rounded-lg transition-colors flex items-center space-x-2"
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
          </svg>
          <span>Copy</span>
        </button>
      </div>
      <pre className="bg-gradient-to-br from-gray-50 to-gray-100 p-6 rounded-xl overflow-x-auto border border-gray-200 text-sm leading-relaxed font-mono">
        {JSON.stringify(data || {}, null, 2)}
      </pre>
    </div>
  )
}

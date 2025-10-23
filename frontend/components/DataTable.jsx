export default function DataTable({ rows }) {
  if (!rows || !rows.length) return (
    <div className="text-center py-8 text-gray-500">
      No data to display
    </div>
  )
  
  const keys = Object.keys(rows[0]).filter(k => k !== 'notes' && k !== 'summary')
  
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gradient-to-r from-blue-50 to-indigo-50">
          <tr>
            {keys.map(k => (
              <th
                key={k}
                className="px-6 py-4 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider"
              >
                {k.replace(/_/g, ' ')}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {rows.map((r, i) => (
            <tr key={i} className="hover:bg-gray-50 transition-colors">
              {keys.map(k => (
                <td key={k} className="px-6 py-4 text-sm text-gray-900">
                  {k === 'confidence' ? (
                    <div className="flex items-center space-x-2">
                      <div className="w-24 h-2 bg-gray-200 rounded-full overflow-hidden">
                        <div
                          className={`h-full rounded-full ${
                            r[k] >= 0.8 ? 'bg-green-500' : 
                            r[k] >= 0.5 ? 'bg-yellow-500' : 'bg-red-500'
                          }`}
                          style={{ width: `${(r[k] || 0) * 100}%` }}
                        />
                      </div>
                      <span className="font-medium">{Math.round((r[k] || 0) * 100)}%</span>
                    </div>
                  ) : (
                    <span className={k === 'bank' ? 'font-semibold text-blue-600' : ''}>
                      {String(r[k] ?? '—')}
                    </span>
                  )}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

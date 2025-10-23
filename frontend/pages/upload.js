import { useState } from 'react'
import axios from 'axios'
import Link from 'next/link'
import FileUploader from '../components/FileUploader'
import DataTable from '../components/DataTable'
import JsonViewer from '../components/JsonViewer'
import Loader from '../components/Loader'
import Notification from '../components/Notification'

export default function Upload() {
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [viewMode, setViewMode] = useState('json') // 'json' or 'table'

  const handleFile = async (file) => {
    setLoading(true)
    setError(null)
    setResult(null)
    
    const form = new FormData()
    form.append('file', file)
    form.append('as_excel', 'false')
    
    try {
      const resp = await axios.post('http://localhost:8000/extract', form, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      setResult(resp.data)
    } catch (e) {
      setError(e.response?.data?.detail || e.message || 'Upload failed')
    } finally {
      setLoading(false)
    }
  }

  const downloadExcel = async () => {
    if (!result) return
    
    try {
      const form = new FormData()
      const file = document.querySelector('input[type="file"]').files[0]
      if (!file) return
      
      form.append('file', file)
      form.append('as_excel', 'true')
      
      const resp = await axios.post('http://localhost:8000/extract', form, {
        headers: { 'Content-Type': 'multipart/form-data' },
        responseType: 'blob'
      })
      
      const url = window.URL.createObjectURL(new Blob([resp.data]))
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', `extraction_${Date.now()}.xlsx`)
      document.body.appendChild(link)
      link.click()
      link.remove()
    } catch (e) {
      setError('Excel download failed')
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-50">
      {/* Navigation */}
      <nav className="bg-white/80 backdrop-blur-md border-b border-gray-200 shadow-sm sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <Link href="/" className="flex items-center space-x-2">
              <div className="w-10 h-10 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-lg flex items-center justify-center">
                <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
              <span className="text-xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
                Sure Financial
              </span>
            </Link>
            <Link href="/" className="text-gray-600 hover:text-blue-600 transition-colors font-medium">
              ← Back to Home
            </Link>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="space-y-8">
          {/* Header */}
          <div className="text-center space-y-4 animate-fade-in">
            <h1 className="text-4xl md:text-5xl font-extrabold text-gray-900">
              Upload Your Statement
            </h1>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto">
              Upload a PDF credit card statement and let our AI extract key information automatically
            </p>
          </div>

          {/* Upload Section */}
          <div className="card animate-slide-up">
            <FileUploader onFile={handleFile} loading={loading} />
          </div>

          {/* Loading State */}
          {loading && (
            <div className="card text-center py-12 animate-fade-in">
              <Loader />
              <p className="mt-4 text-gray-600 font-medium">Processing your statement...</p>
              <p className="text-sm text-gray-500 mt-2">This may take a few seconds</p>
            </div>
          )}

          {/* Error State */}
          {error && (
            <div className="bg-red-50 border border-red-200 rounded-xl p-6 animate-fade-in">
              <div className="flex items-start space-x-3">
                <svg className="w-6 h-6 text-red-600 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                </svg>
                <div>
                  <h3 className="font-semibold text-red-900">Error</h3>
                  <p className="text-red-700 mt-1">{error}</p>
                </div>
              </div>
            </div>
          )}

          {/* Results Section */}
          {result && (
            <div className="space-y-6 animate-fade-in">
              {/* Summary Card */}
              <div className="card bg-gradient-to-br from-blue-50 to-indigo-50 border-blue-200">
                <div className="flex items-start justify-between">
                  <div className="space-y-3 flex-1">
                    <h2 className="text-2xl font-bold text-gray-900">Extraction Complete!</h2>
                    {result.summary && (
                      <p className="text-gray-700 text-lg">{result.summary}</p>
                    )}
                    <div className="flex items-center space-x-2">
                      <span className="text-sm font-medium text-gray-600">Confidence Score:</span>
                      <div className="flex items-center space-x-2">
                        <div className="w-32 h-2 bg-gray-200 rounded-full overflow-hidden">
                          <div
                            className={`h-full rounded-full ${
                              result.confidence >= 0.8 ? 'bg-green-500' : 
                              result.confidence >= 0.5 ? 'bg-yellow-500' : 'bg-red-500'
                            }`}
                            style={{ width: `${(result.confidence || 0) * 100}%` }}
                          />
                        </div>
                        <span className="text-sm font-semibold">{Math.round((result.confidence || 0) * 100)}%</span>
                      </div>
                    </div>
                  </div>
                  <div className="flex-shrink-0">
                    <button onClick={downloadExcel} className="btn-primary">
                      <span className="flex items-center space-x-2">
                        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                        </svg>
                        <span>Download Excel</span>
                      </span>
                    </button>
                  </div>
                </div>
              </div>

              {/* View Toggle */}
              <div className="flex justify-center">
                <div className="inline-flex rounded-lg bg-white shadow-md p-1 border border-gray-200">
                  <button
                    onClick={() => setViewMode('json')}
                    className={`px-6 py-2 rounded-md font-medium transition-all ${
                      viewMode === 'json'
                        ? 'bg-blue-600 text-white shadow-sm'
                        : 'text-gray-600 hover:text-gray-900'
                    }`}
                  >
                    JSON View
                  </button>
                  <button
                    onClick={() => setViewMode('table')}
                    className={`px-6 py-2 rounded-md font-medium transition-all ${
                      viewMode === 'table'
                        ? 'bg-blue-600 text-white shadow-sm'
                        : 'text-gray-600 hover:text-gray-900'
                    }`}
                  >
                    Table View
                  </button>
                </div>
              </div>

              {/* Data Display */}
              <div className="card">
                {viewMode === 'json' ? (
                  <JsonViewer data={result} />
                ) : (
                  <DataTable rows={[result]} />
                )}
              </div>

              {/* Notes/Warnings */}
              {result.notes && result.notes.length > 0 && (
                <div className="bg-yellow-50 border border-yellow-200 rounded-xl p-6">
                  <div className="flex items-start space-x-3">
                    <svg className="w-6 h-6 text-yellow-600 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                    </svg>
                    <div>
                      <h3 className="font-semibold text-yellow-900">Notes</h3>
                      <ul className="mt-2 space-y-1">
                        {result.notes.map((note, i) => (
                          <li key={i} className="text-yellow-700 text-sm">{note}</li>
                        ))}
                      </ul>
                    </div>
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      </main>
    </div>
  )
}

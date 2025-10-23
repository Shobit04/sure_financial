import { useRef, useState } from 'react'

export default function FileUploader({ onFile, loading }) {
  const ref = useRef()
  const [isDragging, setIsDragging] = useState(false)
  const [selectedFile, setSelectedFile] = useState(null)

  const handleDrop = (e) => {
    e.preventDefault()
    setIsDragging(false)
    const file = e.dataTransfer.files[0]
    if (file && file.type === 'application/pdf') {
      setSelectedFile(file)
      onFile(file)
    }
  }

  const handleChange = (e) => {
    const file = e.target.files[0]
    if (file) {
      setSelectedFile(file)
      onFile(file)
    }
  }

  const handleDragOver = (e) => {
    e.preventDefault()
    setIsDragging(true)
  }

  const handleDragLeave = () => {
    setIsDragging(false)
  }

  return (
    <div className="space-y-4">
      <div
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        className={`relative border-2 border-dashed rounded-2xl p-12 text-center transition-all duration-300 ${
          isDragging
            ? 'border-blue-500 bg-blue-50 scale-105'
            : loading
            ? 'border-gray-300 bg-gray-50 opacity-50 cursor-not-allowed'
            : 'border-gray-300 hover:border-blue-400 hover:bg-blue-50/50 cursor-pointer'
        }`}
        onClick={() => !loading && ref.current?.click()}
      >
        <input
          ref={ref}
          type="file"
          accept="application/pdf"
          onChange={handleChange}
          className="hidden"
          disabled={loading}
        />
        
        <div className="space-y-4">
          {/* Upload Icon */}
          <div className="mx-auto w-20 h-20 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-full flex items-center justify-center">
            <svg
              className="w-10 h-10 text-white"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
              />
            </svg>
          </div>

          {/* Text */}
          <div>
            <p className="text-xl font-semibold text-gray-900">
              {isDragging ? 'Drop your file here' : 'Drop PDF file here'}
            </p>
            <p className="text-gray-500 mt-2">or click to browse</p>
          </div>

          {/* File Info */}
          {selectedFile && (
            <div className="inline-flex items-center space-x-2 bg-blue-100 text-blue-700 px-4 py-2 rounded-lg mt-4">
              <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clipRule="evenodd" />
              </svg>
              <span className="font-medium text-sm">{selectedFile.name}</span>
              <span className="text-xs opacity-75">
                ({(selectedFile.size / 1024 / 1024).toFixed(2)} MB)
              </span>
            </div>
          )}

          {/* Supported formats */}
          <p className="text-xs text-gray-400 mt-4">
            Supports: HDFC, ICICI, IDBI, SBI Card, Kotak Mahindra
          </p>
        </div>
      </div>

      {/* Instructions */}
      <div className="grid md:grid-cols-3 gap-4 text-sm">
        <div className="flex items-start space-x-3 p-4 bg-white rounded-lg border border-gray-100">
          <div className="flex-shrink-0 w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 font-bold">
            1
          </div>
          <div>
            <p className="font-medium text-gray-900">Upload PDF</p>
            <p className="text-gray-600 text-xs mt-1">Select your credit card statement</p>
          </div>
        </div>
        <div className="flex items-start space-x-3 p-4 bg-white rounded-lg border border-gray-100">
          <div className="flex-shrink-0 w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 font-bold">
            2
          </div>
          <div>
            <p className="font-medium text-gray-900">AI Processing</p>
            <p className="text-gray-600 text-xs mt-1">We extract key information</p>
          </div>
        </div>
        <div className="flex items-start space-x-3 p-4 bg-white rounded-lg border border-gray-100">
          <div className="flex-shrink-0 w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 font-bold">
            3
          </div>
          <div>
            <p className="font-medium text-gray-900">Download Results</p>
            <p className="text-gray-600 text-xs mt-1">Get JSON or Excel output</p>
          </div>
        </div>
      </div>
    </div>
  )
}

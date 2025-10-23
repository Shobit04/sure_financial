export default function Result({ data }) {
  return (
    <div className="p-8">
      <h2 className="text-xl font-semibold mb-4">Extraction Result</h2>
      <pre className="bg-gray-100 p-4 rounded">{JSON.stringify(data || {}, null, 2)}</pre>
    </div>
  )
}

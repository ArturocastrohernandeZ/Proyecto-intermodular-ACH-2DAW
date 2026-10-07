import { useEffect, useState } from 'react'

export default function App() {
  const [status, setStatus] = useState('loading')

  async function checkBackend() {
    setStatus('loading')
    try {
      const response = await fetch('/api/health/')
      if (!response.ok) throw new Error('Error de conexión')
      const data = await response.json()
      setStatus(data.status === 'ok' ? 'ok' : 'error')
    } catch {
      setStatus('error')
    }
  }

  useEffect(() => {
    checkBackend()
  }, [])

  return (
    <main>
      <span className="label">Hito 1 · Base del proyecto</span>
      <h1>Sistema de Reservas</h1>
      <p>Una aplicación para consultar disponibilidad y gestionar reservas.</p>
      <section aria-live="polite" aria-busy={status === 'loading'}>
        <h2>Estado de la conexión</h2>
        {status === 'loading' && <p>Comprobando la conexión…</p>}
        {status === 'ok' && (
          <>
            <p className="success">Conexión correcta con el backend.</p>
            <p>Respuesta recibida:</p>
            <pre>{'{"status":"ok"}'}</pre>
          </>
        )}
        {status === 'error' && (
          <p className="error">No se pudo conectar. Comprueba que el backend está arrancado.</p>
        )}
        <button onClick={checkBackend} disabled={status === 'loading'}>
          Comprobar de nuevo
        </button>
      </section>
    </main>
  )
}

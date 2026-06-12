import { useState, useEffect, useCallback } from 'react';

let globalStdoutListener: ((text: string) => void) | null = null;
let globalStderrListener: ((text: string) => void) | null = null;
let pyodideInstance: any = null;
let pyodideLoadingPromise: Promise<any> | null = null;

const loadPyodideCached = async () => {
  if (pyodideInstance) return pyodideInstance;
  
  if (!pyodideLoadingPromise) {
    const loadPyodide = (window as any).loadPyodide;
    if (!loadPyodide) {
      throw new Error('Pyodide script not loaded on page. Check index.html CDNs.');
    }
    pyodideLoadingPromise = loadPyodide({
      stdout: (text: string) => {
        if (globalStdoutListener) {
          globalStdoutListener(text);
        } else {
          console.log('[Pyodide stdout]', text);
        }
      },
      stderr: (text: string) => {
        if (globalStderrListener) {
          globalStderrListener(text);
        } else {
          console.error('[Pyodide stderr]', text);
        }
      }
    }).then((instance: any) => {
      pyodideInstance = instance;
      return instance;
    });
  }
  
  return pyodideLoadingPromise;
};

export interface RunResult {
  success: boolean;
  result?: string;
  error?: string;
}

export function usePyodide() {
  const [loading, setLoading] = useState<boolean>(!pyodideInstance);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (pyodideInstance) {
      setLoading(false);
      return;
    }

    let isMounted = true;
    loadPyodideCached()
      .then(() => {
        if (isMounted) setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to load Pyodide:', err);
        if (isMounted) {
          setError(err.message || 'Failed to initialize Python runtime');
          setLoading(false);
        }
      });

    return () => {
      isMounted = false;
    };
  }, []);

  const runCode = useCallback(async (
    code: string,
    onStdout: (text: string) => void,
    onStderr: (text: string) => void
  ): Promise<RunResult> => {
    try {
      const py = await loadPyodideCached();
      
      // Set active listeners for this run
      globalStdoutListener = onStdout;
      globalStderrListener = onStderr;
      
      // Clear modules that might cache variables or sys overrides
      // Run the code in its own clean dict scope
      const globals = py.toPy({});
      
      const result = await py.runPythonAsync(code, { globals });
      
      // Clean up globals object
      globals.destroy();
      
      return {
        success: true,
        result: result !== undefined && result !== null ? String(result) : undefined
      };
    } catch (err: any) {
      return {
        success: false,
        error: err.message || String(err)
      };
    } finally {
      globalStdoutListener = null;
      globalStderrListener = null;
    }
  }, []);

  return {
    loading,
    error,
    runCode
  };
}

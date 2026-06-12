import { useState, useEffect } from 'react';
import Editor from '@monaco-editor/react';
import { usePyodide } from '../hooks/usePyodide';
import { 
  Folder, File, Terminal, 
  Play, Save, RotateCcw, Monitor, Code, Info, Lock
} from 'lucide-react';

interface Lesson {
  id: number;
  filename: string;
  title: string;
  content: string;
}

interface WorkspaceExplorerProps {
  lessons: Lesson[];
  progress: Record<number, 'not_started' | 'in_progress' | 'completed'>;
}

interface FileNode {
  name: string;
  type: 'file' | 'directory';
  content?: string;
  language?: string;
  lessonId?: number;
}

export default function WorkspaceExplorer({ lessons, progress }: WorkspaceExplorerProps) {
  const [selectedFile, setSelectedFile] = useState<FileNode | null>(null);
  const [code, setCode] = useState<string>('');
  const [consoleLogs, setConsoleLogs] = useState<any[]>([]);
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [isSaved, setIsSaved] = useState<boolean>(false);
  const { loading: pyodideLoading, error: pyodideError, runCode } = usePyodide();

  // Create virtual workspace layout
  const fileTree: FileNode[] = [
    {
      name: 'Python Lesson Files',
      type: 'directory',
    },
    ...lessons.map(l => ({
      name: l.filename,
      type: 'file' as const,
      content: l.content,
      language: 'python',
      lessonId: l.id
    })),
    {
      name: 'Config & Web Files',
      type: 'directory',
    },
    {
      name: 'package.json',
      type: 'file',
      language: 'json',
      content: `{
  "name": "python-fundamentals-workspace",
  "version": "1.0.0",
  "description": "Interactive Web & Local Learning environment",
  "dependencies": {
    "react": "^19.2.6",
    "tailwindcss": "^3.4.19",
    "typescript": "~6.0.2"
  }
}`
    },
    {
      name: 'tailwind.config.js',
      type: 'file',
      language: 'javascript',
      content: `export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        pythonblue: "#38bdf8",
        pythonyellow: "#fbbf24"
      }
    }
  }
}`
    }
  ];

  // Open first lesson by default
  useEffect(() => {
    if (lessons.length > 0 && !selectedFile) {
      const firstLesson = fileTree.find(f => f.name === lessons[0].filename);
      if (firstLesson) {
        handleSelectFile(firstLesson);
      }
    }
  }, [lessons]);

  const handleSelectFile = (file: FileNode) => {
    if (file.type === 'directory') return;
    
    setSelectedFile(file);
    
    // Check if there is edited code in localStorage, else load original content
    const storageKey = file.lessonId 
      ? `py_workspace_lesson_${file.lessonId}`
      : `py_workspace_system_${file.name}`;
      
    const saved = localStorage.getItem(storageKey);
    if (saved) {
      setCode(saved);
    } else {
      setCode(file.content || '');
    }

    setConsoleLogs([
      { type: 'system', text: `Loaded file: ${file.name}` }
    ]);
  };

  const handleSave = () => {
    if (!selectedFile) return;
    
    const storageKey = selectedFile.lessonId 
      ? `py_workspace_lesson_${selectedFile.lessonId}`
      : `py_workspace_system_${selectedFile.name}`;
      
    localStorage.setItem(storageKey, code);
    setIsSaved(true);
    setTimeout(() => setIsSaved(false), 2000);
  };

  const handleReset = () => {
    if (!selectedFile) return;
    if (confirm(`Reset ${selectedFile.name} to its original template? All unsaved browser changes will be overwritten.`)) {
      setCode(selectedFile.content || '');
      const storageKey = selectedFile.lessonId 
        ? `py_workspace_lesson_${selectedFile.lessonId}`
        : `py_workspace_system_${selectedFile.name}`;
      localStorage.removeItem(storageKey);
    }
  };

  const handleRunCode = async () => {
    if (!selectedFile || selectedFile.language !== 'python') return;
    
    setIsRunning(true);
    setConsoleLogs([
      { type: 'system', text: `Executing Python script: ${selectedFile.name}...` },
      { type: 'system', text: `> python ${selectedFile.name}` }
    ]);

    const stdoutCallback = (text: string) => {
      setConsoleLogs(prev => [...prev, { type: 'stdout', text }]);
    };

    const stderrCallback = (text: string) => {
      setConsoleLogs(prev => [...prev, { type: 'stderr', text }]);
    };

    const result = await runCode(code, stdoutCallback, stderrCallback);
    
    if (result.success) {
      setConsoleLogs(prev => [
        ...prev,
        { type: 'system', text: 'Script executed successfully.' }
      ]);
      const currentCount = parseInt(localStorage.getItem('py_exec_count') || '0', 10);
      localStorage.setItem('py_exec_count', String(currentCount + 1));
      window.dispatchEvent(new Event('storage'));
    } else {
      setConsoleLogs(prev => [
        ...prev,
        { type: 'stderr', text: result.error || 'Compile Error' },
        { type: 'system', text: 'Script exited with errors.' }
      ]);
    }
    
    setIsRunning(false);
  };

  return (
    <div className="flex flex-col md:flex-row h-[calc(100vh-100px)] border border-white/5 bg-slate-950/40 rounded-2xl overflow-hidden relative z-10">
      
      {/* File Tree Sidebar */}
      <div className="w-full md:w-64 border-b md:border-b-0 md:border-r border-white/5 bg-slate-900/40 flex flex-col shrink-0 overflow-y-auto">
        <div className="p-4 border-b border-white/5">
          <h2 className="text-xs font-bold text-slate-400 uppercase tracking-widest flex items-center gap-2">
            <Monitor className="w-4 h-4 text-sky-400" />
            File Explorer
          </h2>
        </div>
        
        <div className="p-2 space-y-1">
          {fileTree.map((node, index) => {
            if (node.type === 'directory') {
              return (
                <div key={index} className="flex items-center gap-1.5 px-3 py-2 text-xs font-bold text-slate-500 uppercase tracking-wider mt-3 select-none">
                  <Folder className="w-3.5 h-3.5" />
                  {node.name}
                </div>
              );
            }
            
            const isSelected = selectedFile?.name === node.name;
            const isPython = node.language === 'python';
            const isUnlocked = !node.lessonId || node.lessonId === 1 || progress[node.lessonId - 1] === 'completed';
            
            return (
              <button
                key={index}
                onClick={() => handleSelectFile(node)}
                className={`w-full flex items-center justify-between px-4 py-2 rounded-lg text-xs text-left transition-colors ${
                  isSelected 
                    ? 'bg-sky-500/10 text-sky-300 font-semibold border-l-2 border-sky-400' 
                    : isUnlocked 
                      ? 'text-slate-400 hover:text-white hover:bg-white/5' 
                      : 'text-slate-600 hover:text-slate-500 cursor-not-allowed opacity-50'
                }`}
              >
                <span className="truncate flex items-center gap-2">
                  <File className={`w-3.5 h-3.5 shrink-0 ${isPython ? 'text-amber-500' : 'text-indigo-400'}`} />
                  <span className="truncate">{node.name}</span>
                </span>
                {!isUnlocked && <Lock className="w-3 h-3 text-slate-700 shrink-0" />}
              </button>
            );
          })}
        </div>
      </div>

      {/* Editor & Console Panel */}
      <div className="flex-1 flex flex-col overflow-hidden bg-slate-950/80">
        {selectedFile ? (
          (() => {
            const isSelectedFileUnlocked = !selectedFile.lessonId || selectedFile.lessonId === 1 || progress[selectedFile.lessonId - 1] === 'completed';
            
            if (!isSelectedFileUnlocked) {
              return (
                <div className="flex-1 flex flex-col items-center justify-center text-center p-8 space-y-4 bg-[#080c16] backdrop-blur-sm relative z-20">
                  <Lock className="w-12 h-12 text-slate-700 animate-pulse" />
                  <h3 className="text-lg font-bold text-white tracking-tight">🔒 Workspace File Locked</h3>
                  <p className="text-xs text-slate-400 max-w-xs leading-relaxed">
                    This script (<code className="font-mono text-sky-400">{selectedFile.name}</code>) is locked in your sandbox workspace. Complete the previous modules and mark them as completed in the Classroom tab to explore and compile this lesson!
                  </p>
                  <div className="bg-slate-900 border border-white/5 px-4 py-2 rounded-xl text-xs font-semibold text-slate-500">
                    Requires Lesson {selectedFile.lessonId ? selectedFile.lessonId - 1 : ''} Completion
                  </div>
                </div>
              );
            }
            
            return (
              <>
                {/* Header toolbar */}
                <div className="flex justify-between items-center px-6 py-3 bg-slate-900/30 border-b border-white/5 text-xs text-slate-400">
                  <div className="flex items-center gap-2">
                    <Code className="w-4 h-4 text-sky-400" />
                    <span className="font-mono text-slate-200">{selectedFile.name}</span>
                    {selectedFile.language !== 'python' && (
                      <span className="text-[10px] bg-slate-800 text-slate-400 px-1.5 py-0.5 rounded font-mono">
                        READ-ONLY PREVIEW
                      </span>
                    )}
                  </div>
                  
                  <div className="flex items-center gap-4">
                    <button
                      onClick={handleReset}
                      className="hover:text-white flex items-center gap-1 transition-colors font-semibold"
                    >
                      <RotateCcw className="w-3.5 h-3.5" />
                      Reset
                    </button>
                    <button
                      onClick={handleSave}
                      className={`flex items-center gap-1 transition-colors font-semibold ${
                        isSaved ? 'text-emerald-400' : 'hover:text-white'
                      }`}
                    >
                      <Save className="w-3.5 h-3.5" />
                      {isSaved ? 'Saved!' : 'Save changes'}
                    </button>
                    {selectedFile.language === 'python' && (
                      <button
                        onClick={handleRunCode}
                        disabled={isRunning || pyodideLoading}
                        className="flex items-center gap-1.5 bg-gradient-to-r from-sky-400 to-indigo-500 hover:from-sky-500 hover:to-indigo-600 text-slate-950 disabled:opacity-50 px-3 py-1.5 rounded-lg font-bold shadow-md shadow-sky-500/10 active:scale-95 transition-all text-xs"
                      >
                        <Play className="w-3 h-3 fill-current" />
                        {isRunning ? 'Executing...' : 'Run Code'}
                      </button>
                    )}
                  </div>
                </div>

                {/* Monaco Editor */}
                <div className="flex-1 relative min-h-[250px]">
                  <Editor
                    height="100%"
                    language={selectedFile.language}
                    theme="vs-dark"
                    value={code}
                    onChange={(val) => setCode(val || '')}
                    options={{
                      fontSize: 14,
                      fontFamily: 'Fira Code, monospace',
                      minimap: { enabled: false },
                      automaticLayout: true,
                      padding: { top: 16 },
                      scrollBeyondLastLine: false,
                      wordWrap: 'on',
                      readOnly: selectedFile.language !== 'python'
                    }}
                  />
                </div>

                {/* Console Terminal */}
                {selectedFile.language === 'python' ? (
                  <div className="h-44 border-t border-white/5 bg-[#090d16] flex flex-col overflow-hidden">
                    <div className="flex justify-between items-center px-6 py-2.5 bg-[#0d1322] border-b border-white/5 text-xs text-slate-400">
                      <span className="font-semibold uppercase tracking-wider flex items-center gap-2">
                        <Terminal className="w-3.5 h-3.5 text-amber-500" />
                        Terminal Output
                      </span>
                      <button onClick={() => setConsoleLogs([])} className="hover:text-white transition-colors">
                        Clear
                      </button>
                    </div>
                    
                    <div className="flex-1 p-4 overflow-y-auto font-mono text-xs space-y-1 bg-[#05080e]">
                      {pyodideLoading && (
                        <div className="text-sky-400 animate-pulse">Initializing python wasm compiler...</div>
                      )}
                      {pyodideError && (
                        <div className="text-red-400">Error loading compiler: {pyodideError}</div>
                      )}
                      {consoleLogs.length === 0 && (
                        <div className="text-slate-600 italic">Terminal idle. Click "Run Code" to compile.</div>
                      )}
                      {consoleLogs.map((log, index) => {
                        if (log.type === 'system') {
                          return <div key={index} className="text-slate-500 font-semibold">{log.text}</div>;
                        }
                        if (log.type === 'stderr') {
                          return <div key={index} className="text-red-400 bg-red-950/20 px-2 py-0.5 rounded border border-red-900/30">{log.text}</div>;
                        }
                        return <div key={index} className="text-slate-200">{log.text}</div>;
                      })}
                    </div>
                  </div>
                ) : (
                  <div className="p-4 border-t border-white/5 bg-[#090d16] flex items-center gap-3">
                    <Info className="w-5 h-5 text-indigo-400 shrink-0" />
                    <span className="text-xs text-slate-400 leading-normal">
                      Config files are rendered in read-only mode to maintain project compilation consistency. You can modify your Python lesson files freely.
                    </span>
                  </div>
                )}
              </>
            );
          })()
        ) : (
          <div className="flex-1 flex flex-col items-center justify-center text-center p-8 space-y-4">
            <Folder className="w-12 h-12 text-slate-700" />
            <h3 className="text-base font-bold text-slate-300">No File Selected</h3>
            <p className="text-xs text-slate-500 max-w-xs">Select a python script from the sidebar explorer to edit and run it inside the sandbox.</p>
          </div>
        )}
      </div>

    </div>
  );
}

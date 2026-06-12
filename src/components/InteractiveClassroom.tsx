import { useState, useEffect } from 'react';
import Editor from '@monaco-editor/react';
import { usePyodide } from '../hooks/usePyodide';
import { 
  Play, RotateCcw, Save, CheckCircle2, ChevronLeft, 
  Terminal, FileCode, HelpCircle, BookOpen, AlertCircle
} from 'lucide-react';
import ConfirmationModal from './ui/ConfirmationModal';

interface Lesson {
  id: number;
  filename: string;
  title: string;
  sections: {
    tutorial: string;
    activity: string;
    challenge: string;
  };
  content: string;
}

interface InteractiveClassroomProps {
  lesson: Lesson;
  onBack: () => void;
  onMarkComplete: (id: number, status: 'completed' | 'in_progress') => void;
  initialProgress: 'not_started' | 'in_progress' | 'completed';
}

interface ConsoleOutputLine {
  type: 'stdout' | 'stderr' | 'system';
  text: string;
}

export default function InteractiveClassroom({ 
  lesson, 
  onBack, 
  onMarkComplete, 
  initialProgress 
}: InteractiveClassroomProps) {
  
  // Tabs for section selection: 'tutorial' | 'activity' | 'challenge'
  const [activeSection, setActiveSection] = useState<'tutorial' | 'activity' | 'challenge'>('tutorial');
  const [code, setCode] = useState<string>('');
  const [consoleLogs, setConsoleLogs] = useState<ConsoleOutputLine[]>([]);
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [isSaved, setIsSaved] = useState<boolean>(false);
  const [isResetModalOpen, setIsResetModalOpen] = useState<boolean>(false);
  const { loading: pyodideLoading, error: pyodideError, runCode } = usePyodide();

  // Load saved code from LocalStorage or fallback to lesson file content
  useEffect(() => {
    const storageKey = `py_lesson_${lesson.id}_${activeSection}`;
    const savedCode = localStorage.getItem(storageKey);
    if (savedCode) {
      setCode(savedCode);
    } else {
      // Fallback to parsed sections
      setCode(lesson.sections[activeSection] || '');
    }
    setConsoleLogs([
      { type: 'system', text: `Loaded ${lesson.filename} - Section: ${activeSection.toUpperCase()}` }
    ]);
  }, [lesson, activeSection]);

  // Handle Save
  const handleSave = () => {
    const storageKey = `py_lesson_${lesson.id}_${activeSection}`;
    localStorage.setItem(storageKey, code);
    setIsSaved(true);
    setTimeout(() => setIsSaved(false), 2000);
    
    // Set lesson status to in_progress
    if (initialProgress === 'not_started') {
      onMarkComplete(lesson.id, 'in_progress');
    }
  };

  // Handle Reset
  const handleReset = () => {
    setIsResetModalOpen(true);
  };

  const confirmReset = () => {
    setCode(lesson.sections[activeSection] || '');
    const storageKey = `py_lesson_${lesson.id}_${activeSection}`;
    localStorage.removeItem(storageKey);
    setConsoleLogs(prev => [
      ...prev, 
      { type: 'system', text: 'Reset code to default template.' }
    ]);
    setIsResetModalOpen(false);
  };

  // Execute Code using Pyodide
  const handleRunCode = async () => {
    setIsRunning(true);
    setConsoleLogs([
      { type: 'system', text: `Python 3.11.x WebAssembly execution started...` },
      { type: 'system', text: `> python ${lesson.filename}` }
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
        { type: 'system', text: `Process finished successfully.` }
      ]);
      
      // Update running stats or trigger milestone checking if needed
      // Track total execution count
      const currentCount = parseInt(localStorage.getItem('py_exec_count') || '0', 10);
      localStorage.setItem('py_exec_count', String(currentCount + 1));
      window.dispatchEvent(new Event('storage')); // Notify App component of run
    } else {
      setConsoleLogs(prev => [
        ...prev,
        { type: 'stderr', text: result.error || 'Unknown runtime exception' },
        { type: 'system', text: `Process exited with errors.` }
      ]);
    }
    
    setIsRunning(false);
  };

  // Parse Python Comments for Tutorial Sidebar
  const parseComments = (sourceCode: string) => {
    const lines = sourceCode.split('\n');
    const explanationLines: string[] = [];
    const exerciseInstructions: string[] = [];
    let isInsideActivity = false;
    let isInsideChallenge = false;

    lines.forEach(line => {
      const trimmed = line.trim();
      
      // Track section dividers
      if (trimmed.includes('Activity Section') || trimmed.includes('============ActivitySection==========')) {
        isInsideActivity = true;
        isInsideChallenge = false;
        return;
      }
      if (trimmed.includes('Mini Challenge') || trimmed.includes('============Mini Challenge==========')) {
        isInsideChallenge = true;
        isInsideActivity = false;
        return;
      }

      if (trimmed.startsWith('#')) {
        // Remove # and double leading spaces
        const text = trimmed.substring(1).trim();
        if (text.startsWith('===') || text.startsWith('---') || text === lesson.filename) {
          return; // Skip dividers & files titles
        }

        if (isInsideChallenge) {
          exerciseInstructions.push(text);
        } else if (isInsideActivity) {
          exerciseInstructions.push(text);
        } else {
          explanationLines.push(text);
        }
      }
    });

    return {
      tutorialText: explanationLines.join('\n'),
      exerciseText: exerciseInstructions.join('\n')
    };
  };

  const { tutorialText, exerciseText } = parseComments(lesson.content);

  return (
    <div className="flex flex-col h-[calc(100vh-80px)] border border-white/5 rounded-2xl overflow-hidden bg-slate-950/40 relative z-10">
      
      {/* Top action header bar */}
      <div className="flex flex-wrap items-center justify-between px-6 py-4 border-b border-white/5 bg-slate-900/60 backdrop-blur-md gap-4">
        <div className="flex items-center gap-3">
          <button 
            onClick={onBack}
            className="p-2 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white transition-colors"
            title="Go back to Dashboard"
          >
            <ChevronLeft className="w-5 h-5" />
          </button>
          <div>
            <div className="flex items-center gap-2">
              <span className="text-[10px] font-mono text-sky-400 bg-sky-950/60 px-2 py-0.5 rounded border border-sky-900/40 font-bold">
                Module {lesson.id}
              </span>
              <h2 className="text-lg font-bold text-white tracking-tight">{lesson.title}</h2>
            </div>
            <p className="text-xs text-slate-500 mt-0.5 font-mono">{lesson.filename}</p>
          </div>
        </div>

        {/* Section selectors */}
        <div className="flex bg-slate-950/60 p-1 rounded-xl border border-white/5">
          {(['tutorial', 'activity', 'challenge'] as const).map((sec) => (
            <button
              key={sec}
              onClick={() => setActiveSection(sec)}
              className={`px-4 py-1.5 rounded-lg text-xs font-semibold uppercase tracking-wider transition-all duration-200 ${
                activeSection === sec
                  ? 'bg-gradient-to-r from-sky-400 to-indigo-500 text-slate-950 shadow-md font-bold'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              {sec}
            </button>
          ))}
        </div>

        {/* Complete Buttons */}
        <div className="flex items-center gap-3">
          <button 
            onClick={() => onMarkComplete(lesson.id, 'completed')}
            className={`inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-bold transition-all duration-200 ${
              initialProgress === 'completed'
                ? 'bg-emerald-950/40 border border-emerald-500/20 text-emerald-400'
                : 'bg-slate-900 text-slate-300 hover:bg-emerald-950/40 hover:text-emerald-400 hover:border-emerald-500/20 border border-white/5 active:scale-95'
            }`}
          >
            <CheckCircle2 className="w-4 h-4" />
            {initialProgress === 'completed' ? 'Module Finished' : 'Mark Completed'}
          </button>
        </div>
      </div>

      {/* Main splitscreen content */}
      <div className="flex-1 grid grid-cols-1 lg:grid-cols-5 overflow-hidden">
        
        {/* Left Side: Learn Docs / Instructions */}
        <div className="lg:col-span-2 border-r border-white/5 flex flex-col overflow-y-auto bg-slate-900/20 p-6 space-y-6">
          
          {/* Objective summary */}
          <div className="space-y-3">
            <h3 className="text-sm font-bold uppercase tracking-wider text-slate-400 flex items-center gap-2 font-sans">
              <BookOpen className="w-4 h-4 text-sky-400" />
              Lesson Explanation
            </h3>
            <div className="p-4 rounded-xl bg-slate-900/60 border border-white/5 text-sm leading-relaxed text-slate-300 whitespace-pre-line font-sans">
              {tutorialText || 'No detailed instructions written. Read the comments inside the code editor.'}
            </div>
          </div>

          {/* Section specific instructions */}
          {activeSection !== 'tutorial' && exerciseText && (
            <div className="space-y-3">
              <h3 className="text-sm font-bold uppercase tracking-wider text-amber-400 flex items-center gap-2 font-sans">
                <HelpCircle className="w-4 h-4" />
                {activeSection === 'activity' ? 'Activity Objectives' : 'Challenge Details'}
              </h3>
              <div className="p-4 rounded-xl bg-amber-500/5 border border-amber-500/10 text-sm leading-relaxed text-amber-200/90 whitespace-pre-line font-sans">
                {exerciseText}
              </div>
            </div>
          )}

          {/* Info Card */}
          <div className="p-4 rounded-xl bg-slate-950/40 border border-white/5 flex items-start gap-3 mt-auto">
            <AlertCircle className="w-5 h-5 text-sky-400 shrink-0 mt-0.5" />
            <div className="text-xs text-slate-500">
              <span className="text-slate-300 font-bold block mb-1">Local Development Sync</span>
              Your progress is saved locally. If you run code, this runs inside a local WASM runtime (Pyodide). To save these exercises to your local `.py` files, update them in your code editor directly!
            </div>
          </div>

        </div>

        {/* Right Side: Monaco Code Editor + Output Console */}
        <div className="lg:col-span-3 flex flex-col overflow-hidden bg-slate-950/80">
          
          {/* Editor Header Toolbar */}
          <div className="flex justify-between items-center px-6 py-2.5 bg-slate-900/30 border-b border-white/5 text-xs text-slate-400">
            <div className="flex items-center gap-2">
              <FileCode className="w-3.5 h-3.5 text-indigo-400" />
              <span className="font-mono text-slate-300">{lesson.filename} ({activeSection})</span>
            </div>
            
            <div className="flex items-center gap-4">
              <button 
                onClick={handleReset}
                className="hover:text-white transition-colors flex items-center gap-1 font-semibold"
                title="Reset code to original"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                Reset template
              </button>
              <button 
                onClick={handleSave}
                className={`transition-colors flex items-center gap-1 font-semibold ${
                  isSaved ? 'text-emerald-400' : 'hover:text-white'
                }`}
                title="Save changes to LocalStorage"
              >
                <Save className="w-3.5 h-3.5" />
                {isSaved ? 'Saved!' : 'Save Work'}
              </button>
              <button
                onClick={handleRunCode}
                disabled={isRunning || pyodideLoading}
                className="flex items-center gap-1.5 bg-gradient-to-r from-sky-400 to-indigo-500 hover:from-sky-500 hover:to-indigo-600 text-slate-950 disabled:opacity-50 px-3 py-1.5 rounded-lg font-bold shadow-md shadow-sky-500/10 active:scale-95 transition-all text-xs"
              >
                <Play className="w-3 h-3 fill-current" />
                {isRunning ? 'Running...' : 'Run Code'}
              </button>
            </div>
          </div>

          {/* Monaco Editor Container */}
          <div className="flex-1 min-h-[300px] relative">
            <Editor
              height="100%"
              defaultLanguage="python"
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
                lineNumbersMinChars: 3,
                wordWrap: 'on',
              }}
            />
          </div>

          {/* Output Terminal Console */}
          <div className="h-[200px] border-t border-white/5 bg-[#090d16] flex flex-col overflow-hidden">
            <div className="flex justify-between items-center px-6 py-2.5 bg-[#0d1322] border-b border-white/5 text-xs text-slate-400">
              <span className="font-semibold uppercase tracking-wider flex items-center gap-2">
                <Terminal className="w-3.5 h-3.5 text-amber-500" />
                Console Output
              </span>
              <button 
                onClick={() => setConsoleLogs([])}
                className="hover:text-white transition-colors"
              >
                Clear
              </button>
            </div>
            
            <div className="flex-1 p-4 overflow-y-auto font-mono text-xs space-y-1 bg-[#05080e]">
              {pyodideLoading && (
                <div className="text-sky-400 flex items-center gap-2 animate-pulse">
                  <span>●</span> Initializing WebAssembly Python environment...
                </div>
              )}
              {pyodideError && (
                <div className="text-red-400">
                  Error loading compiler: {pyodideError}
                </div>
              )}
              
              {!pyodideLoading && consoleLogs.length === 0 && (
                <div className="text-slate-600 italic">
                  Terminal ready. Write code above and click "Run Script" to see output here.
                </div>
              )}

              {consoleLogs.map((log, index) => {
                if (log.type === 'system') {
                  return <div key={index} className="text-slate-500 font-semibold">{log.text}</div>;
                }
                if (log.type === 'stderr') {
                  return <div key={index} className="text-red-400 bg-red-950/20 px-2 py-0.5 rounded border border-red-900/30 whitespace-pre-wrap">{log.text}</div>;
                }
                return <div key={index} className="text-slate-200 whitespace-pre-wrap">{log.text}</div>;
              })}
            </div>
          </div>

        </div>

      </div>

      <ConfirmationModal
        isOpen={isResetModalOpen}
        title="Reset Template Code"
        message="Are you sure you want to reset the code for this section to the default lesson template? Any unsaved edits will be permanently overwritten."
        confirmText="Reset Code"
        cancelText="Cancel"
        onConfirm={confirmReset}
        onCancel={() => setIsResetModalOpen(false)}
        type="warning"
      />
    </div>
  );
}

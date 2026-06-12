import { useState, useEffect } from 'react';
import Editor from '@monaco-editor/react';
import { usePyodide } from '../hooks/usePyodide';
import { 
  Play, RotateCcw, Save, CheckCircle2, ChevronLeft, 
  Terminal, FileCode, HelpCircle, BookOpen, AlertCircle
} from 'lucide-react';
import ConfirmationModal from './ui/ConfirmationModal';
import { lessonValidators } from '../data/validators';

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

  // Track completion of activity & challenge
  const [activityPassed, setActivityPassed] = useState<boolean>(false);
  const [challengePassed, setChallengePassed] = useState<boolean>(false);

  // Input Modal States
  const [isInputModalOpen, setIsInputModalOpen] = useState<boolean>(false);
  const [inputPrompts, setInputPrompts] = useState<string[]>([]);
  const [inputAnswers, setInputAnswers] = useState<string[]>([]);
  const [pendingRunResolve, setPendingRunResolve] = useState<((values: string[]) => void) | null>(null);


  // Load section completion status on mount/lesson change
  useEffect(() => {
    const activityKey = `py_lesson_${lesson.id}_activity_passed`;
    const challengeKey = `py_lesson_${lesson.id}_challenge_passed`;
    setActivityPassed(localStorage.getItem(activityKey) === 'true');
    setChallengePassed(localStorage.getItem(challengeKey) === 'true');
  }, [lesson.id]);

  // Extract tutorial code by taking everything before the Activity section
  const getTutorialCode = (content: string): string => {
    const lines = content.split('\n');
    let activityStartIdx = -1;
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      if (line.includes('Activity Section') || line.includes('============Activity Section==========')) {
        activityStartIdx = i;
        // Search upwards to catch the comments block boundary of Activity Section
        while (activityStartIdx > 0 && (lines[activityStartIdx - 1].trim().startsWith('#') || lines[activityStartIdx - 1].trim() === '')) {
          activityStartIdx--;
        }
        break;
      }
    }
    if (activityStartIdx !== -1) {
      return lines.slice(0, activityStartIdx).join('\n').trim();
    }
    return content;
  };

  // Load saved code from LocalStorage or fallback to lesson file content
  useEffect(() => {
    const storageKey = `py_lesson_${lesson.id}_${activeSection}`;
    const savedCode = localStorage.getItem(storageKey);
    if (savedCode) {
      setCode(savedCode);
    } else {
      // Clean start templates
      if (activeSection === 'tutorial') {
        setCode(getTutorialCode(lesson.content));
      } else if (activeSection === 'activity') {
        setCode(`print("============Activity Section==========\\n")\n\n# Write your activity code below\n`);
      } else if (activeSection === 'challenge') {
        setCode(`print("============Mini Challenge==========\\n")\n\n# Write your challenge code below\n`);
      }
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
    
    // Set lesson status to in_progress if not already completed
    if (initialProgress === 'not_started') {
      onMarkComplete(lesson.id, 'in_progress');
    }
  };

  // Handle Reset
  const handleReset = () => {
    setIsResetModalOpen(true);
  };

  const confirmReset = () => {
    let defaultCode = '';
    if (activeSection === 'tutorial') {
      defaultCode = getTutorialCode(lesson.content);
    } else if (activeSection === 'activity') {
      defaultCode = `print("============Activity Section==========\\n")\n\n# Write your activity code below\n`;
    } else if (activeSection === 'challenge') {
      defaultCode = `print("============Mini Challenge==========\\n")\n\n# Write your challenge code below\n`;
    }

    setCode(defaultCode);
    const storageKey = `py_lesson_${lesson.id}_${activeSection}`;
    localStorage.removeItem(storageKey);
    setConsoleLogs(prev => [
      ...prev, 
      { type: 'system', text: 'Reset code to default template.' }
    ]);
    setIsResetModalOpen(false);
  };

  // Extract input() prompts from Python code (ignoring comments)
  const extractPrompts = (sourceCode: string): string[] => {
    const prompts: string[] = [];
    const cleanCode = sourceCode
      .split('\n')
      .filter(line => !line.trim().startsWith('#'))
      .join('\n');

    // Match input("...") or input('...')
    const regex = /input\s*\(\s*(['"`])(.*?)\1\s*\)/g;
    let match;
    while ((match = regex.exec(cleanCode)) !== null) {
      prompts.push(match[2]);
    }

    // Also match empty input()
    const simpleRegex = /input\s*\(\s*\)/g;
    let simpleCount = 0;
    while (simpleRegex.exec(cleanCode) !== null) {
      simpleCount++;
    }
    for (let i = 0; i < simpleCount; i++) {
      prompts.push(`Input value ${prompts.length + 1}:`);
    }

    return prompts;
  };

  const handleInputSubmit = () => {
    if (pendingRunResolve) {
      pendingRunResolve(inputAnswers);
    }
    setIsInputModalOpen(false);
  };

  const handleInputCancel = () => {
    setIsInputModalOpen(false);
    setConsoleLogs(prev => [
      ...prev,
      { type: 'system', text: 'Execution cancelled: Input prompt dismissed.' }
    ]);
    setIsRunning(false);
  };

  const handleAnswerChange = (index: number, value: string) => {
    setInputAnswers(prev => {
      const copy = [...prev];
      copy[index] = value;
      return copy;
    });
  };

  // Execute Code using Pyodide and validate correctness
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

    // 1. Scan for inputs
    const prompts = extractPrompts(code);
    let answers: string[] = [];
    if (prompts.length > 0) {
      try {
        answers = await new Promise<string[]>((resolve) => {
          setInputPrompts(prompts);
          setInputAnswers(new Array(prompts.length).fill(''));
          setIsInputModalOpen(true);
          setPendingRunResolve(() => resolve);
        });
      } catch (e) {
        setIsRunning(false);
        return;
      }
    }

    // Grab validation script if this is Activity or Challenge tab
    const validator = activeSection !== 'tutorial' ? lessonValidators[lesson.id]?.[activeSection] : null;
    const validationCode = validator ? validator.pythonCode : undefined;

    const result = await runCode(code, stdoutCallback, stderrCallback, validationCode, answers);
    
    if (result.success) {
      // Record execution metrics locally
      const currentCount = parseInt(localStorage.getItem('py_exec_count') || '0', 10);
      localStorage.setItem('py_exec_count', String(currentCount + 1));
      window.dispatchEvent(new Event('storage'));

      if (activeSection !== 'tutorial') {
        if (result.validationSuccess) {
          setConsoleLogs(prev => [
            ...prev,
            { type: 'system', text: `Process finished successfully.` },
            { type: 'system', text: `🎉 CORRECT! You have successfully completed the ${activeSection} objectives!` }
          ]);

          // Save completion status
          const key = `py_lesson_${lesson.id}_${activeSection}_passed`;
          localStorage.setItem(key, 'true');
          if (activeSection === 'activity') {
            setActivityPassed(true);
          } else {
            setChallengePassed(true);
          }

          // Automatically set status to in_progress
          if (initialProgress === 'not_started') {
            onMarkComplete(lesson.id, 'in_progress');
          }
        } else {
          setConsoleLogs(prev => [
            ...prev,
            { type: 'system', text: `Process finished successfully.` },
            { type: 'stderr', text: `❌ INCORRECT: Requirements not met.\nHint: ${result.validationError || validator?.errorMessage}` }
          ]);
        }
      } else {
        setConsoleLogs(prev => [
          ...prev,
          { type: 'system', text: `Process finished successfully.` }
        ]);
      }
    } else {
      setConsoleLogs(prev => [
        ...prev,
        { type: 'stderr', text: result.error || 'Unknown runtime exception' },
        { type: 'system', text: `Process exited with errors.` }
      ]);
    }
    
    setIsRunning(false);
  };

  // Parse Python Comments for clean layout instructions
  const parseComments = (sourceCode: string) => {
    const lines = sourceCode.split('\n');
    const tutorialLines: string[] = [];
    const activityLines: string[] = [];
    const challengeLines: string[] = [];
    
    let currentSection: 'tutorial' | 'activity' | 'challenge' = 'tutorial';

    lines.forEach(line => {
      const trimmed = line.trim();
      
      // Track section dividers
      if (trimmed.includes('Activity Section') || trimmed.includes('============ActivitySection==========') || trimmed.includes('============Activity Section==========')) {
        currentSection = 'activity';
        return;
      }
      if (trimmed.includes('Mini Challenge') || trimmed.includes('============Mini Challenge==========') || trimmed.includes('============MiniChallenge==========')) {
        currentSection = 'challenge';
        return;
      }

      if (trimmed.startsWith('#')) {
        const text = trimmed.substring(1).trim();
        if (text.startsWith('===') || text.startsWith('---') || text === lesson.filename) {
          return; // Skip dividers
        }

        if (currentSection === 'challenge') {
          challengeLines.push(text);
        } else if (currentSection === 'activity') {
          activityLines.push(text);
        } else {
          tutorialLines.push(text);
        }
      }
    });

    return {
      tutorialText: tutorialLines.join('\n'),
      activityText: activityLines.join('\n'),
      challengeText: challengeLines.join('\n')
    };
  };

  const { tutorialText, activityText, challengeText } = parseComments(lesson.content);

  return (
    <div className="flex flex-col h-[calc(100vh-80px)] border border-white/5 rounded-2xl overflow-hidden bg-slate-950/40 relative z-10 font-sans">
      
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
        <div className="flex bg-slate-950/60 p-1 rounded-xl border border-white/5 gap-1">
          {(['tutorial', 'activity', 'challenge'] as const).map((sec) => {
            const isPassed = sec === 'activity' ? activityPassed : sec === 'challenge' ? challengePassed : false;
            return (
              <button
                key={sec}
                onClick={() => setActiveSection(sec)}
                className={`px-4 py-1.5 rounded-lg text-xs font-semibold uppercase tracking-wider transition-all duration-200 flex items-center gap-1.5 ${
                  activeSection === sec
                    ? 'bg-gradient-to-r from-sky-400 to-indigo-500 text-slate-950 shadow-md font-bold'
                    : 'text-slate-400 hover:text-white hover:bg-white/5'
                }`}
              >
                {sec}
                {isPassed && (
                  <span className={`w-1.5 h-1.5 rounded-full ${activeSection === sec ? 'bg-slate-950' : 'bg-emerald-400'}`}></span>
                )}
              </button>
            );
          })}
        </div>

        {/* Complete Buttons */}
        <div className="flex items-center gap-3">
          <button 
            disabled={initialProgress !== 'completed' && !(activityPassed && challengePassed)}
            onClick={() => onMarkComplete(lesson.id, 'completed')}
            className={`inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-bold transition-all duration-200 ${
              initialProgress === 'completed'
                ? 'bg-emerald-950/40 border border-emerald-500/20 text-emerald-400'
                : activityPassed && challengePassed
                  ? 'bg-slate-900 text-slate-300 hover:bg-emerald-950/40 hover:text-emerald-400 hover:border-emerald-500/20 border border-white/5 active:scale-95 cursor-pointer'
                  : 'bg-slate-950 text-slate-600 border border-white/5 opacity-55 cursor-not-allowed'
            }`}
            title={initialProgress === 'completed' ? 'Module finished' : activityPassed && challengePassed ? 'Mark lesson as completed' : 'Finish both Activity and Challenge to complete the module'}
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
          
          {/* Tutorial Section Explanation */}
          {activeSection === 'tutorial' && (
            <div className="space-y-3">
              <h3 className="text-sm font-bold uppercase tracking-wider text-slate-400 flex items-center gap-2">
                <BookOpen className="w-4 h-4 text-sky-400" />
                Lesson Explanation
              </h3>
              <div className="p-4 rounded-xl bg-slate-900/60 border border-white/5 text-sm leading-relaxed text-slate-300 whitespace-pre-line">
                {tutorialText || 'No detailed instructions written. Read the comments inside the code editor.'}
              </div>
            </div>
          )}

          {/* Activity Section Objectives */}
          {activeSection === 'activity' && (
            <div className="space-y-3">
              <h3 className="text-sm font-bold uppercase tracking-wider text-sky-400 flex items-center gap-2">
                <HelpCircle className="w-4 h-4 text-sky-400" />
                Activity Objectives
              </h3>
              <div className="p-4 rounded-xl bg-sky-950/20 border border-sky-500/10 text-sm leading-relaxed text-slate-300 whitespace-pre-line">
                {activityText || 'No Activity objectives found for this lesson.'}
              </div>
              {activityPassed && (
                <div className="p-4 rounded-xl bg-emerald-950/20 border border-emerald-500/10 text-xs font-semibold text-emerald-400 flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 animate-pulse" />
                  Activity completed successfully!
                </div>
              )}
            </div>
          )}

          {/* Challenge Section Details */}
          {activeSection === 'challenge' && (
            <div className="space-y-3">
              <h3 className="text-sm font-bold uppercase tracking-wider text-amber-400 flex items-center gap-2">
                <HelpCircle className="w-4 h-4 text-amber-400" />
                Challenge Details
              </h3>
              <div className="p-4 rounded-xl bg-amber-500/5 border border-amber-500/10 text-sm leading-relaxed text-slate-300 whitespace-pre-line">
                {challengeText || 'No Challenge details found for this lesson.'}
              </div>
              {challengePassed && (
                <div className="p-4 rounded-xl bg-emerald-950/20 border border-emerald-500/10 text-xs font-semibold text-emerald-400 flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 animate-pulse" />
                  Challenge completed successfully!
                </div>
              )}
            </div>
          )}

          {/* Info Card */}
          <div className="p-4 rounded-xl bg-slate-950/40 border border-white/5 flex items-start gap-3 mt-auto">
            <AlertCircle className="w-5 h-5 text-sky-400 shrink-0 mt-0.5" />
            <div className="text-xs text-slate-500 leading-normal">
              <span className="text-slate-300 font-bold block mb-1">Local Development Sync</span>
              Your progress is saved locally. When you run code, this runs inside a local WASM runtime (Pyodide). To save these exercises to your local `.py` files, update them in your code editor directly!
            </div>
          </div>

        </div>

        {/* Right Side: Monaco Code Editor + Output Console */}
        <div className="lg:col-span-3 flex flex-col overflow-hidden bg-slate-950/80">
          
          {/* Editor Header Toolbar */}
          <div className="flex justify-between items-center px-6 py-2.5 bg-slate-900/30 border-b border-white/5 text-xs text-slate-400">
            <div className="flex items-center gap-2 font-mono">
              <FileCode className="w-3.5 h-3.5 text-indigo-400" />
              <span className="text-slate-300">{lesson.filename} ({activeSection})</span>
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

      <InputModal
        isOpen={isInputModalOpen}
        prompts={inputPrompts}
        answers={inputAnswers}
        onAnswerChange={handleAnswerChange}
        onSubmit={handleInputSubmit}
        onCancel={handleInputCancel}
      />
    </div>
  );
}

interface InputModalProps {
  isOpen: boolean;
  prompts: string[];
  answers: string[];
  onAnswerChange: (index: number, value: string) => void;
  onSubmit: () => void;
  onCancel: () => void;
}

function InputModal({ isOpen, prompts, answers, onAnswerChange, onSubmit, onCancel }: InputModalProps) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50 p-4">
      {/* Backdrop */}
      <div 
        className="fixed inset-0 bg-black/60 backdrop-blur-sm"
        onClick={onCancel}
      />
      
      {/* Modal Content */}
      <div className="relative w-full max-w-md bg-[#090d16]/95 border border-white/10 rounded-2xl shadow-2xl backdrop-blur-md p-6 overflow-hidden animate-scale-in">
        <div className="absolute top-0 right-0 w-40 h-40 bg-sky-500/5 rounded-full blur-3xl pointer-events-none"></div>
        
        <div className="flex items-center gap-3 mb-5 border-b border-white/5 pb-4">
          <div className="w-8 h-8 rounded-lg bg-sky-500/10 flex items-center justify-center text-sky-400 shrink-0">
            <Terminal className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-sm font-bold text-white uppercase tracking-wider">Input Required</h3>
            <p className="text-[10px] text-slate-500 font-mono">PROVIDE PARAMETERS FOR RUNTIME</p>
          </div>
        </div>

        <div className="space-y-4 max-h-[300px] overflow-y-auto pr-1 mb-6">
          {prompts.map((promptText, idx) => (
            <div key={idx} className="space-y-1.5">
              <label className="text-xs font-semibold text-slate-300 block">
                {promptText}
              </label>
              <input
                type="text"
                value={answers[idx] || ''}
                onChange={(e) => onAnswerChange(idx, e.target.value)}
                className="w-full bg-slate-950 border border-white/10 rounded-xl px-4 py-2.5 text-slate-200 focus:border-sky-400 focus:outline-none focus:ring-1 focus:ring-sky-400 text-xs font-mono"
                placeholder="Type input value..."
                autoFocus={idx === 0}
                onKeyDown={(e) => {
                  if (e.key === 'Enter') {
                    onSubmit();
                  }
                }}
              />
            </div>
          ))}
        </div>

        <div className="flex items-center justify-end gap-3 pt-2">
          <button
            onClick={onCancel}
            className="px-5 py-2.5 rounded-xl border border-white/5 text-slate-400 hover:text-white bg-slate-900/50 hover:bg-slate-900 transition-all font-bold text-xs"
          >
            Cancel Run
          </button>
          <button
            onClick={onSubmit}
            className="px-6 py-2.5 rounded-xl bg-gradient-to-r from-sky-400 to-indigo-500 text-slate-950 font-bold text-xs hover:shadow-lg hover:shadow-sky-500/20 active:scale-95 transition-all"
          >
            Submit Inputs
          </button>
        </div>
      </div>
    </div>
  );
}

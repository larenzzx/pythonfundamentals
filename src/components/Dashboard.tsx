import { useState } from 'react';
import { BookOpen, CheckCircle, Clock, Play, Code, Star, Trophy, ArrowRight, Lock, Layers, ShieldAlert } from 'lucide-react';

interface Lesson {
  id: number;
  filename: string;
  title: string;
  sections: {
    tutorial: string;
    activity: string;
    challenge: string;
  };
}

interface DashboardProps {
  lessons: Lesson[];
  progress: Record<number, 'not_started' | 'in_progress' | 'completed'>;
  onSelectLesson: (id: number) => void;
  executedCount: number;
  isAdmin?: boolean;
}

export default function Dashboard({ lessons, progress, onSelectLesson, executedCount, isAdmin }: DashboardProps) {
  const [adminOverride, setAdminOverride] = useState<boolean>(true);
  const completedCount = Object.values(progress).filter(p => p === 'completed').length;
  const inProgressCount = Object.values(progress).filter(p => p === 'in_progress').length;
  const percentComplete = Math.round((completedCount / lessons.length) * 100);
  const hasStarted = completedCount > 0 || inProgressCount > 0;

  // Compute achievements
  const achievements = [
    {
      id: 'first_steps',
      title: 'Hello World!',
      description: 'Completed Lesson 1: Variables and Data Types',
      unlocked: progress[1] === 'completed',
      icon: <Star className="w-5 h-5 text-yellow-400" />
    },
    {
      id: 'logic_wizard',
      title: 'Logic Wizard',
      description: 'Completed Control Flow & Loop structures',
      unlocked: progress[4] === 'completed' && progress[5] === 'completed',
      icon: <Trophy className="w-5 h-5 text-indigo-400" />
    },
    {
      id: 'structure_pro',
      title: 'Data Wrangler',
      description: 'Completed Lists, Dictionaries, and Tuples/Sets',
      unlocked: progress[6] === 'completed' && progress[7] === 'completed' && progress[10] === 'completed',
      icon: <Code className="w-5 h-5 text-cyan-400" />
    },
    {
      id: 'oop_master',
      title: 'Architect',
      description: 'Unlocked Object-Oriented Programming principles',
      unlocked: progress[14] === 'completed',
      icon: <Play className="w-5 h-5 text-emerald-400" />
    },
    {
      id: 'api_architect',
      title: 'API Architect',
      description: 'Mastered HTTP Methods, Status Codes, and JSON',
      unlocked: progress[17] === 'completed',
      icon: <Layers className="w-5 h-5 text-purple-400" />
    },
    {
      id: 'web_dev',
      title: 'Web Developer',
      description: 'Built APIs utilizing the FastAPI web framework',
      unlocked: progress[18] === 'completed',
      icon: <Trophy className="w-5 h-5 text-amber-400" />
    }
  ];

  return (
    <div className="space-y-10 animate-fade-in relative z-10 pb-12">
      {/* Welcome Card & Summary Stats */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        {/* Welcome message */}
        <div className="lg:col-span-2 relative overflow-hidden rounded-2xl border border-white/5 bg-slate-900/60 p-8 backdrop-blur-xl">
          <div className="absolute top-0 right-0 w-80 h-80 bg-gradient-to-br from-sky-500/10 to-indigo-500/10 rounded-full blur-3xl pointer-events-none"></div>
          <div className="relative z-10 flex flex-col justify-between h-full space-y-6">
            <div>
              <span className="text-sky-400 text-xs font-semibold uppercase tracking-wider bg-sky-950/50 px-3 py-1 rounded-full border border-sky-900/50">Personal Workspace</span>
              <h1 className="text-3xl font-extrabold mt-4 text-white tracking-tight sm:text-4xl">
                Welcome to your <span className="bg-gradient-to-r from-sky-400 via-indigo-300 to-amber-200 bg-clip-text text-transparent">Python Sandbox</span>
              </h1>
              <p className="text-slate-400 mt-2 max-w-lg text-sm sm:text-base">
                An interactive coding lab built around your local python files. Practice writing real code, execute it in the browser, and track your learnings in real-time.
              </p>
            </div>
            
            <div className="flex flex-wrap gap-4 items-center pt-2">
              <button 
                onClick={() => {
                  const nextLessonId = lessons.find(l => progress[l.id] !== 'completed')?.id || 1;
                  if (nextLessonId === 1 || progress[nextLessonId - 1] === 'completed') {
                    onSelectLesson(nextLessonId);
                  }
                }}
                className="inline-flex items-center gap-2 bg-gradient-to-r from-sky-400 to-indigo-500 text-slate-950 hover:shadow-lg hover:shadow-sky-500/20 active:scale-95 transition-all duration-200 px-5 py-3 rounded-xl font-bold text-sm"
              >
                <Play className="w-4 h-4 fill-current" />
                {hasStarted ? 'Resume Learning' : 'Start Learning'}
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>

        {/* Circular Progress & Metrics */}
        <div className="rounded-2xl border border-white/5 bg-slate-900/60 p-8 backdrop-blur-xl flex flex-col items-center justify-between text-center relative overflow-hidden">
          <div className="absolute top-0 left-0 w-40 h-40 bg-amber-500/5 rounded-full blur-3xl pointer-events-none"></div>
          <h2 className="text-sm font-semibold text-slate-400 uppercase tracking-wider">Workspace Completion</h2>
          
          <div className="relative my-4 flex items-center justify-center">
            {/* SVG Progress Circle */}
            <svg className="w-32 h-32 transform -rotate-90">
              <circle
                cx="64"
                cy="64"
                r="52"
                className="stroke-slate-800"
                strokeWidth="10"
                fill="transparent"
              />
              <circle
                cx="64"
                cy="64"
                r="52"
                className="stroke-sky-400 transition-all duration-1000 ease-out"
                strokeWidth="10"
                fill="transparent"
                strokeDasharray={326.7}
                strokeDashoffset={326.7 - (326.7 * percentComplete) / 100}
                strokeLinecap="round"
              />
            </svg>
            <div className="absolute flex flex-col items-center justify-center">
              <span className="text-3xl font-extrabold text-white">{percentComplete}%</span>
              <span className="text-xs text-slate-500">{completedCount} / {lessons.length} Done</span>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4 w-full pt-2 border-t border-white/5 text-left">
            <div>
              <div className="text-slate-500 text-[10px] uppercase font-bold tracking-wider">Executed Runs</div>
              <div className="text-lg font-bold text-amber-400 flex items-center gap-1.5 mt-0.5">
                <Code className="w-4 h-4" />
                {executedCount}
              </div>
            </div>
            <div>
              <div className="text-slate-500 text-[10px] uppercase font-bold tracking-wider">In Progress</div>
              <div className="text-lg font-bold text-sky-400 flex items-center gap-1.5 mt-0.5">
                <Clock className="w-4 h-4" />
                {inProgressCount}
              </div>
            </div>
          </div>
        </div>

      </div>

      {/* Grid of Achievements */}
      <div className="space-y-4">
        <h2 className="text-xl font-bold text-white tracking-tight flex items-center gap-2">
          <Trophy className="w-5 h-5 text-amber-400" />
          Milestones & Badges
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {achievements.map((ach) => (
            <div 
              key={ach.id} 
              className={`p-5 rounded-xl border transition-all duration-300 flex items-center gap-4 ${
                ach.unlocked 
                  ? 'bg-slate-900/80 border-sky-500/20 shadow-md shadow-sky-500/5' 
                  : 'bg-slate-950/40 border-white/5 opacity-60'
              }`}
            >
              <div className={`p-2.5 rounded-lg ${ach.unlocked ? 'bg-sky-500/10' : 'bg-slate-800/50'}`}>
                {ach.icon}
              </div>
              <div>
                <h3 className={`text-sm font-bold ${ach.unlocked ? 'text-white' : 'text-slate-400'}`}>{ach.title}</h3>
                <p className="text-xs text-slate-500 mt-0.5">{ach.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Lesson Index Roadmap */}
      <div className="space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <h2 className="text-xl font-bold text-white tracking-tight flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-sky-400" />
            Learning roadmap ({lessons.length} Modules)
          </h2>
          
          {isAdmin && (
            <div className="flex items-center gap-3 bg-indigo-950/30 border border-indigo-900/40 px-3.5 py-2 rounded-xl text-xs font-bold text-indigo-300 shrink-0 select-none">
              <ShieldAlert className="w-4 h-4 text-indigo-400 animate-pulse" />
              <span>Admin Lock Bypass</span>
              <button 
                onClick={() => setAdminOverride(!adminOverride)}
                className={`w-9 h-5 rounded-full transition-colors relative border border-white/5 cursor-pointer flex items-center ${
                  adminOverride ? 'bg-indigo-500' : 'bg-slate-800'
                }`}
                title="Toggle admin lock bypass"
              >
                <span 
                  className={`w-3.5 h-3.5 rounded-full bg-white shadow-sm transition-all absolute ${
                    adminOverride ? 'right-0.5' : 'left-0.5'
                  }`} 
                />
              </button>
            </div>
          )}
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {lessons.map((lesson) => {
            const status = progress[lesson.id] || 'not_started';
            const isUnlocked = (isAdmin && adminOverride) || lesson.id === 1 || progress[lesson.id - 1] === 'completed';
            
            return (
              <div 
                key={lesson.id} 
                onClick={() => isUnlocked && onSelectLesson(lesson.id)}
                className={`group relative flex flex-col justify-between p-6 rounded-xl border transition-all duration-300 ${
                  isUnlocked 
                    ? 'border-white/5 bg-slate-900/40 hover:bg-slate-900/80 hover:border-sky-500/30 hover:-translate-y-1 hover:shadow-lg hover:shadow-sky-500/5 cursor-pointer' 
                    : 'border-white/5 bg-slate-950/10 opacity-40 cursor-not-allowed'
                }`}
              >
                <div>
                  <div className="flex justify-between items-start">
                    <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest font-mono">
                      Module {String(lesson.id).padStart(2, '0')}
                    </span>
                    {status === 'completed' && (
                      <span className="text-emerald-400 bg-emerald-950/40 px-2 py-0.5 rounded text-[10px] font-bold border border-emerald-900/40 flex items-center gap-1">
                        <CheckCircle className="w-3 h-3" />
                        Completed
                      </span>
                    )}
                    {status === 'in_progress' && (
                      <span className="text-sky-400 bg-sky-950/40 px-2 py-0.5 rounded text-[10px] font-bold border border-sky-900/40 flex items-center gap-1">
                        <Clock className="w-3 h-3 animate-pulse" />
                        In Progress
                      </span>
                    )}
                    {status === 'not_started' && isUnlocked && (
                      <span className="text-amber-400 bg-amber-950/30 px-2 py-0.5 rounded text-[10px] font-bold border border-amber-900/40">
                        Available
                      </span>
                    )}
                    {!isUnlocked && (
                      <span className="text-slate-500 bg-slate-950/50 px-2 py-0.5 rounded text-[10px] font-bold border border-slate-900/50 flex items-center gap-1">
                        <Lock className="w-3 h-3" />
                        Locked
                      </span>
                    )}
                  </div>
                  
                  <h3 className="text-base font-bold text-slate-100 mt-3 group-hover:text-sky-300 transition-colors">
                    {lesson.title}
                  </h3>
                  
                  {/* Extract brief tags / topics if possible, else show file path */}
                  <p className="text-xs text-slate-500 mt-2 font-mono break-all bg-slate-950/20 p-2 rounded border border-white/5">
                    {lesson.filename}
                  </p>
                </div>

                <div className="flex items-center justify-between mt-5 pt-4 border-t border-white/5">
                  <span className="text-xs text-slate-400 flex items-center gap-1">
                    <Code className="w-3.5 h-3.5 text-amber-500" />
                    Interactive Sandbox
                  </span>
                  
                  {isUnlocked ? (
                    <span className="text-xs text-sky-400 group-hover:translate-x-1 transition-transform flex items-center gap-1 font-bold">
                      Start Code
                      <ArrowRight className="w-3.5 h-3.5" />
                    </span>
                  ) : (
                    <span className="text-xs text-slate-500 flex items-center gap-1 font-semibold">
                      <Lock className="w-3.5 h-3.5 text-slate-600" />
                      Locked
                    </span>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

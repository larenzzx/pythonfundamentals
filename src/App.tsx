import { useState, useEffect } from 'react';
import { AuthProvider, useAuth } from './hooks/useAuth';
import { supabase } from './lib/supabase';
import Dashboard from './components/Dashboard';
import InteractiveClassroom from './components/InteractiveClassroom';
import WorkspaceExplorer from './components/WorkspaceExplorer';
import CheatSheet from './components/CheatSheet';
import Login from './components/Login';
import ResetPassword from './components/ResetPassword';
import AdminDashboard from './components/AdminDashboard';
import ConfirmationModal from './components/ui/ConfirmationModal';

// Import compiled lessons data
import lessonsData from './data/lessons.json';

import { 
  LayoutDashboard, BookOpen, Monitor, Layers, 
  Terminal, Menu, X, Lock, LogOut, ShieldAlert
} from 'lucide-react';

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

const lessonsList = lessonsData as Lesson[];

function MainLayout() {
  const { user, profile, loading: authLoading, signOut } = useAuth();
  const [activeTab, setActiveTab] = useState<'dashboard' | 'classroom' | 'workspace' | 'cheatsheet' | 'admin'>('dashboard');
  const [selectedLessonId, setSelectedLessonId] = useState<number | null>(null);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState<boolean>(false);
  const [isResettingPassword, setIsResettingPassword] = useState<boolean>(false);
  const [isLogoutModalOpen, setIsLogoutModalOpen] = useState<boolean>(false);
  
  // Progress state: maps lessonId -> status
  const [progress, setProgress] = useState<Record<number, 'not_started' | 'in_progress' | 'completed'>>({});
  const [executedCount, setExecutedCount] = useState<number>(0);
  const [syncing, setSyncing] = useState<boolean>(false);

  // Check URL path for password reset recovery or invite types
  useEffect(() => {
    const isRecovery = window.location.pathname === '/reset-password' || 
                        window.location.hash.includes('type=recovery') ||
                        window.location.search.includes('type=recovery') ||
                        window.location.hash.includes('type=invite') ||
                        window.location.hash.includes('type=signup');
    if (isRecovery) {
      setIsResettingPassword(true);
    }
  }, []);

  // Fetch progress from Supabase once user is loaded
  useEffect(() => {
    if (!user) return;

    const fetchUserProgress = async () => {
      setSyncing(true);
      try {
        const { data, error } = await supabase
          .from('user_progress')
          .select('lesson_id, status')
          .eq('user_id', user.id);

        if (error) throw error;

        const progressMap: Record<number, 'not_started' | 'in_progress' | 'completed'> = {};
        // Seed default locks
        lessonsList.forEach(l => {
          progressMap[l.id] = 'not_started';
        });
        
        // Populate DB records
        if (data) {
          data.forEach((row: any) => {
            progressMap[row.lesson_id] = row.status as 'not_started' | 'in_progress' | 'completed';
          });
        }
        setProgress(progressMap);
      } catch (e) {
        console.error('Failed to load user progress from Supabase:', e);
      } finally {
        setSyncing(false);
      }
    };

    fetchUserProgress();

    // Executed Runs (keep client side or store locally)
    const count = parseInt(localStorage.getItem('py_exec_count') || '0', 10);
    setExecutedCount(count);

    const handleStorageChange = () => {
      const updatedCount = parseInt(localStorage.getItem('py_exec_count') || '0', 10);
      setExecutedCount(updatedCount);
    };
    window.addEventListener('storage', handleStorageChange);
    return () => window.removeEventListener('storage', handleStorageChange);
  }, [user]);

  // Check if a lesson is unlocked
  const isLessonUnlocked = (lessonId: number) => {
    if (profile?.role === 'admin') return true;
    if (lessonId === 1) return true;
    return progress[lessonId - 1] === 'completed';
  };

  // Sync individual lesson progress state with database
  const handleMarkComplete = async (lessonId: number, status: 'completed' | 'in_progress') => {
    if (!user) return;
    
    // Update local state optimistically
    setProgress(prev => ({
      ...prev,
      [lessonId]: status
    }));

    try {
      const { error } = await supabase
        .from('user_progress')
        .upsert({
          user_id: user.id,
          lesson_id: lessonId,
          status: status,
          updated_at: new Date().toISOString()
        }, {
          onConflict: 'user_id,lesson_id' // Requires unique index on (user_id, lesson_id)
        });

      if (error) throw error;
    } catch (e) {
      console.error('Failed to sync lesson progress to Supabase:', e);
    }
  };

  const selectedLesson = lessonsList.find(l => l.id === selectedLessonId);

  // Navigation handlers
  const handleTabChange = (tab: 'dashboard' | 'classroom' | 'workspace' | 'cheatsheet' | 'admin') => {
    setActiveTab(tab);
    setIsMobileMenuOpen(false);
    
    // Automatically select first unlocked lesson if entering classroom without selection
    if (tab === 'classroom' && !selectedLessonId) {
      const firstUnlocked = lessonsList.find(l => isLessonUnlocked(l.id));
      if (firstUnlocked) {
        setSelectedLessonId(firstUnlocked.id);
      }
    }
  };

  const handleSelectLessonFromDashboard = (lessonId: number) => {
    if (isLessonUnlocked(lessonId)) {
      setSelectedLessonId(lessonId);
      setActiveTab('classroom');
    }
  };

  // Loading Screens
  if (authLoading) {
    return (
      <div className="min-h-screen bg-[#060913] text-white flex flex-col items-center justify-center space-y-4">
        <div className="w-10 h-10 border-t-2 border-sky-400 border-solid rounded-full animate-spin"></div>
        <p className="text-xs text-slate-400 font-mono">Syncing sandbox credentials...</p>
      </div>
    );
  }

  // Redirect to Reset Password screen if type=recovery
  if (isResettingPassword) {
    return <ResetPassword />;
  }

  // Redirect to Login if unauthorized
  if (!user) {
    return <Login />;
  }

  return (
    <div className="flex min-h-screen bg-[#060913] text-[#f8fafc] overflow-hidden font-sans relative">
      
      {/* Background Animated Blobs */}
      <div className="absolute top-[-20%] right-[-10%] w-[600px] h-[600px] bg-sky-500/10 rounded-full blur-[140px] pointer-events-none animate-float-slow z-0"></div>
      <div className="absolute bottom-[10%] left-[-20%] w-[500px] h-[500px] bg-amber-500/5 rounded-full blur-[120px] pointer-events-none animate-float-slower z-0"></div>

      {/* Backdrop for Mobile Sidebar Drawer */}
      {isMobileMenuOpen && (
        <div 
          className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 md:hidden"
          onClick={() => setIsMobileMenuOpen(false)}
        />
      )}

      {/* Sidebar Navigation (Fixed on Desktop, Drawer on Mobile) */}
      <aside className={`fixed top-0 bottom-0 left-0 w-64 border-r border-white/5 bg-[#090d16]/95 backdrop-blur-md flex flex-col shrink-0 z-50 h-screen overflow-hidden transition-all duration-300 ${
        isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'
      }`}>
        
        {/* Logo Section */}
        <div className="p-6 border-b border-white/5 flex items-center gap-3">
          <img 
            src="/python-logo.svg" 
            alt="Python Logo" 
            className="w-8 h-8 object-contain animate-pulse-slow"
          />
          <div>
            <h1 className="text-sm font-extrabold tracking-tight text-white">PyFundamentals</h1>
            <span className="text-[10px] text-slate-500 font-mono">WORKSPACE IDE V1.0</span>
          </div>
        </div>

        {/* Navigation List */}
        <nav className="flex-1 p-4 space-y-1.5 overflow-y-auto">
          <button
            onClick={() => handleTabChange('dashboard')}
            className={`w-full flex items-center justify-between px-4 py-3 rounded-xl text-xs font-bold uppercase tracking-wider transition-all duration-200 ${
              activeTab === 'dashboard'
                ? 'bg-gradient-to-r from-sky-400/10 to-indigo-500/10 border-l-2 border-sky-400 text-sky-400 font-extrabold'
                : 'text-slate-400 hover:text-white hover:bg-white/5'
            }`}
          >
            <span className="flex items-center gap-3">
              <LayoutDashboard className="w-4 h-4" />
              Dashboard
            </span>
          </button>
          
          <button
            onClick={() => handleTabChange('classroom')}
            className={`w-full flex items-center justify-between px-4 py-3 rounded-xl text-xs font-bold uppercase tracking-wider transition-all duration-200 ${
              activeTab === 'classroom'
                ? 'bg-gradient-to-r from-sky-400/10 to-indigo-500/10 border-l-2 border-sky-400 text-sky-400 font-extrabold'
                : 'text-slate-400 hover:text-white hover:bg-white/5'
            }`}
          >
            <span className="flex items-center gap-3">
              <BookOpen className="w-4 h-4" />
              Classroom
            </span>
          </button>

          <button
            onClick={() => handleTabChange('workspace')}
            className={`w-full flex items-center justify-between px-4 py-3 rounded-xl text-xs font-bold uppercase tracking-wider transition-all duration-200 ${
              activeTab === 'workspace'
                ? 'bg-gradient-to-r from-sky-400/10 to-indigo-500/10 border-l-2 border-sky-400 text-sky-400 font-extrabold'
                : 'text-slate-400 hover:text-white hover:bg-white/5'
            }`}
          >
            <span className="flex items-center gap-3">
              <Monitor className="w-4 h-4" />
              Workspace
            </span>
          </button>

          <button
            onClick={() => handleTabChange('cheatsheet')}
            className={`w-full flex items-center justify-between px-4 py-3 rounded-xl text-xs font-bold uppercase tracking-wider transition-all duration-200 ${
              activeTab === 'cheatsheet'
                ? 'bg-gradient-to-r from-sky-400/10 to-indigo-500/10 border-l-2 border-sky-400 text-sky-400 font-extrabold'
                : 'text-slate-400 hover:text-white hover:bg-white/5'
            }`}
          >
            <span className="flex items-center gap-3">
              <Layers className="w-4 h-4" />
              Cheat Sheets
            </span>
          </button>

          {/* Admin Dashboard Tab (Only shown to Admin users) */}
          {profile?.role === 'admin' && (
            <button
              onClick={() => handleTabChange('admin')}
              className={`w-full flex items-center justify-between px-4 py-3 rounded-xl text-xs font-bold uppercase tracking-wider transition-all duration-200 ${
                activeTab === 'admin'
                  ? 'bg-indigo-500/10 border-l-2 border-indigo-500 text-indigo-400 font-extrabold'
                  : 'text-slate-500 hover:text-white hover:bg-white/5'
              }`}
            >
              <span className="flex items-center gap-3">
                <ShieldAlert className="w-4 h-4" />
                Admin Panel
              </span>
            </button>
          )}

          {/* Quick Classroom Sub-Tree of unlocked lessons */}
          {activeTab === 'classroom' && (
            <div className="mt-6 pt-4 border-t border-white/5 space-y-1">
              <span className="px-4 text-[9px] font-bold text-slate-500 uppercase tracking-widest block mb-2">
                Lessons Directory
              </span>
              {lessonsList.map(l => {
                const unlocked = isLessonUnlocked(l.id);
                const isCurrent = selectedLessonId === l.id;
                
                return (
                  <button
                    key={l.id}
                    disabled={!unlocked}
                    onClick={() => {
                      setSelectedLessonId(l.id);
                      setIsMobileMenuOpen(false);
                    }}
                    className={`w-full flex items-center justify-between px-4 py-2 rounded-lg text-[11px] text-left transition-all ${
                      isCurrent 
                        ? 'bg-sky-500/10 text-sky-300 font-semibold' 
                        : unlocked 
                          ? 'text-slate-400 hover:text-white hover:bg-white/5' 
                          : 'text-slate-600 cursor-not-allowed opacity-50'
                    }`}
                  >
                    <span className="truncate flex items-center gap-2">
                      <span className="font-mono text-[9px] opacity-75">{String(l.id).padStart(2, '0')}</span>
                      {l.title}
                    </span>
                    {!unlocked && <Lock className="w-3 h-3 text-slate-700 shrink-0" />}
                  </button>
                );
              })}
            </div>
          )}
        </nav>

        {/* Sidebar Footer */}
        <div className="p-4 border-t border-white/5 bg-[#070b12] text-xs space-y-3 shrink-0">
          <div className="flex items-center justify-between text-slate-400 font-mono text-[9px]">
            <span className="truncate max-w-[120px]">{profile?.email || user.email}</span>
            <button 
              onClick={() => setIsLogoutModalOpen(true)}
              className="text-red-400 hover:text-red-300 flex items-center gap-0.5 transition-colors"
              title="Sign Out"
            >
              <LogOut className="w-3 h-3" />
              Exit
            </button>
          </div>
          <div className="flex items-center gap-2 text-slate-500 font-mono text-[10px]">
            <Terminal className="w-3.5 h-3.5 text-amber-500" />
            WASM Compiler: Active
          </div>
        </div>
      </aside>

      {/* Main Content Area (Offset by Pl-64 to accommodate fixed sidebar) */}
      <div className="flex-1 flex flex-col min-w-0 md:pl-64 h-screen overflow-y-auto z-10">
        
        {/* Top Navbar Header */}
        <header className="h-16 border-b border-white/5 bg-[#090d16]/40 backdrop-blur-md flex items-center justify-between px-6 md:px-8 shrink-0 static top-0 z-30">
          <div className="flex items-center gap-3">
            {/* Hamburger Button for Mobile Menu */}
            <button
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              className="p-2 -ml-2 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white transition-colors md:hidden"
              title="Toggle Menu"
            >
              {isMobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>

            <div className="flex items-center gap-2 md:hidden">
              <img src="/python-logo.svg" alt="Python Logo" className="w-6 h-6 object-contain" />
              <span className="text-xs font-bold text-white uppercase tracking-wider">PyFundamentals</span>
            </div>

            <div className="hidden md:block">
              <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest font-mono">
                Learning Space / {activeTab.toUpperCase()}
              </span>
            </div>
          </div>

          {/* Quick Status Pill */}
          <div className="flex items-center gap-4 text-xs font-bold text-slate-400">
            {syncing && (
              <span className="text-[10px] text-slate-500 animate-pulse font-mono">
                Syncing database...
              </span>
            )}
            <div className="bg-slate-900 border border-white/5 rounded-xl px-3.5 py-1.5 flex items-center gap-1.5 shadow-sm">
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              <span className="hidden sm:inline">Browser Runtime Ready</span>
              <span className="sm:hidden">Ready</span>
            </div>
          </div>
        </header>

        {/* Core Pages Routing */}
        <main className="flex-1 p-4 md:p-8 overflow-y-auto">
          {activeTab === 'dashboard' && (
            <Dashboard 
              lessons={lessonsList} 
              progress={progress} 
              onSelectLesson={handleSelectLessonFromDashboard}
              executedCount={executedCount}
              isAdmin={profile?.role === 'admin'}
            />
          )}

          {activeTab === 'classroom' && selectedLesson && (
            <InteractiveClassroom
              lesson={selectedLesson}
              onBack={() => {
                setSelectedLessonId(null);
                setActiveTab('dashboard');
              }}
              onMarkComplete={handleMarkComplete}
              initialProgress={progress[selectedLesson.id] || 'not_started'}
            />
          )}

          {activeTab === 'workspace' && (
            <WorkspaceExplorer 
              lessons={lessonsList} 
              progress={progress}
            />
          )}

          {activeTab === 'cheatsheet' && (
            <CheatSheet />
          )}

          {activeTab === 'admin' && profile?.role === 'admin' && (
            <AdminDashboard />
          )}
        </main>
      </div>

      <ConfirmationModal
        isOpen={isLogoutModalOpen}
        title="Sign Out Confirmation"
        message="Are you sure you want to end your current session and sign out of PyFundamentals?"
        confirmText="Sign Out"
        cancelText="Stay"
        onConfirm={signOut}
        onCancel={() => setIsLogoutModalOpen(false)}
      />
    </div>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <MainLayout />
    </AuthProvider>
  );
}

import { useState } from 'react';
import { supabase } from '../lib/supabase';
import { Lock, Mail, Play, AlertCircle, CheckCircle, Info } from 'lucide-react';

export default function Login() {
  const [mode, setMode] = useState<'login' | 'forgot_password'>('login');
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [successMsg, setSuccessMsg] = useState<string | null>(null);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setErrorMsg(null);
    setSuccessMsg(null);

    try {
      const { error } = await supabase.auth.signInWithPassword({
        email,
        password
      });

      if (error) throw error;
    } catch (err: any) {
      setErrorMsg(err.message || 'Failed to authenticate user.');
    } finally {
      setLoading(false);
    }
  };

  const handleForgotPassword = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setErrorMsg(null);
    setSuccessMsg(null);

    try {
      const { error } = await supabase.auth.resetPasswordForEmail(email, {
        redirectTo: `${window.location.origin}/reset-password`
      });

      if (error) throw error;
      setSuccessMsg('A password recovery email has been sent. Please check your inbox.');
    } catch (err: any) {
      setErrorMsg(err.message || 'Failed to send recovery email.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-[#060913] text-white p-6 relative">
      
      {/* Decorative gradient blobs */}
      <div className="absolute top-1/4 left-1/4 w-80 h-80 bg-sky-500/10 rounded-full blur-[100px] pointer-events-none z-0"></div>
      <div className="absolute bottom-1/4 right-1/4 w-80 h-80 bg-amber-500/5  rounded-full blur-[100px] pointer-events-none z-0"></div>

      <div className="w-full max-w-md bg-[#090d16]/80 border border-white/5 rounded-2xl p-8 backdrop-blur-xl relative z-10 shadow-2xl space-y-6">
        
        {/* Brand logo */}
        <div className="flex flex-col items-center text-center space-y-2">
          <img src="/python-logo.svg" alt="Python Logo" className="w-12 h-12 object-contain" />
          <h1 className="text-2xl font-extrabold tracking-tight text-white mt-2">PyFundamentals</h1>
          <p className="text-xs text-slate-400">Interactive Coding Workspace & Sandbox</p>
        </div>

        {errorMsg && (
          <div className="p-3.5 rounded-xl border border-red-500/20 bg-red-950/20 text-red-400 text-xs flex items-start gap-2">
            <AlertCircle className="w-4 h-4 shrink-0 mt-0.5" />
            <span>{errorMsg}</span>
          </div>
        )}

        {successMsg && (
          <div className="p-3.5 rounded-xl border border-emerald-500/20 bg-emerald-950/20 text-emerald-400 text-xs flex items-start gap-2">
            <CheckCircle className="w-4 h-4 shrink-0 mt-0.5" />
            <span>{successMsg}</span>
          </div>
        )}

        {mode === 'login' ? (
          <form onSubmit={handleLogin} className="space-y-4">
            <div className="space-y-1">
              <label className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">Email Address</label>
              <div className="relative">
                <Mail className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-500" />
                <input
                  type="email"
                  required
                  placeholder="name@domain.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full bg-slate-950/40 border border-white/5 text-white pl-10 pr-4 py-3 text-xs font-semibold rounded-xl focus:outline-none focus:border-sky-500 transition-colors placeholder-slate-600"
                />
              </div>
            </div>

            <div className="space-y-1">
              <div className="flex justify-between items-center">
                <label className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">Password</label>
                <button
                  type="button"
                  onClick={() => { setMode('forgot_password'); setErrorMsg(null); setSuccessMsg(null); }}
                  className="text-[10px] text-sky-400 hover:underline font-semibold"
                >
                  Forgot password?
                </button>
              </div>
              <div className="relative">
                <Lock className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-500" />
                <input
                  type="password"
                  required
                  placeholder="••••••••"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full bg-slate-950/40 border border-white/5 text-white pl-10 pr-4 py-3 text-xs font-semibold rounded-xl focus:outline-none focus:border-sky-500 transition-colors placeholder-slate-600"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full bg-gradient-to-r from-sky-400 to-indigo-500 hover:from-sky-500 hover:to-indigo-600 text-slate-950 font-bold text-xs uppercase tracking-wider py-3.5 rounded-xl active:scale-95 transition-all flex items-center justify-center gap-2 mt-4"
            >
              <Play className="w-3.5 h-3.5 fill-current" />
              {loading ? 'Authenticating...' : 'Sign In'}
            </button>
          </form>
        ) : (
          <form onSubmit={handleForgotPassword} className="space-y-4">
            <div className="space-y-1">
              <label className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">Email Address</label>
              <div className="relative">
                <Mail className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-500" />
                <input
                  type="email"
                  required
                  placeholder="name@domain.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full bg-slate-950/40 border border-white/5 text-white pl-10 pr-4 py-3 text-xs font-semibold rounded-xl focus:outline-none focus:border-sky-500 transition-colors placeholder-slate-600"
                />
              </div>
              <p className="text-[10px] text-slate-500 leading-normal mt-1">
                Enter your email address and we will email you a secure link to update your login password.
              </p>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full bg-gradient-to-r from-sky-400 to-indigo-500 hover:from-sky-500 hover:to-indigo-600 text-slate-950 font-bold text-xs uppercase tracking-wider py-3.5 rounded-xl active:scale-95 transition-all flex items-center justify-center gap-2 mt-4"
            >
              {loading ? 'Sending Recovery Email...' : 'Reset Password'}
            </button>

            <button
              type="button"
              onClick={() => { setMode('login'); setErrorMsg(null); setSuccessMsg(null); }}
              className="w-full text-center text-xs text-slate-400 hover:text-white transition-colors py-2 block font-semibold"
            >
              Back to Login
            </button>
          </form>
        )}

        <div className="border-t border-white/5 pt-4 text-center">
          <div className="text-[10px] text-slate-500 flex items-center justify-center gap-1.5 leading-normal">
            <Info className="w-3.5 h-3.5 text-sky-400 shrink-0" />
            <span>Invite-only system. Contact the administrator to create your account credentials.</span>
          </div>
        </div>

      </div>
    </div>
  );
}

import { useState, useEffect } from 'react';
import { supabase } from '../lib/supabase';
import { useAuth } from '../hooks/useAuth';
import ConfirmationModal from './ui/ConfirmationModal';
import lessonsData from '../data/lessons.json';
import { 
  Users, Trash2, Shield, UserPlus, Info, Check, 
  UserCheck, AlertCircle, RefreshCw, GraduationCap
} from 'lucide-react';

interface ProfileNode {
  id: string;
  email: string;
  role: 'student' | 'admin';
  created_at: string;
  completed_count?: number;
}

const lessonsCount = lessonsData.length;

export default function AdminDashboard() {
  const { user: currentUser } = useAuth();
  const [usersList, setUsersList] = useState<ProfileNode[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [successMsg, setSuccessMsg] = useState<string | null>(null);
  const [actionUserId, setActionUserId] = useState<string | null>(null);
  
  // Custom Modal States
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState<boolean>(false);
  const [deleteTargetId, setDeleteTargetId] = useState<string | null>(null);
  const [deleteTargetEmail, setDeleteTargetEmail] = useState<string>('');

  const fetchUsers = async () => {
    setLoading(true);
    setErrorMsg(null);
    try {
      // Call Postgres security definer function RPC
      const { data, error } = await supabase.rpc('get_all_users');
      
      if (error) throw error;
      setUsersList((data || []) as ProfileNode[]);
    } catch (e: any) {
      console.error('Error fetching users:', e);
      setErrorMsg(e.message || 'Access Denied: Only administrators can query the user registry.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleRoleChange = async (targetId: string, newRole: 'admin' | 'student') => {
    setActionUserId(targetId);
    setErrorMsg(null);
    setSuccessMsg(null);

    if (targetId === currentUser?.id) {
      setErrorMsg('You cannot modify your own administrator role.');
      setActionUserId(null);
      return;
    }

    try {
      const { error } = await supabase
        .from('profiles')
        .update({ role: newRole })
        .eq('id', targetId);

      if (error) throw error;

      setSuccessMsg(`Role updated successfully to ${newRole.toUpperCase()}.`);
      // Update local state
      setUsersList(prev => prev.map(u => u.id === targetId ? { ...u, role: newRole } : u));
    } catch (e: any) {
      setErrorMsg(e.message || 'Failed to update user role.');
    } finally {
      setActionUserId(null);
    }
  };

  const handleDeleteUser = (targetId: string, targetEmail: string) => {
    if (targetId === currentUser?.id) {
      alert('You cannot delete your own admin account.');
      return;
    }
    setDeleteTargetId(targetId);
    setDeleteTargetEmail(targetEmail);
    setIsDeleteModalOpen(true);
  };

  const confirmDeleteUser = async () => {
    if (!deleteTargetId) return;
    
    setActionUserId(deleteTargetId);
    setIsDeleteModalOpen(false);
    setErrorMsg(null);
    setSuccessMsg(null);

    try {
      // Call Postgres security definer function RPC to delete from auth schema
      const { error } = await supabase.rpc('delete_user_by_admin', {
        target_user_id: deleteTargetId
      });

      if (error) throw error;

      setSuccessMsg(`User ${deleteTargetEmail} was successfully deleted from the platform.`);
      // Remove from local list
      setUsersList(prev => prev.filter(u => u.id !== deleteTargetId));
    } catch (e: any) {
      setErrorMsg(e.message || 'Failed to delete user.');
    } finally {
      setActionUserId(null);
      setDeleteTargetId(null);
      setDeleteTargetEmail('');
    }
  };

  // Metrics calculations
  const totalCount = usersList.length;
  const adminCount = usersList.filter(u => u.role === 'admin').length;
  const studentCount = usersList.filter(u => u.role === 'student').length;

  return (
    <div className="space-y-8 animate-fade-in pb-12 relative z-10">
      
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-extrabold text-white tracking-tight flex items-center gap-2">
            <Users className="w-6 h-6 text-sky-400" />
            Admin Control Center
          </h1>
          <p className="text-xs text-slate-400 mt-1">Manage platform users, modify authorization roles, and audit workspace access.</p>
        </div>
        
        <button
          onClick={fetchUsers}
          disabled={loading}
          className="p-2 rounded-xl bg-slate-900 border border-white/5 text-slate-400 hover:text-white hover:bg-slate-800 disabled:opacity-50 transition-all flex items-center gap-1.5 text-xs font-semibold"
          title="Refresh User Directory"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} />
          Refresh
        </button>
      </div>

      {/* Overview stats */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="p-6 bg-slate-900/60 border border-white/5 rounded-2xl flex items-center gap-4">
          <div className="p-3.5 rounded-xl bg-sky-500/10 text-sky-400">
            <Users className="w-6 h-6" />
          </div>
          <div>
            <span className="text-slate-500 text-[10px] uppercase font-bold tracking-wider">Total Users</span>
            <h3 className="text-2xl font-extrabold text-white">{loading ? '...' : totalCount}</h3>
          </div>
        </div>

        <div className="p-6 bg-slate-900/60 border border-white/5 rounded-2xl flex items-center gap-4">
          <div className="p-3.5 rounded-xl bg-indigo-500/10 text-indigo-400">
            <Shield className="w-6 h-6" />
          </div>
          <div>
            <span className="text-slate-500 text-[10px] uppercase font-bold tracking-wider">Administrators</span>
            <h3 className="text-2xl font-extrabold text-white">{loading ? '...' : adminCount}</h3>
          </div>
        </div>

        <div className="p-6 bg-slate-900/60 border border-white/5 rounded-2xl flex items-center gap-4">
          <div className="p-3.5 rounded-xl bg-amber-500/10 text-amber-400">
            <GraduationCap className="w-6 h-6" />
          </div>
          <div>
            <span className="text-slate-500 text-[10px] uppercase font-bold tracking-wider">Students</span>
            <h3 className="text-2xl font-extrabold text-white">{loading ? '...' : studentCount}</h3>
          </div>
        </div>
      </div>

      {/* Notifications */}
      {errorMsg && (
        <div className="p-4 rounded-xl border border-red-500/20 bg-red-950/20 text-red-400 text-xs flex items-start gap-2.5">
          <AlertCircle className="w-4.5 h-4.5 shrink-0 mt-0.5" />
          <span>{errorMsg}</span>
        </div>
      )}

      {successMsg && (
        <div className="p-4 rounded-xl border border-emerald-500/20 bg-emerald-950/20 text-emerald-400 text-xs flex items-start gap-2.5">
          <Check className="w-4.5 h-4.5 shrink-0 mt-0.5" />
          <span>{successMsg}</span>
        </div>
      )}

      {/* Main Grid: User table & Invitation guide */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-start">
        
        {/* Users Table */}
        <div className="lg:col-span-2 bg-slate-900/40 border border-white/5 rounded-2xl overflow-hidden shadow-xl">
          <div className="px-6 py-4 border-b border-white/5 bg-slate-900/40">
            <h3 className="text-sm font-bold text-white tracking-tight uppercase tracking-widest font-mono">User Registry</h3>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs border-collapse">
              <thead>
                <tr className="border-b border-white/5 text-slate-500 font-bold uppercase tracking-wider">
                  <th className="px-6 py-3.5 font-bold">Email Address</th>
                  <th className="px-6 py-3.5 font-bold">Joined Date</th>
                  <th className="px-6 py-3.5 font-bold">Authority Role</th>
                  <th className="px-6 py-3.5 font-bold">Progress</th>
                  <th className="px-6 py-3.5 text-right font-bold">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-white/5 text-slate-300">
                {loading ? (
                  <tr>
                    <td colSpan={5} className="px-6 py-8 text-center text-slate-500 animate-pulse">
                      Loading user directory...
                    </td>
                  </tr>
                ) : usersList.length === 0 ? (
                  <tr>
                    <td colSpan={5} className="px-6 py-8 text-center text-slate-500 italic">
                      No users registered. Use the Invite guide to invite your first user.
                    </td>
                  </tr>
                ) : (
                  usersList.map((usr) => (
                    <tr key={usr.id} className="hover:bg-white/5 transition-colors">
                      <td className="px-6 py-4 font-semibold text-white truncate max-w-xs">{usr.email}</td>
                      <td className="px-6 py-4 font-mono text-[10px] text-slate-500">
                        {new Date(usr.created_at).toLocaleDateString()}
                      </td>
                      <td className="px-6 py-4">
                        <span className={`px-2 py-0.5 rounded text-[10px] font-extrabold uppercase border ${
                          usr.role === 'admin' 
                            ? 'text-indigo-400 bg-indigo-950/40 border-indigo-900/40' 
                            : 'text-amber-400 bg-amber-950/40 border-amber-900/40'
                        }`}>
                          {usr.role}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-slate-400">
                        <div className="flex flex-col gap-1.5 max-w-[120px]">
                          <div className="flex items-center gap-1 text-[10px] font-mono">
                            <span className="text-white font-bold">{usr.completed_count || 0}</span>
                            <span className="text-slate-600">/</span>
                            <span>{lessonsCount}</span>
                            <span className="text-sky-400 font-bold ml-auto">{Math.round(((usr.completed_count || 0) / lessonsCount) * 100)}%</span>
                          </div>
                          <div className="w-full h-1.5 bg-slate-950 border border-white/5 rounded-full overflow-hidden">
                            <div 
                              className="h-full bg-gradient-to-r from-sky-400 to-indigo-500 rounded-full transition-all duration-300"
                              style={{ width: `${Math.min(100, Math.round(((usr.completed_count || 0) / lessonsCount) * 100))}%` }}
                            />
                          </div>
                        </div>
                      </td>
                      <td className="px-6 py-4 text-right flex items-center justify-end gap-2.5">
                        {usr.id !== currentUser?.id ? (
                          <>
                            {usr.role === 'student' ? (
                              <button
                                onClick={() => handleRoleChange(usr.id, 'admin')}
                                disabled={actionUserId !== null}
                                className="px-2.5 py-1.5 rounded-lg border border-indigo-500/20 bg-indigo-500/10 text-indigo-300 hover:bg-indigo-500 hover:text-slate-950 transition-all text-[10px] font-bold"
                                title="Promote to Administrator"
                              >
                                Make Admin
                              </button>
                            ) : (
                              <button
                                onClick={() => handleRoleChange(usr.id, 'student')}
                                disabled={actionUserId !== null}
                                className="px-2.5 py-1.5 rounded-lg border border-amber-500/20 bg-amber-500/10 text-amber-300 hover:bg-amber-500 hover:text-slate-950 transition-all text-[10px] font-bold"
                                title="Demote to Student"
                              >
                                Demote
                              </button>
                            )}
                            
                            <button
                              onClick={() => handleDeleteUser(usr.id, usr.email)}
                              disabled={actionUserId !== null}
                              className="p-1.5 rounded-lg bg-red-500/10 hover:bg-red-500 hover:text-slate-950 text-red-400 transition-all border border-red-500/20"
                              title="Delete User Credentials & Progress"
                            >
                              <Trash2 className="w-3.5 h-3.5" />
                            </button>
                          </>
                        ) : (
                          <span className="text-[10px] text-slate-500 italic flex items-center gap-1 font-semibold">
                            <UserCheck className="w-3.5 h-3.5 text-emerald-400" />
                            Active Admin
                          </span>
                        )}
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>

        {/* Invitation / Admin Help Panel */}
        <div className="p-6 bg-slate-900/60 border border-white/5 rounded-2xl space-y-6">
          <h3 className="text-sm font-bold text-white uppercase tracking-widest font-mono flex items-center gap-2">
            <UserPlus className="w-4 h-4 text-sky-400" />
            Invite Workspace User
          </h3>

          <div className="space-y-4 text-xs text-slate-400 leading-relaxed">
            <p>
              Because you have selected an **invite-only system**, new users can only be registered when they receive a secure token invite link sent directly by you.
            </p>

            <div className="p-4 rounded-xl bg-slate-950/40 border border-white/5 space-y-3">
              <span className="font-bold text-slate-200 block">How to invite a new student:</span>
              <ol className="list-decimal pl-4 space-y-2 text-slate-400">
                <li>Log in to your **Supabase Project Console**.</li>
                <li>Navigate to **Authentication &gt; Users**.</li>
                <li>Click **Add User** and select **Invite User**.</li>
                <li>Enter their email address and click send.</li>
                <li>They will receive an email prompting them to claim their account and set their password!</li>
              </ol>
            </div>

            <div className="p-3 rounded-xl bg-sky-500/5 border border-sky-500/10 flex items-start gap-2.5">
              <Info className="w-4 h-4 text-sky-400 shrink-0 mt-0.5" />
              <p className="text-[11px] leading-normal text-sky-300">
                Once the user clicks the link in their email and sets their password, our database trigger automatically sets up their public workspace profile and gives them student credentials.
              </p>
            </div>
          </div>
        </div>

      </div>

      <ConfirmationModal
        isOpen={isDeleteModalOpen}
        title="Delete User Account"
        message={`Are you absolutely sure you want to delete user ${deleteTargetEmail}? This action is permanent and will completely remove their credentials, workspace profiles, and progress.`}
        confirmText="Yes, Delete"
        cancelText="Cancel"
        onConfirm={confirmDeleteUser}
        onCancel={() => {
          setIsDeleteModalOpen(false);
          setDeleteTargetId(null);
          setDeleteTargetEmail('');
        }}
        type="danger"
      />
    </div>
  );
}

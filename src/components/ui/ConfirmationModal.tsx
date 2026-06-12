import { LogOut, Trash2, RotateCcw, X } from 'lucide-react';

interface ConfirmationModalProps {
  isOpen: boolean;
  title: string;
  message: string;
  confirmText?: string;
  cancelText?: string;
  onConfirm: () => void;
  onCancel: () => void;
  type?: 'danger' | 'warning' | 'info';
}

export default function ConfirmationModal({
  isOpen,
  title,
  message,
  confirmText = 'Confirm',
  cancelText = 'Cancel',
  onConfirm,
  onCancel,
  type = 'info'
}: ConfirmationModalProps) {
  if (!isOpen) return null;

  // Icon switcher based on type
  const getIcon = () => {
    switch (type) {
      case 'danger':
        return (
          <div className="p-3 rounded-full bg-red-500/10 text-red-500">
            <Trash2 className="w-6 h-6" />
          </div>
        );
      case 'warning':
        return (
          <div className="p-3 rounded-full bg-amber-500/10 text-amber-500">
            <RotateCcw className="w-6 h-6" />
          </div>
        );
      default:
        return (
          <div className="p-3 rounded-full bg-sky-500/10 text-sky-400">
            <LogOut className="w-6 h-6" />
          </div>
        );
    }
  };

  // Button style switcher
  const getConfirmButtonStyle = () => {
    switch (type) {
      case 'danger':
        return 'bg-red-500 hover:bg-red-600 text-white shadow-red-500/10';
      case 'warning':
        return 'bg-amber-500 hover:bg-amber-600 text-slate-950 shadow-amber-500/10';
      default:
        return 'bg-sky-500 hover:bg-sky-600 text-slate-950 shadow-sky-500/10';
    }
  };

  return (
    <div className="fixed inset-0 z-[9999] flex items-center justify-center p-4">
      {/* Backdrop */}
      <div 
        className="fixed inset-0 bg-black/60 backdrop-blur-sm transition-opacity"
        onClick={onCancel}
      />

      {/* Modal Box */}
      <div className="relative w-full max-w-md bg-[#090d16] border border-white/5 rounded-2xl p-6 shadow-2xl backdrop-blur-xl animate-fade-in space-y-4">
        
        {/* Close Button */}
        <button 
          onClick={onCancel}
          className="absolute right-4 top-4 p-1.5 rounded-lg hover:bg-white/5 text-slate-400 hover:text-white transition-colors"
        >
          <X className="w-4 h-4" />
        </button>

        {/* Modal Content */}
        <div className="flex flex-col items-center text-center space-y-4 pt-2">
          {getIcon()}
          
          <div className="space-y-1">
            <h3 className="text-base font-bold text-white tracking-tight">{title}</h3>
            <p className="text-xs text-slate-400 leading-normal max-w-sm">{message}</p>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex gap-3 pt-2">
          <button
            onClick={onCancel}
            className="flex-1 bg-slate-900 hover:bg-slate-800 text-slate-300 font-bold text-xs uppercase tracking-wider py-3 rounded-xl border border-white/5 transition-colors"
          >
            {cancelText}
          </button>
          
          <button
            onClick={onConfirm}
            className={`flex-1 font-bold text-xs uppercase tracking-wider py-3 rounded-xl active:scale-95 transition-all shadow-lg ${getConfirmButtonStyle()}`}
          >
            {confirmText}
          </button>
        </div>

      </div>
    </div>
  );
}

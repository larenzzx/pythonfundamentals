import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL || '';
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY || '';

// Fallback to empty client if variables are not filled yet to avoid crash,
// but warn the developer in console.
if (!supabaseUrl || supabaseUrl.includes('your_supabase_project_url_here')) {
  console.warn(
    'Supabase environment variables are missing or placeholders. ' +
    'Please configure VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY in your .env file.'
  );
}

export const supabase = createClient(supabaseUrl, supabaseAnonKey);

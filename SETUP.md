# Setup & Configuration Guide

This guide walks you through running, configuring, hosting, and deploying the **PyFundamentals** interactive learning space.

---

## 1. Local Development Setup

### Prerequisites
- **Node.js**: Version 18.x or higher installed.
- **Python 3**: For editing and coding in the local `.py` scripts.

### Installation
1. Navigate to the project root directory.
2. Install npm dependencies:
   ```bash
   npm install
   ```

### Running the App
Start the Vite local development server:
   ```bash
   npm run dev
   ```
The app will run locally at **[http://localhost:5173/](http://localhost:5173/)**.

---

## 2. Supabase Database Configuration

### A. Find Your API Keys
Log in to your [Supabase Dashboard](https://supabase.com/dashboard) and open your project.
1. Go to **Project Settings** (gear icon) > **API**.
2. **Project URL**: Copy the URL value and paste it as `VITE_SUPABASE_URL` in your `.env` file.
3. **Project API Keys**: Copy the **`anon` / `public`** key.
   *   ⚠️ **IMPORTANT**: Use the key labelled **`anon` / `public`**.
   *   🛑 **WARNING**: Do **NOT** copy the `service_role` / `secret` key. That key bypasses security and must never be put in frontend files.

Paste these values into your [`.env`](file:///.env) file:
```env
VITE_SUPABASE_URL=https://your-project-id.supabase.co
VITE_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### B. Run Database Setup SQL
1. Go to the **SQL Editor** in the Supabase Sidebar.
2. Click **New query**.
3. Copy and paste the SQL Setup script below and click **Run**:

```sql
-- 1. Create profiles table (maps to Auth users)
CREATE TABLE public.profiles (
  id uuid REFERENCES auth.users ON DELETE CASCADE PRIMARY KEY,
  email text NOT NULL,
  role text NOT NULL DEFAULT 'student' CHECK (role IN ('student', 'admin')),
  created_at timestamp with time zone DEFAULT now()
);

-- Enable Row Level Security (RLS) on profiles
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

-- Profiles Policies
CREATE POLICY "Allow public read-access to profiles" ON public.profiles
  FOR SELECT USING (true);

CREATE POLICY "Allow users to update own profile" ON public.profiles
  FOR UPDATE USING (auth.uid() = id);

-- Trigger: Automatically create a profile row when a user signs up
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS trigger AS $$
BEGIN
  INSERT INTO public.profiles (id, email, role)
  VALUES (new.id, new.email, 'student');
  RETURN new;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE OR REPLACE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- 2. Create user_progress table
CREATE TABLE public.user_progress (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id uuid REFERENCES public.profiles(id) ON DELETE CASCADE NOT NULL,
  lesson_id integer NOT NULL,
  status text NOT NULL CHECK (status IN ('not_started', 'in_progress', 'completed')),
  updated_at timestamp with time zone DEFAULT now(),
  UNIQUE (user_id, lesson_id) -- Enable upserting on conflict
);

-- Enable RLS on progress
ALTER TABLE public.user_progress ENABLE ROW LEVEL SECURITY;

-- Progress Policies
CREATE POLICY "Users can view own progress" ON public.user_progress
  FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own progress" ON public.user_progress
  FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own progress" ON public.user_progress
  FOR UPDATE USING (auth.uid() = user_id);

-- 3. Admin Remote Procedure Calls (RPCs)
-- Function to list all users (allowed only for admins)
CREATE OR REPLACE FUNCTION public.get_all_users()
RETURNS TABLE (
  id uuid,
  email text,
  role text,
  created_at timestamptz,
  completed_count bigint
) AS $$
BEGIN
  IF EXISTS (
    SELECT 1 FROM public.profiles 
    WHERE profiles.id = auth.uid() AND profiles.role = 'admin'
  ) THEN
    RETURN QUERY 
    SELECT 
      p.id, 
      p.email, 
      p.role, 
      p.created_at,
      COALESCE(count(up.id) FILTER (WHERE up.status = 'completed'), 0) as completed_count
    FROM public.profiles p
    LEFT JOIN public.user_progress up ON p.id = up.user_id
    GROUP BY p.id, p.email, p.role, p.created_at;
  ELSE
    RAISE EXCEPTION 'Access Denied: Only administrators can view users.';
  END IF;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Function to delete a user from Auth schema (allowed only for admins)
CREATE OR REPLACE FUNCTION public.delete_user_by_admin(target_user_id uuid)
RETURNS void AS $$
BEGIN
  IF EXISTS (
    SELECT 1 FROM public.profiles 
    WHERE profiles.id = auth.uid() AND profiles.role = 'admin'
  ) THEN
    DELETE FROM auth.users WHERE auth.users.id = target_user_id;
  ELSE
    RAISE EXCEPTION 'Access Denied: Only administrators can delete users.';
  END IF;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
```

### C. Promote Yourself to Admin
When you first log in or invite yourself, your profile is created with the `student` role by default.
To make yourself the **Administrator**:
1. Go to the **Table Editor** in Supabase.
2. Select the `profiles` table.
3. Find your row/email.
4. Double-click the `role` cell and change it from `student` to `admin`. Save changes.
*Alternatively, you can run this SQL command in the SQL Editor:*
```sql
UPDATE public.profiles SET role = 'admin' WHERE email = 'your-admin-email@domain.com';
```

### D. Disable Public Signups
1. Go to **Authentication > Providers > Email**.
2. Disable the **"Allow signup"** toggle.
3. Save changes.
4. Invite users by clicking **Add User > Invite User** in the Supabase Users panel.

---

## 3. Deployment & Hosting (Vercel)

### Deploying the App
1. Create a free account on [Vercel](https://vercel.com).
2. Install the Vercel CLI locally or connect your Git repository (GitHub/GitLab/Bitbucket) to the Vercel Dashboard.
3. Import the project.
4. Under **Environment Variables**, configure:
   *   `VITE_SUPABASE_URL` = (Your project url)
   *   `VITE_SUPABASE_ANON_KEY` = (Your anon public key)
5. Click **Deploy**. Vercel will build and host the app on a free `vercel.app` subdomain.

---

## 4. Git Version Control (Pushing Changes)

When you make changes to python files or application layouts, commit and push them using standard Git actions:
```bash
git add .
git commit -m "feat: updated app settings and python template files"
git push origin main
```
If your repository is connected to Vercel, pushing to `main` will automatically trigger a production rebuild and redeployment!

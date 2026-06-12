# PyFundamentals: Vercel Deployment & Invite-Only Flow Guide

This guide explains how to deploy your interactive Python workspace to **Vercel**, how the **Invite-Only System** functions behind the scenes, and how to configure your Supabase settings so that invited users can set up their password and log in successfully.

---

## 🚀 Part 1: Step-by-Step Vercel Deployment

Vercel is the recommended hosting provider for your Vite + React + TypeScript application. Follow these steps to host your application online for free.

### Step 1: Push Your Code to GitHub
Ensure all your project code is committed and pushed to a GitHub repository:
1. Initialize git (if not already done):
   ```bash
   git init
   git add .
   git commit -m "feat: complete application setup with invite routing and confirmation modals"
   ```
2. Create a new repository on GitHub (e.g., `python-fundamentals`).
3. Link and push your local codebase:
   ```bash
   git remote add origin https://github.com/your-username/python-fundamentals.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Import Project into Vercel
1. Log in to [Vercel](https://vercel.com/) (create a free account if you don't have one).
2. On your Vercel Dashboard, click **Add New** > **Project**.
3. Select your GitHub repository from the list and click **Import**.

### Step 3: Configure Project Settings & Environment Variables
On the Vercel import page:
1. **Framework Preset**: Vercel will automatically detect **Vite**. Leave this as default.
2. **Root Directory**: Keep it as `./` (the default).
3. **Environment Variables**: Expand this section and add the two environment variables from your `.env` file:
   * **`VITE_SUPABASE_URL`**: Enter your Supabase Project URL.
   * **`VITE_SUPABASE_ANON_KEY`**: Enter your Supabase Anon Public Key.
   
   > [!IMPORTANT]
   > Ensure these names are copied exactly as shown above. Do **NOT** expose or add your `service_role` or database system passwords.

4. Click **Deploy**. Vercel will build your project and provide a public URL (e.g., `https://python-fundamentals-abc.vercel.app`).

---

## 📧 Part 2: How the Invite Flow Works (And How Users Log In)

The application operates on an **invite-only** basis (`Allow Signup` is disabled in Supabase). Here is the lifecycle of an invited user:

### Why do users get "Invalid Credentials" when typing email/password first?
When you invite a user via the Supabase Dashboard:
1. Supabase creates a user entry under `auth.users` and the `profiles` table is automatically populated.
2. **Crucially, the user does not have a password set yet.**
3. If they attempt to log in using their email and any password on the main screen, Supabase responds with **Invalid credentials** because there is no matching password on file.
4. **They must click the link in their invitation email** to create a password before they can sign in normally.

---

## 🔗 Part 3: Step-by-Step Invitation Setup

To make invitations work correctly for your live Vercel site, you must update the redirect URLs in your Supabase project. Otherwise, Supabase will redirect invited users to `localhost` or block the redirect entirely.

### Step 1: Configure Supabase Authentication Redirects
1. Go to your [Supabase Dashboard](https://supabase.com/dashboard) and select your project.
2. Navigate to **Authentication** (sidebar) > **URL Configuration**.
3. **Site URL**: Enter your live Vercel URL:
   * *Example:* `https://python-fundamentals.vercel.app/`
4. **Redirect URLs**: Add your live URL here as well. Click **Add URL** and paste:
   * `https://python-fundamentals.vercel.app/**` (The `**` acts as a wildcard for routes and hash tokens).
5. Click **Save**.

### Step 2: Send the Invitation
1. Go to **Authentication** > **Users** in Supabase.
2. Click **Add User** > **Invite User**.
3. Enter the email address of the student/user you want to invite.
4. Click **Invite**.

### Step 3: User Accepts & Sets Password (The Login Process)
1. The invited user receives an email with the subject: **"You have been invited"**.
2. They click the **"Accept Invitation"** link inside the email.
3. Supabase redirects them to your live Vercel site URL. The URL will look like:
   `https://python-fundamentals.vercel.app/#access_token=ey...&type=invite`
4. **The App Intercepts the Invite**:
   * The app detects `#type=invite` in the URL.
   * Since Supabase automatically starts a temporary authenticated session from the email token, the app immediately loads the **Reset Password / Choose Password** screen.
5. The user types their desired password and clicks **"Save Password"**.
6. The app updates their credentials on the database.
7. **Subsequent Logins**: The user is now fully configured! They can now log in at any time from the main login portal using their email and the password they just created.

---

## 🛠️ Part 4: Advanced Admin Administration

Once you are set up, you can perform administrative tasks.

### Promote Your User to Admin
By default, new users get the `'student'` role. To make your own account an admin:
1. In Supabase, go to **SQL Editor** > **New Query**.
2. Run the following command:
   ```sql
   UPDATE public.profiles SET role = 'admin' WHERE email = 'your-admin-email@domain.com';
   ```
3. Once updated, logging in will show the **Admin Panel** tab in your sidebar.

### Deleting Users Properly
As an admin, you can delete users directly from the **Admin Panel** in the app.
* The frontend makes a call to the custom RPC `delete_user_by_admin(target_user_id)`.
* This safely removes the user from `auth.users`, and Cascade rules automatically delete their row from `public.profiles` and `public.user_progress`.

---

## 📄 File: `vercel.json` SPA Routing
To prevent Vercel from returning 404 errors when pages are reloaded or direct paths (like `/reset-password`) are entered, the project includes a `vercel.json` file in the root containing:
```json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
```
This guarantees Vercel routes all traffic to the client-side single page app.

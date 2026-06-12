# PyFundamentals — Interactive Python Sandbox & Classroom

PyFundamentals is a premium, full-stack, interactive learning space designed to teach Python fundamentals sequentially. It pairs a guided curriculum of 16 structured lessons with a live WebAssembly-powered Python compiler, automated coding exercises, correctness validation tests, and a secure admin management portal.

---

## 🌟 Core Features

### 1. Dynamic Lesson Roadmap
* **Progressive Locking:** The course contains 16 structured modules. Module 1 is unlocked initially; each subsequent module requires completing both the activity and challenge sections of the previous module.
* **Workspace Locking:** Files inside the workspace explorer are disabled and overlayed with lock modals until their prerequisites are met.

### 2. Three-Stage Lesson Layout
* **Tutorial:** Theoretical explanations and code examples running on a Monaco Editor container in the browser.
* **Activity:** Guided coding exercises. The right-hand editor is kept clean of comments, and the objectives are presented in the left-hand details panel.
* **Mini Challenge:** Real-world coding scenarios designed to test problem-solving skills in the sandbox.

### 3. WebAssembly-powered Sandbox (Pyodide)
* Executes Python code directly in the browser environment at native speed using **Pyodide** (WASM).
* Zero backend server execution required for compiling or running Python code, providing an instant feedback loop for students.

### 4. Real-time Correctness & Assertions Engine
* When a student clicks **"Run Code"** on an Activity or Challenge, a hidden Python unit test checks their variables, types, calculations, and code patterns.
* Prints helpful feedback and hints on failure (e.g., `❌ INCORRECT: Variable 'city' must be a string (text)`) without showing the correct answer, encouraging active learning.
* Green checkmark badges are applied to tabs once they are validated as correct.

### 5. Invite-Only Signup Workflow
* Public signup is disabled to prevent unauthorized access.
* The system uses Supabase Auth email invitations. Clicking the invitation link automatically captures the token, logs the user in, and forces a password creation step before they can proceed.

### 6. Admin Panel
* Administrator accounts can view all registered users and their completion progress logs.
* Admins can promote/demote users between `'student'` and `'admin'` roles.
* Admins can delete users securely. This fires database RPC calls (with `SECURITY DEFINER` privileges) to safely wipe users from both the private Auth schemas and user progress logs.

---

## 💻 Tech Stack

### Frontend & Core Interface
* **Vite + React 19 + TypeScript:** Quick build bundling, typed modules, and dynamic state management.
* **Tailwind CSS:** Rich typography, custom dark-mode colors, glassmorphism, responsive sidebar drawer layouts, and subtle animations.
* **Monaco Editor (`@monaco-editor/react`):** Premium IDE code editor (same engine that powers VS Code) with syntax highlighting, autocomplete, and code formatting.
* **Lucide React:** Iconography for navigation, locks, alerts, and success marks.

### Python Sandbox Runtime
* **Pyodide (v0.26.x):** compiled CPython WebAssembly runtime loaded into the browser context.

### Database, Security & Authentication
* **Supabase (PostgreSQL):**
  * **Auth schema:** Handles secure invitations, email sessions, and passwords.
  * **Row Level Security (RLS):** Strict policies preventing students from writing to profiles or reading other students' progress.
  * **Triggers & PL/pgSQL Functions:** Automatically provisions user profiles upon signup and handles admin RPC operations with restricted security overrides.

### Hosting & Routing
* **Vercel:** Hosts the client bundle and serves the single-page application.
* **Vercel JSON Routing:** Custom rewrites to map all browser queries to `index.html` to prevent 404s on route reloads.

---

## 🛠️ Configuration & Setup Files

Detailed guides for configuring, hosting, and running this application are available in your repository:
* 📖 **[SETUP.md](file:///C:/PythonFundamentals/SETUP.md):** Guides you through local installation, database SQL scripts, and admin setup.
* 🚀 **[DEPLOYMENT.md](file:///C:/PythonFundamentals/DEPLOYMENT.md):** Step-by-step instructions for deploying to Vercel and configuring Supabase Authentication Redirect URLs.

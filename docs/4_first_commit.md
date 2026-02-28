Good. This is a very important moment.

Right now your repo is in a **dangerous but common state**:

* You are on `main`
* You have untracked project files
* If you commit now → you’ll pollute `main`
* No `dev` branch yet
* No feature isolation yet

We fix this cleanly.

---

# 🚨 Step 0 — Do NOT commit on main

We’re going to:

1. Create `dev`
2. Move all work there
3. Keep `main` clean

---

# ✅ Step 1 — Create dev Branch NOW

From current state:

```bash
git checkout -b dev
```

You are now on:

```
dev
```

Verify:

```bash
git branch
```

You should see:

```
main
* dev
```

---

# ✅ Step 2 — Add a Proper .gitignore (VERY IMPORTANT)

Before committing anything, create `.gitignore`:

```bash
touch .gitignore
```

Add this:

```text
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.db

# Virtual env
venv/

# macOS
.DS_Store

# MySQL temp
*.log

# VSCode
.vscode/

# Environment files
.env
```

Save it.

---

# ✅ Step 3 — Stage Everything Cleanly

Now check:

```bash
git status
```

Then:

```bash
git add .
```

Check again:

```bash
git status
```

Make sure `venv/` is NOT included.

---

# ✅ Step 4 — First Proper Commit (On dev)

```bash
git commit -m "Initial project structure with auth engine and DB layer"
```

---

# ✅ Step 5 — Push dev Branch

```bash
git push -u origin dev
```

Now GitHub has:

```
main
dev
```

---

# 🔥 Step 6 — Keep main Clean

Now switch back:

```bash
git checkout main
```

Your `main` branch should still be clean and minimal.

That’s good.

---

# 🧠 From Now On

Workflow becomes:

```
main → stable
dev → integration
feature/* → specific features
```

Next thing you will do:

```bash
git checkout dev
git checkout -b feature/radius-header
```

And start implementing RADIUS header parsing there.

---

# 🎯 Why This Matters

Open source projects die when:

* main is messy
* no branch discipline
* giant commits
* no clear version history

You are building FA3H like infrastructure software.

That requires discipline.

---

# 📌 Next Question

Before we move to feature branch:

Do you want to:

1. Commit a clean README first
2. Create LICENSE file
3. Set up repo metadata (description, topics, etc.)
4. Move straight to `feature/radius-header`

Choose the move.

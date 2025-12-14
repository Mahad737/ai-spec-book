# Chapter 6: Managing Content with Git and GitHub

## 6.1 Why Version Control Matters for a Book

A professional book—especially a technical one—is never written in a single pass. Content evolves through edits, rewrites, fixes, and updates. **Version control** allows you to manage these changes safely and systematically.

Git treats your book like a software project. Every chapter, edit, and improvement is tracked, reversible, and auditable. This is essential when working with AI‑generated drafts, where frequent iteration is expected.

---

## 6.2 Understanding Git vs GitHub

Although often used together, Git and GitHub serve different purposes:

* **Git** → A version control system that runs locally
* **GitHub** → A cloud platform for hosting Git repositories

Git tracks changes on your machine. GitHub stores those changes remotely and enables collaboration, backup, and deployment.

---

## 6.3 Initializing a Git Repository

If your Docusaurus project is not already a Git repository, initialize it:

```
git init
```

Then add all files:

```
git add .
```

Create your first commit:

```
git commit -m "Initial book setup"
```

This commit becomes the foundation of your book’s history.

---

## 6.4 Creating a GitHub Repository

On GitHub:

1. Create a new repository
2. Do not initialize with README
3. Copy the repository URL

Connect your local project:

```
git remote add origin https://github.com/username/my-book.git
git branch -M main
git push -u origin main
```

Your book is now safely stored on GitHub.

---

## 6.5 Organizing Commits Professionally

Good commit habits make long projects manageable.

### Best Practices

* One logical change per commit
* Clear, descriptive commit messages
* Commit chapter‑level changes

### Example Messages

* `Add Chapter 3: Docusaurus setup`
* `Refine AI prompt examples`
* `Fix sidebar ordering`

Avoid committing large unrelated changes together.

---

## 6.6 Branching for Safety and Experiments

Branches allow you to work without risking the main content.

### Common Branches

* `main` → Stable published content
* `drafts` → Experimental or AI‑generated drafts
* `feature/chapter-7` → New chapters

Create a branch:

```
git checkout -b drafts
```

Merge only after review.

---

## 6.7 Working with AI Using Git

AI‑assisted writing benefits greatly from Git.

Recommended workflow:

1. Generate AI draft
2. Commit as draft
3. Edit manually
4. Commit refined version

This preserves both AI output and human improvements.

---

## 6.8 Handling Mistakes and Rollbacks

Mistakes are inevitable.

### Useful Commands

* View history:

```
git log
```

* Undo last commit (keep changes):

```
git reset --soft HEAD~1
```

* Restore a file:

```
git checkout -- filename.md
```

Git gives you confidence to experiment freely.

---

## 6.9 Collaboration and Reviews

GitHub enables collaboration through:

* Pull requests
* Code reviews
* Issue tracking

Even for solo authors, pull requests help review changes objectively before merging.

---

## 6.10 Backup and Reliability

GitHub acts as:

* A backup system
* A publishing source
* A deployment trigger

Your book is safe even if your local machine fails.

---

## 6.11 Chapter Summary

In this chapter, you learned how to:

* Use Git for book version control
* Host your book on GitHub
* Organize commits and branches
* Manage AI‑generated drafts safely

Version control transforms book writing into a reliable, professional process.

---

## 6.12 What’s Next

Chapter 7 will focus on **styling and customization**, including themes, fonts, and visual polish for your book.

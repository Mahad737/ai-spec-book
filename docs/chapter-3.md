# Chapter 3: Setting Up Docusaurus

## 3.1 Why Docusaurus for Book Writing

Docusaurus is a modern static site generator developed by Meta. Although it is mainly used for documentation, its structure makes it an excellent choice for writing **technical and educational books**. It allows authors to focus on content while handling navigation, layout, and deployment automatically.

For spec-driven book creation, Docusaurus provides:

* Clear chapter organization
* Markdown-based writing
* Automatic sidebar navigation
* Easy version control with Git
* Seamless deployment to GitHub Pages

This combination makes it ideal for long-term, maintainable book projects.

---

## 3.2 Prerequisites

Before setting up Docusaurus, make sure the following tools are installed on your system:

* **Node.js** (version 18 or higher)
* **npm** (comes with Node.js)
* **Git**
* A code editor (VS Code recommended)

Verify installation using:

```
node -v
npm -v
git --version
```

If any command fails, resolve it before continuing. Most setup issues are caused by incorrect Node.js versions.

---

## 3.3 Creating a New Docusaurus Project

Navigate to the directory where you want to create your book project and run:

```
npx create-docusaurus@latest my-book classic
```

During setup:

* Choose the **classic** template
* Select **JavaScript** (recommended for beginners)
* Accept default settings unless customization is required

After installation completes, move into the project directory:

```
cd my-book
```

Your Docusaurus project is now ready.

---

## 3.4 Understanding the Project Structure

After setup, the project structure looks like this:

```
my-book/
├── docs/
├── blog/
├── src/
├── static/
├── docusaurus.config.js
├── sidebars.js
├── package.json
```

### Key Components

* **docs/** → Contains all book chapters
* **sidebars.js** → Defines chapter order and navigation
* **docusaurus.config.js** → Main configuration file

For book writing, most work happens inside the `docs` folder.

---

## 3.5 Cleaning the Project for Book Use

Docusaurus includes demo content that is not required for a book. To simplify:

* Remove the `blog` folder if unused
* Delete sample files inside `docs`
* Keep only chapter-related Markdown files

A clean structure improves focus and maintainability.

---

## 3.6 Creating Chapter Files

Inside the `docs` folder, create Markdown files for each chapter:

```
docs/
├── chapter-1-introduction.md
├── chapter-2-book-specification.md
├── chapter-3-docusaurus-setup.md
```

Each file represents a complete chapter of the book.

---

## 3.7 Configuring the Sidebar

Open `sidebars.js` and configure the book structure:

```
module.exports = {
  bookSidebar: [
    'chapter-1-introduction',
    'chapter-2-book-specification',
    'chapter-3-docusaurus-setup'
  ],
};
```

The sidebar functions as the book’s table of contents.

---

## 3.8 Running the Development Server

Start the local development server using:

```
npm start
```

Open your browser at:

```
http://localhost:3000
```

You should now see your book interface with chapters listed in the sidebar. Any changes to Markdown files will appear instantly.

---

## 3.9 Common Errors and Solutions

**Error: package.json not found**

* Ensure you are inside the project directory

**Error: Unsupported Node version**

* Upgrade Node.js to version 18 or higher

**Sidebar not showing chapters**

* Check that sidebar IDs match file names exactly

Most issues are related to incorrect paths or versions.

---

## 3.10 Chapter Summary

In this chapter, you:

* Installed Docusaurus
* Understood the project structure
* Prepared the environment for book writing
* Created chapter files
* Configured the sidebar
* Ran the project locally

Your Docusaurus setup is now complete and ready for content creation.

---

## 3.11 What’s Next

In Chapter 4, we will focus on **structuring chapters professionally**, including headings, long-form readability, internal links, and best practices for technical books.

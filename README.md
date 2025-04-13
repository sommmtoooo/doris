# Doris - Your Journal & Note-Taking Buddy 📚

Doris is a **simple, fast, and flexible journal & note-taking tool** for your terminal.
It helps you manage **daily journals** and **quick notes** using your favorite text editor (**Vim, Nano, Emacs, etc.**).

---

## ✨ Why Doris?

- ✔ **Minimalist & distraction-free**
- ✔ **Uses your preferred editor** (Vim, Nano, Emacs, etc.)
- ✔ **Fast & lightweight** (CLI-first, no bloat)
- ✔ **Easy search & organization**
- ✔ **Fully open-source & customizable**

---

## 🚀 Features

- 📄 **Journaling**: Quickly open a daily journal entry (`doris journal`)
- 📝 **Notes**: Create, organize, and edit notes (`doris note "Meeting Notes"`)
- 🔍 **Search**: Find keywords across notes & journals (`doris search "project"`)
- ⚙ **Editor Customization**: Use Vim, Nano, Emacs, or any other editor (`doris set-editor nano`)
- 📂 **Organized Storage**: Journals & notes are stored in `~/.doris/`
- ❌ **Delete Journals**: Remove old journal entries (`doris delete-journal YYYY-MM-DD`)

---

## 📦 Installation

### **🔢 Run Doris from an Executable**

Check the `assets/` folder for pre-built executables. Download the latest version for your OS and run it directly.

### **♻ Build & Run Locally**

#### **1. Clone the Repository**

```bash
git clone https://github.com/sommmtoooo/doris.git
cd doris
```

#### **2. Set Up Virtual Environment & Install Dependencies**

```bash
python -m venv venv
source venv/bin/activate  # (On Windows use: venv\Scripts\activate)
pip install -r requirements.txt
```

#### **3. Run Doris Locally**

```bash
python doris.py --help
```

#### **4. Build & Package Doris Locally**

- **Run in development mode:**

```bash
briefcase dev
```

- **Build an executable:**

```bash
briefcase package
```

---

## 🛠 Usage

### **📄 Journal Management**

```bash
doris journal         # Open today's journal
doris list-journals   # List all journal entries
doris delete-journal 2024-03-05  # Delete a journal entry by date
```

### **📝 Note-Taking**

```bash
doris note "Meeting"  # Create a note titled 'Meeting'
doris list-notes      # List all notes
doris delete-note "Meeting"  # Delete a specific note
```

### **🔍 Search**

```bash
doris search "project"  # Find occurrences of 'project' in notes & journals
```

### **⚙ Set Preferred Editor**

```bash
doris open vim  # Opens doris folder using preferred editor
doris set-editor vim  # Use Vim as the default editor
```

---

## 💌 Roadmap & Upcoming Features

🚀 **Planned Enhancements:**

- 🎯 **Tagging system** (`doris note "Task" --tags work,urgent`)
- 🔄 **Cloud sync support** (Dropbox, GitHub, etc.)
- 🔐 **Encryption for private entries**
- ⚖ **Interactive TUI Mode** (Optional UI for easier navigation)

---

## 🛠 Contributing

Contributions are welcome! 🎉

1. Fork the repo
2. Create a new branch (`feature-xyz`)
3. Submit a Pull Request

---

## 📝 License

Doris is **MIT Licensed** – use it, modify it, improve it!

📢 **Follow updates & contribute:** [GitHub Link](https://github.com/sommmtoooo/doris.git) 🚀

---

### 📈 Next Steps

- ✅ Add **badges** (Python version, Build status, License)
- ✅ Improve **example screenshots** in README
- ✅ Optimize **installation instructions** for multiple OS
- ✅ Publish Doris as a pre-built package
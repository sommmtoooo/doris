---
# Doris - A Minimalist TUI Journal & Note-Taking Companion 📓

Doris is a **simple, fast, and flexible journal & note-taking tool** for your terminal.
It helps you manage **daily journals** and **quick notes** using your favorite text editor (**Vim, Nano, Emacs, etc.**).

✨ **Why Doris?**
✔ **Minimalist & distraction-free**
✔ **Uses your preferred editor** (Vim, Nano, Emacs, etc.)
✔ **Fast & lightweight** (CLI-first, no bloat)
✔ **Easy search & organization**
✔ **Fully open-source & customizable**
---

## **🚀 Features**

- 📔 **Journaling**: Quickly open a daily journal entry (`doris journal`)
- 📝 **Notes**: Create, organize, and edit notes (`doris note "Meeting Notes"`)
- 🔍 **Search**: Find keywords across notes & journals (`doris search "project"`)
- ⚙ **Editor Customization**: Use Vim, Nano, Emacs, or any other editor (`doris set-editor nano`)
- 📂 **Organized Storage**: Journals & notes are stored in `~/.doris/`

---

## **📦 Installation**

### **1️⃣ Install Using Pip**

```bash
pip install doris-cli
```

### **2️⃣ Clone & Build Locally**

```bash
git clone https://github.com/sommmtoooo/doris.git
cd doris
pip install -r requirements.txt
python doris.py --help
```

---

## **🛠 Usage**

### **📔 Journal Management**

```bash
doris journal         # Open today's journal
doris list-journals   # List all journal entries
```

### **📝 Note-Taking**

```bash
doris note "Meeting"  # Create a note titled 'Meeting'
doris list-notes      # List all notes
```

### **🔍 Search**

```bash
doris search "project"  # Find occurrences of 'project' in notes & journals
```

### **⚙ Set Preferred Editor**

```bash
doris set-editor vim  # Use Vim as the default editor
```

---

## **🔧 Development & Building**

### **1️⃣ Build a Local Executable**

```bash
python build.py build
```

This will generate an executable in `dist/doris`.

### **2️⃣ Run Tests**

```bash
pytest
```

---

## **📌 Roadmap**

🚀 **Upcoming Features**:

- 🏷 **Tagging system** (`doris note "Task" --tags work,urgent`)
- 🔄 **Syncing support** (Cloud & local sync)
- 🔐 **Encryption for private entries**

---

## **🤝 Contributing**

Contributions are welcome! 🎉

1. Fork the repo
2. Create a new branch (`feature-xyz`)
3. Submit a Pull Request

---

## **📝 License**

Doris is **MIT Licensed** – use it, modify it, improve it!

📢 **Follow updates & contribute:** [GitHub Link] 🚀

```

---

### **📌 Next Steps**
🔲 Add **badges** (Python version, Build status, License)
🔲 Improve **example screenshots** in README
🔲 Optimize **installation instructions** for multiple OS

```

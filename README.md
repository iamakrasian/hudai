# Word Vault — Windows Setup Guide

## What is Word Vault?

Word Vault is a personal word tracking system that runs on your local computer. You type one word or many words at a time, and the system does two things depending on whether the word already exists in your collection.

If the word exists, it tells you exactly which file it is saved in. If the word is new, it adds it automatically to the last active file. Each file holds a maximum of 10 words. When a file becomes full, the system creates the next file on its own and continues adding there — so your collection grows file by file without you managing anything manually.

All your words are stored in plain `.txt` files inside a folder called `wordfiles` on your computer. You can open these files in Notepad at any time and read them directly. Nothing is sent to the internet. Everything stays on your machine.

You use it through a simple browser window that opens on your computer — just type words into the search box and press Enter.

---

## Step 1 — Install Python

1. Open your browser and go to **https://www.python.org/downloads/**
2. Click the big yellow **Download Python** button
3. Run the downloaded file (e.g. `python-3.12.x-amd64.exe`)
4. On the first screen of the installer:

   > ⚠️ **Tick the checkbox — "Add python.exe to PATH"** before clicking Install Now.
   > If you skip this, nothing will work.

5. Click **Install Now** and wait for it to finish

---

## Step 2 — Verify Python is installed

1. Press `Windows key + R`, type `cmd`, press **Enter** — a black window opens
2. Type this and press Enter:

   ```
   python --version
   ```

3. You should see something like:

   ```
   Python 3.12.4
   ```

   If you see that, Python is ready. If you see an error, reinstall and make sure you ticked the PATH checkbox.

---

## Step 3 — Create your project folder

1. Open **File Explorer**
2. Go to any location you like, for example `Documents`
3. Right-click → **New → Folder**
4. Name it `WordVault`

   > Example full path: `C:\Users\Akrasian\Documents\WordVault`

5. Copy `word_vault.py` (downloaded from chat) into this folder

---

## Step 4 — Open Command Prompt and navigate to your folder

> ⚠️ **From this step onward, every command runs inside the black Command Prompt (cmd) window — not PowerShell.**
> PowerShell is the blue window. If you see a blue window, close it and open cmd instead.
> To open cmd: press `Windows key + R`, type `cmd`, press Enter.

Once cmd is open, you need to navigate to your `WordVault` folder using the `cd` command.
`cd` stands for "change directory" — it moves you into a folder.

Type this and press Enter (replace the path with wherever you created your folder):

```
cd C:\Users\Akrasian\Documents\WordVault
```

You will see the prompt change to show your folder:

```
C:\Users\Akrasian\Documents\WordVault>
```

That means you are now inside the `WordVault` folder. All commands from here run inside it.

**Useful cd tips:**

```
cd Documents                    navigate into a subfolder one level down
cd Documents\WordVault          navigate into a subfolder two levels down
cd ..                           go one level up (back to the parent folder)
cd C:\Users\Akrasian            navigate to any full path from anywhere
dir                             list all files and folders in the current location
```

---

## Step 5 — Create a virtual environment

Type this and press Enter:

```
python -m venv venv
```

Wait a few seconds. A new folder called `venv` will appear inside `WordVault`.
You only do this **once**.

---

## Step 6 — Activate the virtual environment

Type this and press Enter:

```
venv\Scripts\activate
```

You will see `(venv)` appear at the start of the line:

```
(venv) C:\Users\Akrasian\Documents\WordVault>
```

> You must run this activation command **every time** you open a new cmd window for this project.

---

## Step 7 — Install the required package

Type this and press Enter:

```
pip install streamlit
```

Wait for it to finish. You will see a lot of text scrolling — that is normal.
When it stops and the prompt comes back, it is done.

---

## Step 8 — Run the app

Type this and press Enter:

```
streamlit run word_vault.py
```

Your browser will open automatically at:

```
http://localhost:8501
```

The Word Vault app is now running. Type any word or multiple words (comma or space separated) and press Enter.

---

## Your folder should look like this

```
WordVault\
├── wordfiles\          ← created automatically, stores your word .txt files
├── venv\               ← created in Step 5, do not touch
└── word_vault.py       ← downloaded from chat
```

---

## Daily use — after first setup

Every time you want to open the app:

1. Press `Windows key + R` → type `cmd` → press Enter
2. Navigate to your folder:
   ```
   cd C:\Users\Akrasian\Documents\WordVault
   ```
3. Activate the environment:
   ```
   venv\Scripts\activate
   ```
4. Start the app:
   ```
   streamlit run word_vault.py
   ```
5. Browser opens. Use the app.
6. When done, press `Ctrl + C` in the cmd window to stop.

"""
word_vault.py  —  Simple word tracker
Type one or many words, comma or space separated.
- Word exists  →  tells you which file
- Word is new  →  adds it to the last file (creates new file when full)

Run: streamlit run word_vault.py
"""

import os
import streamlit as st

VAULT_FOLDER = "wordfiles"
MAX_WORDS    = 10

st.set_page_config(page_title="Word Vault", page_icon="📚")
st.title("📚 Word Vault")

# ── File helpers ─────────────────────────────────────────────────────────────

def ensure_vault():
    if not os.path.isdir(VAULT_FOLDER):
        os.makedirs(VAULT_FOLDER)

def get_files():
    ensure_vault()
    return sorted([
        os.path.join(VAULT_FOLDER, f)
        for f in os.listdir(VAULT_FOLDER)
        if f.endswith(".txt")
    ])

def load_all_words():
    """Return {word_lowercase: filename} for every word across all files."""
    word_map = {}
    for fpath in get_files():
        fname = os.path.basename(fpath)
        for line in open(fpath, encoding="utf-8"):
            w = line.strip().lower()
            if w:
                word_map[w] = fname
    return word_map

def count_words(fpath):
    try:
        return sum(1 for line in open(fpath, encoding="utf-8") if line.strip())
    except FileNotFoundError:
        return 0

def add_word(word):
    """Append word to last file. Creates a new file if last one is full."""
    ensure_vault()
    files = get_files()
    if not files or count_words(files[-1]) >= MAX_WORDS:
        n      = len(files) + 1
        target = os.path.join(VAULT_FOLDER, f"words_{n:03d}.txt")
        open(target, "w", encoding="utf-8").close()
    else:
        target = files[-1]
    with open(target, "a", encoding="utf-8") as f:
        f.write(word.strip() + "\n")
    return os.path.basename(target)

# ── Sidebar stats ─────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("### Stats")
    files     = get_files()
    all_words = load_all_words()
    st.write(f"**Files:** {len(files)}")
    st.write(f"**Total words:** {len(all_words)}")
    if files:
        st.write(f"**Latest file:** {count_words(files[-1])} / {MAX_WORDS} words")
    st.divider()
    st.markdown("### Files")
    for f in reversed(files):
        st.caption(f"{os.path.basename(f)}  —  {count_words(f)} words")
    st.divider()
    MAX_WORDS = st.number_input("Max words per file", 1, 200, MAX_WORDS, step=1)

# ── Main input ────────────────────────────────────────────────────────────────

raw = st.text_input("Enter word(s) — separate multiple words with commas or spaces")

if raw:
    # Split on commas or whitespace, remove blanks
    import re
    words = [w.strip() for w in re.split(r"[,\s]+", raw) if w.strip()]

    all_words = load_all_words()   # reload after any additions

    for word in words:
        key = word.lower()
        if key in all_words:
            st.info(f"**{word}** — already in `{all_words[key]}`")
        else:
            saved_to = add_word(word)
            all_words[key] = saved_to   # update local map so next word sees it
            st.success(f"**{word}** — added to `{saved_to}`")

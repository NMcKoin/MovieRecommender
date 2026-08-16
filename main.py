import re
import json
import tkinter as tk
from tkinter import ttk
from typing import List, Dict, Any

# ---------------------------------------------------------
# 1. Knowledge Base (Example Items)
# ---------------------------------------------------------

def load_database(path="database.json"):
    with open(path, "r") as f:
        return json.load(f)

ITEMS = load_database()

# ---------------------------------------------------------
# 2. Keyword Extraction
# ---------------------------------------------------------

KEYWORD_MAP = {
    "genres": ["action", "adventure", "horror", "comedy", "drama", "sci-fi",
               "fantasy", "thriller", "rpg", "fps", "strategy", "sandbox"],
    "tones": ["dark", "lighthearted", "serious", "goofy", "emotional", "gritty"],
    "pacing": ["fast", "slow", "story-heavy", "dialogue-heavy"],
    "content": ["magic", "space", "zombies", "romance", "cyberpunk", "medieval"],
}

def extract_preferences(text: str) -> Dict[str, Any]:
    text = text.lower()
    prefs = {category: [] for category in KEYWORD_MAP}

    for category, words in KEYWORD_MAP.items():
        for w in words:
            if w in text:
                prefs[category].append(w)

    return prefs

# ---------------------------------------------------------
# 3. Rule Engine (Platform-Neutral)
# ---------------------------------------------------------

def score_item(item: Dict[str, Any], prefs: Dict[str, Any]) -> int:
    score = 0

    # Genre matches
    for g in prefs["genres"]:
        if g in item["genre"]:
            score += 3

    # Tone matches
    for t in prefs["tones"]:
        if t in item["tone"]:
            score += 2

    # Pacing matches
    for p in prefs["pacing"]:
        if p == item["pacing"]:
            score += 2

    # Content keyword matches
    for c in prefs["content"]:
        if c in item["keywords"]:
            score += 1

    # Composite rule example
    if "dark" in prefs["tones"] and "fantasy" in prefs["genres"]:
        if "dark" in item["tone"] and "fantasy" in item["genre"]:
            score += 4

    return score

# ---------------------------------------------------------
# 4. Recommendation Function
# ---------------------------------------------------------

def recommend(text: str) -> List[Dict[str, Any]]:
    prefs = extract_preferences(text)
    results = []

    for item in ITEMS:
        s = score_item(item, prefs)
        results.append({"item": item, "score": s})

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

# ---------------------------------------------------------
# 5. Example Usage
# ---------------------------------------------------------

if __name__ == "__main__":
    user_input = "I want a dark fantasy game, story-heavy but not slow."
    recs = recommend(user_input)

    print("\nRecommendations:\n")
    for r in recs:
        print(f"{r['item']['title']}  (Score: {r['score']})")

# ---------------------------------------------------------
# 6. Console UI
# ---------------------------------------------------------


        
# ---------------------------------------------------------
# 7. Tkinter GUI
# ---------------------------------------------------------

def run_gui():
    root = tk.Tk()
    root.title("Movie/Game Recommender")
    root.geometry("700x700")
    root.resizable(False, False)

    ttk.Label(root, text="Rule-Based Recommender", font=("Arial", 20)).pack(pady=10)

    # Show available options
    options_frame = ttk.Frame(root)
    options_frame.pack(pady=10)

    def make_label(title, items):
        text = f"{title}: " + ", ".join(items)
        ttk.Label(options_frame, text=text, wraplength=650, justify="left").pack(anchor="w", pady=5)

    make_label("Genres", KEYWORD_MAP["genres"])
    make_label("Tones", KEYWORD_MAP["tones"])
    make_label("Pacing", KEYWORD_MAP["pacing"])
    make_label("Content Keywords", KEYWORD_MAP["content"])

    # Input box
    ttk.Label(root, text="Describe what you want:", font=("Arial", 14)).pack(pady=10)

    input_box = tk.Text(root, height=4, width=80)
    input_box.pack()

    # Results box
    results_box = tk.Text(root, height=20, width=80)
    results_box.pack(pady=10)

    # Recommend button (bigger)
    style = ttk.Style()
    style.configure("Large.TButton", font=("Arial", 16))

    def on_recommend():
        user_text = input_box.get("1.0", tk.END).strip()
        recs = recommend(user_text)

        results_box.delete("1.0", tk.END)

        if not recs:
            results_box.insert(tk.END, "No matches found.\n")
            return

        for r in recs[:10]:
            results_box.insert(tk.END, f"{r['item']['title']} (Score: {r['score']})\n")

    recommend_btn = ttk.Button(root, text="Recommend", command=on_recommend, style="Large.TButton")
    recommend_btn.pack(pady=20, ipadx=20, ipady=10)

    root.mainloop()


if __name__ == "__main__":
    run_gui()
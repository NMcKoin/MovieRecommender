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
def build_keyword_map(items):
    genres = set()
    tones = set()
    pacing = set()
    content = set()

    for item in items:
        for g in item.get("genre", []):
            genres.add(g.lower())

        for t in item.get("tone", []):
            tones.add(t.lower())

        p = item.get("pacing")
        if p:
            pacing.add(p.lower())

        for k in item.get("keywords", []):
            content.add(k.lower())

    return {
        "genres": sorted(genres),
        "tones": sorted(tones),
        "pacing": sorted(pacing),
        "content": sorted(content)
    }

KEYWORD_MAP = build_keyword_map(ITEMS)

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
    prefs = extract_preferences(text.lower())

    # Detect user intent
    want_game = "game" in text.lower() or "play" in text.lower()
    want_movie = "movie" in text.lower() or "watch" in text.lower()

    # Filter items based on intent
    filtered_items = []
    for item in ITEMS:
        if want_game and item["type"] != "game":
            continue
        if want_movie and item["type"] != "movie":
            continue
        filtered_items.append(item)

    # Score filtered items
    results = []
    for item in filtered_items:
        s = score_item(item, prefs)
        results.append({"item": item, "score": s})

    # Sort and limit to 10
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:10]

# ---------------------------------------------------------
# 5. Example Usage
# ---------------------------------------------------------

#   user_input = "I want a dark fantasy game, story-heavy but not slow."
 #   recs = recommend(user_input)
#
#    print("\nRecommendations:\n")
#    for r in recs:
#        print(f"{r['item']['title']}  (Score: {r['score']})")

# ---------------------------------------------------------
# 6. Console UI
# ---------------------------------------------------------


        
# ---------------------------------------------------------
# 7. Tkinter GUI
# ---------------------------------------------------------

def run_gui():
    root = tk.Tk()
    root.title("Movie/Game Recommender")
    root.geometry("700x650")
    root.resizable(False, False)

    # Title
    ttk.Label(root, text="Rule-Based Recommender", font=("Arial", 22)).pack(pady=15)

    # Main question
    ttk.Label(root, text="What are you in the mood for?", font=("Arial", 16)).pack(pady=10)

    # Example inputs
    example_frame = ttk.Frame(root)
    example_frame.pack(pady=5)

    ttk.Label(
        example_frame,
        text="Example (Game): \"I want a lighthearted Disney game with keyblades\"",
        font=("Arial", 11),
        foreground="#555"
    ).pack(anchor="w", pady=2)

    ttk.Label(
        example_frame,
        text="Example (Movie): \"I'm in the mood for a dark sci-fi space thriller\"",
        font=("Arial", 11),
        foreground="#555"
    ).pack(anchor="w", pady=2)

    # Input box
    input_box = tk.Text(root, height=4, width=80, font=("Arial", 12))
    input_box.pack(pady=15)

    # Results box
    results_box = tk.Text(root, height=20, width=80, font=("Arial", 12))
    results_box.pack(pady=10)

    # Button style
    style = ttk.Style()
    style.configure("Large.TButton", font=("Arial", 16))

    # Recommend button
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
from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3
import requests
import random
import os

app = Flask(__name__)

# ---- SQLite Setup ----
db = sqlite3.connect("mood_journal.db", check_same_thread=False)
cursor = db.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    mood_label TEXT,
    mood_score REAL
)
""")
db.commit()

# ---- Hugging Face API ----
HF_API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
HF_HEADERS = {"Authorization": f"Bearer {os.getenv('HF_API_TOKEN', 'YOUR_HUGGINGFACE_API_TOKEN')}"}

def get_emotion(text, use_dummy=False):
    if use_dummy:
        labels = ["POSITIVE", "NEGATIVE", "NEUTRAL"]
        label = random.choice(labels)
        score = round(random.uniform(0.5, 1.0), 2)
        return label, score
    
    try:
        response = requests.post(HF_API_URL, headers=HF_HEADERS, json={"inputs": text}, timeout=60)
        result = response.json()
        if isinstance(result, list) and len(result) > 0:
            return result[0]['label'], float(result[0].get('score', 0))
        return "NEUTRAL", 0.5
    except Exception as e:
        print("Error fetching from HF API:", e)
        return "NEUTRAL", 0.5

# ---- Routes ----
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    entry = request.form.get("entry")
    use_dummy = request.form.get("dummyToggle") == "on"
    
    label, score = get_emotion(entry, use_dummy)
    
    cursor.execute(
        "INSERT INTO entries (text, mood_label, mood_score) VALUES (?, ?, ?)",
        (entry, label, score)
    )
    db.commit()
    
    return redirect(url_for('index'))

@app.route("/get_data")
def get_data():
    cursor.execute("SELECT mood_label, mood_score FROM entries ORDER BY id ASC")
    data = cursor.fetchall()
    return jsonify(data)

# ---- Run app ----
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

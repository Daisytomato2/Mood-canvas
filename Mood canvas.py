import tkinter as tk
import random
import difflib

# Expanded emotion alias mapping
emotion_aliases = {
    # Happy
    "happy": "happy", "joyful": "happy", "content": "happy", "glad": "happy", "cheerful": "happy", "pleased": "happy",
    
    # Sad
    "sad": "sad", "melancholy": "sad", "down": "sad", "depressed": "sad", "blue": "sad", "unhappy": "sad",
    
    # Angry
    "angry": "angry", "mad": "angry", "furious": "angry", "irritated": "angry", "annoyed": "angry",
    
    # Relaxed
    "relaxed": "relaxed", "calm": "relaxed", "peaceful": "relaxed", "serene": "relaxed", "chill": "relaxed",
    
    # Anxious
    "anxious": "anxious", "nervous": "anxious", "worried": "anxious", "stressed": "anxious", "uneasy": "anxious",
    
    # Surprised
    "surprised": "surprised", "shocked": "surprised", "amazed": "surprised", "astonished": "surprised",
    
    # Love
    "love": "love", "loving": "love", "affectionate": "love", "romantic": "love", "caring": "love",
    
    # Bored
    "bored": "bored", "uninterested": "bored", "disinterested": "bored", "uninspired": "bored",
    
    # Confused
    "confused": "confused", "puzzled": "confused", "perplexed": "confused", "lost": "confused",
    
    # Excited
    "excited": "excited", "thrilled": "excited", "elated": "excited", "ecstatic": "excited",
    
    # Tired
    "tired": "tired", "exhausted": "tired", "sleepy": "tired", "fatigued": "tired",
    
    # Scared
    "scared": "scared", "afraid": "scared", "terrified": "scared", "panicked": "scared",
    
    # Grateful
    "grateful": "grateful", "thankful": "grateful", "appreciative": "grateful",

    # Confident
    "confident": "confident", "proud": "confident", "assured": "confident", "bold": "confident",
    
    # Embarrassed
    "embarrassed": "embarrassed", "ashamed": "embarrassed", "humiliated": "embarrassed",
    
    # Lonely
    "lonely": "lonely", "isolated": "lonely", "abandoned": "lonely",
    
    # Curious
    "curious": "curious", "interested": "curious", "inquisitive": "curious",
    
    # Guilty
    "guilty": "guilty", "remorseful": "guilty", "regretful": "guilty",
    
    # Jealous
    "jealous": "jealous", "envious": "jealous",
    
    # Sick
    "sick": "sick", "ill": "sick", "unwell": "sick", "nauseous": "sick",
    
    # Determined
    "determined": "determined", "focused": "determined", "persistent": "determined",
}

# Emotion color and emoji mapping
emotion_colors = {
    "happy": ("#FFD700", "😊"),
    "sad": ("#87CEFA", "😢"),
    "angry": ("#FF6347", "😡"),
    "relaxed": ("#98FB98", "😌"),
    "anxious": ("#D3D3D3", "😰"),
    "surprised": ("#FFA500", "😲"),
    "love": ("#FFB6C1", "🥰"),
    "bored": ("#CCCCCC", "😐"),
    "confused": ("#DA70D6", "😕"),
    "excited": ("#FF69B4", "🤩"),
    "tired": ("#A9A9A9", "😴"),
    "scared": ("#8B0000", "😱"),
    "grateful": ("#ADD8E6", "🙏"),
    "confident": ("#20B2AA", "😎"),
    "embarrassed": ("#FFC0CB", "😳"),
    "lonely": ("#778899", "😔"),
    "curious": ("#F0E68C", "🧐"),
    "guilty": ("#D2B48C", "😞"),
    "jealous": ("#9ACD32", "😒"),
    "sick": ("#B0C4DE", "🤢"),
    "determined": ("#4682B4", "💪"),
}

# Fuzzy matching function
def get_closest_emotion(word):
    all_keywords = list(emotion_aliases.keys())
    match = difflib.get_close_matches(word.lower(), all_keywords, n=1, cutoff=0.7)
    if match:
        return emotion_aliases[match[0]]
    return None

# Create main window
root = tk.Tk()
root.title("Emotion-Based Color Interface")
root.geometry("400x400")

canvas = tk.Canvas(root, width=400, height=400, highlightthickness=0)
canvas.pack(fill="both", expand=True)

def draw_emojis(emoji):
    canvas.delete("emoji")
    for _ in range(10):
        x = random.randint(20, 380)
        y = random.randint(20, 330)
        canvas.create_text(x, y, text=emoji, font=("Arial", 20), tags="emoji")

# UI components
label = tk.Label(canvas, text="Enter your emotion:", font=("Arial", 14), bg="white")
canvas.create_window(200, 30, window=label)

emotion_entry = tk.Entry(canvas, font=("Arial", 14))
canvas.create_window(200, 70, window=emotion_entry)

status_label = tk.Label(canvas, text="", font=("Arial", 12), bg="white")
canvas.create_window(200, 110, window=status_label)

# Show supported emotions
unique_emotions = sorted(set(emotion_aliases.values()))
supported_emotions = ", ".join(unique_emotions)
support_label = tk.Label(
    canvas,
    text=f"Supported emotions:\n{supported_emotions}",
    font=("Arial", 9),
    bg="white",
    fg="gray",
    wraplength=380,
    justify="center"
)
canvas.create_window(200, 260, window=support_label)

# Change background function
def change_color():
    input_emotion = emotion_entry.get().strip().lower()
    mapped_emotion = get_closest_emotion(input_emotion)
    if mapped_emotion and mapped_emotion in emotion_colors:
        color, emoji = emotion_colors[mapped_emotion]
        canvas.configure(bg=color)
        status_label.config(text=f"Detected emotion: {mapped_emotion}", fg="black", bg=color)
        draw_emojis(emoji)
    else:
        canvas.configure(bg="white")
        status_label.config(text="Emotion not recognized. Please try again.", fg="red", bg="white")
        canvas.delete("emoji")

# Button
btn = tk.Button(canvas, text="Change Color", font=("Arial", 14), command=change_color)
canvas.create_window(200, 170, window=btn)

# Run app
root.mainloop()

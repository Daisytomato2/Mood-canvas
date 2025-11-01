# Mood-canvas


An interactive Tkinter application that changes its background color and displays emojis based on your emotion.  
Enter an emotion like “happy”, “sad”, or “angry” and see your mood visualized �



##  Features

-  **Emotion Recognition**: Automatically detect and map your input to a standard emotion, including synonyms.  
-  **Dynamic Background**: Changes the interface color according to the detected emotion.  
-  **Emoji Animation**: Randomly display multiple emojis to enhance the mood.  
-  **Fuzzy Matching**: Recognizes emotions even if the spelling is slightly off (e.g., “happpy”).  
-  **Wide Emotion Support**: Includes 20+ basic emotions and many synonyms.



##  Supported Emotions

- 😄 **Happy** – joyful, glad, cheerful  
- 😢 **Sad** – melancholy, down, blue  
- 😡 **Angry** – mad, furious, irritated  
- 😌 **Relaxed** – calm, peaceful, chill  
- 😰 **Anxious** – nervous, worried, stressed  
- 🥰 **Love** – affectionate, caring  
- 😐 **Bored** – uninterested, uninspired  
- 😕 **Confused** – puzzled, lost  
- 🤩 **Excited** – thrilled, elated  
- 😴 **Tired** – sleepy, fatigued  
- 😱 **Scared** – afraid, terrified  
- 🙏 **Grateful** – thankful, appreciative  
- 😎 **Confident** – proud, bold  
- 😳 **Embarrassed** – ashamed, humiliated  
- 😔 **Lonely** – isolated, abandoned  
- 🧐 **Curious** – interested, inquisitive  
- 😞 **Guilty** – remorseful, regretful  
- 😒 **Jealous** – envious  
- 🤢 **Sick** – ill, unwell  
- 💪 **Determined** – focused, persistent



##  How It Works

- **Emotion Mapping**:  
  A dictionary (`emotion_aliases`) maps many emotion synonyms to standard emotion categories.

- **Fuzzy Matching**:  
  Uses `difflib.get_close_matches()` to detect emotions even with slight spelling mistakes.

- **Visual Feedback**:  
  Changes the background color of a `tk.Canvas` and draws emojis dynamically.

- **User Interface**:  
  Simple Tkinter UI with input box, button, and status label.




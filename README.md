# Sentiment Analysis Project
 # 💬 Sentiment Analysis CLI Tool using TextBlob

A beginner-friendly **Python command-line tool** that uses `TextBlob` to analyze the **sentiment** of text comments. It identifies whether a comment is **positive**, **neutral**, or **negative**, and displays a corresponding message with emojis for an engaging experience.

---

## 🚀 How It Works

1. Run the script.
2. Enter a comment.
3. It shows:
   - The sentiment polarity score (from -1 to 1)
   - The sentiment category: Positive 😊👍, Neutral 😐, or Negative 😞👎
4. Repeat until you type `exit`.

---

## 🧠 Technologies Used

- Python 3
- TextBlob (for sentiment analysis)

---

## 📥 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/sentiment-analysis-cli.git
cd sentiment-analysis-cli

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install textblob
python -m textblob.download_corpora



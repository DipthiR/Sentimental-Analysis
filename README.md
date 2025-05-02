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

💻 Usage
bash
Copy
Edit
python sentiment_analyzer.py
✨ Sample Output:
pgsql
Copy
Edit
Enter the comment here (or type 'exit' to quit): I love this!

Comment: "I love this!"
Polarity: 0.50
Sentiment: Positive 😊👍
Thank you For Your Comment

Enter the comment here (or type 'exit' to quit): This is awful.

Comment: "This is awful."
Polarity: -1.00
Sentiment: Negative 😞👎
We're sorry to hear that. 💔
📄 File Overview
bash
Copy
Edit
sentiment-analysis-cli/
├── sentiment_analyzer.py   # Python script for analysis
└── README.md               # This file
📜 License
MIT License

👤 Author
Your Name

GitHub: @yourusername

yaml
Copy
Edit

---

Let me know if you want me to include:
- A `requirements.txt` file
- Color output with `colorama`
- CSV export functionality  
Happy to help!
💻 Usage
bash
Copy
Edit
python sentiment_analyzer.py
✨ Sample Output:
pgsql
Copy
Edit
Enter the comment here (or type 'exit' to quit): I love this!

Comment: "I love this!"
Polarity: 0.50
Sentiment: Positive 😊👍
Thank you For Your Comment

Enter the comment here (or type 'exit' to quit): This is awful.

Comment: "This is awful."
Polarity: -1.00
Sentiment: Negative 😞👎
We're sorry to hear that. 💔
📄 File Overview
bash
Copy
Edit
sentiment-analysis-cli/
├── sentiment_analyzer.py   # Python script for analysis
└── README.md               # This file

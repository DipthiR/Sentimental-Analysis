from textblob import TextBlob

def analyze_comment(comment):
    analysis = TextBlob(comment)
    polarity = analysis.sentiment.polarity

    print(f"\nComment: \"{comment}\"")
    print(f"Polarity: {polarity:.2f}")
    
    if polarity > 0:
        print("Sentiment: Positive 😊👍\nThank you For Your Comment")
    elif polarity == 0:
        print("Sentiment: Neutral 😐")
    else:
        print("Sentiment: Negative 😞👎\nWe're sorry to hear that. 💔")

# Main loop
while True:
    user_input = input("Enter the comment here (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    analyze_comment(user_input)

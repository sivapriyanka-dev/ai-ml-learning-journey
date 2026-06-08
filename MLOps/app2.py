def predict_spam(message):

    spam_words = [
        "free",
        "win",
        "prize",
        "offer"
    ]

    message = message.lower()

    for word in spam_words:

        if word in message:
            return "Spam"

    return "Not Spam"


message = (
    "You won a free prize!"
)

prediction = predict_spam(
    message
)

print(
    "Message:",
    message
)

print(
    "Prediction:",
    prediction
)

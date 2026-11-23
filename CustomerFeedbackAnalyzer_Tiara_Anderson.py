# Customer Feedback Analyzer for Processing and Prioritizing Customer Reviews

print("**********************************************")
print("** WELCOME TO CUSTOMER FEEDBACK ANALYZER **")
print("**********************************************")

while True:
    feedback = input("Enter feedback here: ")
    trimmedFeedback = feedback.strip()
    lowerFeedback = trimmedFeedback.lower()

    print("\n--- Analysis Results ---")
    print("Original Feedback: ", feedback)
    print("Trimmed & Lowercased Feedback: ", lowerFeedback)

    refundCount = lowerFeedback.count("refund")
    replacementCount = lowerFeedback.count("replacement")

    print("Keyword 'refund':", refundCount)
    print("Keyword 'replacement':", replacementCount)

    updatedFeedback = lowerFeedback.replace("asap", "as soon as possible")
    print("Updated Feedback: ", updatedFeedback)

    firstSentence = trimmedFeedback.split(".", 1)[0]
    print("First Sentence: ", firstSentence)

    if "thank you" in lowerFeedback or "thanks" in lowerFeedback:
        print("Customer expressed gratitude!")
    else:
        print("No gratitude detected.")

    wordCount = len(trimmedFeedback.split())

    print("\n--- Advanced Analysis ---")
    print("Word count: ", wordCount)

    words = trimmedFeedback.split()

    for word in words:
        cleanWord = word.strip(".,!?")
        if len(cleanWord) >= 3 and cleanWord.isupper():
            print("Capitalized word found: ", cleanWord)

    again = input("\nWould  you like to analyze more reviews (Type 'y' to continue or 'n' to exit)?:")

    if again.lower() == "n":
        print("Goodbye!")
        break

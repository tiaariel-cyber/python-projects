# Question Extraction and Reporting System
# Tiara Anderson

# Open the customer feedback file for reading

feedbackFile = open("customer_feedback.txt", "r")

# Read all feedback lines

feedbackLines = feedbackFile.readlines()

# Close the input file
feedbackFile.close()

# Open the report file for writing
reportFile = open("questions_report_Tiara_Anderson.txt", "w")

# Write the report heading
reportFile.write("*************************************\n")
reportFile.write("** Report of Questions by Customers **\n")
reportFile.write("**************************************\n\n")

# Counters
feedbackCount = 0
questionNumber = 1

# Process each customer feedback
for line in feedbackLines:

    # Skip blank lines
    if line.strip() == "":
        continue

    feedbackCount += 1

    # Separate the customer's name from their feedback
    parts = line.split("||")

    customerName = parts[0].strip()
    feedback = parts[1].strip()

    # Split the feedback into sentences
    sentences = feedback.split(". ")

    # Check each sentence for a question mark
    for sentence in sentences:
        if "?" in sentence:

            # Split at the question mark
            questionParts = sentence.split("?")

            # Extract the portion before the question mark
            question = questionParts[0].strip()+ "?"

            # Write the question to the report
            reportFile.write(
                f"{questionNumber}) {customerName} asked: {question}\n\n"
            )
            questionNumber += 1

# Calculate number of question extracted
questionCount = questionNumber - 1

# Write report totals
reportFile.write("------------------------------------------------------\n\n")
reportFile.write(f"No. of Feedbacks Processed: {feedbackCount}\n")
reportFile.write(f"No. of Extracted Questions: {questionCount}\n")
reportFile.write("************************************\n")

# Close the report file
reportFile.close()

# Display success message
print("Success! The questions_report_Tiara_Anderson.txt file has been generated.")
import requests

# Fetch the quiz data from the URL
url = "https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json"
response = requests.get(url)
quiz_data = response.json()

# Ask the user for the question ID and convert
# the ID to integer to match the type in the json data
question_id = int(input("Enter the question ID: "))

# Initialize variables to track the correct answer and whether the question was found
correct_answer = None
question_found = False

# Find and print the correct answer
for quiz in quiz_data["quizzes"]:
    for question in quiz["questions"]:
        if question["id"] == question_id:
            question_found = True
            for choice, is_correct in question["choices"].items():
                if is_correct:
                    correct_answer = choice

# Check if the question with the given ID is found
if question_found:
    # Check if there was a correct answer
    if correct_answer:
        print(f"The correct answer is: {correct_answer}")
    else:
        print("No correct answer found for the given question ID.")
else:
    print("Question ID not found.")
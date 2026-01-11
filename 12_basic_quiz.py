# A basic True/False quiz game using dictionaries
question_data = [
    {"text": "A slug's blood is green.", "answer": "T"},
    {"text": "The loudest animal is the African Elephant.", "answer": "F"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "T"},
    {"text": "The total surface area of two human lungs is approximately 70 square metres.", "answer": "T"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "T"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are technically entitled to a state funeral.", "answer": "F"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "T"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "F"},
    {"text": "Google was originally called 'Backrub'.", "answer": "T"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "T"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "F"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "T"}
]
score=0
question_number=0
print(f"Welcome to the quiz game ")
print(f"We shall now begin")
print(f"You must answer in T/F (True/False) format")
for question in question_data:
    question_number+=1
    user_answer=input(f"Q.{question_number}: {question["text"]}:T/F: ").upper()
    if user_answer==question["answer"]:
        print("Congratulations The answer is correct")
        print("The Next Question is ")
        score+=1
    else:
        print(f"Oops wrong answer: The Correct answer was {question["answer"]}")
print(f"The Quiz is completed \n Your score is {score}/{len(question_data)}")
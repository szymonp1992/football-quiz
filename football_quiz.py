# This is a simple quiz written using Python programming language

questions = [{"question": "Who won the FIFA World Cup 2018? ", "answer": "France"}, {"question": "Who was the FIFA World Cup 2022 top scorer? (surname) ", "answer": "Mbappe"}, {"question": "Who won the Golden Glove in 2022 World Cup? (surname) ", "answer": "Martinez"}, {"question": "Which one of these did not make it into skysports team of the tournament? Livakovic, Acuna, Modric or Hakimi? ", "answer": "Modric"}]

score = 0

for question in questions:
    user_answer = input(question["question"])
    if user_answer.lower() == question["answer"].lower():
        score += 1
        print("")
        print("Good answer")
        print("")
    else:
        print("")
        print("Wrong answer")
        print("")

print(f"Your final score in this quiz is {score}")
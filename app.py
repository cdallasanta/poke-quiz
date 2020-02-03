from quiz import Quiz

def main():
  print("Welcome trainer!")
  print("Please select a difficulty:")
  print("0: Easy - The pokemon's types are shown, only need to guess one correct answer")
  print("1: Medium - The pokemon's types are shown,  must guess all correct answers")
  print("2: Hard - The pokemon's types are not shown, only need to guess one correct answer")
  print("3: Very Difficult - The pokemon's types are not shown, must guess all correct answers")
  difficulty = input()
  quiz = Quiz(difficulty)
  quiz.run()

if __name__ == "__main__":
  main()
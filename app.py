from quiz import Quiz

def main():
  print("Welcome trainer!")
  print("Would you like to have the pokemon's type displayed? (makes the game easier)")
  show_types = validate_input()
  print("Would you like to have to guess all correct answers? (makes the game harder)")
  all_answers = validate_input()
  quiz = Quiz(show_types, all_answers)
  quiz.run()

def validate_input():
  acceptable_answers = ["yes", "y", "no", "n", "true", "false"]
  i = input("(yes/no): ").lower()
  while not i in acceptable_answers:
    print("Input not recognized, please use \"yes\" or \"no\"")
    i = input()
  return i in ["yes", "y", "true"]


if __name__ == "__main__":
  main()
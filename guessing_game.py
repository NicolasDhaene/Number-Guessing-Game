"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    greetings = "Welcome to the Number Guessing Game by Nicolas Dhaene"
    answer_low_limit = 1
    answer_high_limit = 10
    question = "Try to guess a number between "+str(answer_low_limit)+" and "+str(answer_high_limit)+" :    "
    answer = random.randint(answer_low_limit,answer_high_limit)
    attempt = 0
    high_score = 1000000000000
    print("-"*len(greetings))
    print(greetings)
    print("-"*len(greetings))
    print("") 
    while True:
      guess_answer = input(question)
      try: 
        guess_answer = int(guess_answer)
      except ValueError:
        print(guess_answer, "is not a valid guess :( We are looking for integers here...")
        continue
      attempt += 1
      if guess_answer == answer:
        print("")
        print("You won! The answer was indeed",answer,"! It took you",attempt,"attempts to guess it right.")
        if high_score > attempt:
            high_score = attempt
        print("")
        print("Current high score:", high_score, "attempt(s)")
        play_again = input("Would like to play again? Type 'Y'    ")
        if play_again == "Y":
          print("")
          answer = random.randint(answer_low_limit,answer_high_limit)
          attempt = 0
          continue
        else:
          print("OK then, see you next time!")
          break
      elif guess_answer > answer:
        if guess_answer > answer_high_limit:
          print("Come on... You should know it's lower than that! Try Again.")
          continue
        else:
          print("Nope, it is a lower number than",guess_answer,". Try Again.")
          continue  
      elif guess_answer < answer:
        if guess_answer < answer_low_limit:
          print("Come on... You should know it's higher than that! Try Again.")
          continue
        else:
          print("Nope, it is a higher number than",guess_answer,". Try Again.")
        continue  

        
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

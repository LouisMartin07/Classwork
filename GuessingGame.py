#import random

class GuessingGame:

    def __init__(self,answer_number):
        self.answer = answer_number
        self.is_solved = False
        
    def guess(self,user_guess):
        if user_guess > self.answer:
            return "high"
        elif user_guess < self.answer:
            return "low"
        else:
            self.is_solved = True
            return "correct"

    def solved(self):
       return self.is_solved

game = GuessingGame(10)

print(game.solved())   # => False

print(game.guess(5))  # => 'low'
print(game.guess(20)) # => 'high'
print(game.solved())   # => False

print(game.guess(10)) # => 'correct'
print(game.solved())   # => True



# ----- main.py -----
# game = GuessingGame(random.randint(1,100))
# last_guess  = None
# last_result = None

# while not game.solved():
#   if last_guess is not None: 
#     print(f"Oops! Your last guess ({last_guess}) was {last_result}.\n")

#   last_guess  = int(input("Enter your guess: "))
#   last_result = game.guess(last_guess)


# print(f"{last_guess} was correct!")
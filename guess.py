guess =  __import__("random").randint(1,10)
while True: (lambda num: (print("You Won"*int(num == guess) + "You guessed too high"*int(num > guess) + "You guessed too low"*int(num < guess)),__import__("sys").exit() if num == guess else print("")))((lambda noom: int(noom) if noom.isdigit() else -1)(input("Enter a number between 1 and 10:  ")))

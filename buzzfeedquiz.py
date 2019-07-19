def ask(question,acceptable):
    while 1:
        answer = input(question + "  ")
        if answer in acceptable: break
        print("Answer not acceptable it must be one of: " + str(acceptable))
    return acceptable.index(answer)
foreword,answer = [print(str(i + str(__import__("time").sleep(1)))[:-4]) for i in ["This quiz will determine if you like Minecraft or Fortnite","Minecraft is one of the most popular games in the world","Fortnite was a hit battle royale shooter that was extremely popular"]],(lambda answer: print(int(answer < 3)*"You like Minecraft" + int(answer >= 3)*"You like Fortnite"))(sum(ask(i[0],i[1]) for i in [("What is your favorite game?",("Minecraft","Fortnite")),("Should you dig straight down?",("No","Yes")),("Have you bought the fortnite battle pass?",("No","Yes")),("Can you sleep in the nether?",("No","Yes")),("Did Notch create minecraft",("Yes","No")),("Did Tim create Minecraft?",("No","Yes"))]))


import random

rock = """
    _______
---'   ____)
      (_____ )
      (_____ )
      (____ )
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def jokenpo(contagem=0):
    choose = int(input("WHAT DO YOU CHOOSE? TYPE 0 FOR ROCK, 1 FOR PAPER OR 2 FOR SCISSORS: "))
    if choose == 0:
        print(rock)
    elif choose == 1:
        print(paper)
    elif choose == 2:
        print(scissors)

    comp_choose = int(random.random() * 3)

    if comp_choose == 0:
        print(rock)
        print("COMPUTER CHOOSE ROCK")
        if choose == 0:
            print("TIE")
        elif choose == 1:
            print("YOU WIN")
            contagem += 1
        elif choose == 2:
            print("YOU LOSE")
            contagem -= 1

    elif comp_choose == 1:
        print(paper)
        print("COMPUTER CHOOSE PAPER")
        if choose == 0:
            print("YOU LOSE")
            contagem -= 1
        elif choose == 1:
            print("TIE")
        elif choose == 2:
            print("YOU WIN")
            contagem += 1

    elif comp_choose == 2:
        print(scissors)
        print("COMPUTER CHOOSE SCISSORS")
        if choose == 0:
            print("YOU WIN")
            contagem += 1
        elif choose == 1:
            print("YOU LOSE")
            contagem -= 1
        elif choose == 2:
            print("TIE")
    print(contagem)
    jokenpo()

jokenpo()

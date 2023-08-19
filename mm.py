import os
from time import sleep
from colorama import Fore
from random import shuffle, choice
class Mastermind():
    def __init__(self):
        self.code = []
        self.guesses = []  
    def set_code(self, code):

        self.code = code

        os.system('clear')
        print('Code has been set!')
        print('Starting Game...')
        print(self.code)

    def game(self):
        
        while len(self.guesses) != 8:
            self.flags = []
            self.guess = input(f"{Fore.RESET}[{Fore.RED}+{Fore.RESET}]Enter your guess {len(self.guesses) + 1} (seperated by spaces): ").split(" ")
            self.guesses.append(self.guess)


            #Flags
            if self.guess == self.code:
                print("You win!")
                exit()
            else:
                for x,color in enumerate(self.guess):
                    if color in self.code and (self.guess[x] == self.code[x]):
                        self.flags.append("Red Flag")
                    elif color in self.code and (self.guess[x] != self.code[x]):
                        self.flags.append("White Flag")
            
            shuffle(self.flags)
            print(f"{Fore.RESET}{self.guess} - {self.flags}")

            sleep(2)

        print('You Lose')




if __name__ == "__main__":
    mastermind = Mastermind()
    print(f"""{Fore.RED}RULES{Fore.RESET} \n Colors available are: {Fore.WHITE}White, {Fore.BLACK}Black, {Fore.GREEN}Green, {Fore.RED}Red, {Fore.BLUE}Blue, {Fore.YELLOW}Yellow""")

    sleep(2)

    print(f"    {Fore.RESET}Input should be entered like so: color color color color")

    sleep(2)

    print(f"         Each guess will return up to four flags. \n{Fore.RED}Red Flag - Correct color in the correct spot \n{Fore.WHITE}White Flag - Correct color in the wrong spot. \nWrong color in the wrong spot will receive no flag")

    sleep(3)

    gamemode = input("Singleplayer or Multiplayer? ")
    if gamemode.lower() == "multiplayer":
        code = input("Enter the code (seperated by spaces): ")
        mastermind.set_code(code)
        mastermind.game()
    else:
        colours = ["white", "black", "yellow", "red", "green", "blue"]
        code = [choice(colours) for x in range(4)]
        mastermind.set_code(code)
        mastermind.game()


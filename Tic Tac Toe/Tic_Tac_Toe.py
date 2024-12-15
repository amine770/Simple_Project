import os

def cleanning_Terminal():
    if os.name == "nt":
        os.system("cls")

class Game:
    def __init__(self):
        self.__palyers = [Player(),Player()]
        self.__menu = Menu()
        self.__board = Board()
    
    def game_start(self):
        if self.__menu.start_game() == 2:
            print("fuck you !!")
        else:
            cleanning_Terminal()
            i = 1
            for player in self.__palyers:
                print(f"Player {i} enter your detail")
                player.set_name()
                player.set_symbole()
                i+=1
                cleanning_Terminal()
            self.game_play()

    def game_play(self):
        self.__board.display()
        print("\n")
        is_running = True
        index = 0
        while is_running:
            print(f"{self.__palyers[index].get_name()}, turn ({self.__palyers[index].get_symbole()})")
            pos = int(input("Chose a cell (1-9) : "))
            while not(1<=pos<=9) or not(self.valid_position(self.__board.get_board(),pos)):
                pos = int(input("Chose other position cell (1-9) : "))
            
            cleanning_Terminal()
            self.__board.upgrade(pos,self.__palyers[index].get_symbole())
            self.__board.display()

            if self.check_draw(self.__board.get_board()) == True:
                print("This is a draw good game !!")
                is_running = False
            elif self.check_win(self.__board.get_board(),self.__palyers[index].get_symbole()) == True:
                print(f"{self.__palyers[index].get_name()} you win")
                is_running = False
            else:
                if index == 0:
                    index = 1
                else:
                    index = 0

    def check_draw(self,board):
        for i in board:
            if "1"<=i<="9":
                return False
        return True

    def check_win(self,board,symbole):
        winning_combination = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]

        for combo in winning_combination:
            if board[combo[0]]==board[combo[1]]==board[combo[2]]==symbole:
                return True
        return False

    def valid_position(self,board,pos):
        if not("1"<=board[pos-1]<="9"):
            return False
        else:
            return True
        
class Player:
    def __init__(self):
        self.__name = ""
        self.__symbole = ""
    
    def set_name(self):
        name = input("Enter your name : ")
        while name.isalpha()==False:
            name = input("Enter your name (only alpha) : ")
        self.__name = name
    
    def set_symbole(self):
        symbole = input(f"{self.__name}, Enter your symbole : ")
        while not("A"<=symbole.upper()<="Z"):
            symbole = input(f"{self.__name}, Enter your symbole (between A and Z) : ")
        self.__symbole = symbole.upper()

    def get_name(self):
        return self.__name
    
    def get_symbole(self):
        return self.__symbole

class Board:
    def __init__(self):
        self.__board = ["1","2","3","4","5","6","7","8","9"]
    
    def get_board(self):
        return self.__board
    
    def display(self):
        for i in range(0,len(self.__board),3):
            string = ""
            for item in range(i,i+3):
                string += self.__board[item]+"|"
            print(string[:len(string)-1])
            print("-"*len(string))

    def upgrade(self,pos,char):
        self.__board[pos-1] = char

class Menu:
    def start_game(self):
        print("-----------WELCOM TO THE GAME------------")
        print("1- Run the game\n2- Quit")
        choice = int(input("Ente your chocie : "))
        while not(1<=choice<=2):
            choice = int(input("Enter your choice (should be  1 or 2) : "))
        return choice
    
    def end_game(self):
        print("Nice Game !!")
        print("1- Start new game+\n2- Quite ")
        choice = int(input("Ente your chocie : "))
        while not(1<=choice<=2):
            choice = int(input("Enter your choice (should be  1 or 2) : "))
        return choice


Game().game_start()

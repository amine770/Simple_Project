import random

#Set up the constants:
HEARTS = chr(9829) #'♥'
DIAMONDS = chr(9830) #'♦'
SPADES = chr(9824) #'♠'
CLUBS = chr(9827) #'♣'
Suite_Symb = [HEARTS,DIAMONDS,SPADES,CLUBS]

print("""
Blackjack game :

    Rules:
        Try to get as close to 21 without going over.
        King, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their fac value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        on your first play, you can (D)ouble down to increase your bet

        but must hit exactly one more time before standing.
        In case of a tie, the bet is rreturned to the player.
        the dealer stops hitting at 17.
""")

def main():
    Money = 5000

    print("How much do you bet ? (1-5000)")
    bet = int(input("> "))
    while not(1<=bet<=5000):
        print("your bet is not available !!")
        bet = int(input("> "))
    
    player_cards = [[random.randint(1,14),Suite_Symb[random.randint(0,3)]], [random.randint(1,14),Suite_Symb[random.randint(0,3)]]]
    dealer_cards = [[random.randint(1,14),Suite_Symb[random.randint(0,3)]], [random.randint(1,14),Suite_Symb[random.randint(0,3)]]]

    player_score = Score(player_cards)

    print("DEALER : ???\n\n")
    Semi_Affiche(dealer_cards)

    print(f"PLAYER: {player_score} ")
    Affiche(player_cards)

    is_running = True
    while is_running:
        print("\n\n(H)IT, (S)tand, (D)ouble down")
        choice = input("> ")
        if choice == "H":
            Hit(player_cards)
        elif choice == "S":
            print("You chose to stand")
        else:
            bet *= 2
            Hit(player_cards)

        if Score(dealer_cards)<17:
            dealer_cards.append([random.randint(1,14),Suite_Symb[random.randint(0,3)]])
        
        print(f"DEALER: {Score(dealer_cards)} ")
        Affiche(dealer_cards)

        print(f"PLAYER: {Score(player_cards)}")
        Affiche((player_cards))

        if check_win(player_cards,dealer_cards) == 1:
            print(f"You won ${bet}!")
            is_running = False
        elif check_win(player_cards,dealer_cards) == -1:
            print(f"You lose ${bet}")
            is_running = False
        else:
            print("This is a tie")
            is_running = False
        

def Score(cards):
    score = 0
    for i in range(len(cards)):
        if cards[i][0]<=10:
            score += cards[i][0]
        elif cards[i][0]<=13:
            score += 10
        else:
            if (score + 11)<=21:
                score +=11
            else:
                score += 1

    return score



def Semi_Affiche(cards):
    values = ["J", "Q", "K"]
    rows = [" ___   ","|## |  ","|###|  ","|_##|  "]

    symbol = cards[1][1]
    if cards[1][0]<=10:
        value = str(cards[1][0])
    elif cards[1][0]<=13:
        value = str(values[cards[1][0]-11])
    else:
        value = "Ac"
        
    row0 = " ___ "
    row2 = f"| {symbol} |"
    if len(value)>1:
        row1 = f"|{value} |"
        row3 = f"|_{value}|"
    else:
        row1 = f"|{value}  |"
        row3 = f"|__{value}|"
        
    rows[0] += row0+"  "
    rows[1] += row1+"  "
    rows[2] += row2+"  "
    rows[3] += row3+"  "
    
    for row in rows:
        print(row)



def Affiche(cards):
    values = ["J", "Q", "K"]
    rows = ["","","",""]

    for card in cards:
        symbol = card[1]
        if card[0]<=10:
            value = str(card[0])
        elif card[0]<=13:
            value = str(values[card[0]-11])
        else:
            value = "Ac"
        
        row0 = " ___ "
        row2 = f"| {symbol} |"
        if len(value)>1:
            row1 = f"|{value} |"
            row3 = f"|_{value}|"
        else:
            row1 = f"|{value}  |"
            row3 = f"|__{value}|"
        
        rows[0] += row0+"  "
        rows[1] += row1+"  "
        rows[2] += row2+"  "
        rows[3] += row3+"  "
    
    for row in rows:
        print(row)

def Hit(cards):
    cards.append([random.randint(1,14),Suite_Symb[random.randint(0,3)]])
    print(f"You drew a {cards[len(cards)-1][0]} of {cards[len(cards)-1][1]} ")
    

def check_win(cards1,cards2):
    if Score(cards1)>21:
        return -1
    elif Score(cards2)>21:
        return 1
    elif Score(cards1)>Score(cards2):
        return 1
    elif Score(cards1)<Score(cards2):
        return -1
    else:
        return 0

main()
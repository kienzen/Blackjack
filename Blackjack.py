import random


class CardDeck():
    def __init__(self):
        self.deck = {"2": 4, "3": 4, "4": 4, "5": 4, "6": 4, "7": 4, "8": 4, "9": 4, "10": 4, "Jack": 4, "Queen": 4,
                     "King": 4, "Ace": 4}

    def disp(self):
        print(str(self.deck))

    def pull(self, x):
        pull_set = []
        for n in range(0, x):
            while True:
                m = random.choice(list(self.deck.keys()))
                if self.deck[m] >= 1:
                    pull_set.append(m)
                    self.deck[m] = self.deck[m] - 1
                    break
        return pull_set


class Hand(list):
    def __init__(self, pull_set):
        self.cards = pull_set
        self.values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10,
                       "Queen": 10, "King": 10, "Ace": 10}
        self.values2 = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10,
                        "Queen": 10, "King": 10, "Ace": 1}

    def getCard(self, pull_set):
        self.cards = self.cards + pull_set

    def display(self):
        return self.cards

    def cdisplay(self):
        return self.cards[1:]

    def score(self):
        score1 = 0
        score2 = 0
        for n in list(self.cards):
            score1 += (self.values[n])
            score2 += (self.values2[n])
        return max(score1, score2)


class Player():
    def __init__(self, name, money):
        self.name = str(name)
        self.money = int(money)

    def bet(self, money):
        self.money = int(self.money) + int(money)

    def account(self):
        return self.money

    def name(self):
        return self.name


def blackjack():
    print("Welcome to Blackjack by Adam")
    name = input("Enter your name:")
    print("Hello", name, "!")
    money = input("How much money do you have to play with?\n")
    player1 = Player(name, money)
    on = True
    firsthand = True
    while on:
        if not firsthand:
            out = input('Would you like to continue playing?\nPress "o" to leave or any other button to continue\n')
            if out == "o":
                return player1.name, ",you left with", player1.account()
        bet = int(input("How much would you like to bet?\n"))
        deck = CardDeck()
        chang = Hand(deck.pull(2))
        phand = Hand(deck.pull(2))
        print("Your cards:", phand.display())
        print("Your Score is:", phand.score())
        print("Computer Cards:", chang.cdisplay(), "plus one hidden")
        while True:
            Hit_or_Stay = input("Would you like to Hit or Stay?Type h or s  ")
            if Hit_or_Stay == "h":
                phand.getCard(deck.pull(1))
                print("Your cards:", phand.display())
                print("Your Score is:", phand.score())
                print("\n")
            if phand.score() > 21:
                print("You have lost the round!")
                player1.bet(bet * -1)
                print("You have so much money left:", player1.account())
                out = input("If you would like to stop playing, press 'e' or any other letter to continue\n")
                if out == "e":
                    return player1.name, ",you left with", player1.account()
                else:
                    firsthand = False
                    break
            chang.getCard(deck.pull(1))
            print("Your cards:", phand.display())
            print("Your Score is:", phand.score())
            print("Computer Cards:", chang.cdisplay(), "plus one hidden")
            print("\n")
            if chang.score() > 21:
                print("You have won the round!")
                player1.bet(bet)
                print("You have so much money left:", player1.account())
                out = input("If you would like to stop playing, press e\n")
                if out == "e":
                    return player1.name, ",you left with", player1.account()
                else:
                    firsthand = False
                    break




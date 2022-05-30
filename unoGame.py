import random

def newDeck():

    numbers = ["0","1","2","3","4","5","6","7","8","9","+2","RoundChange","SkipTurn"]
    colors = ["Green","Yellow","Blue","Red"]
    # especials = ["+4 Wildcard","ColorChange"]
    deck = [(number,color) for number in numbers for color in colors]
    # especials = [card for card in especials for i in range(4)]
    # deck += especials
    return deck


def deal(deck):
    playerCards = random.sample(deck,7)
    for card in playerCards:
        deck.remove(card)
    pcCards = random.sample(deck,7)
    for card in pcCards:
        deck.remove(card)
    return deck,playerCards,pcCards


def shuffledeck(deck):
    random.shuffle(deck)


def playerTurn(playerCards,frontcard,deck):
    print("Your hand: ")
    print("0- Grab a card")

    for idx,card in enumerate(playerCards):
        print(f"{idx+1}- {card}")

    print(f"Front card: {frontcard}")

    card = input("Pick a card: ")

    while card == "" or not (card.isnumeric()):
        card = input("Pick a card: ")
    while not 0 <= int(card) < len(playerCards)+1:
            card = input("Pick a card: ")

    if int(card) != 0:
        card = playerCards[int(card)-1]
    else:
        grabCard(playerCards,deck)
        print("Your hand: ")
        print("0- Pass")

        for idx, card in enumerate(playerCards):
            print(f"{idx + 1}- {card}")

        print(f"Front card: {frontcard}")
        card = input("Pick a card: ")

        while not 0 <= int(card) < len(playerCards) + 1:
            card = input("Pick a card: ")

        if int(card) != 0:
            card = playerCards[int(card) - 1]
        else:
            return playerCards, deck, frontcard

    if checkplay(card,frontcard):
        frontcard = card
        print(f"Front card: {frontcard}")
        playerCards.remove(card)
        return playerCards,deck,frontcard
    else:
        print("Wrong answer, picking a card")
        playerCards,deck = grabCard(playerCards,deck)
        return playerCards,deck,frontcard

def pcTurn(pcCards,frontcard,deck):

    print("1 turn",pcCards)

    sameColor = [card for card in pcCards if card[1] == frontcard[1]]
    sameNumber = [card for card in pcCards if card[0] == frontcard[0]]

    if sameColor:
        sameColor.sort()
        print("Color",sameColor)
        frontcard = sameColor[-1]
        pcCards.remove(frontcard)

    elif sameNumber:
        sameNumber.sort()
        print("Number", sameNumber)
        frontcard = sameNumber[-1]
        pcCards.remove(frontcard)

    else:
        grabCard(pcCards,deck)
        print("2 turn",pcCards)
        sameColor = [card for card in pcCards if card[1] == frontcard[1]]
        sameNumber = [card for card in pcCards if card[0] == frontcard[0]]

        if sameColor:
            sameColor.sort()
            print("Color", sameColor)
            frontcard = sameColor[-1]
            pcCards.remove(frontcard)

        elif sameNumber:
            sameNumber.sort()
            print("Number", sameNumber)
            frontcard = sameNumber[-1]
            pcCards.remove(frontcard)

    print("front",frontcard)

    return pcCards,deck,frontcard


def checkplay(card,frontcard):
    especials = ["+4 Wildcard", "ColorChange"]

    if card[0] == frontcard[0] or card[1] == frontcard[1] or card in especials:
        return True
    else:
        return False


def grabCard(hand,deck):
    hand += [deck.pop()]
    return hand,deck

def printHand(playerCards):
    print("Your hand: ")
    for idx, card in enumerate(playerCards):
        print(f"{idx + 1}- {card}")

def randomTurn(turn):
    players = [1,2]
    turn = random.choice(players)
    return turn



def newGame():
    deck, playerCards, pcCards = deal(newDeck())
    random.shuffle(deck)
    frontcard = deck.pop()
    print("front",frontcard)

    while pcCards != [] and playerCards != []:
        pcCards,deck,frontcard = pcTurn(pcCards,frontcard,deck)
        print("")
        if deck == 0 or pcCards == []:
            break
        playerCards, deck, frontcard = playerTurn(playerCards, frontcard, deck)
        if deck == 0:
            break
        print("")
    if pcCards == []:
        print("PC WIN")
    else:
        print("YOU WIN")


newGame()

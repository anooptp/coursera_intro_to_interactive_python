# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        

    def __str__(self):
        h=""
        for i in self.cards:
            h=str(h)+" "+str(i)
        return "Hand contains"+h

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        val = 0
        for j in [str(i)[1] for i in self.cards]:
            val += VALUES[j]
        if 'A' in [str(i)[1] for i in self.cards] and val + 10 <= 21:
            val += 10
        return val
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        dist = 1
        for card in self.cards:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(str(card)[1]), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(str(card)[0]))
            #print  str(card)[1], str(card)[0]
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0] + (dist * 100), pos[1] + CARD_CENTER[1]], CARD_SIZE)
            dist +=1
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [Card(i,j) for i in SUITS for j in RANKS]

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        card = ""
        for i in self.deck:
            card = card +" " + str(i)
        return "Deck contains"+card 


#define event handlers for buttons
def deal():
    global outcome, in_play, decks, player, dealer, message, score
    message = ""
    
    if in_play:
        message = "You Lose"
        score -=1
        in_play = False
    # your code goes here
    decks = Deck()
    decks.shuffle()
    
    player = Hand()
    dealer = Hand()
    for i in range(2):
        player.add_card(decks.deal_card())
        dealer.add_card(decks.deal_card())
        
    print decks
    print "Player",player
    print "Dealer",dealer
    
    outcome = "Hit or stand?"
    in_play = True

def hit():
    global outcome, in_play, decks, player, dealer, message, score
    # if the hand is in play, hit the player
    message = ""
    if in_play:
        if player.get_value() <= 21:
            player.add_card(decks.deal_card())
            print "Player",player
            if player.get_value() > 21:
                print "You went bust and lose"
                message = "You went bust and lose"
                score -= 1
                in_play = False
        else:
            # if busted, assign a message to outcome, update in_play and score
            print "You went bust and lose"
            message = "You went bust and lose"
            score -= 1
            in_play = False
        outcome = "New deal?"
    
       
def stand():
    global outcome, in_play, decks, player, dealer, message, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(decks.deal_card())
            print "Dealer",dealer
        if dealer.get_value() <= 21:
            if dealer.get_value() >= player.get_value():
                print "Dealer Wins"
                message = "You lose"
                score -= 1
                in_play = False
            else:
                print "Player Wins"
                message = "You Win"
                score += 1
                in_play = False
        else:
            print "Dealer Burst"
            message = "Dealer went bust and You WIN"
            score += 1
            in_play = False
        outcome = "New deal?"
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    canvas.draw_text('Blackjack', [100, 100], 40, 'Black')
    canvas.draw_text('Score : '+str(score), [400, 100], 30, 'Black')
    canvas.draw_text('Dealer', [30, 170], 30, 'Black')
    canvas.draw_text(message, [250, 170], 30, 'Black')
    dealer.draw(canvas, [-50, 200])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [CARD_BACK_CENTER[0] + 50, 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
            
    canvas.draw_text('Player', [30, 370], 30, 'Black')
    canvas.draw_text(outcome, [250, 370], 30, 'Black')
    player.draw(canvas, [-50, 400])
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
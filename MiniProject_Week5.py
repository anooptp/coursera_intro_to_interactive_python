# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck, exposed, state, first_ind, sec_ind, turns
    deck =range(8)+range(8)
    random.shuffle(deck)
    #print deck
    exposed = [False for i in range(16)]
    turns, state, first_ind, sec_ind=0, 0, None, None
    label.set_text("Turns = "+str(turns))

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, first_ind, sec_ind, turns
    #print pos
    if state==0:
        if exposed[pos[0]//50]==False:
            exposed[pos[0]//50]=True
            state=1
            first_ind=pos[0]//50
    elif state==1:
        if exposed[pos[0]//50]==False:
            exposed[pos[0]//50]=True
            state=2
            sec_ind=pos[0]//50
            turns=turns+1
            label.set_text("Turns = "+str(turns))
    else:
        if exposed[pos[0]//50]==False:
            exposed[pos[0]//50]=True
            state=1
            if deck[first_ind]!=deck[sec_ind]:
                exposed[first_ind]=False
                exposed[sec_ind]=False
            first_ind, sec_ind=pos[0]//50,None
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i=0
    for card in deck:
        if exposed[i]:
            canvas.draw_text(str(card), (50*i+20, 60), 40, 'White')
            canvas.draw_line([50*i, 0], [50*i, 100], 1, 'White')
        else:
            #canvas.draw_line([50*i, 0], [50*i, 100], 1, 'White')
            canvas.draw_polygon([[50*i, 0], [50*(i+1), 0], [50*(i+1), 100], [50*i, 100]], 1, 'Black','Green')
        i+=1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
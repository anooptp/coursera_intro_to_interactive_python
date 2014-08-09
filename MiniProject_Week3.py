# template for "Stopwatch: The Game"

import simplegui

# define global variables
time_num=0
success_count=0
total_count=0
timer=''

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    B_str=''
    
    A=t/(60*10)
    B=(t-(A*60*10))/10
    if len(str(B))==1:
        B_str='0'+str(B)
    else:
        B_str=str(B)
    D=t%10
    return str(A)+':'+B_str+'.'+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    global timer
    if not timer.is_running():
        timer.start()

def stop_button_handler():
    global timer, success_count, total_count, time_num
    if timer.is_running():
        timer.stop()
        total_count += 1
        if time_num % 10 == 0:
            success_count += 1

def reset_button_handler():
    global timer, time_num, success_count, total_count
    if timer.is_running():
        timer.stop()
    time_num = 0
    success_count=0
    total_count=0



# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_num
    time_num += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time_num), (100, 150), 30, 'White')
    canvas.draw_text(str(success_count)+'/'+str(total_count), (260, 25), 20, 'White')
    
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300,300)

# register event handlers
frame.set_draw_handler(draw_handler)
start_but = frame.add_button('Start', start_button_handler, 70)
stop_but = frame.add_button('Stop', stop_button_handler, 70)
reset_but = frame.add_button('Restart', reset_button_handler, 70)


# start frame
frame.start()

timer = simplegui.create_timer(100, timer_handler)


# Please remember to review the grading rubric

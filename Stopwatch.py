# template for "Stopwatch: The Game"

import simplegui

# define global variables

time = 0
turn = True
success = 0
attempt = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(total_decaseconds):
    
    min = int(total_decaseconds/600)
    #seconds = int((total_decaseconds - (minutes*600))/10)
    #decaseconds = total_decaseconds - (seconds*10) - (minutes*600)
    sec = int((total_decaseconds%600)/10)
    decasec = total_decaseconds%10 
    
        
    if sec < 10:
        form = str(min)+":0"+str(sec)+"."+str(decasec)
    else:
        form = str(min)+":"+str(sec)+"."+str(decasec)
        
    return form
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()
    global attempt
    attempt = attempt + 1
    if(time%10 == 0):
        global success
        success = success + 1
    
    
def reset():
    global time
    time = 0.00
    timer.stop()
    turn = False
    global attempt
    attempt = 0
    global success
    success = 0
 


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time = time + 1
    
        
    
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [100,100], 36, "White")
    canvas.draw_text(str(success) + "/" + str(attempt), [270,20], 20, "White")
    

    
# create frame
frame = simplegui.create_frame("Timer Begins!", 300,200)


# register event handlers

timer = simplegui.create_timer(100, tick)

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)


# start frame
frame.start()



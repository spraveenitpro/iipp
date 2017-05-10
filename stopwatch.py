# template for "Stopwatch: The Game"

# define global variables

import simplegui
count = 0
is_running = False
total_stops = 0
total_hits = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(value):
    #return str (value // 60) , str(value // 10)
    tenth_sec = (value) % 10
    sec = int(value / 10) % 10
    minutes = int(value / 600) % 600
    ten_min = int(value / 100) % 6
    string = str(minutes) + ":" + str(ten_min) + str(sec) + "." + str(tenth_sec)
    return string

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def startclock():
    global is_running
    is_running = True
    timer.start()

def stopclock():
    global is_running, total_stops, total_hits
    if is_running == True:
        if count % 10 == 0 and count != 0:
            total_stops +=1
            total_hits +=1
        elif count != 0:
            total_stops +=1
                        
    is_running = False
    timer.stop()

def resetclock():
     global count, total_stops, total_hits
     count = 0
     total_stops = 0
     total_hits = 0
     is_running = False
     timer.stop()
    
    
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count = count + 1
    #print count
    

# define draw handler
def draw_handler(canvas):
    global count
    canvas.draw_text(format(count), [80,240], 50, "White")
    canvas.draw_text(str(total_stops), [290,60], 50, "White")
    canvas.draw_text(str(total_hits), [350,60], 50, "White")
    
# create frame

frame = simplegui.create_frame("Alarm_Clock", 400, 400)
button1 = frame.add_button('Start', startclock, 100)
button2 = frame.add_button('Stop', stopclock, 100)
button3 = frame.add_button('Reset', resetclock, 100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)



# register event handlers


# start frame

frame.start()
#timer.start()


# Please remember to review the grading rubric

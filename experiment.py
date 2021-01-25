##########################################################################################
### ME 224 Project
### Version 1 Preliminary Testing

import time
from Tkinter import*
import random


##########################################################################################
### Helper Functions

# Hides an item
def hide(item):
    canvas.itemconfig(item, state = 'hidden')
    animation.update()

# Show a hidden item by returning the state of an item to normal
def show(item):
    canvas.itemconfig(item, state = 'normal')
    animation.update()

# Takes in a dot, makes a copy of it at the coords input
def copy(dot, x0, y0, x1, y1):
	config = canvas.itemconfig(dot)
	new_config = {key: config[key][-1] for key in config.keys()}
	canvas.create_oval(x0, y0, x1, y1, **new_config)
	animation.update()

# Takes in a dot, returns its width (diamter)
def width(dot):
    dotPos = canvas.coords(dot)
    return dotPos[2] - dotPos[0]

# Takes in 2 dots, returns the difference between their diameters (abs of dot2 width - dot1 width)
def diffD(dot1, dot2):
    w1 = width(dot1)
    w2 = width(dot2)
    diff = abs(w2 - w1)
    return round(diff)

# Takes in a dot, hides original dot, creates a new dot with radius changed by x
# returns newDot as id of the new dot
# x should be an even number
# In x-direction: keep inner coordinate the same and extends outer coordinate to
# increase radius, so that the gap remains the same. In y-direction: splits evenly
def chgRadius(dot, x):
    dotPos = canvas.coords(dot)
    if dotPos[0] < animation.winfo_width() / 2:
        x0 = dotPos[0] - x
        x1 = dotPos[2]
    elif dotPos[0] > animation.winfo_width() / 2:
        x0 = dotPos[0]
        x1 = dotPos[2] + x
    y0 = dotPos[1] - x
    y1 = dotPos[3]
    #print ' New Width: ' + str(x1 - x0)
    #print ' New Height: ' + str(y1 - y0)

    config = canvas.itemconfig(dot)
    new_config = {key: config[key][-1] for key in config.keys()}
    hide(dot)
    newDot = canvas.create_oval(x0, y0, x1, y1, **new_config)
    animation.update()
    return newDot


class Item():
    def __init__(self):
       self.trial = False
       self.test = False
       self.dotSize = False			# Small, medium, or Large
       self.baseSize = False		# Stores if base dot is smaller or larger than test dot
       self.difference = False		# stores the difference between the dots' diameters for the test
       self.guess = False
       self.answer = False			# answer stores which side the larger dot was on
       self.correct = False

##########################################################################################
### Initialize the window and figure
animation = Tk()
animation.title('Experiment')											# Title the figure
canvas = Canvas(animation, width = 1270, height = 750, bg = '#818181')	# Create Figure & background
canvas.pack()
animation.update()
##########################################################################################
### Initialize constants and standard dots

W = animation.winfo_width()			# Width of figure
H = animation.winfo_height()		# Height of figure

### Create standard dots: small, medium, and large, left and right side, as well as center red dot
### These dots are initially hidden

## Large dot
ldot_w = W/3 + 100  #523
ldot_cdist = W / 2  #635						# c-to-c dist
ldot_h = ldot_w
ldot_Lx0 = W/4 - ldot_w / 2		 #56					# X0 pos of left side
ldot_Rx0 = ldot_Lx0 + ldot_cdist #691					# X0 pos of right side
ldot_y0 = H/2 - (ldot_h)/2		 #114

# Large dot diameter = W/3; c-to-c dist = W/2
# CENTER TO CENTER DISTANCE IS CONSTANT FOR ALL DOT SIZES
ldotLft = canvas.create_oval(ldot_Lx0, ldot_y0, ldot_Lx0 + ldot_w, ldot_y0 + ldot_h, fill = '#6C6C6C', outline = '#6C6C6C', state = 'hidden')
ldotRt = canvas.create_oval(ldot_Rx0, ldot_y0, ldot_Rx0 + ldot_w, ldot_y0 + ldot_h, fill = '#6C6C6C', outline = '#6C6C6C', state = 'hidden')
#topline1 = canvas.create_rectangle(ldot_Lx0, ldot_y0 - 3, ldot_Rx0 + ldot_w, ldot_y0 - 2)
#topline2 = canvas.create_rectangle(ldot_Lx0, ldot_y0 + ldot_h + 2, ldot_Rx0 + ldot_w, ldot_y0 + ldot_h + 3)
## Medium dot
mdot_w = W/8			#158
mdot_cdist = W / 2		#635
mdot_h = mdot_w			#158
mdot_Lx0 = W/4 - mdot_w / 2			#238
mdot_Rx0 = mdot_Lx0 + mdot_cdist	#873
mdot_y0 = H/2 - (mdot_h)/2			#296

# Medium dot diameter = W/8
mdotLft = canvas.create_oval(mdot_Lx0, mdot_y0, mdot_Lx0 + mdot_w, mdot_y0 + mdot_h, fill = '#6C6C6C', outline = '#6C6C6C', state = 'hidden')
mdotRt = canvas.create_oval(mdot_Rx0, mdot_y0, mdot_Rx0 + mdot_w, mdot_y0 + mdot_h, fill = '#6C6C6C', outline = '#6C6C6C', state = 'hidden')

## Small dot
sdot_w = W/22			#57
sdot_cdist = W / 2		#635
sdot_h = sdot_w			#57
sdot_Lx0 = W/4 - sdot_w / 2			#289
sdot_Rx0 = sdot_Lx0 + mdot_cdist	#924
sdot_y0 = H/2 - (sdot_h)/2			#347

# Small dot diameter = W/22
sdotLft = canvas.create_oval(sdot_Lx0, sdot_y0, sdot_Lx0 + sdot_w, sdot_y0 + sdot_h, fill = '#6C6C6C', outline = '#6C6C6C', state = 'hidden')
sdotRt = canvas.create_oval(sdot_Rx0, sdot_y0, sdot_Rx0 + sdot_w, sdot_y0 + sdot_h, fill = '#6C6C6C', outline = '#6C6C6C', state = 'hidden')

# Center plus
cplus_tot = 9
cplus_in = 3
cdot1 = canvas.create_rectangle(W/2 - cplus_tot/2, H/2 - cplus_in/2, W/2 + cplus_tot/2, H/2 + cplus_in/2, fill = '#000000')
cdot2 = canvas.create_rectangle(W/2 - cplus_in/2, H/2 - cplus_tot/2, W/2 + cplus_in/2, H/2 + cplus_tot/2, fill = '#000000')
##########################################################################################
### Loop through a sample
raw_input("Start Test? ")
time.sleep(1)
cond = True
while cond == True:
    testDotmL = mdotLft
    testDotmR = mdotRt
    testDotChg = chgRadius(testDotmR, 50)
    show(testDotmL)
    show(testDotChg)
    time.sleep(1)
    hide(testDotmL)
    hide(testDotChg)

    status = raw_input("Left or Right? (F or J) ")
    if status != 'F' and status != 'J':
        cond = False

##########################################################################################
### Loop through the experiment

raw_input("Start Experiment? ")
trials = [1, 2, 3, 4, 5, 6]
random.shuffle(trials)
tests = 20 					# Set the maximum possible number of tests per trial
results = [False] * (tests * len(trials) + 1)
trialDisp = 1

for r in trials:
    cont = True
    testNum = 0
    trialText = canvas.create_text(W/2, 50, text = 'Trial ' + str(trialDisp))
    trialDisp = trialDisp + 1

    if r == 1 or r == 4:			# Set size of dot for each test (randomize this in the future)
        currDotLft = ldotLft
        currDotRt = ldotRt
    elif r == 2 or r == 5:
        currDotLft = mdotLft
        currDotRt = mdotRt
    elif r == 3 or r == 6:
        currDotLft = sdotLft
        currDotRt = sdotRt
    diff = round(0.5 * width(currDotLft))
    #step = round(0.1 * width(currDotLft))
    step = diff/2
    mult = 0.5
    if r < 4:
        prevDotLft = chgRadius(currDotLft, diff)
        prevDotRt = chgRadius(currDotRt, diff)
        dir = 1
    else:
        prevDotLft = chgRadius(currDotLft, -diff)
        prevDotRt = chgRadius(currDotRt, -diff)
        dir = -1
    while cont == True:
        wait = 1#random.uniform(2, 4)			# Choose a random amount of time from 2-4 seconds
        time.sleep(wait)						# Pause for this amount of time before showing dots
        testNum = testNum + 1					# Set number of the current test in the trial
        curritem = Item()
        curritem.trial = r					# create curritem, an instance of an Item, and set
        curritem.test = testNum				# it's trial and test numbers to the current values
        testText = canvas.create_text(W/2, 100, text = 'Test ' + str(testNum)) # Display the test number
        animation.update()


        side = random.randint(0, 1)		    # Randomly choose 0 or 1 to decide which side has standard dot
        if r < 4:
            if side == 0: ans = 'R'			# store the larger side (L, or R) in ans
            else: ans = 'L'
        else:
            if side == 0: ans = 'L'
            else: ans = 'R'
        curritem.answer = ans				# set curritem.ans to store the answer

		# If side = 0, base dot is on left. If 1, base dot on right
		# Trials 1, 2, 3: base dot is smaller. 4, 5, 6: base dot is larger

        if testNum < 3:				# Separate case for first 2 tests (before there are 2 previous tests to view)
            step = diff * mult
            if step < 1:
                step = 1
            newDotRt = chgRadius(prevDotRt, -step*dir)
            newDotLft = chgRadius(prevDotLft, -step*dir)
        elif results[(r-1)*tests+testNum - 1].correct == 'Yes' \
        and results[(r-1)*tests+testNum - 2].correct == 'Yes' :  	# Else if correct on the past 2 tests
            step = diff * mult
            if step < 1:
                step = 1
            if diff <= 1:
                newDotRt = chgRadius(prevDotRt, 0)
                newDotLft = chgRadius(prevDotLft, 0)
            else:
                newDotRt = chgRadius(prevDotRt, -step*dir)
                newDotLft = chgRadius(prevDotLft, -step*dir)
        elif results[(r-1)*tests+testNum - 1].correct == 'Yes' :	# Else if correct on just the past test,
            newDotRt = chgRadius(prevDotRt, 0)						# Keep dots same size
            newDotLft = chgRadius(prevDotLft, 0)
        else:
            newDotRt = chgRadius(prevDotRt, step*dir)
            newDotLft = chgRadius(prevDotLft, step*dir)
            mult = mult / 2
            step = diff * mult
            if step < 1:
                step = 1
                #print 'Multiplier: ' + str(mult)
            if step < 1 or testNum >= tests:
                cont = False

        if side == 0:						# If 0, show standard size dot on left
            show(currDotLft)
            show(newDotRt)
            diff = diffD(newDotRt, currDotLft)
        elif side == 1:						# If 1, show standard size dot on right
            show(currDotRt)
            show(newDotLft)
            diff = diffD(newDotLft, currDotRt)

        time.sleep(1)					# Display the dots for 10 milliseconds
        curritem.difference = diff			# Store dot difference in curritem
        hide(currDotLft)					# Hide all dots
        hide(currDotRt)						# currDot is always the standard dot
        hide(newDotRt)						# newDot and prevDot are the chged dots
        hide(newDotLft)
        prevDotRt = newDotRt				# change dots from this test to be prev dots
        prevDotLft = newDotLft
        animation.update()


        currGuess = raw_input("Left or Right? (F or J) ")		# Take guess as input from user;
        if currGuess == "F":
            curritem.guess = "L"
        elif currGuess == "J":					# Store this guess in curritem
            curritem.guess = "R"
        if curritem.guess == curritem.answer:
            curritem.correct = "Yes"			# Set correct to be Yes or No in curritem,
        else: curritem.correct = "No"			# depending on if guess is correct

		#print 'Diff' + str(curritem.difference)
		#print 'Correct?' + str(curritem.correct)

        if r == 1:
            curritem.dotSize = 'Large'
            curritem.baseSize = 'Smaller'
        elif r == 2:
            curritem.dotSize = 'Medium'
            curritem.baseSize = 'Smaller'
        elif r == 3:
            curritem.dotSize = 'Small'
            curritem.baseSize = 'Smaller'
        elif r == 4:
            curritem.dotSize = 'Large'
            curritem.baseSize = 'Larger'
        elif r == 5:
            curritem.dotSize = 'Medium'
            curritem.baseSize = 'Larger'
        elif r == 6:
            curritem.dotSize = 'Small'
            curritem.baseSize = 'Larger'

        results[(r-1)*tests+testNum] = curritem # store curritem in results vector

        hide(testText)
    hide(trialText)
    moveOn = raw_input("Next Trial? ")			# Require input to move on to next trial

##########################################################################################
### Output Data

num_correct = 0
tot_num_trials = 0
for i in range(len(results)):
    if results[i] != False:
        tot_num_trials = tot_num_trials + 1
        print 'Trial: ' + str(results[i].trial) + ' Test: ' + str(results[i].test)    \
	      + ' Dot Size: ' + str(results[i].dotSize) \
	      + ' Standard Dot Larger/Smaller than Test Dot? ' + str(results[i].baseSize) \
	      + ' Answer: ' + str(results[i].answer) + ' Guess: ' + str(results[i].guess) \
	      + ' Correct? ' + str(results[i].correct) + ' Difference: ' \
	      + str(results[i].difference)
        if results[i].correct == 'Yes':
			num_correct = num_correct + 1
print 'Total number correct: ' + str(num_correct) + ' out of ' + str(tot_num_trials)



animation.mainloop()

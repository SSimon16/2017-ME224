# 2017-ME224

Python code for ME224: Experimental Engineering experiment (Fall 2017)

## Summary
This code runs a program to test visual perception in users. Specifically, this code was used to experimentally determine the human visual perception limit when viewing two dots on a screen.
  
The experiment involves displaying two dots of various sizes on a computer screen for a short period of time: one on the left side and one on the right side. The user then inputs which dot is larger. The dot sizes adjust based on user input. If the user correctly inputs which dot is larger, then the next trial will display dots that are closer in size. If the user is incorrect, then the dots will have a larger gap in size on the next trial.

This approach narrows in on the range at which a user can determine which of the two dots is larger. The experiment runs through many tests over multiple trials, and then prints the results to screen when finished.

## How To Use
Run the experiment.py file in the command line. 

Enter "Y" in the command line when prompted to move to the next step.

The program will open a new window to display dots, which looks like this:
![Sample Window Image](https://github.com/SSimon16/2017-ME224/blob/main/sample-screen.png)


Once the dots have disappeared, type "J" in the command line if the dot on the right is larger, and type "F" if the dot on the left is larger. Hit enter, and the next set of dots will be displayed about a second later.

Continue through all 3 trials, and then results will be printed to the terminal screen.

## Notes
This project is part of the ME224: Experimental Engineering course at Northwestern Unversity in Fall 2017. 

This code runs on Python 2.X

## Questions and Feedback
Please contact Spencer Simon at spencersimon16@gmail.com with questions or feedback.


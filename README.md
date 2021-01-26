# 2017-ME224

Python code for ME224: Experimental Engineering experiment (Fall 2017)

## Overview
This code runs a program to test visual perception in users. Specifically, this code was used to experimentally determine the human visual perception limit when viewing two dots on a screen.
  
The experiment involves displaying two dots of various sizes on a computer screen for a short period of time: one on the left side and one on the right side. The user then inputs which dot is larger. The dot sizes adjust based on user input. If the user correctly inputs which dot is larger, then the next trial will display dots that are closer in size. If the user is incorrect, then the dots will have a larger gap in size on the next trial. This adaptive staircase method is a quick and reliable way to determine the threshold.

This approach narrows in on the range at which a user can determine which of the two dots is larger. The experiment runs through many tests over multiple trials, and then prints the results to screen when finished.

### Project Goal
This project seeks to quantify the human eye’s ability to discriminate intensity (size) differences between similar shapes of various sizes. By comparing sets of circles with diameters of ranging magnitude and size differences, we can create a simple model for size discrimination across a
variety of stimuli intensities.

This model has applications in typography and marketing, where subtle, perceptible changes in font or image size can impact the consumer perception of depth or importance as well as the emerging field of augmented and virtual reality, where creating an accurate stereoscopic environment enhances users' experience.

### Hypothesis 
The change in size of similar shapes that is just noticeable is proportional to the original shape size and can possibly be modeled with the Weber-Fechner law such that the the change in a stimulus that will be just noticeable is a constant ratio of the original stimulus.

## How To Use
Run the experiment.py file in the command line. 

Enter "Y" in the command line when prompted to move to the next step.

The program will open a new window to display dots, which look like this:
![Sample Window Image](https://github.com/SSimon16/2017-ME224/blob/main/sample-screen.png)


Once the dots have disappeared, type "J" in the command line if the dot on the right is larger, and type "F" if the dot on the left is larger. Hit enter, and the next set of dots will be displayed about a second later.

Continue through all 3 trials, and then results will be printed to the terminal screen.

## Notes
This project is part of the ME224: Experimental Engineering course at Northwestern Unversity in Fall 2017. This project was undertaken in partnership with Marshall Auer, Patrick Doyle, Benjamen Lim, Gabe Pinkus, and Spencer Simon.

This code runs on Python 2.X. All code was written by Spencer Simon. 

## Questions and Feedback
Please contact Spencer Simon at spencersimon16@gmail.com with questions or feedback.


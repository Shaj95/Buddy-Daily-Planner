"""
This program is a comprehensive day planner called "Buddy".

It prompts the user to input their favorite foods, hobbies, music, study plans
and sleeping habits.

It then provides recommendations and reminders of how to go about the day
as well as the total caloric intake, the total cost of food

The program checks up on the user everyday and provides emotional support and recommendations

It then asks the user to indicate how many recommendations were followed
"""
import random

# Greeting

print("Welcome to Buddy! This program will plan your day for you based on your work, hobbies, music, favorite foods etc. and will provide you with \
recommendations of how to go about your day")
print("Buddy will also check up on you every now and then and provide you with emotional support")
print("Let me hand you over to Buddy now!")

from Data_Test import Data
from Data_Test import breakfast, lunch, dinner

x = Data()

print(f"\nHi {x.getUsername()}! My name is Buddy and I will be helping you plan your day and providing you with various recommendations.\
\nBut first I need to collect some information in order to create a planner and recommendations that cater to your lifestyle.")

x.addHobbies()
x.addSubjects()
x.addSongs()
x.addBreakfast()
x.addLunch()
x.addDinner()



print(f"\nGood morning {x.getUsername()}!")
print("Here's how I have planned your day out for you:\n")
x.getBreakfastPick()
print("9:00 am – Start study/work")
x.getHobbyPick()
x.getLunchPick()
print("3:00 pm – Library/work again")
print("7:00 pm - I will help you take a break")
x.getDinnerPick()

print("\n-----------\nEvening Arrives\n-------------")

print("\nIt’s evening, you’ve spent a lot of time on your work. It’s time to take a breather. Close your books. Close your eyes. \
Clear your mind and listen to these 7 songs that I have selected for you. This will help you relax for the next 40 minutes.\n")

print(x.getSongPicks())

from Buddy_CheckUp_Function import get_complaint_type

from Buddy_CheckUp_run import buddyChecksUp
    
buddyChecksUp()

had_dinner = input("\nIt's 10:00 pm – Have you had dinner yet?\n")

if (had_dinner == "yes" or had_dinner == "YES" or had_dinner[0] == "y" or had_dinner[0] == "Y"):
    print("Good!")
else:
    print("Don’t go to bed on an empty stomach!")
        
print("\nYou should probably wind down now and play guitar, watch a series or talk to your family")

follow_recs = eval(input("\nIt's 11:30 pm – It’s bedtime. How many of my recommendations did you follow today?\n"))

while follow_recs < 0 or follow_recs > 12:
    print("sorry, please input a number from 0 to 12")
    follow_recs = eval(input("How many of my recommendations did you follow today?\n"))
else:
    if (follow_recs <= 4):
        print("Oh, you can do better! Remember: these are designed to improve your time management, relieve \
        stress and to help keep you active in your personal interests. Let’s try again tomorrow. Goodnight!")
    elif (follow_recs > 4 and follow_recs <= 6):
        print("That’s a good start! Goodnight!")
    elif (follow_recs > 6 and follow_recs <= 8):
        print("That's pretty good! Goodnight!")
    else:
        print("Glad I could help! Goodnight!")

total_cal = breakfast[1] + lunch[1] + dinner[1]
total_cost = breakfast[2] + lunch[2] + dinner[2]
print(f"\nThe total calories consumed today are {total_cal}cal and your total cost of food today is $ {total_cost:.2f}")

print("\n-----------\nWeekend Arrives\n-------------")

from Buddy_Weekend_Checkup import WeekendCheckUp
WeekendCheckUp()

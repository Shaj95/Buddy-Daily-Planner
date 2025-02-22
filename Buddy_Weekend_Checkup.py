
def WeekendCheckUp():

    #Precondition:

    suggested_actions = ["meditating", "sleeping eight hours at night", \
    "relaxing and listening to music", "going out on weekends", "spending two hours a day with friends",]

    new_recommend = set()

    #Post1:

    complaint = input("Following up on our previous chat, let me know what you're feeling now: \n")

    #Post2:

    duration = eval(input("How many days (between 1 and 31) have you experienced '" + complaint + "'? \n"))

    # Month validity

    while duration < 1 or duration > 31:
        print("Sorry, input a value between 1 and 31")
        duration = eval(input("How many days has it been?\n"))
    else:

        # Sympathy Sessage
            
        print(duration, "days is significant. Sorry to hear it.")

        # Action Recommended

        if duration >= 3:    

            for action in suggested_actions:
                answer = input('Have you tried ' + action + '? Please answer y for Yes or n for No:' + "\n")
                if (answer[0] == "n" or answer[0] == "N"):
                    new_recommend.add(action)

        # Actions not taken
                    
            print("After careful analysis, here is Buddy's advice:")
            for actions_not_taken in new_recommend:
                print(actions_not_taken)

        # if number of months is greater than or equal to 1 but less than 3

        else:
            print("However, we'll see if it continues after " + str(3 - int(duration)) +" days.")
        

#Precondition:



def buddyChecksUp():

    from Buddy_CheckUp_Function import get_complaint_type
    
    #the following list of lists has list elements that will be selected based on the complaint_type 
    advice_per_type = [["That's great to hear!"],
                       ["I think you should take a break from work and try distract yourself.", "Given how you are feeling, it's okay to reach out to someone.", "I'd suggest that you schedule a counselling visit if this persists."],
                       ["These things happen from time to time.", "It's okay. They'll come around", "Maybe try and reflect on how you could have handled things differently?"],
                       ["Don't forget you'll be meeting them soon during the winter vacations!", "Perhaps call a family member this evening after dinner?"],
                       ["Maybe you're feeling like this because you missed your workout", "You've got to eat and remember to stay hydrated!"]]

    #Post1:

    user_complaint=input("\nJust wanted to check up on you this evening. How are you feeling today?\n")

    #Post4:

    observed_complaint_type = get_complaint_type(user_complaint)
    #print (observed_complaint_type)

    #Post (remedies):
             
    for complaint in observed_complaint_type:
        for advice in advice_per_type[complaint]:
            print (advice)

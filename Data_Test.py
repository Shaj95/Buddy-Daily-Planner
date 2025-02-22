import random

breakfast, lunch, dinner = [], [], []

class Data:

    def __init__(self):

        #Prompt username
        
        self.__user_name = input("\nWhat is your name?\n")

        # Lists and dictionaries to be populated
        
        self.__songs = []       
        self.__hobbies = []
        self.__subjects = []
        self.__breakfast = {}
        self.__lunch = {}
        self.__dinner = {}

        global breakfast, lunch, dinner

    def addHobbies(self):

        print("\nLet's start off by telling me 5 hobbies.\n")
        
        for i in range (5):
            user_hobbies = input("Please enter a hobby:\n")
            self.__hobbies.append(user_hobbies)

    def addSubjects(self):

        print("\nGreat! Now tell me how many university subjects you have, followed by what those subjects are called")
        num_subjects = eval(input("How many subjects do you have?\n"))

        for i in range (0, num_subjects):
            user_subjects = input("Please enter a subject:\n")
            self.__subjects.append(user_subjects)
        
    def addSongs(self):

        print("\nPerfect! Now tell me 10 songs that you like to listen to when relaxing.")

        for i in range (10):
            user_songs = input("Please enter a song:\n")
            self.__songs.append(user_songs)

    def addBreakfast(self):

        print("\nThose are good songs! And lastly, tell me 4 meal options each that you could have for breakfast, lunch and dinner.")
        print("\nWhen prompted, give me the name of the meal followed by caloric value and cost")
        print("For example:\n")
        print("\nmeal name")
        print("x, y") 

        # Breakfast

        print("\nWhat are 2 meals that you like to have for breakfast?\n")
        for i in range(2):
            meal = input("Please enter a meal:\n")
            data = tuple(input("Enter its data:\n").split(', '))
        
            self.__breakfast[meal] = data

    def addLunch(self):

        print("\nWhat are 2 meals that you like to have for lunch?\n")
        for i in range(2):
            meal = input("Please enter a meal:\n")
            data = tuple(input("Enter its data:\n").split(', '))

            self.__lunch[meal] = data


    def addDinner(self):

        print("\nWhat are 2 meals that you like to have for dinner?\n")
        for i in range(2):
            meal = input("Please enter a meal:\n")
            data = tuple(input("Enter its data:\n").split(', '))

            self.__dinner[meal] = data
        
    def getUsername(self):
        #print("Your username is:\n")
        return self.__user_name

    def getSongs(self):
        return self.__songs

    def getSongPicks(self):
        
        playing_songs = random.sample(self.__songs, 7)
        for i in playing_songs:
            print(i)

    def getHobbies(self):
        return self.__hobbies

    def getHobbyPick(self):
        hobby_pick = random.choice(self.__hobbies)
        print(f"1:00 pm – I'd suggest {hobby_pick} if you don't workout today")
        

    def getSubjects(self):
        return self.__subjects

    def getBreakfastDict(self):
        return self.__breakfast

    def getBreakfastPick(self):
        bfast_pick = key, val = random.choice(list(self.__breakfast.items()))
        bfast_meal = bfast_pick[0]
        bfast_data = bfast_pick[1]
        bfast_cal = int(bfast_data[0])
        bfast_cost = float(bfast_data[1])
        breakfast.append(bfast_meal)
        breakfast.append(bfast_cal)
        breakfast.append(bfast_cost)

        print(f"8:30 am – Breakfast: {bfast_meal}. It's Caloric Value is {bfast_cal}Cal and it costs you $ {bfast_cost:.2f}")

    def getLunchDict(self):
        return self.__lunch

    def getLunchPick(self):

        lunch_pick = key, val = random.choice(list(self.__lunch.items()))
        lunch_meal = lunch_pick[0]
        lunch_data = lunch_pick[1]
        lunch_cal = int(lunch_data[0])
        lunch_cost = float(lunch_data[1])
        lunch.append(lunch_meal)
        lunch.append(lunch_cal)
        lunch.append(lunch_cost)

        print(f"2:00 pm – Lunch: {lunch_meal}. It's Caloric Value is {lunch_cal}Cal and it costs you $ {lunch_cost:.2f}")

    def getDinnerDict(self):
        return self.__dinner


    def getDinnerPick(self):

        dinner_pick = key, val = random.choice(list(self.__dinner.items()))
        dinner_meal = dinner_pick[0]
        dinner_data = dinner_pick[1]
        dinner_cal = int(dinner_data[0])
        dinner_cost = float(dinner_data[1])
        dinner.append(dinner_meal)
        dinner.append(dinner_cal)
        dinner.append(dinner_cost)
        
        print(f"9:30 pm – Dinner: {dinner_meal}. It's Caloric Value is {dinner_cal}Cal and it costs you $ {dinner_cost:.2f}")

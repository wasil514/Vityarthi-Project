def datetime():
    import datetime
    result= datetime.datetime.now()
    return str(result)

def patient_workout(person):
    times= int(input("for how many times does the patient needs to do exercise\n"))
    for i in range (0,times,1):
        with open(person +"_workout.txt",'a')as p:
            text=input("Enter the exercises to be done today\n")
            p.write("["+datetime()+"]"+" - ")
            p.write(text+"\n\n")


def patient_diet(person):
    times=int(input("For how many times do u want to log for the meal\n"))
    for i in range(times):
       meal=input("Enter the meal name and the time of the meal like breakfast, dinner\n")
       with open(person+"_diet.txt",'a') as d:
           d.write("["+datetime()+"]"+" - ")
           d.write(meal+"\n\n")

def retrieve_patient_diet(person):
    with open(person+"_diet.txt") as d:
        for line in d:
            print(line)

def retrieve_patient_workout(person):
    with open(person+"_workout.txt") as w:
        for line in w:
            print(line)


Trainer_or_patient=  input("Enter who is using the system trainer or the patient\n").capitalize()
if Trainer_or_patient=="Trainer":
    diet_or_workout= input("Good morning sir!, Do you want to log the workout or the diet\n").capitalize()
    if diet_or_workout=="Workout":
        patient= input("For which patient do you want to write to workout plan for \n\nRobin\nCadence\nJulie\nJett\n").capitalize()
        if patient=="Robin":
           patient_workout(patient)
        elif patient=="Cadence":
            patient_workout(patient)
        elif patient=="Julie":
            patient_workout(patient)
        elif patient=="Jett":
            patient_workout(patient)
        else:
            print("Please enter a valid person\n")
    
    elif diet_or_workout=="Diet":
        patient=input("For which patient do you want to write to workout plan for \n\nRobin\nCadence\nJulie\nJett\n").capitalize()
        if patient=="Robin":
            patient_diet(patient)
        elif patient=="Cadence":
            patient_diet(patient)
        elif patient=="Julie":
            patient_diet(patient)
        elif patient=="Jett":
            patient_diet(patient)
        else:
            print("Please enter a valid person\n")

elif Trainer_or_patient=="Patient":
    workout_or_diet=input("Enter whether you want to retrieve Diet schedule or exercise schedule\n").capitalize()
    if workout_or_diet=="Diet":
        person=input("who is using the patient manual \n is it Robin\nCadence\nJulie\t or\nJett\n").capitalize()
        if person=="Robin":
            retrieve_patient_diet(person)
        elif person=="Cadence":
            retrieve_patient_diet(person)
        elif person=="Julie":
            retrieve_patient_diet(person)
        elif person=="Jett":
            retrieve_patient_diet(person)
        else:
            print("Please enter a valid person's input\n")

    elif workout_or_diet=="Workout":
        person=input("who is using the patient manual \n is it Robin\nCadence\nJulie\t or\nJett\n").capitalize()
        if person=="Robin":
            retrieve_patient_workout(person)
        elif person=="Cadence":
            retrieve_patient_workout(person)
        elif person=="Julie":
            retrieve_patient_workout(person)
        elif person=="Jett":
            retrieve_patient_workout(person)
        else:
            print("Please enter a valid input\n")
        


    




    
#calculator using no packages

solution = 0
answers = []
keep_going = True

#USER INPUT --------------------------------------------------------------------------------------------------------------------------------------------------------------

while keep_going == True:
    #ASKING AND VERIFYING FOR RESPONSE TO TYPE OF EQUATION
    while True:
        userinput = input("Do you want to ADD, SUBTRACT, MULTIPLY, DIVIDE, or see your previous ANSWERS: ") 
        if userinput.lower() not in ('add', 'subtract', 'multiply', 'divide', 'answers') :     
            print("You have entered an incorrect response")
            continue
        else:
            break
    
    #IF IT ISNT ANSWER, ASK FOR NUMBERS, ELSE, RETRIEVE PREVIOUS ANSWERS
    if userinput != "answers":
        #ASKING AND VERIFYING FOR RESPONSE TO WHAT IS FIRST NUMBER
        while True:
            try:
                x = float(input('First number: '))
                break
            except ValueError:
                print("The input was not a valid number. ")
                continue

        #ASKING AND VERIFYING FOR RESPONSE TO WHAT IS SECOND NUMBER
        while True:
            try:
                y = float(input('Second number: '))
                break
            except ValueError:
                print("The input was not a valid number. ")
                continue
    else:
        if len(answers) == 0:
            print("You have no previous answers. ")
        else: 
            result = ', '.join(str(item) for item in answers)
            print("Your previous answers are: " + result)
    
    #OPERATIONS -------------------------------------------------------------------------------------------------------------------------------------------------------

    userinput.lower()

    #ADDITION
    if userinput == "add":
        solution = x + y
        answers.append(solution)
        print("The solution is: " + str(solution))

    #SUBTRACT
    if userinput == "subtract":
        solution = x - y
        answers.append(solution)
        print("The solution is: " + str(solution))

    #MULTIPLY
    if userinput == "multiply":
        solution = x * y
        answers.append(solution)
        print("The solution is: " + str(solution))

    #DIVIDE
    if userinput == "divide":
        solution = x / y
        answers.append(solution)
        print("The solution is: " + str(solution))
    

    #ASKING AND VERIFYING CONTINUATION OR QUITTING --------------------------------------------------------------------------------------------------------------------

    while True:
        userinput = input("Do you want to QUIT or CONTINUE: ") 
        if userinput.lower() not in ('quit', 'continue') :     
            print("You have entered an incorrect response, please try again")
            continue
        if userinput.lower() == "quit":
            keep_going = False
            break
        if userinput.lower() == "continue":
            keep_going = True
            break

input("Press any key to exit")
    
    



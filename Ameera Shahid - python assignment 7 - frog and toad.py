#menu
print('Hello and welcome to the lilypad game')

option = input('\nMenu\nPlease enter one of the following\nD) Demonstration\nP) Play game\nR) Reset\nE) Exit\n').lower()
optiond = 'd'
optionp = 'p'
optionr = 'r'
optione = 'e'
optionc = 'c'

#while loop to ensure the user inputs a valid option
while option != optiond and option != optionp and option != optionr and option != optione:
    print('\n\nPlease choose a valid option')
    option = input('\nMenu\n----\nPlease enter one of the following\n\nD) Demonstration\nP)Play game\nR) Reset\nE) Exit \n').lower()

#while loop as there is no need to restart the game before the player even starts the game - ensures the player chooses to play first
while option == optionr:
    print('There is no need to restart the game before you even start, please choose another option first')
    option = input('\nMenu\n----\nPlease enter one of the following\n\nD) Demonstration\nP)Play game\nR) Reset\nE) Exit \n').lower()

#while loop so that whilst the player still wants to play, the game continues
while option != optione:
    
    #states different lists that will be used throughout
    frogandtoad= ['F','F','F',' ', 'T','T','T']
    finalfrogandtoad = ['T','T','T',' ','F','F','F']
    exampleofmove = ['F','F','','F','T','T','T']
    positionpanel = ['1','2','3','4','5','6','7']
    moves = 0

    #function for demonstration - easier than copying it out every time - calls frogandtoad, finalfrogandtoad and exampleofmove to display the instructions
    def demonstration(frogandtoad, finalfrogandtoad, exampleofmove):
        print('\nDEMONSTRATION \n-------------')
        print('\nAIM OF THE GAME: switch positions of the frogs(F) and toads(T) as shown:\n',frogandtoad, 'to', finalfrogandtoad)
        print('\nTo move, you must enter a FROM and TO position for each move:5')
        print('\nFor example, from the starting postion', frogandtoad,':')
        print('FROM: 3 \nTO: 4 \nGives', exampleofmove)
        print('\nRULES \n-----')
        print('\n1) Frogs can only move to the right and toads can only move to the left')
        print('\n2) The frog or toad can move one place into an empty space or jump over on other frog or toad to move into an empty space')

    # function to swap the positions of firstposition and secondposition within the list frogandtoad
    def swappositions(frogandtoad, firstposition, secondpostion): 
      
        frogandtoad[firstposition], frogandtoad[secondposition] = frogandtoad[secondposition], frogandtoad[firstposition]
        return frogandtoad

    # calls on and displays demonstration function when user needs it
    if option == optiond:
        demonstration(frogandtoad, finalfrogandtoad, exampleofmove)

    # player plays the game
    elif option == optionp:
        #prints position and lilypad panel so user can see the list
        print ('position panel', positionpanel)
        print ('lillypad panel', frogandtoad)

        
        #while game has not been won - keep playing
        while frogandtoad != finalfrogandtoad :

            #allows user to choose whether they want to keep playing, look at the demonstration, restart or exit the game
            optiontwo = input('C) Continue\nD) Demonstration\nR) Restart\nE) Exit\n')

            #while loop to ensure a valid option is entered
            while (optiontwo != optionc) and (optiontwo != optiond) and (optiontwo!= optionr):
                print('please enter a valid option')
                optiontwo = input('C) Continue\nD) Demonstration\nR) Restart\nE) Exit\n')

            # while they do not want to restart, keep playing the game
            while (optiontwo != optionr) and (frogandtoad != finalfrogandtoad):
                if optiontwo == optionc:
            
                    firstposition = (int(input('FROM\n')))
                    while(firstposition != 1 and firstposition != 2 and firstposition != 3 and firstposition != 4 and firstposition != 5 and firstposition != 6 and firstposition != 7 ) :
                        firstposition = (int(input('Please choose a valid value in the range 1-7\nFROM')))
                

                    secondposition = (int(input('TO\n')))
            
                    while (secondposition != 1 and secondposition != 2 and secondposition != 3 and secondposition != 4 and secondposition != 5  and secondposition != 6  and secondposition != 7):
                        secondposition = (int(input('Please enter a valid value between 1 and 7\nTO:')))
    
                    firstposition = firstposition -1
                    secondposition = secondposition -1
            
                    # for loop, checks valid moves within the list
                    for i in frogandtoad[secondposition]:
                        if (i != ' ') or (secondposition != firstposition +1) and (secondposition != firstposition +2) and (secondposition != firstposition -1) and (secondposition != firstposition -2) :
                            print('Invalid move - can only move frog or toad one space to a free space or jump over one frog or toad')

                        elif (i == ' '):
                            for i in frogandtoad[firstposition]:
                                if (i == 'F') and (secondposition <= firstposition):
                                    print('Invalid move - Frogs can only move right')
                                elif ( i == 'T') and (secondposition >= firstposition):
                                    print('Invalid move- Toads can only move left')
                                else:
                                    print ('position panel', positionpanel)
                                    print('lilypad panel ', swappositions(frogandtoad, firstposition, secondposition))
                                    moves = moves+1
                        # print out position and lilypad panel and the swaps that have been made each round so the user can see what theyre doing
                        # add 1 move so user can see how many moves it took at the end
                        else:
                            print ('position panel', positionpanel)
                            print('lilypad panel ', swappositions(frogandtoad, firstposition, secondposition))
                            moves = moves+1
                        
                    optiontwo = input('C) Continue\nD) Demonstration\nR) Restart\nE) Exit\n')
                    while (optiontwo != optionc) and (optiontwo != optiond) and (optiontwo!= optionr):
                        print('please enter a valid option')
                        optiontwo = input('C) Continue\nD) Demonstration\nR) Restart\nE) Exit\n')

                    
                #asks for optiontwo again so the game knows if it has t leave the while loop to restart or not
                elif optiontwo == optiond:
                    demonstration(frogandtoad, finalfrogandtoad, exampleofmove)
                    optiontwo = input('C) Continue\nD) Demonstration\nR) Restart\nE) Exit\n')
                    while (optiontwo != optionc) and (optiontwo != optiond) and (optiontwo!= optionr):
                        print('please enter a valid option')
                        optiontwo = input('C) Continue\nD) Demonstration\nR) Restart\nE) Exit\n')
                    if optiontwo == optionc:
                        print ('position panel', positionpanel)
                        print ('lillypad panel', frogandtoad)
                        
            #restarts the game when the user wants 
            while optiontwo ==optionr and (frogandtoad != finalfrogandtoad):
                frogandtoad= ['F','F','F',' ', 'T','T','T']
                moves = 0
    
                
                print ('position panel', positionpanel)
                print ('lillypad panel', frogandtoad)
            
                firstposition = (int(input('FROM\n')))
                while(firstposition != 1 and firstposition != 2 and firstposition != 3 and firstposition != 4 and firstposition != 5 and firstposition != 6 and firstposition != 7 ) :
                    firstposition = (int(input('Please choose a valid value in the range 1-7\nFROM')))
                

                secondposition = (int(input('TO\n')))
            
                while (secondposition != 1 and secondposition != 2 and secondposition != 3 and secondposition != 4 and secondposition != 5  and secondposition != 6  and secondposition != 7):
                    secondposition = (int(input('Please enter a valid value between 1 and 7\nTO:')))
    
                firstposition = firstposition -1
                secondposition = secondposition -1
            
        
                for i in frogandtoad[secondposition]:
                    if (i != ' ') or (secondposition != firstposition +1) and (secondposition != firstposition +2) and (secondposition != firstposition -1) and (secondposition != firstposition -2) :
                        print('Invalid move - can only move frog or toad one space to a free space or jump over one frog or toad')

                    elif (i == ' '):
                        for i in frogandtoad[firstposition]:
                            if (i == 'F') and (secondposition <= firstposition):
                                print('Invalid move - Frogs can only move right')
                            elif ( i == 'T') and (secondposition >= firstposition):
                                 print('Invalid move- Toads can only move left')
                            else:
                                print ('position panel', positionpanel)
                                print('lilypad panel ', swappositions(frogandtoad, firstposition, secondposition))
                                moves = moves+1
                            
                    else:
                        print ('position panel', positionpanel)
                        print('lilypad panel ', swappositions(frogandtoad, firstposition, secondposition))
                        moves = moves+1
                        
                optiontwo = input('C) Continue\nD) Demonstration\nR) Restart\nE) Exit\n')
                while (optiontwo != optionc) and (optiontwo != optiond) and (optiontwo!= optionr):
                    print('please enter a valid option')
                    optiontwo = input('C) Continue\nD) Demonstration\nR) Restart\nE) Exit\n')

        
        # shows the user they have won the game once they complete it and how many moves it took
        if frogandtoad == finalfrogandtoad:
            print("You have won the game")
            print('Total moves:',moves)
            print('Minimum number of moves = 15')
            
    
    # once game ends, menu is redisplayed and the user can choose to leave the game or continue.
    option = input('\nMenu\n----\nPlease enter one of the following\nD) Demonstration\nP)Play game\nR) Reset\nE) Exit \n').lower()
    while option != optiond and option != optionp and option != optionr and option != optione:
        print('\n\nPlease choose a valid option')
        option = input('\nMenu\n----\nPlease enter one of the following\nD) Demonstration\nP)Play game\nR) Reset\nE) Exit \n').lower()
    
#ends game
if option == optione:
    print('\nThank you for playing \nGoodbye')
    

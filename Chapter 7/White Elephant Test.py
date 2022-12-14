#Imports
import random

def white_elephant(): #Exercise 12 ###############################    FAILED
    #white elephant accepts no arguments
    #it will contain people from many departments
    #and they will all give gifts to other
    #people in other apartments
    #SECRET SANTA
    
    #Create a try block
    try:
        
        #Create a list with everyone's name
        people = ['Julia','Oliver','Abigail','Camden','Kayleigh','Cooper','Kerrigan'
                  ,'Avergy','Charlotte','Elle']
        
        #Create two more lists for those who've given gifts and those who've been given gifts
        given = []
        received = []
        
        #Create another list to never have two peple give gifts to each other(unless it works)
        past_index = [0,1,2,3,4,5,6,7,8,9]
        
        #Create three booleans
        cont = False
        done = False
        keep_going = False
        
        #Add accumulators to know how many people from each department has given gifts
        DD = 0
        HRD = 0
        SD = 0
        
        #Message before the loops
        print('Here are the results:')
        
        #Create a loop for everything
        while not done:
            
            #Create a loop to find gifters
            while not cont:
                
                #Reset keep_going to True everytime
                keep_going = True
                    
                #Find the person who will give a gift
                giving_index = random.randint(0,9)
                gifter = people[giving_index]
                
                #Check to see if that person has given yet
                #If so, loop again
                if gifter in given:
                    cont = False
                #If not, add them to the list and stop looping
                else:
                    cont = True
                    given.append(gifter)
                    
            #Reset the boolean
            cont = False
            print(giving_index)
            #Check and see if the department chosen has already had two gifters
            if DD == 2 and giving_index <= 2:
                keep_going = False
            elif SD == 2 and giving_index >= 7:
                keep_going = False
            elif HRD == 2 and giving_index >=3 and giving_index <= 6:
                keep_going = False
            
            #If all of the departments had had 2 people already, then continue
            if DD >= 2 and SD >= 2 and HRD >= 2:
                keep_going = True
            
            #Run these if statements IF AND ONLY IF keep_going is True
            if keep_going:
                    
                #Check to see which department that person came from and choose a random number from a different department
                if giving_index <= 2: #If they are in DD
                    
                    #Add 1 to the Development Department
                    DD += 1
                    
                    #Create a while loop to find receivers
                    while not cont:
                        
                        #Find a random number between the other two departments
                        index = random.randint(3,9)
                        receiver = people[index]
                        print(index)
                        #Check to see if that person has recieved yet
                        #If so, loop again
                        if receiver in received:
                            cont = False
                        elif past_index[giving_index] == index:
                            cont = False
                        #If not, add them to the list and stop looping
                        else:
                            cont = True
                            received.append(receiver)
                            
                    #Reset the boolean variable
                    cont = False
                    
                    #put the giver's number into the receiver's spot in the past index list
                    past_index[index] = giving_index
                    
                #Check to see which department that person came from and choose a random number from a different department
                elif giving_index >= 3 and giving_index <= 6: #If they are in HRD
                    
                    #Add to the HR Department
                    HRD += 1
                    
                    #Create a while loop to find receivers
                    while not cont:
                        
                        #Find a random number between the other two departments
                        index = random.randint(0,9)
                        receiver = people[index]
                        print(index)
                        #Check to see if that person has recieved yet
                        #If so, loop again
                        if receiver in received or index >= 3 and index <= 6:
                            cont = False
                        elif past_index[giving_index] == index:
                            cont = False
                        #If not, add them to the list and stop looping
                        else:
                            cont = True
                            received.append(receiver)
                            
                    #Reset the boolean variable
                    cont = False
                    
                    #put the giver's number into the receiver's spot in the past index list
                    past_index[index] = giving_index

                #Check to see which department that person came from and choose a random number from a different department
                elif giving_index >= 7: #If they are in SD
                    
                    #Add 1 to the Sales Department
                    SD += 1
                    
                    #Create a while loop to find receivers
                    while not cont:
                        
                        #Find a random number between the other two departments
                        index = random.randint(0,6)
                        receiver = people[index]
                        print(index)
                        #Check to see if that person has recieved yet
                        #If so, loop again
                        if receiver in received:
                            cont = False
                        elif past_index[giving_index] == index:
                            cont = False
                        #If not, add them to the list and stop looping
                        else:
                            cont = True
                            received.append(receiver)
                            
                    #Reset the boolean variable
                    cont = False
                    
                    #put the giver's number into the receiver's spot in the past index list
                    past_index[index] = giving_index
                    
                #Print out the message at the end of everything
                print(gifter, 'gifts to', receiver)
            
            #Check to see if everyone has been used
            if len(people) == len(given) == len(received):
                done = True
            else:
                done = False
        print(given, '\n', received)
    except ValueError as err:
        print(err)

#=======#
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#=======#
        
def we2(): #For Exercise 12 ###############################      FAILED
    #white elephant accepts no arguments
    #it will basically create a secret santa list
    #for everyone within three companies
    
    #Create a try block
    try:
        
        #Create a list for all the people in their respective companies
        DD = ['Julia','Oliver','Abigail']
        HRD = ['Camden','Kayleigh','Cooper','Kerrigan']
        SD = ['Avery','Charlotte','Elle']
        
        #Combine the lists
        people = DD + HRD + SD
        
        #Mix the list
        random.shuffle(people)
        
        #Create boolean variables
        cont = False
        keep_going2 = True
        
        #Accumulators
        index1 = 0
        DDc = 0
        HRDc = 0
        SDc = 0
        
        #Loop eveything
        while keep_going2:
                
            #Loop to find persons
            while not cont:
                    
                #Pair each person in the list with the person to their right
                gifter = people[index1]
                index1 += 1
                i = people[index1]
                if i in DD and gifter in DD or i in HRD and gifter in HRD or i in SD and gifter in SD:
                    cont = False
                    index1 -= 1
                    random.shuffle(people)
                else:
                    cont = True
                    receiver = i
            
            #Print that person and their receiver
            print(gifter, 'gifts to', receiver)
            
            #Check to see if any company is done
            if gifter in DD:
                DDc += 1
            elif gifter in HRD:
                HRDc += 1
            elif gifter in SD:
                SDc += 1
            
            #Remove people if necessary
            if DDc >= 3:
                people.remove('Julia')
                people.remove('Oliver')
                people.remove('Abigail')
            elif HRDc >= 3:
                people.remove('Camden')
                people.remove('Kayleigh')
                people.remove('Coooper')
                people.remove('Kerrigan')
            elif SDc >= 3:
                people.remove('Avery')
                people.remove('Charlotte')
                people.remove('Elle')
                
            if people == []:
                keep_going2 = False
                
    except NameError as err:
        print(err)
            
#============#
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def we(): #For Exercise 12 ################################   FAILED
    #white elephant accepts no arugments
    #it will play secret santer
    
    #Create lists for all the names in their own companies
    DD = ['Julia','Oliver','Abigail']
    HRD = ['Camden','Kayleigh','Cooper','Kerrigan']
    SD = ['Avery','Charlotte','Elle']
    
    #Create a list that has everyone
    people = DD + HRD + SD
    #Shuffle all of the lists
    random.shuffle(DD)
    random.shuffle(HRD)
    random.shuffle(SD)
    
    #Variable
    index = 0
    
    #Apply names in DD to names in HRD or SD
    gifter = DD[index]
    num = random.randint(3,9)
    receiver = people[index]
     
    #Create a list that 
    
    
#=====================#
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def white(): #For Exercise 12
    #secret santa
    
    #Create lists for all the names in their own companies
    DD = ['Julia','Oliver','Abigail']
    HRD = ['Camden','Kayleigh','Cooper','Kerrigan']
    SD = ['Avery','Charlotte','Elle']
    
    #Create a list that has everyone
    people = DD + HRD + SD
    
    #Shuffle all of the lists
    random.shuffle(people)
    
    print('Here are the results:')
    
    #Apply givers to receivers
    gifter = people[3]
    receiver = people[9]
    
    #print
    print(gifter, 'gifts to', receiver)
    
    #Apply givers to receivers
    gifter = people[9]
    receiver = people[1]
    
    #print
    print(gifter, 'gifts to', receiver)
    
    #Apply givers to receivers
    gifter = people[1]
    receiver = people[6]
    
    #print
    print(gifter, 'gifts to', receiver)
    
    #Apply givers to receivers
    gifter = people[6]
    receiver = people[0]
    
    #print
    print(gifter, 'gifts to', receiver)
    
    #Apply givers to receivers
    gifter = people[0]
    receiver = people[8]
    
    #print
    print(gifter, 'gifts to', receiver)
    
    #Apply givers to receivers
    gifter = people[8]
    receiver = people[3]
    
    #print
    print(gifter, 'gifts to', receiver)
    
    #Apply givers to receivers
    gifter = people[7]
    receiver = people[5]
    
    #print
    print(gifter, 'gifts to', receiver)
    
    #Apply givers to receivers
    gifter = people[5]
    receiver = people[4]
    
    #print
    print(gifter, 'gifts to', receiver)
    
    #Apply givers to receivers
    gifter = people[4]
    receiver = people[2]
    
    #print
    print(gifter, 'gifts to', receiver)
    
    #Apply givers to receivers
    gifter = people[2]
    receiver = people[7]
    
    #print
    print(gifter, 'gifts to', receiver)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def white_elephant(): #THIS IS MISSING THE PART WHERE IT CHECKS TO SEE IF IndexR IS IN THE SAME COMPANY AS IndexG VICE VERSA
    #white elephant accepts no arguments
    #it will pair people from different companies that will give gifts to each other
    #this is basically a program for making a Secret Santa list
    
    #Create a try block
    try:
        
        #Create a list for everyone and their respective companies
        DD = ['Julia','Oliver','Abigail']
        HRD = ['Camden','Kayleigh','Cooper','Kerrigan']
        SD = ['Avery','Charlotte','Elle']
        
        people = DD + HRD + SD #Remove people from this list to signify that they have gone
        
        persons = [] #Main list to pull names
        
        Receivers = [] #Remove people from this list to signify that they've received a gift
        
        #Copy the names from people into persons
        for name in people:
            persons.append(name)
            
        #Copy the names from people into Receivers
        for name in people:
            Receivers.append(name)
        
        #Create a while loop for the entire process
        for thing in range(1,len(persons)+1):
            
            #Create a boolean variable
            cont = False
            
            #Create a while loop for the gifters
            while not cont:
                #Create a try block
                try:
                    #Get the random index for gifters
                    indexG = random.randint(0,len(persons))
                    
                    #Check to see if the gifter has already given a gift
                    if persons[indexG] in people: #If they haven't
                        p = 6+5
                    else: #If they have
                        e = v + i
                #Loop again if gifter has already given a gift
                except:
                    cont = False
                #Break the loop if the gifter has yet to give a gift and remove them from the people list
                else:
                    cont = True
                    people.remove((persons[indexG]))
                            
            #Assign the gifter to gifter
            gifter = persons[indexG]
            
            #Reset the boolean variable
            cont = False
            
            #Create a while loop for the receivers
            while not cont:
                #Create a try block
                try:
                    
                    #Create an index for the receivers
                    indexR = random.randint(0,len(persons))
                    
                    #Check to see if the receiver has already received a gift AND if their name matches the gifter
                    if persons[indexR] in Receivers and persons[indexG] != persons[indexR]: #If both are True
                        o = 1+1
                    else: #If they both are False
                        o = b + u
                        
                    #Check to see which department the gifter is from. Then use a for loop
                    #to check if the gifter and the receiver are in the same department.
                    if indexG <= 2: #Development Department
                        for name in DD:
                            if persons[indexR] == name:
                                o = b + e
                            else:
                                o = 1+1
                    elif indexG >= 3 and indexG <= 6: #HR Department
                        for name in HRD:
                            if persons[indexR] == name:
                                o = b + u
                            else:
                                o = 1+1
                    elif indexG >= 7: #Sales Department
                        for name in SD:
                            if persons[indexR] == name:
                                o = b+9
                            else:
                                o=1+1
                #If there is a crash anywhere, then loop again
                except:
                    cont = False
                #If no crash, break the loop and remove the receiver from the Receivers list
                else:
                    cont = True
                    Receivers.remove((persons[indexR]))
            
            #Assign the receiver to receiver
            receiver = persons[indexR]
            
            #Print the results and loop again
            print(gifter, 'gifts to', receiver)

    #Except messages
    except NameError:
        print('There are one or more variables that have a mispelled name')
    except:
        print('There was an issue within the program')
        
white_elephant()
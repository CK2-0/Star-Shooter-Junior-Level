score = 0

answer = input("Do you want to play Conrad's Quiz? (type no/yes here \n \n")

if answer.upper() == "NO":
     print ("Well then you suck like stinky toilet! \n \n")

if answer.upper() == ("YES"):
    print ("Cool lets play SUCKERS \n \n") 

    answer = input("How many times has india won the cricket world cup? \nA) 4 \nB) 2 \nC) 3 \nD) 1 \n")

    if answer.upper() == "2" or answer.upper() == "D":
        print ("Correct dummies, well done:) \n \n")
        score = score + 1
    else:
        print ("Incorrect MEGA dummies, tough luck, the answer was 2 or D:( \n \n")
        
    answer = input("which is the longest river in jamaica? \nA) Black River \nB) Negro River \nC) Rio Minho \nD) Yallahs River \n")

    if answer.upper() == "RIO MINHO" or answer.upper() == "C":
        print ("Correct dummies, well done:) \n \n")
        score = score + 1
    else:
        print ("Incorrect MEGA dummies, tough luck, the answer was Rio Minho or C:( \n \n")

    answer = input("Which is the tallest building in Jamaica? \nA) Le Meridien Jamaica Pegasus \nB) Scotiabank Centre \nC) Sunset Jamaica Grande II \nD) Wyndham Kingston Jamaica \n")

    if answer.upper() == "LE MERIDIEN JAMAICA PEGASUS" or answer.upper() == "A":
        print ("Correct dummies, well done:) \n \n")
        score += 1
    else:
        print ("Incorrect MEGA dummies, tough luck, the answer was Le Meridien Jamaica Pegasus:( \n \n")

    answer = input("What is the capital of germany? \nA) Hamburg \nB) Munich \nC) Frankfurt \nD) Berlin \n")

    if answer.upper() == "BERLIN" or answer.upper() == "D":
        print ("Correct dummies, well done:) \n \n")
        score += 1
    else:
        print ("Incorrect MEGA dummies, tough luck, the answer was Berlin or D:(\n \n")

    answer = input("What year was Adolf Hitler born? \nA) 1990 \nB) 1889 \nC) 1898 \nD) 1980 \n")

    if answer.upper() == "1889" or answer.upper() == "B":
        print ("Correct dummies, well done:) \n")
        score += 1
    else:
        print ("Incorrect MEGA dummies, tough luck, the answer was 1889 or B:( \n \n")

    answer = input("What is the maker of this quizes favourite football team?(IF YOU KNOW THE ANSWER DONT SAY IT) \nA) Liverpool \nB) Arsenal \nC) Chelsea \nD) Tottenham \n")

    if answer.upper() == "LIVERPOOL" or answer.upper() == "A":
        print ("Correct dummies, well done:) \n")
        score += 1
    else:
        print ("Incorrect MEGA dummies, tough luck, the answer was Liverpool or A:( \n \n")

    answer = input("Which Indian city hosted the first Kabaddi World Cup? \nA) Chennai \nB) Kolkata \nC) Bangalore \nD) Mumbai \n")

    if answer.upper() == "MUMBAI" or answer.upper() == "D":
        print ("Correct dummies, well done:) \n \n")
        score += 1
    else:
        print ("Incorrect MEGA dummies, tough luck, the answer was Mumbai or D:( \n \n")

    answer = input(" What is black and white and red all over? \nA) newspaper \nB) teapot \nC) writing \nD) earth \n")

    if answer.upper() == "NEWSPAPER" or answer.upper() == "A":
        print ("Correct dummies, well done:) \n \n")
        score += 1
    else:
        print ("Incorrect MEGA dummies, tough luck, the answer was Newspaper or A:( \n \n")

    answer = input("Where did chess first originate? \nA) spain \nB) china  \nC) iran \nD) india \n")

    if answer.upper() == "INDIA" or answer.upper() == "D":
        print ("Correct dummies, well done:) \n \n")
        score += 1
    else:
        print ("Incorrect MEGA dummies, tough luck, the answer was India or D:) \n \n")

    answer = input (" What is the speed limit in Germany?")

    if answer.upper() in ["none","they have none","Germany deosn't have a speed limit","infinite"]:
        print ("Correct dummies, well done:) \n \n")
        score += 1
    else:
        print ("Incorrect MEGA dummies, tough luck, the answer was India or D:) \n \n")


    answer = input (" Which out of these 4 countries has the smallest population? \nA) Germany \nB) India \nC) Jamaica \nD) England \n")



    if answer.upper() == "JAMAICA" or answer.upper() == "C":
        print ("Correct dummies, well done:) \n \n")
        score += 1
    else:
        print ("Incorrect MEGA dummies, tough luck, the answer was Jamaica or C.:) \n \n")
    print("Thankyou for playing my quiz, you got ",score,"/11 \n")
    
    print (" https://poki.com/en/g/thunderdogs-io click this link to play one of my favourite games! \n")

    print (" What position would you play in football? Lets find out! \n")

    score = 0

    answer = input ("How would your friends describe you? \nA) Outgoing and flashy \nB) Dedicated and hard worker \n")

    if answer == "A DEDICATED AND HARD WORKER" or answer.upper() == "B":
        score = score + 4
    else:
        score = score + 2

    answer = input ("What's your favourite drill in training? \nA) A fun drill \nB) A saving shots drill \n")

    if answer == "A FUN DRILL" or answer.upper() == "A":
        score = score + 10
    else:
        score = score + 1

    answer = input ("What's your biggest advantage on the pitch? \nA) Fearless \nB) Speed \n")

    if answer == "SPEED" or answer.upper() == "B":
        score = score + 2
    else:
        score = score + 5

    answer = input ("What animal are you most like? \nA) A falcon \nB) A monkey \nC) A lynx \n")

    if answer.upper() == "A LYNX" or answer.upper() == "B":
        score = score + 3
        
    if answer.upper() == "A FALCON" or answer.upper() == "A":
        score = score - 4
    else:
        score = score - 3.5

    if score > 15:
        print("You are a striker!")
    elif score > 10:
        print("You are a midfielder!")
    elif score > 5:
        print("You are a defender!")
    elif score > 0:   
        print("You are a goalkeeper!")

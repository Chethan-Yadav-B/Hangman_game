import os 
print("\n\t\t\t\t\t\t **WELCOME TO HANGMAN GAME***\n")

def game():
    print("\n\t\t1.START") 
    print("\n\t\t2.RULES")
    print("\n\t\t3.EXIT")
    b=int(input("\n\t\t SELECT YOUR OPTION :"))
    os.system("cls") 
    if(b<1 or b>3):
        print("\n\n\n\t\t\t\t\t\tPLEASE SELECT A VALID INPUT\n\n\n")
        game()
    if(b==2):
        print("\n\t\t RULES FOR HANGMAN GAME\n")
        print("\n\t\t1) The Game: Here, a random word is picked up from")
        print("\t\t our collection and the player gets limited chances to win the game") 
        print("\t\t 2) If a guessed letter appears in the word, all instances")
        print("\t\t of it are revealed. If not, the guesser loses a chance.")
        print("\t\t If the guesser figures out the secret word before he or she runs out of chances. ")
        print("\t\t he or she wins. If not, the player who chose the word wins.")
        print("\n\t\t3) The number of lifes left will be displayed each time so that the")
        print("\t\t player can be cautious before giving an attempt.")
        b=(input("\n\t\tBACK: "))
        os.system("cls")
        game() 
    elif(b==1):
        z=int(input("\t\t\t\t select difficulty level \n \t 1. EASY \t2.MEDIUM\n\n \t3. HARD\n\n \tselect your choice:"))
        os.system("cls")

        def hangman():
            os.system("cls")
            if(z==1):
                file=open(r"C:\Users\User\Downloads\3rd sem engineering\CTPY\MINI PROJECT\wordlists_easy.txt")
                f=file.read()
                words=f.split()
                file.close()
            if(z==2):
                file=open(r"C:\Users\User\Downloads\3rd sem engineering\CTPY\MINI PROJECT\wordlist.py")
                f=file.read()
                words=f.split()
                file.close()
            if(z==3):
                file=open(r"C:\Users\User\Downloads\3rd sem engineering\CTPY\MINI PROJECT\wordslist_hard.txt")
                f=file.read() 
                words=f.split()
                file.close()
            
            import random
            word=random.choice(words) [:] 
            if((z==1 and len(word) <=5) or (z==2 and len(word)<=7)or(z==3 and len(word)<=13)):
                lifes=3
                guesses=[]
                done=False
                count=0
                while not done:
                    for letter in word:
                        if(count==0):
                            if(len(word)>=5):
                                print("\n\n....HINT...\n")
                                print("First letter", word[0].lower())
                                print("Second letter", word[1].lower(),"\n\n")
                                count+1 
                            else:
                                print("\n\n....HINT....\n")
                                print("First letter:",word[0], "\n\n")
                                count+=1
                        if letter.lower() in guesses:
                             print(letter.lower(), end=' ')
                        else:
                            print('_',end=' ')
                    guess=input(f"\n\t\n lifes left {lifes} Next guess : ")
                    guesses.append(guess.lower())
                    if guess.lower() not in word.lower():
                        lifes=lifes-1
                        if lifes==0:
                            break
                    done=True
                    for letter in word:
                        if letter.lower() not in guesses:
                            done=False
                if done:
                    print(f"\n\t\nCONGRATULATIONS YOU FOUND THE WORD {word}!!!\n\n")
                    print("\n\t1. Play again\n") 
                    print("\n\t2.menu\n")
                    print("\n\t3.Exit\n") 
                    a=int(input("\n\tPLEASE SELECT AN OPTION : "))
                    if(a==1):
                        os.system("cls")
                        hangman()
                    elif(a==2):
                        os.system("cls")
                        game()
                    else:
                        print("Thank you")
                else:
                    print(f"\n\t\nGAME OVER. WORD WAS {word} \n\n") 
                    print("\n\t1. Play again\n")
                    print("\n\t2.menu\n") 
                    print("\n\t3. Exit\n")
                    a=int(input("\n\tPLEASE SELECT AN OPTION : "))
                    if(a==1):
                        os.system("cls")
                        hangman()
                    elif(a==2):
                        os.system("cls")
                        game()
                    else:
                        print("\tThank you")
            else:
                os.system("cls")
                hangman()
        hangman()        
    if(b==3):
        print("\tThank you")
game()
def main():

    import random
    import sys
    
    def start_game():
        
        print("Welcome to the Guessing Game!")
        print("There is no game without risk! You will only be allowed 5 attempts and the number you are looking for is between 1 and 10. GOOD LUCK my friend!")

    
        correct_answer = random.randrange(1, 10)
        attempt_count = 1  
       
        while True:
            try:
                guess = int(input("Guess a number!: "))
                if attempt_count >= 2:
                    print("You have made {} attempts so far...".format(attempt_count))
                if guess > 10:
                    print("That's quite far out. Remeber, the number you are looking for is betweek 1 and 10. Try again!")    
                if attempt_count > 5:
                    sys.exit("oooo unlucky I'm afraid you've exceeded the 5 attempts. Better Luck next time!")
                    if restart == "yes":
                        main()
                        
                    else:
                        exit()
                        
                attempt_count += 1
                if guess == int(correct_answer):
                    print("Congratulations, {} is the right answer!!!".format(guess))
                    print("It took you {} attempts well done! That is the end of the game.".format(attempt_count))
                    restart = input("Would you like to try again? yes/no ")
                    if restart == "yes":
                        main()
                        
                    else:
                        exit()
                    #taken from https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=2ahUKEwjv4O6g9ariAhWlVBUIHfU9AxAQ-4ACMAB6BAgLEAY&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DSZdQX4gbql0&usg=AOvVaw091tCI51bex_gv00opRwj8
                   
                
                elif guess > int(correct_answer):
                    print("The correct number is lower. Try again.")
                    continue
                
                elif guess < int(correct_answer):
                    print("The correct number is higher. Try again.")
                    continue
                #Create an argument that doesn't allow the user to select a number outside the parameters also that they cannot enter another text
            
            except ValueError:
                print("Error: You did not enter a number")
            
    if __name__ == '__main__':
        start_game()
        
main()
        
            
            

    
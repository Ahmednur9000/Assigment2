import time
import os
def game_rules(): 
    print("WELCOME ! \n")
    print("PIG : DICE GAME \n" )
    print("The Game Rules: \n") 
    
    print("Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to \"hold\": " ) 
    print("-> If the player rolls a 1, they score nothing and it becomes the next player's turn.\n")
    print("-> ")
    
    time.sleep(5)
    os.system("cls")
    
def main ():
    
    
    print("1. Play \n")
    print("2. Show History \n")
    print("3. Rules\n")
    print("4. Restart \n")
    print("5. Quit")
        
    choice = input()
    
    
    
    

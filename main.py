import game
import player
import compter

def main ():
    #intializing game obj
    Game = game.Game()
    Game.game_rules()
    
    print("Here are your options")
    print("1. Play ")
    print("2. Show History ")
    print("3. Rules")
    print("4. Restart")
    print("5. Quit")
        
    choice = int(input("Enter the choice: "))
    print("------------------------------------------------------------------------------------------------------------- ")
    
    while(choice != 5):
        
        if (choice == 1):
            
            print("1.Single player mode")
            print("2.Multiplayer mode")
            option = int(input("Enter your choice: "))
            if option == 1 :
                print("You would be faccing Mister Robot.")
                #Taking the player name , intitalizing a obj and a robot 
                name = input("Enter your name: ")
                
                player_obj = player.Player(name)
                computer_obj = compter.Computer()
                Game.add_player_obj(player_obj)
                Game.add_player_obj(computer_obj)
                print(" ")
                Game.Play_game()
                
                
            elif option == 2:
                
                pass
        elif (choice == 2):
            pass
        elif(choice == 3):
            pass
        elif(choice == 4):
            pass
        else:
            pass
            
            
            
    
    
if __name__ == "__main__":
    main()
    

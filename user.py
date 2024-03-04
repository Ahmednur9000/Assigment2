import pickle 
   # objective of the class:
     # save the data of the objects 
     # load the data of the objects
     # searchfor a player
     #create a player 
class User:
    
    def __init__(self):
        self.__filename = 'players.bin'
        self.__Player_objs = []
    # save the playes objects to a binary file.
    def save_players_list(self):
        with open(self.__filename, 'a+b') as file: 
            pickle.dump(self.__Player_objs, file)
    # load the data in the binary file to a list of player objects 
    def load_players_list(self):
        try: 
            with open(self.__filename, 'rb') as file:  
                self.__Player_objs == pickle.load(file)
        except FileNotFoundError:
            print("the file cannot be find , no player is loaded.")
            
    #List containing names
    def create_player(self, p_name):
        if p_name in self.__players:
            print("Name already taken. Please select another name.")
            return True  # Indicate that name is already taken
        else:
            self.__players.append(p_name)
            print("Player created.")
            return False   # Indicate that name is available & player created.
    #searching through a list        
    def search_player(self, p_name):       
        if p_name not in self.__Player_objs:
            print("Please enter correct name.")
            return True  
        else:
            return False      # Indicate that name is available # print("Enter correct name: ")             
        
    def change_name(self, orig_name, new_name):
        if orig_name in self.__Player_objs and new_name not in self.__Player_objs:
            self.__Player_objs.remove(orig_name)
            self.__Player_objs.append(new_name)
            print("Name changed successfully.")
        elif orig_name in self.__Player_objs and new_name in self.__player:
            print("Name already taken. Please select another name.")
        else:
            print("Name does not exist. Select option 'Create New Player'.")

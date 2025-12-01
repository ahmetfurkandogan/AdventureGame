# Starting game function
def start_game():
    print('Welcome to the Adventure Game!')
    name = input('What is your name: ')
    print("Welcome, " + name + "! Your adventure begins now.")
    #Asking inital choice forest and cave
    initial_choice = input("You have to choice, choose one of them: explore a forest or enter a cave ? (forest/cave) ").lower()

    # if user choose forest path call forest path function else call cave path function
    # else: say invalid choice.
    if initial_choice == 'forest':
        forest_path()
    elif initial_choice == 'cave':
        cave_path()
    else:
        print("Invalid choice. Please choose 'forest' or 'cave'.")
        start_game()
    ask_replay()

# Forest Path Function
def forest_path():
            # User have two choices for forest path: follow river or climb a tree
            print("You choosen forest path, you have two options: follow a river or climb a tree. (choose 'follow river' or 'climb a tree')")
            # Getting user choice
            choose = input("Your choice: ").lower()
            if choose == 'follow river':
                print("You follow the river and find a treasure chest filled with gold!")
            elif choose == 'climb a tree':
                print("You climb the tree and find a nest of magical birds that grant you three wishes!")
            else:
                print('Invalid choice. Please try again!')
                forest_path()

# Cave Path Function
def cave_path():
        # User have two choices for cave path: light a torch or proceed in the dark
        print("You choosen cave path, you have two options: light a torch or proceed in the dark. (choose 'light torch' or 'proceed dark')")
        choose = input("Your choice: ").lower()
        if choose == 'light torch':
            print("You light the torch and discover ancient cave paintings that tell a forgotten story!")
        elif choose == 'proceed dark':
            print("You proceed in the dark and stumble upon a sleeping dragon guarding a pile of jewels!")
        else:
            print('Invalid choice. Please try again!')
            cave_path()

# Restart function for replaying the game
def ask_replay():
     # Asking user for replaying the game: Yes or No
     replay = input("Do you want to play again? (yes/no): ").lower()
     # if user choose yes call start game function and game will restart
     if replay == 'yes':
          start_game()
    # elif user choose no end of the game
     elif replay == 'no':
            print("Thank you for playing! Goodbye!")
     # else say invalid choice       
     else:
          print("Invalid choice.Please answer 'yes' or 'no' ")
          ask_replay() 
     
# main function call, for this code main function is start game function.
if __name__ == '__main__':
    start_game()
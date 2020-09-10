game_list1= [' ',' ',' ']
game_list2= [' ',' ',' ']
game_list3= [' ',' ',' ']


def display_game(game_list1,game_list2,game_list3):
    print("these are the index positions and list positions to be followed")
    print('''[1,2,3]:1
[1,2,3]:2
[1,2,3]:3''')
    print("This is the current list: ")
    print(game_list1)
    print(game_list2)
    print(game_list3)



def list_choice():
    choice = "string"
    
    while choice not in ["1","2","3"]:
        choice = input("Which list you wanna choose? : ")
        if choice == "1":
            position_list = game_list1
            choice = 1
            break
        elif choice == "2":
            position_list = game_list2
            choice = 2
            break
        else:
            position_list = game_list3
            choice = 3
            break
    return position_list,choice



def position_choice(position_list):
    choice = "string"
    while choice not in ["1","2","3"]:
        choice = input("Which index? : ")
        if choice == "1":
            index_choice = 0
        elif choice == "2":
            index_choice = 1
        else:
            index_choice = 2
    return index_choice



def replacement(index_choice):
    choice = "string"
    while choice.lower() not in ["x","o"]:
        choice = input(f"Which value? [X or O] at position {index_choice + 1} and list {position_list}. : ")
        if choice.lower() == "x":
            position_list[index_choice] = "X"
        else:
            position_list[index_choice] = "O"
    if choice_list == 1:
        game_list1 = position_list
    elif choice_list == 2:
        game_list2 = position_list
    else:
        game_list3 = position_list
    
    return position_list

        
def game_on():
    choice = "none"
    while choice.lower() not in ["y","x"]:
        choice = input("Do you wanna play again? (Y or N): ")
        if choice.lower() not in ["y","n"]:
            print("invalid choice")
        else:
            break
    choice = choice.lower()
    if choice == "y":
        return 1
    else:
        return 0


game = 1
game_list1 = [' ',' ',' ']
game_list2 = [' ',' ',' ']
game_list3 = [' ',' ',' ']
while game == 1:
    display_game(game_list1,game_list2,game_list3)
    position_list,choice_list = list_choice()
    index_position = position_choice(position_list)
    replacement(index_position)
    display_game(game_list1,game_list2,game_list3)
    
    game = game_on()
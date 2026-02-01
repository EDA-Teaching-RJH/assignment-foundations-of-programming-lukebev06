
def main():
 name = input("what is your full name: ")

 names = ["Picard","Spock","Geordi","Kathryn","Riker"]
 ranks = ["Captain","Commander","Lt. commander","Captain","Commander"]
 divisions = ["Command","Science","Operations","Science","Command"]
 IDs = ["231-427-1701","179-425-2267","452-199-639","746-358-74656","402-857-935"]


 print("BOOTING SYSTEM...")
 print("...")
 print("WELCOME TO FLEET COMMAND")

 def init_database():
        
    for i in range(len(names)):
        print(f"{names[i]} - {ranks[i]} - {divisions[i]} - {IDs[i]}")

 def display_menu():
        
        print(f"\n--- MENU --- {name} ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        option = input("select an option: ")
        if option == "1" :
            init_database()
        elif option == "2":
            add_members()
        elif option =="3":
            remove_member()

 def add_members():
        all_ranks = ["Captain","Commander","Lt. Commander","Lieutenant","Lt. junior","Ensign"]

        new_name = input("Name: ")
        new_division = input("Div: ")
        
        n = 0 
        while n != 1 :
        
            new_id = input("enter a unique id (in the format xxx-xxx-xxx): ")
            print("\n---enter one of the valid ranks---")
            print("Captain ,Commander ,Lt. Commander ,Lieutenant ,Lt. junior ,Ensign")
            new_rank = input("Rank:")

            if new_rank in all_ranks: 
                if new_id in IDs:
                    print("that id already exists please try again. ")

                else:
                    names.append(new_name)
                    ranks.append(new_rank)
                    divisions.append(new_division)
                    IDs.append(new_id)
                    n = 1
                    display_menu()
            else:
                print("That rank doesnt exist please try again. ")
            
 def remove_member ():
     
     rem_id = input("id of profile to remove: ")

     if rem_id in IDs : 
        pos = IDs.index(rem_id)

        print_name = names[pos]
        names.pop(pos)
        ranks.pop(pos)
        divisions.pop(pos)
        IDs.pop(pos)

        print(f"Removed {print_name}")
        display_menu()


 display_menu()
main()
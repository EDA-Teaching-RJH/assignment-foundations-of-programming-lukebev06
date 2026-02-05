
def main():
 name = input("what is your full name: ")

 


 print("BOOTING SYSTEM...")
 print("...")
 print("WELCOME TO FLEET COMMAND")

 def init_database(names,ranks,divisions,IDs):
        
    names = ["Picard","Spock","Geordi","Kathryn","Riker"]
    ranks = ["Captain","Commander","Lt. commander","Captain","Commander"]
    divisions = ["Command","Science","Operations","Science","Command"]
    IDs = ["231-427-1701","179-425-2267","452-199-639","746-358-74656","402-857-935"]

 def display_menu():
     while True:   
        print(f"\n--- MENU --- {name} ---")
        print("1: View database")
        print("2: Add crewmember")
        print("3: Remove crewmember")
        print("4: Update crewmember rank")
        print("5: Display crew")
        print("6: Search term for crewmember")
        print("7: Filter by divison")
        print("8: Total payroll")
        print("")

        option = input("select an option: ")
        if option == "1" :
            init_database()
        elif option == "2":
            add_members()
        elif option =="3":
            remove_member()
        elif option =="4":
            update_rank()
        elif option =="5":
            display_roster()
        elif option == "6":
            search_crew()
        elif option =="7":
            filter_by_divisions()
        elif option =="8":
            calculate_payroll()
        elif option =="9":
            count_officers()
        elif option =="10":
            print("Shutting Down......")
            break

 def add_members(names,ranks,divisions,IDs):
        
    all_ranks = ["Captain","Commander","Lt. Commander","Lieutenant","Lt. junior","Ensign"]

    new_name = input("Name: ")
    new_division = input("Div: ")
        
    n = 0 
    while n != 1 :
        
        new_id = input("enter a unique id (in the format xxx-xxx-xxx): ")
        print("\n---enter one of the valid ranks---")
        print("Captain ,Commander ,Lt. Commander ,Lieutenant ,Lt. Junior ,Ensign")
        new_rank = input("Rank:")

        if new_rank in all_ranks: 
            if new_id in IDs:
                print("that id already exists please try again. ")

            elif:
                names.append(new_name)
                ranks.append(new_rank)
                divisions.append(new_division)
                IDs.append(new_id)
                n = 1
    display_menu()
        
 def remove_member (names,ranks,divisions,IDs):
     
     rem_id = input("id of profile to remove: ")
     
     try:
         pos = IDs.index(rem_id)
         print_name = names[pos]
         names.pop(pos)
         ranks.pop(pos)
         divisions.pop(pos)
         IDs.pop(pos)

         print(f"Removed {print_name}")
     except ValueError:
         print("that is not a valid ID. ")

     display_menu()

 def update_rank(names, ranks, IDs):
     id_check = input("enter the id number of the person whos rank is changing: ")
     try:  
         position = IDs.index(id_check)
         change_newrank = input("what is the new rank you would like to enter: ")
         ranks[position] = change_newrank
         display_menu()
     except ValueError:
         print(f"{id_check} is not a valid id please try again" )
         
 def display_roster(names,ranks,divisions,IDs):
     
     for i in range(len(names)):

        print(f"{names[i]} - {ranks[i]} - {divisions[i]} - {IDs[i]}")  
     display_menu()
 
 def search_crew(names, ranks, divisions, IDs):
     term = input("what term are you searching for? ")
     for i in range(names[i]):
         if term in names[i]:
            
             print(f"{names[i]} - {ranks[i]} - {divisions[i]} - {IDs[i]}")
     display_menu()
    
 def filter_by_divisions(names, divisions):
     for i in range(len(name)):
         print("Command, Operations, Sciences")
         div = input("please enter a division in the list above: ")
        
         if div == divisions[i]:
            print(f"{names[i]} is in {div}")
     display_menu()
         
 def calculate_payroll(ranks):
     total_pay = 0
     for i in range(len(ranks)):
         if ranks[i] == "Captain" :
             total = total + 600
         elif ranks[i] == "Commander":
             total = total + 500
         elif ranks[i] == "Lt. Commander":
             total = total + 400
         elif ranks[i] == "Lieutenant":
             total = total + 300
         elif ranks[i] == "Lt. Junior":
             total = total + 200
         elif ranks[i] == "Ensign":
             total = total + 100
     display_menu()

 def count_officers(ranks):
     total_command = 0
     for i in range[len(ranks)]:
         if ranks[i] == "Captain" or ranks[i] == "Commander":
             total_command = total_command + 1
     print(f"There are {total_command} in command.")
    
     display_menu()

         

 display_menu()
main()
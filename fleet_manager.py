
def main():

    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")

    def init_database(names,ranks,divisions,IDs):
        names = ["Picard","Spock","Geordi","Kathryn","Riker"]
        ranks = ["Captain","Commander","Lt. commander","Captain","Commander"]
        divisions = ["Command","Science","Operations","Science","Command"]
        IDs = ["231-427-1701","179-425-2267","452-199-639","746-358-74656","402-857-935"]
        for i in range(len(names)):
            print(f"{names[i]} - {ranks[i]} - {divisions[i]} - {IDs[i]}")

    def display_menu():
        name = input("what is your full name: ")
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

    def add_members(names,ranks,divisions,IDs):
        all_ranks = ["Captain","Commander","Lt. Commander","Lieutenant","Lt. junior","Ensign"]

        new_name = input("Name: ")
        new_division = input("Div: ")
        

        while n != 1 :
            n = 0
            new_id = input("enter a unique id (in the format xxx-xxx-xxx): ")
            print("\n---enter one of the valid ranks---")
            print("Captain ,Commander ,Lt. Commander ,Lieutenant ,Lt. junior ,Ensign")
            new_rank = input("Rank:")

            if IDs.index(new_id, 0 ) < 0 and all_ranks.index(new_rank,0) >=0: 
                names.append(new_name)
                ranks.append(new_rank)
                divisions.append(new_division)
                IDs.append(new_id)
                n = 1
            elif all_ranks.index(new_rank,0) == "":
                print("that rank is incorrect. please try again.")

            elif IDs.index(new_id,0) >= 0:
                print("that id is in use. please select another one")
        
        # cannot compare a null resilt from index use different method. for future reference.







    display_menu()
main()
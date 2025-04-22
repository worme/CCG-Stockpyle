import sys

class Collection:
    """"""
    def __init__(self, card_name, quantity):
        self.card_list = []
        self.card_quantity = quantity
        self.card_name = card_name
    '''
    Collection has-a list, quantity, 
    '''

    def add_card(self):
        self.card_name = input("Enter the name of the card to add: ")
        self.card_list.append(self.card_name)
        self.card_quantity += 1

    def edit_card(self):
        pass

    def view_list(self):
        if self.card_quantity <= 0:
            print("There are no cards in this collection, make new selection.")  
        else:
            print("You have " + str(self.card_quantity) + " cards in your collection:")
            for item in self.card_list:
                print(item)

    def exit_app(self):
        print("Exiting CCG Stockpyle...")
        sys.exit()


def main():
    """Main loop"""
    collection_object = Collection(card_name="", quantity=0)

    while True:
        print("")
        user_input = input(("What would you like to do? (add, edit, view, or exit): "))

        if user_input.lower() == "exit":
            collection_object.exit_app()
        
        elif user_input.lower() == "add":
            collection_object.add_card()

        elif user_input.lower() == "view":  
            collection_object.view_list()
        
        else:
            print("That is not a valid entry. Try again: ")


if __name__ == "__main__":
    main()
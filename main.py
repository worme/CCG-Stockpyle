import sys

class Collection:
    """This class represents the instance of a collection."""
    def __init__(self, card_name, quantity):
        self.card_list = []
        self.card_quantity = quantity
        self.card_name = card_name

    def add_card(self):
        """This method handles adding a card to the collection of cards."""
        self.card_name = input("Enter the name of the card to add: ")
        self.card_list.append(self.card_name)
        self.card_quantity += 1

    def remove_card(self):
        """This method handles removing a card from the collection of cards."""
        self.card_name = input("Enter the name of the card to remove: ")
        self.card_list.remove(self.card_name)
        self.card_quantity -= 1

    def view_list(self):
        """This method handles displaying the list of cards in the collection."""
        if self.card_quantity <= 0:
            print("There are no cards in this collection, make new selection.")  
        else:
            print("You have " + str(self.card_quantity) + " cards in your collection:")
            for item in self.card_list:
                print(item)


class Card:
    """This class respresents the instance of a card."""
    def __init__(self, quantity, name):
        self.quantity = quantity
        self.name = name

    def get_name(self):
        """This method handles getting the name of a card."""
        pass

    def get_quantity(self):
        """This method handles getting the quantity of a card."""
        pass

def main():
    """Main loop"""
    collection_object = Collection(card_name="", quantity=0)
    card_object = Card(quantity=0, name="")

    while True:
        print("")
        user_input = input(("What would you like to do? (add, edit, view, or exit): "))

        if user_input.lower() == "exit":
            print("Exiting CCG Stockpyle...")
            sys.exit()
        
        elif user_input.lower() == "add":
            collection_object.add_card()

        elif user_input.lower() == "view":  
            collection_object.view_list()
        
        else:
            print("That is not a valid entry. Try again: ")


if __name__ == "__main__":
    main()
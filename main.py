import sys

class Collection:
    """This class represents the instance of a collection."""
    def __init__(self, collection_name, collection_quantity):
        self.collection_dict = {}
        self.collection_quantity = collection_quantity
        self.collection_name = collection_name

    def add_card(self, card_object):
        """This method handles adding a card to the collection of cards."""
        print(card_object.get_name() + " has been added to the collection.")
        self.collection_dict[card_object.get_name()] = card_object.get_quantity()
        self.collection_quantity += 1
        print(self.collection_dict)

    #FIXME remove_card method
    # def remove_card(self):
    #     """This method handles removing a card from the collection of cards."""
    #     card_name = input("Enter the name of the card to remove: ")
    #     self.collection_dict.remove(card_name)
    #     self.collection_quantity -= 1

    def view_list(self):
        """This method handles displaying the list of cards in the collection."""
        if self.collection_quantity <= 0:
            print("There are no cards in this collection, make new selection.")  
        else:
            print("You have " + str(self.collection_quantity) + " cards in your collection:")
            for item in self.collection_dict:
                print(item)


class Card:
    """This class respresents the instance of a card."""
    def __init__(self, card_quantity, card_name):
        self.card_quantity = card_quantity
        self.card_name = card_name

    def get_name(self):
        """This method handles getting the name of a card."""
        return self.card_name

    def set_name(self, name):
        """This method sets the name of a card."""
        self.card_name = name

    def get_quantity(self):
        """This method handles getting the quantity of a card."""
        return self.card_quantity

    #FIXME card quantity methods
    # def add_quantity(self):
    #     self.card_quantity += 1

    # def subtract_quantity(self):
    #     self.card_quantity -= 1

def main():
    """Main loop"""
    collection_object = Collection(collection_name="", collection_quantity=0)
    card_object = Card(card_quantity=1, card_name="")

    while True:
        print("")
        user_input = input(("What would you like to do? (add, edit, view, or exit): "))

        if user_input.lower() == "exit":
            print("Exiting CCG Stockpyle...")
            sys.exit()
        
        elif user_input.lower() == "add":
            name = input("Enter the name of the card to add: ")
            card_object.set_name(name)
            collection_object.add_card(card_object)

        elif user_input.lower() == "view":  
            collection_object.view_list()
        
        else:
            print("That is not a valid entry. Try again: ")


if __name__ == "__main__":
    main()
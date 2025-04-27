import sys

class Collection:
    """This class represents the instance of a collection."""
    def __init__(self, collection_quantity):
        self.collection_list = []
        self.collection_quantity = collection_quantity

    def add_card(self, card_object):
        """This method handles adding a card to the collection of cards."""
        if card_object.get_name() not in self.collection_list:
            self.collection_list.append(card_object)
            self.collection_quantity += 1
            print(card_object.get_name() + " has been added to the collection.")

        else:
            print(card_object.get_name() + " is already in the collection.")
            print("Increasing the quantity by one.")
            self.collection_dict[card_object.get_name()] += 1
            self.collection_quantity += 1

    #FIXME remove_card method
    def delete_card(self, card_object):
        """This method handles removing a card from the collection of cards."""   
        if card_object.get_name() in self.collection_dict:
            del self.collection_dict[card_object.get_name()]
            print(card_object.get_name() + " has been deleted from the collection.")
        else:
            print("That card is not in the collection.")
            print("Make a different selection.")
    def view_list(self):
        """This method handles displaying the list of cards in the collection."""
        if self.collection_quantity <= 0:
            print("There are no cards in this collection, make new selection.")  
        else:
            print("You have " + str(self.collection_quantity) + " cards in your collection:")
            for item in self.collection_list:
                print(item.get_name(), item.get_quantity())                


class Card:
    """This class respresents the instance of a card."""
    def __init__(self, card_name, card_quantity):
        self.card_name = card_name
        self.card_quantity = card_quantity

    def get_name(self):
        """This method handles getting the name of a card."""
        return self.card_name

    def get_quantity(self):
        """This method handles getting the quantity of a card."""
        return self.card_quantity

def main():
    """Main loop"""
    collection_object = Collection(collection_quantity=0)

    while True:
        print("")
        user_input = input(("What would you like to do? (add, edit, view, or exit): "))

        if user_input.lower() == "exit":
            print("Exiting Stockpyle Syndrome...")
            sys.exit()
        
        elif user_input.lower() == "add":
            card_name = input("Enter the name of the card to add: ")
            card_object = Card(card_name, card_quantity=1)
            collection_object.add_card(card_object)

        elif user_input.lower() == "delete":
            name = input("Enter the name of the card to delete: ")
            collection_object.delete_card(card_object)

        elif user_input.lower() == "view":  
            collection_object.view_list()
        
        else:
            print("That is not a valid entry. Try again: ")


if __name__ == "__main__":
    main()
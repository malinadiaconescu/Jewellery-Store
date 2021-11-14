#import category
#from json import JSONDecodeError
import json
import MyStore
import necklace
import bracelet
import Earring
import order
import product
# define some functions to be used in the main menu. You can follow the
# suggestion described in the lab requirement, by simulating a switch
# instruction using a dictionary, or just using multiple 'if' branches
# which is, obviously, much uglier
import categories


def add_category():
    nume=input("Enter a category:")
    import category
    newcategory=category.Category(nume)
    store.add_category(newcategory)
    print("Category added! :)")

def remove_category():
    nume = input("Enter a category:")
    import category
    oldcategory=category.Category(nume)
    store.remove_category(oldcategory)
    print("Category removed! :)")

def display_categories():
    store.display_categories()
    print("Categories displayed! :)")

def add_product():
    kind_of_jewellery=int(input("Please select what kind of jewellry you want to add to our range of products. We currently have the following accessories: \n"+
                                "1 - Necklaces\n"+
                                "2 - Bracelets\n"+
                                "3 - Earrings\n"+"Your choice:"))
    if kind_of_jewellery==1:
        material=input("Material of the jewellery:")
        color=input("Color of the jewellery:")
        weight=int(input("Weight of the jewellery:"))
        length=int(input("Length of the jewellery:"))
        store.add_product(necklace.Necklace("Necklace",material,color,weight,length))
    elif kind_of_jewellery==2:
        material = input("Material of the jewellery:")
        color = input("Color of the jewellery:")
        weight = int(input("Weight of the jewellery:"))
        length = int(input("Length of the jewellery:"))
        store.add_product(bracelet.Bracelet("Bracelet", material, color, weight, length))
    elif kind_of_jewellery==3:
        material = input("Material of the jewellery:")
        color = input("Color of the jewellery:")
        weight = int(input("Weight of the jewellery:"))
        diameter= int(input("Diameter of the jewellery:"))
        store.add_product(Earring.Earring("Earring",material,color,weight,diameter))

    print("Product added! :)")

def remove_product():
    for i in range(len(store.products)):
        print(str(i)+"-"+str(store.products[i])+"\n")

    number=int(input("Please choose the number corresponding to which product you want to remove:"))
    if number<len(store.products):
        store.remove_product(store.products[number])

    print("Product removed! :)")

def display_products():
    store.display_products()
    print("Products available displayed! :)")

def add_order():
    products_chosen=[]
    print("Select the numbers corresponding to the jewellery you want to purchase:")
    for i in range(len(store.products)):
        print(str(i) + "-" + str(store.products[i]) + "\n")
    print(str(len(store.products))+"-to end your order")
    number = int(input("Your choice:"))
    if(number<len(store.products)):
        quantity=int(input("How many things of this jewellery you want:"))
    while(number<len(store.products)):
        products_chosen.append((store.products[number],quantity))
        number = int(input("Your choice:"))
        if (number < len(store.products)):
            quantity = int(input("How many things of this jewellery you want:"))

    if(number>=len(store.products)):
        address=input("Put in your address:")
    import order
    new_order=order.Order(address,products_chosen)
    store.add_order(new_order)
    print("Order sent! :)")

def display_orders():
    store.display_orders()

def exit_program():
    quit()

def menu():
    print("1. Add category \n" +
          "2. Remove category \n" +
          "3. Display all the categories \n" +
          "4. Add a product \n" +
          "5. Remove a product \n" +
          "6. Display all products \n" +
          "7. Place new order \n" +
          "8. Display all orders \n" +
          "9. Exit")

if __name__ == "__main__":
    store=MyStore.MyStore()
    # taking the products from file
    try:
        loaded_orders = order.Order.load_orders()
    except json.JSONDecodeError as e:
        loaded_orders = None
    # appending the existing products
    for order in loaded_orders:
        store.orders.append(order)

    #taking the products from file
    try:
        loaded_products=product.Product.load_products()
    except json.JSONDecodeError as e:
        loaded_products = None
    #appending the existing products
    for product in loaded_products:
        store.products.append(product)

    #taking the categories from file
    try:
        categories = categories.Categories.load_categories()
    except json.JSONDecodeError as e:
        categories = None

    #appending the existing categories
    for category in categories:
        store.categories.append(category)

    menus = {1: add_category, 2: remove_category, 3: display_categories,
             4: add_product, 5: remove_product, 6: display_products,
             7: add_order, 8: display_orders, 9: exit_program}

    ok=True

    while ok:
        menu()
        comanda=int(input("Enter your option:"))
        func=menus.get(comanda)
        func()

    '''
    # below some usage examples

    # create some categories
    cat_1 = Category("Necklaces")
    cat_2 = Category("Bracelets")
    cat_3 = Category("Earrings")

    # add them inside the Categories collection, and also save them
    # on the disk
    Categories.add_category(cat_1)
    Categories.add_category(cat_2)
    Categories.add_category(cat_3)

    # display the existing categories
    try:
        categories = Categories.load_categories()
        for cat in categories:
            print(cat.name)
    except JSONDecodeError as e:
        categories = None

    # remove one category from the Categories collection
    Categories.remove_category(cat_3)

    # display again the existing categories
    for cat in categories:
        print(cat.name)
    '''
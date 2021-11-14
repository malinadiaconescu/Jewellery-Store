import product
class MyStore:
    orders=[]
    categories=[]
    products=[]
    def __init__(self):
        orders=[]

    def add_order(self,neworder):
        self.orders.append(neworder)
        import order
        order.Order.add_order(neworder)

    def remove_order(self,order):
        if len(self.orders)==0:
            pass
        else:
            if order in self.orders:
                self.orders.remove(order)

    def display_orders(self):
        print(self.orders)

    def add_category(self,category):
        self.categories.append(category)
        import categories
        categories.Categories.add_category(category)

    def remove_category(self,category):
        if category in self.categories:
                self.categories.remove(category)
                import categories
                categories.Categories.remove_category(category)

    def display_categories(self):
        print(self.categories)

    def add_product(self,newproduct):
        self.products.append(newproduct)
        product.Product.add_product(newproduct)

    def remove_product(self,oldproduct):
        if len(self.products)==0:
            pass
        else:
            if oldproduct in self.products:
                self.products.remove(oldproduct)
        product.Product.remove_product(oldproduct)

    def display_products(self):
        for prod in self.products:
            print(prod)
        #print(self.products)
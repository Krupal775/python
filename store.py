class store:
    def __init__(self,listofproduct):
        self.product = listofproduct

    def dispalyAvailableproduct(self):
        print("item is present: ")
        for product in self.product:
            print(" *" + product)
        
    def borrowproduct(self,productName):
        if productName in self.product:
            print(f"you have been issued {productName}. please keep it safe..!")
            self.product.remove(productName)
            return True
        else:
            print("sorry, This product has sold.")
            return False

    def returnProduct(self,productName):
        self.product.append(productName)
        print("we got your issued. we are trying to handle it out soon")

class buyer:
    def requestProduct(self):
        self.product = input("Enter the name o the product..! you want to borrow..")
        return self.product

    def returnProduct(self):
        self.product = input("Enter the name of the product you want ot return..!!")
        return self.product


if __name__ =="__main__":
    centralstore = store(['ipod','band','shoes','watches'])
    centralstore.dispalyAvailableproduct()
    Buyer = buyer()
    while(True):
        welcomeMsg= ''' ===Welcome to amazon====
        please Choose an option: 
        1. listing all product
        2. request a product
        3. returna a product
        4. logout 
        '''
        print(welcomeMsg)
        a = int(input("enter a choice: "))
        if a==1 :
            centralstore.dispalyAvailableproduct()
        elif a==2:
            centralstore.borrowproduct(Buyer.requestProduct())
        elif a==3:
            centralstore.returnProduct(Buyer.returnProduct())
        elif a==4:
            print("good day..")
            exit()
        else:
            print("INVALID")
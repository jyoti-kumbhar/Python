#calculate bill of Bag and Makeup set

def Bag():
    print("Bag @5000")
    prod_name = "H&M Bag"
    price = 5000
    quantity = int(input("Enter no. of quantity:"))
    BasicAmt = price * quantity
    gstAmt = BasicAmt * 0.18
    TotalAmt = gstAmt + BasicAmt
    bill(prod_name,price,quantity,BasicAmt,gstAmt,TotalAmt)

def Makeup_set():
    print("Makeup Set @2000")
    prod_name = "Sugar Ultimate Makeup kit"
    price = 2000
    quantity = int(input("Enter no. of quantity:"))
    BasicAmt = price * quantity
    gstAmt = BasicAmt * 0.18
    TotalAmt = gstAmt + BasicAmt
    bill(prod_name,price,quantity,BasicAmt,gstAmt,TotalAmt)

def bill(prod_name,price,quantity,BasicAmt,gstAmt,TotalAmt):
    print("INVOICE".center(40,"_"))
    print("Product Name:",prod_name)
    print("Product Price:",price)
    print("Quantity:",quantity)
    print("Basic Amount Rs.",BasicAmt)
    print("GST Amount Rs.",gstAmt)
    print("Total Bill Rs.",TotalAmt)


if __name__=="__main__":
    print(1 ,"- H&M Bag",)
    print(2, "- Sugar Ultimate Makeup kit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Bag()
    elif choice == 2:
        Makeup_set()
    else:
        print("Wrong Input!")
    print("Thank you".center(40,"~"))
    

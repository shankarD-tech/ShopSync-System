import pywhatkit
import datetime
from pythonproject1moduleofavailableproductsprices import*
from pythonproject1moduleofstock import*
login=input("admin/user")
if(login=="admin"):
    password=input("enter your password:")
    if(password=="admin@123"):
        print(availableproducts)
        print(prices)
        print(stock)
        if_any_stockupdate=input("is there is any stock update(yes/no):")
        if(if_any_stockupdate=="yes" or if_any_stockupdate=="YES" or if_any_stockupdate=="Yes"):
            a=True
            while a:
                stockupdate=input("enter the item:")
                if(stockupdate=="rice" or stockupdate=="basmatirice" or stockupdate=="idlyrice" or stockupdate=="wheatflour" or stockupdate=="maida" or stockupdate=="ragi" or stockupdate=="sooji" or stockupdate=="poha" or stockupdate=="toordal" or stockupdate=="urdal" or stockupdate=="moongdal" or stockupdate=="channadal" or stockupdate=="rajma" or stockupdate=="chickpeas" or stockupdate=="sunfloweroil" or stockupdate=="groundnutoil" or stockupdate=="mustardoil" or stockupdate=="ricebranoil" or stockupdate=="ghee" or stockupdate=="salt" or stockupdate=="sugar" or stockupdate=="turmeric" or stockupdate=="chillipowder" or stockupdate=="garammasala" or stockupdate=="pepper" or stockupdate=="corianderpowder" or stockupdate=="jeera" or stockupdate=="milk" or stockupdate=="curd" or stockupdate=="butter" or stockupdate=="cheese" or stockupdate=="paneer" or stockupdate=="biscuits" or stockupdate=="chips" or stockupdate=="namkeen" or stockupdate=="instantnoodles" or stockupdate=="oats" or stockupdate=="cornflakes" or stockupdate=="readymix" or stockupdate=="instantupma" or stockupdate=="instantpoha" or stockupdate=="soupmix" or stockupdate=="bread" or stockupdate=="cake" or stockupdate=="bun" or stockupdate=="rusk" or stockupdate=="tea" or stockupdate=="coffee" or stockupdate=="juice" or stockupdate=="softdrink" or stockupdate=="waterbottle" or stockupdate=="jam" or stockupdate=="honey" or stockupdate=="pickles" or stockupdate=="ketchup" or stockupdate=="floorcleaner" or stockupdate=="toiletcleaner" or stockupdate=="dishwash" or stockupdate=="detergentpowder" or stockupdate=="detergentbar" or stockupdate=="soap" or stockupdate=="shampoo" or stockupdate=="toothpaste" or stockupdate=="toothbrush" or stockupdate=="facewash" or stockupdate=="hairoil" or stockupdate=="broom" or stockupdate=="mop" or stockupdate=="bucket" or stockupdate=="dustbin" or stockupdate=="clothhanger" or stockupdate=="pressurecooker" or stockupdate=="pan" or stockupdate=="cookwareset" or stockupdate=="knife" or stockupdate=="cuttingboard" or stockupdate=="onion" or stockupdate=="potato" or stockupdate=="tomato" or stockupdate=="carrot" or stockupdate=="beans" or stockupdate=="cabbage" or stockupdate=="apple" or stockupdate=="banana" or stockupdate=="orange" or stockupdate=="mango" or stockupdate=="grapes"):
                    updatequuantity=int(input("enter the quantity to update"))
                    stock[stockupdate]=updatequuantity
                    print(stock)
                    file = open("pythonproject1moduleofstock.py", "w")
                    file.write("stock = " + str(stock))
                    file.close()
                else:
                    print("invalid item")
                rep=input("do you want continue the update(yes/no)")
                if(rep=="yes" or rep=="Yes" or rep=="YES"):
                    a=True
                else:
                    a=False    
        elif(if_any_stockupdate=="no" or if_any_stockupdate=="No" or if_any_stockupdate=="NO"):
            print("ok sir")
        else:
            print("invalid comment")
    else:
        print("wrong password")
elif(login=="user"):
    coustomerattending=input("welcome sir/mam,do you like to purchase anything(yes/no)")
    if(coustomerattending=="yes" or coustomerattending=="Yes" or coustomerattending=="YES"):
        name=input("enter you name")
        phoneno=input("enter phone number")
        print("prices of the product=",prices)
        a=True
        while a:
            print("available stock=",stock)
            item=input("enter the item:")
            if(item=="rice" or item=="basmatirice" or item=="idlyrice" or item=="wheatflour" or item=="maida" or item=="ragi" or item=="sooji" or item=="poha" or item=="toordal" or item=="urdal" or item=="moongdal" or item=="channadal" or item=="rajma" or item=="chickpeas" or item=="sunfloweroil" or item=="groundnutoil" or item=="mustardoil" or item=="ricebranoil" or item=="ghee" or item=="salt" or item=="sugar" or item=="turmeric" or item=="chillipowder" or item=="garammasala" or item=="pepper" or item=="corianderpowder" or item=="jeera" or item=="milk" or item=="curd" or item=="butter" or item=="cheese" or item=="paneer" or item=="biscuits" or item=="chips" or item=="namkeen" or item=="instantnoodles" or item=="oats" or item=="cornflakes" or item=="readymix" or item=="instantupma" or item=="instantpoha" or item=="soupmix" or item=="bread" or item=="cake" or item=="bun" or item=="rusk" or item=="tea" or item=="coffee" or item=="juice" or item=="softdrink" or item=="waterbottle" or item=="jam" or item=="honey" or item=="pickles" or item=="ketchup" or item=="floorcleaner" or item=="toiletcleaner" or item=="dishwash" or item=="detergentpowder" or item=="detergentbar" or item=="soap" or item=="shampoo" or item=="toothpaste" or item=="toothbrush" or item=="facewash" or item=="hairoil" or item=="broom" or item=="mop" or item=="bucket" or item=="dustbin" or item=="clothhanger" or item=="pressurecooker" or item=="pan" or item=="cookwareset" or item=="knife" or item=="cuttingboard" or item=="onion" or item=="potato" or item=="tomato" or item=="carrot" or item=="beans" or item=="cabbage" or item=="apple" or item=="banana" or item=="orange" or item=="mango" or item=="grapes"):
                quantity=int(input("enter the quantity:"))
                stockofiteminshop=(stock[item])
                cost=(prices[item])
                if(quantity<=stockofiteminshop):
                    stock[item]=stockofiteminshop-quantity
                    file = open("pythonproject1moduleofstock.py", "w")
                    file.write("stock = " + str(stock))
                    file.close()
                    total=cost*quantity
                    #order=f"name={name}\nphone number={phoneno}\nproduct={item}\nquantity={quantity}\nprice of product={cost}\ntotal amount={total}"
                    order = f"""-------------------------------
            BILL
-------------------------------
Customer Name   : {name}
Phone Number    : {phoneno}

Product Details:
-------------------------------
Product Name    : {item}
Quantity        : {quantity}
Price per Item  : ₹{cost}

-------------------------------
Total Amount    : ₹{total}
-------------------------------

Thank you for your purchase!
"""
                    time= datetime.datetime.now()
                    time=str(time)
                    hrs=(time[11:13])
                    minutes=(time[14:16])
                    hrs=int(hrs)
                    minutes=int(minutes)
                    finalminutes=minutes+1
                    try:
                        pywhatkit.sendwhatmsg(f"+91{phoneno}",f"{order}",hrs,finalminutes)
                    except:
                        print("an uxpected error")
                else:
                    print("stock not available")
            else:
                print("item  not available")
            rep=input("do u want palce more order(yes/no)")
            if(rep=="yes" or rep=="Yes" or rep=="YES"):
                a=True
            else:
                a=False
    elif(coustomerattending=="no" or coustomerattending=="NO" or coustomerattending=="No"):
        print("thank you visiting")
    else:
        print("invalid comment")
else:
    print("invalid comment")



    

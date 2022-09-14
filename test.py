from datetime import datetime 

name=input("Enter your name:")

lists='''
rice   Rs 20/kg
suger  Rs 30/kg 
salt   Rs 2o/kg
oil    Rs 80/liter 
paneer Rs 110/kg 
maggi  Rs 50/kg 
Boost  Rs 90/each 
colagate Rs 85/each
'''
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]



items={'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':110,'maggi':50,'Boost':90,'colgate': 85}

option=int(input("for list of items press 1"))
if option==1:
    print(lists)

for i in range(len(items)):
    inp1=int(input("if you want to buy 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry your entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the item yes or no:")
    if inp=='yes':
        pass
        if  finalamount!=0:
            print(25*"=","ravi supermarket",25*"=") 
            print(28*" ","wanaparthy")
            print("Nname:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])   
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",50*" ",gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(50*" ","thanks for visting")
            print(75*"-")



                                                   
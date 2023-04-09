#!/usr/bin/env python
# coding: utf-8

# In[55]:


total_seats=150
normal_remaining_seats=130
recliner_remaining_seats=20
normal_seat_price=250
recliner_price=380
while True:
    amount_normal=0
    amount_recliner=0
    print("welcome to allen park")
    name=input("Enter name:")
    phone_no=int(input("enter phone no"))
    abc=input("what type of seat??(normal/recliner)")
    while True:
        if abc=="normal":
            XYZ=int(input("how many seats you need"))
            if XYZ<=normal_remaining_seats:
                amount_normal+=XYZ*normal_seat_price
                normal_remaining_seats=XYZ
                print(amount_normal)
                print("seats left",normal_remaining_seats)
            else:
                print("seats unavalability")
        if abc=="recliner":
            XYZ=int(input("how many seats you need??"))
            if XYZ<-recliner_remaning_seats:
                Amount_recliner+=XYZ*recliner_price
                recliner_remaining_seats=XYZ
                print(Amount_recliner)
                print("remainingseats",recliner_remaning_seats)
        repeat=input("add more seats??(yes/no)")
        if repeat=="no" or repeat=="No" or repeat=="NO":
             break
    print("_"*80)
    print("customer name",name)
    print("phone no",phone_no)
    if abc=="normal":
        print("total amount",amount_normal)
    else:
        print("total amount",Amount_recliner)
    print("visit again")
    print("_"*80)
    repeat_customer=input("new customer??(yes/no)")
    if repeat_customer=="no" or repeat_customer=="No" or repeat_customer=="NO":
        break
        


# In[ ]:





# In[ ]:





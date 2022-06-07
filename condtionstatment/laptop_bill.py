print("1. Dell(RS:2000) 2. Toshiba(Rs:3000) 3. Mac(Rs:5000)")
option = int(input("enter your choice "))
dell_price = 0
toshiba_price = 0
mac_price = 0
quantity = 0
if option == 1:
    print("dell laptop")
    quantity =int(input("enter quantity: "))
    dell_price = 2000* quantity
elif option == 2:
    print("toshiba laptop")
    quantity = int(input("enter quantity "))
    toshiba_price = 3000* quantity
elif option == 3:
    print("mac laptop")
    quantity = int(input("enter quantity "))
    mac_price = 5000* quantity
else:
    print("invalide option")
    exit()

print("1. home delivery(Rs.1000) 2. pickup")
home_delivery = 0
pick_up = 0
delivery_option = int(input("enter delivery option "))
if delivery_option == 1:
    print("home delivery")
    home_delivery += 1000
elif option == 2:
    print("pick up")
else:
    print("option invalide")
    exit()

print("1. bag(Rs.1000) 2. plastic bag(Rs.500) 3. gift bag(Rs.2000)")
bag_price = 0
plastic_price = 0
gift_bag_price = 0
bag_option = int(input("enter bag option "))
if bag_option == 1:
    bag_price += 1000
elif bag_option == 2:
    plastic_price += 500
elif bag_option == 3:
    gift_bag_price += 2000
else:
    print("invalide option")

price = dell_price + toshiba_price + mac_price
print("1.kathmandu(include 13% VAT) 2. bhaktapur 3.lalitpur")
VAT_amount = 0
location = int(input("enetr loctaion option "))
if location == 1:
    VAT_amount += price * 13 / 100


grand_total = dell_price + toshiba_price + mac_price + home_delivery + bag_option + plastic_price +gift_bag_price + VAT_amount

print("laptop price:", price)
if home_delivery == 1000:
    print("delivery amount:",home_delivery)
if bag_price > 0:
    print(" bag price:", bag_price)
if gift_bag_price > 0:
    print("gift bag price:", gift_bag_price)
if  plastic_price >0:
    print("plastic bag price", plastic_price)
if VAT_amount > 0:
    print("VAT amount", VAT_amount)
print("grand total:", grand_total)





nepali= int(input("nepali marks "))
maths = int(input("maths marks "))
science = int(input("science marks "))
social = int(input("social marks "))
total = (nepali + maths  + science + social)
print(total)
percentage = (total/4)
print(percentage)
if percentage > 35 and percentage <= 45:
    print("third")
elif percentage > 45 and percentage <= 60:
        print("second")
elif percentage > 60 and percentage <= 80:
            print("first")
elif percentage > 80 and percentage <= 100:
                print("top")
else:
            print("fail")

nepali= int(input("Enter Nepali marks "))
maths = int(input("Enter Maths marks "))
science = int(input("Enter Science marks "))
social = int(input("Enter Social marks "))
HPE = int(input("Enter HPE marks "))
Opt_maths = int(input("Enter Opt.Maths marks "))
coputer = int(input("Enter Computer marks "))
english = int(input("Enter English marks "))
total = (nepali + maths  + science + social + HPE + Opt_maths + coputer + english)
print("total marks: ",total)
percentage = (total/8)
print("obtained percentage: ",percentage)
if percentage > 50 and percentage <= 60:
    print("Grade: C+")
elif percentage > 60 and percentage <= 70:
    print("Grade: B")
elif percentage > 70 and percentage <= 80:
        print("Grade: B+")
elif percentage > 80 and percentage <= 90:
            print("Grade: A")
elif percentage > 90 and percentage <= 100:
                print("GPA: A+")
else:
            print("FAIL")

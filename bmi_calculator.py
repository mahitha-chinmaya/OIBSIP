ht=float(input("Enter the height(cm):"))
wt=float(input("Enter the Weight(kg):"))
h=ht/100
bmi=wt/(h**2)
if(bmi<=16):
        print(bmi,"\n Severe Thinness")
elif(16<bmi<=17):
        print(bmi,"\n Mild Thinness")
elif(17<bmi<=18.5):
        print(bmi,"\n Moderate Thinness")
elif(18.5<bmi<=25):
        print(bmi,"\n Normal")
elif(25<bmi<=30):
        print(bmi,"\n OverWeight")
elif(30<bmi<=35):
        print(bmi,"\n Obese Class-I")
elif(35<bmi<=40):
        print(bmi,"\n Obese Class-II")
elif(bmi>40):
        print(bmi,"\n Obese Class-III")
        print(bmi,"\n Obese Class-III")

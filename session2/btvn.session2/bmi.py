# factorial
n = int(input("n= "))
tich = 1
for i in range(1,n+1):
    tich = tich*i
    
print("giai thừa của ",n,"=", tich)



# calculate BMI
x = int(input("chieu cao cua ban (cm): "))/100

bmi = z = float(input("can nang cua ban (kg): ")) / (x*x)

if bmi < 16 : 
    print ("chỉ số bmi là: ","%.2f" % bmi,"  ==> Severely underweight")
elif bmi < 18.5 and bmi >= 16 : 
        print ("chỉ số bmi là: ","%.2f" % bmi,"  ==> Underweight")
elif bmi < 25 and bmi >= 18.5  :
        print ("chỉ số bmi là: ","%.2f" % bmi,"  ==> Normal")
elif bmi < 30 and bmi >= 25 : 
    print ("chỉ số bmi là: ","%.2f" % bmi,"  ==> Overweight")
else: 
    print ("chỉ số bmi là: ","%.2f" % bmi,"  ==> Obese")
	


# print without moving to new line
print("Hello", end="")
print(", my name", end="")
print(" is B-max")


    
         
# Some say paying taxes makes Finns happy, 
# so let's see if the secret of happiness lies 
# in one of the taxes set out in Finnish tax code.

#According to the Finnish Tax Administration, 
# a gift is a transfer of property to another person against no compensation or payment. 
# If the total value of the gifts you receive
#  from the same donor in the course of 3 years is €5,000 or more,
# you must pay gift tax.

valueOfGift = int(input("Value of gift: "))

if 0 <valueOfGift < 5000:
    print("No tax!")
if 5000<= valueOfGift <= 25000 :
    tax = ((valueOfGift - 5000) * 0.08 )+ 100
    print("Amount of tax:", float(tax),"euros")

elif  25000 <= valueOfGift <= 55000 : 
    tax = ((valueOfGift - 25000) * 0.10 )+ 1700
    print("Amount of tax:", float(tax),"euros")

elif  55000 <= valueOfGift <= 200000 : 
    tax = ((valueOfGift - 55000) * 0.12 )+ 4700
    print("Amount of tax:", float(tax),"euros")

elif  200000 <= valueOfGift <= 1000000 : 
    tax = ((valueOfGift - 200000) * 0.15 )+ 22100
    print("Amount of tax:", float(tax),"euros")
elif valueOfGift > 1000000:
    tax = ((valueOfGift - 1000000)* 0.17) + 142100
    print("Amount of tax:", float(tax),"euros")
else: 
    print("")
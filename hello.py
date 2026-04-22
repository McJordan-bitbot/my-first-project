def is_even(n):
        rem = n % 2
        if rem == 0:
            return True
        else:
            return False
           
n = int(input('n? '))
print(is_even(n))


#BILL SPLITTER
running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill, 2)
print(f'Each person pays: {each_pays}')

#TRY 2 (THIS ONE WORKS BETTER)
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ") 
if unit == "L" or unit == "l":
    unit_in_kg = round(weight * 0.453592, 1)
    print(f'Weight in Kg: {unit_in_kg}')
elif unit == "K" or unit == "k":
    unit_in_lbs = round(weight / 0.453592, 1)
    print(f'Weight in Lbs: {unit_in_lbs}')
else:
    print("Invalid unit. Please enter 'L' for pounds or 'K' for kilograms.")

#TRY 1
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ") 
num = float(2.20462)
unit_in_kg = weight * float(num)
if unit == "L" or unit == "l":
    print("Weight in Kg: " + str(round(unit_in_kg, 1)))


#cool one fam
First = input("First number: ")
Second = input("second number: ")
sum = float(First) + float(Second)
difference = float(First) - float(Second)
division = float(First) / float(Second)
multiplication = float(First) * float(Second)
print('Hello, I am McJordan and I am becoming a software engineer! \nAnd my ARITHMETIC is given below')

print(f"When you add, the Sum is: {str(sum)}")
print(f"When you Subtract: {str(difference)}")
print(f"When you Divide: {division}")
print(f"When you Multiply: {str(multiplication)}")
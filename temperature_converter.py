temp=float(input("Enter the temperature:"))
unit=input("enter the unit is Celcius or Fahrenheit C/F :").lower()
if unit in["c","celcius"]:
    temp=round((temp*9/5)+32,2)
    print(f"the temperature in Fahrenheit is:{temp}F")
elif unit in["f","fahrenheit"]:
    temp=round((temp-32)*5/9,2)
    print(f"the temperature in Celcius is :{temp}C")
else:
    print("the unit is not in a list")

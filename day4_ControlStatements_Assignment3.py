#Write a Python program that determines if a given year is a leap year or not.
year=int(input("Enter the year: "))
if year%400==0 and year%100==0: # divided by 100 means century year ending with 00, century year divided by 400 is leap year
    print(year,"is a leap year")
elif year%4==0 and year%100!=0:  # not divided by 100 means not a century year and year divided by 4 is a leap year
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#answer
"""
Enter the year: 2024
2024 is a leap year
"""

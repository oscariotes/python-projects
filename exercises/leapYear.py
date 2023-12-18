    # A year is a leap year if it is divisible by 4.
    # However, if a year is divisible by 100, it is not a leap year, unless...
    # The year is also divisible by 400. In that case, it is a leap year.

year = int(input('Enter the year to calculate if it\'s a leap year:  '))
def leapyear(a):
    if (year % 4 == 0 and year % 100 == 0) or (year % 400 == 0):
        print(f'{str(year)} is a leap year!' )
    else:
        (print(f'{str(year)} is not a leap year'))

leapyear(year)
   
print ("what is the year?")
year = input("what is the year?")
if (int(year)-543) % 400 == 0:
    print("Leap year")
elif (int(year)-543) % 100 == 0:
    print("Not a leap year")
elif (int(year)-543) % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

def male():  
  try:
    age = int(input("Your age:\n"))
    if age >= 65:
        print("Ok, bro, you need on pension")
    else: print("It is too eraly to retire")
  except ValueError:
    print("You try type words, plese type only numbers")

male()
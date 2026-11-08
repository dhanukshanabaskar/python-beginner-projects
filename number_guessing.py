number = 10
while True:
   num = int(input("guess the number between 1 and 30"))
   print (num)
   if num > number:
    print("too high")
   elif num < number:
    print("too low")
   else:
      print("correct")
      break
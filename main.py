n = int(input('How many staircases would you like?: '))
if (n < 1):
  print ("Maybe this estqablishment isn't for you.")
elif (n > 15):
  print ("Maybe you'll have better luck with a wholesaler.")
else:
  b = int(input('And how many stairs would you like in each? : '))
  if (n%2 == 0):
    a = 0
    while (a < n):
      for x in range(b+1):
        print (x * "*")

      for y in range(b+1):
        print ((65-y) * " " + y * "*")
        a += 2
  else:
    a = 0
    while (a <= n-1):
      for x in range(b+1):
        print (x * "*")

      for y in range(b+1):
        print ((65-y) * " " + y * "*")
        a += 2
    for z in range(b+1):
      print (z * "*")

print ("Please visit again!")
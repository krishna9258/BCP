a = int(input("enter a: "))
rev = 0
temp = a
while temp>0:
  digit = temp%10
  rev = rev*10+digit
  temp//=10
  if a == rev:
    print("yes")
else:
  print("no")
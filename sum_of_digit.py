n = int(input("enter a number: "))
total = 0
while  n>0:
  digit = n%10
  total+=digit
  n//=10
print("sum of digit=",total)
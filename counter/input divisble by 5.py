# taker input from the user and print if "divisible" if the number is divisible otherwise print the sum of the input
i=1
sum=0
while i<=10:
 userinput=int(input("enter the number"))
 if userinput%5==0:
  print("divisible")
 sum=sum+userinput
 print(sum)
i+=1
n = input("What is your max?\n")


def fizzbuzz(max):
  num = list(range(max))
  for i in range(len(num)):
    number = num[i] + 1
    if number % 5 == 0 and number % 3 == 0:
      print("fizzbuzz")
    elif number % 5 == 0:
      print("buzz")
    elif number % 3 == 0:
      print("fizz")
    else:
      print(number)
      
fizzbuzz(int(n))
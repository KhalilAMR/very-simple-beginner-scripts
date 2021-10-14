print("--------------------")
print("CLOCK PROJECT START")
print("--------------------")
hour = int(input("Choose a number between 1 and 24: "))
if hour < 0:
  print("ERROR")
elif hour <= 6:
  print("Why are you still awake?!")
elif hour <= 12:
  print("Good Morning!")
elif hour <= 17:
  print("Good Afternoon!")
elif hour <= 21:
  print("Good Evening!")
elif hour <= 24:
  print("Good Night!")
elif hour < 0:
  print("ERROR")
elif hour > 24:
  print("ERROR")
else:
  print("ERROR")
print("--------------------")
print("CLOCK PROJECT END")
print("--------------------")
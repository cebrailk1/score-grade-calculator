score = input("Enter Score 0-1: ")
score = float(score)
if score < 0 or score > 1: 
  print ("score out of range")
  exit()

elif score >= 0.9:
  print("A")
elif score >= 0.8:
  print("B")
elif score >= 0.7:
  print("C")
elif score >= 0.6:
  print("D")
elif score < 0.6:
  print("F")

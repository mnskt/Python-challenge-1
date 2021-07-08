import ASCII_art as art
import game_data as gd
import random as rand

score = 0
isRunning = True

print(art.logo)
print(f"Your score is: {score}")

#declare and print A comparison initial values
compareA = rand.choice(gd.data)
compareA_name = compareA["name"]
compareA_follow = compareA["follower_count"]
compareA_desc = compareA["description"]
compareA_country = compareA["country"]
print(compareA_name, compareA_follow, compareA_desc, compareA_country,"\n")

while isRunning == True:
  compareA = rand.choice(gd.data)
  compareA_name = compareA["name"]
  compareA_follow = compareA["follower_count"]
  compareA_desc = compareA["description"]
  compareA_country = compareA["country"]

  compareB = rand.choice(gd.data)
  if compareB == compareA:
    while True:
      compareB = rand.choice(gd.data)
  else:
    compareB_name = compareB["name"]
    compareB_follow = compareB["follower_count"]
    compareB_desc = compareB["description"]
    compareB_country = compareB["country"]

  print(compareA_name, compareA_follow, compareA_desc, compareA_country,"\n")
  print(compareB_name, compareB_follow, compareB_desc, compareB_country)


  if compareB_follow > compareA_follow:
    print("you ded")
    isRunning = False
  elif compareB_follow < compareA_follow:
    score+=1
    print(score)

  print("testest")
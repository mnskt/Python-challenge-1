import ASCII_art as art
import game_data as gd
import random as rand
import os

clear = lambda: os.system("cls")

score = 0
isRunning = True

def comparisonA():
  #declare and print A comparison initial values
  compareA = rand.choice(gd.data)
  compareA_name = compareA["name"]
  compareA_follow = compareA["follower_count"]
  compareA_desc = compareA["description"]
  compareA_country = compareA["country"]
  return compareA, compareA_name, compareA_follow, compareA_desc, compareA_country

def comparisonB():
  #declare and print B comparison initial values
  compareB = rand.choice(gd.data)
  compareB_name = compareB["name"]
  compareB_follow = compareB["follower_count"]
  compareB_desc = compareB["description"]
  compareB_country = compareB["country"]
  return compareB, compareB_name, compareB_follow, compareB_desc, compareB_country

compareA, compareA_name, compareA_follow, compareA_desc, compareA_country = comparisonA()

while isRunning == True:

  compareB, compareB_name, compareB_follow, compareB_desc, compareB_country = comparisonB()
  if compareB_name == compareA_name:
    compareB_name = rand.choice(gd.data)["name"]

  clear()
  print(art.logo)
  print(f"Your current score is: {score}")

  print("\n---Entry A---")
  print(f"Name: {compareA_name}\nDescription: {compareA_desc}\nCountry: {compareA_country}\nFollowers: {compareA_follow} M.\n")
  print("\n---Entry B:---")
  print(f"Name: {compareB_name}\nDescription: {compareB_desc}\nCountry: {compareB_country}\n")

  user_choice = str(input(f"Does '{compareB_name} have higher or lower follower count than '{compareA_name}': "))

  if compareB_follow > compareA_follow and user_choice == "lower":
    print("\nIncorrect guess. You lost.\n")
    print(f"Final score: {score}")
    isRunning = False
  elif compareB_follow > compareA_follow and user_choice == "higher":
    score+=1
  elif compareB_follow < compareA_follow and user_choice == "lower":
    score+=1
  elif compareB_follow < compareA_follow and user_choice == "higher":
    print("\nIncorrect guess. You lost.\n")
    print(f"'{compareB_name}' has {compareB_follow} M. followers.")
    print(f"\nFinal score: {score}")
    isRunning = False

  if score == 49:
    clear()
    print(art.logo)
    print("\nCongratulations! You have won the game!\n")
    print(f"Your final score: {score}")
    isRunning = False

  compareA, compareA_name, compareA_follow, compareA_desc, compareA_country = \
  compareB, compareB_name, compareB_follow, compareB_desc, compareB_country

  if isRunning == False:
    play_again_choice = str(input("\nWould you like to play again? (yes/no): "))
    if play_again_choice == "yes":
      isRunning = True
      score = 0
      compareA, compareA_name, compareA_follow, compareA_desc, compareA_country = comparisonA()

    elif play_again_choice == "no":
      isRunning = False

    else:
      print("Wrong input. Please type yes or no.")



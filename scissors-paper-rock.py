#!/usr/bin/env python3



def main():
	
	def rock():
		
		if random == 1:
			print("rock beats scissors")
			print("you won!!")
			wantleave()
		elif random == 2:
			print("paper beats rock")
			print("you lost")
			wantleave()
		elif random == 3:
			print("It was a draw")
			wantleave()
	def paper():

		if random == 1:  #scissors
			print("scissors beats paper")
			print("you lost!!")
			wantleave()
		elif random == 2:  #paper
			print("It was a draw")
			wantleave()
		elif random == 3:  #rock
			print("paper beats rock")
			print("you won!!")
			wantleave()

	def scissors():
		if random == 1:
			print("It was a draw")
			wantleave()
			os.system("clear")
		elif random == 2:
			print("scissors beats paper")
			print("you won!!")
			wantleave()
		elif random == 3:
			print("rock beats paper")
			print("you lost!!")
			wantleave()


	def wantleave():
		choice = input("do you want to leave? ")
		lower_choice = choice.lower()
		if lower_choice == ["y","yes"]:
			exit()
		else:
			main()
	import random
	import os
	random = random.randrange(1,4)
	our_choice = input(("Pick Rock, Paper, or Scissiors (R,P,S) : ").lower())
	lower_our_choice = our_choice.lower()
	if lower_our_choice == "s":
		
		scissors()

	elif lower_our_choice == "p":
		
		paper()

	elif lower_our_choice == "r":
		
		rock()	
		
	else:
		os.system("clear")
		print("invalid input")
		exit()
	







main()

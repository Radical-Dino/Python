import time
from sys import exit
name = raw_input("Type in your name\n>")
def start():
	print("[Story] You live in a village.")
	time.sleep(3)
	print("[Story] You want to explore the world.")
	time.sleep(3)
	print("[Story] Today, you want to explore the jungle.")
	time.sleep(3)
	print("[Story] You walked to the jungle.")
	time.sleep(3)
	print("[Story] You saw a tiger with wings in the jungle.")
	time.sleep(3)
	print("[Story] You did not know what it was.")
	time.sleep(3)
	print("[Choice] Do you want to go to it or go back to the village?")
	time.sleep(3)
	print("[Choice] Type weird tiger or village.")
	
	while True:
		choice = raw_input(">")
		if choice == "weird tiger" or choice == "Weird tiger":
			print("[Story] You walked to the tiger.")
			time.sleep(3)
			meetSnowflake()
		elif choice == "village" or choice == "Village":
			print ("[Story] You ran back to the vilage.")
			time.sleep(3)
			print ("[Story] It was getting dark so you went to bed.")
			time.sleep(3)
			print ("[Story] The next day, you was preparing to go out.")
			time.sleep(3)
			print ("[Story] When you walked out the door, you saw the tiger.")
			meetSnowflake()
		else:
			print ("Not a choice.")
			time.sleep(1)
			print ("Plese type again.")
			time.sleep(1)
			print ("weird tiger or village")

def meetSnowflake():
	print ("[Story] Then the tiger said something.")
	time.sleep(3) 
	print ("[Tiger] Hi " + name + ", I am a mythical animal.")
	time.sleep(3)
	print ("[Tiger] I am from another dimension.")
	time.sleep(3)
	print ("[You] Wait, how do you know my name?")
	time.sleep(3)
	print ("[Tiger] I know everyone.")
	time.sleep(3)
	print ("[You] Umm ok...")
	time.sleep(2)
	print ("[You] Hi ...")
	time.sleep(2)
	print ("[Tiger] Oh sorry. My name is Snowflake.")
	time.sleep(3)
	print ("[You] Hi Snowflake.")
	time.sleep(2)
	print ("[Snowflake] " + name + ", follow me.")
	time.sleep(3)
	print("[Story] You followed Snowflake to a portal.")
	time.sleep(3)
	print("[Snowflake] Go in.")
	landOfMagic()

def landOfMagic():
	print ("[Story] Poof!")
	time.sleep(1)
	print ("[Snowflake] We are in the land of magic.")
	time.sleep(3)
	print ("[You] Wow! This place is cool!")
	time.sleep(2)
	print ("[Story] You walked up the staircase to the floating island.")
	time.sleep(3)
	print ("[Snowflake] Come this is my house.")
	time.sleep(2)
	print ("[Story] You walked into Snowflake's house.")
	time.sleep(2)
	print ("[Story] Snowflake picked up a necklace.")
	time.sleep(2)
	print ("[Snowflake] Here have this.")
	time.sleep(2)
	print ("[You] What is this?")
	time.sleep(2)
	print ("[Snowflake] This necklace lets you teleport here anytime you want.")
	time.sleep(3)
	print ("[You] But then I will not be in my dimension. Everyone will be looking for me.")
	time.sleep(6)
	print ("[Snowflake] A fake 'You' will be put in your dimension.")
	time.sleep(3)
	print ("[Snowflake] Its getting late so you should go back.")
	time.sleep(3)
	print ("[Snowflake] Touch your necklace and think of your home.")
	time.sleep(3)
	print ("[Story] You touched your necklace and then you woke up in your bed.")
	time.sleep(4)
	print ("[Story] You did not know what just happened.")
	time.sleep(3)
	print ("[Story] You thought it was all a dream.")
	time.sleep(2)
	print ("[Story] The whole day went pass quickly.")
	time.sleep(2)
	print ("[Story] Until you realised your necklace was still there and it was glowing.")
	time.sleep(4)
	print ("[Story] You touched your necklace and thought of Snowflake ")
	time.sleep(3)
	print ("[Story] Poof! You landed in front of Snowflake.")
	time.sleep(3)	
	evilWitch()

def evilWitch():
	print ("[Story] Snowflake looked very worried.")
	time.sleep(3)
	print ("[Snowflake] A evil witch is atacking The land of magic.")
	time.sleep(3)
	print ("[Snowflake] He is destroying this dimension.")
	time.sleep(3)
	print ("[Choice] Do you want to fight or run?")
	time.sleep(1)
	print ("[Choice] Type fight or run.")
	while True:
		choice = raw_input (">")
		if  choice == "fight" or choice == "Fight":
			fight()
		elif choice == "run" or choice == "Run":
			print ("[Story] The wisard took over the universe and everything died.")
			time.sleep(2)
			die()
		else:
			print ("[Choice] You dont have much time left.")
			time.sleep(1)
			print ("[Choice] fight or run")
			time.sleep(1)

def die():
	print ("YOU DIED! GAME OVER!")
	exit(0)

def fight():
	print ("[Snowflake] But we are not strong enough.")
	choice = raw_input("[Choice] Tell Snowflake\n(1)I am strong enough\n(2)I know we are strong enough.\nType 1 or 2\n>")
	if choice == "1":
		print ("[Note] Snowflake is not confident in herself.")
		noSnowflake()
	elif choice == "2":
		print (" [Note] Snowflake is confident in herself.")
		teamwork()

def noSnowflake():
	print ("[Story] You went to fight the witch by yourself because Snowflake was too scared.")
	time.sleep(4)
	print ("[Story] The witch died.")
	time.sleep(2)
	print ("[Witch] Noooooooooooo!")
	time.sleep(2)
	print ("To be continued...")
	time.sleep(2)
	print ("Code for next episode = 1")
	exit(0)

def teamwork():
	print ("[Snowflake] Ok. lets do this!")
	time.sleep(2)
	print ("[Story] You and Snowflake worked as a team to kill the witch.")
	time.sleep(3)
	print ("[Story] The witch eventually died.")
	time.sleep(3)
	print ("[Witch] Noooooooooooooo!")
	time.sleep(1)
	print ("To be continued...")
	time.sleep(2)
	print ("Code for next episode = 0")
	time.sleep(5)
	exit(0)

start()

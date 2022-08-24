import random

ladder = {1:38, 4:14, 8:30, 21:42, 28:76, 50:67, 71:92, 80:99}
snake = {32:10, 34:6, 48:26, 62:18, 88:24, 95:56, 97:78}
pos1 = 0
pos2 = 0

def move(pos):
	dice = random.randint(1,6)
	print(f"dice:{dice}")
	pos = pos + dice
	if pos in snake:
		print("Bitten by snake")
		pos = snake[pos]
		print(f"position:{pos}")
	elif pos in ladder:
		print("Climed by ladder")
		pos = ladder[pos]
		print(f"position:{pos}")
	else:
		print(f"position:{pos}")
	print("\n")
	return pos

while True:
	A = input("player 1 enter \"A\" to throw dice:")
	pos1 = move(pos1)
	if pos1 >= 100:
		print("game over!!! \n player 1 wins")
		break

	B = input("player 2 enter \"B\" to throw dice:")
	pos2 = move(pos2)
	if pos2 >= 100:
		print("game over!!! \n player 2 wins")
		
		break
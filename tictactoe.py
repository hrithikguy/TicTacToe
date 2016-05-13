import sys

class Node:
    """
    Class Node
    """
    def __init__(self, value, children=None):
        self.move = value
        self.moves = []
        self.parent = None
        self.children = []
        self.status = 0
        self.winningpercentage = -1.0
        if children:
        	for child in children:
        		self.children.append(child)

def add_new_layer(root):
	if not root.children and root.status == 0:
		for i in range(1, 10):
			if i not in root.moves:
				y = Node(i)
				y.moves = list(root.moves)
				y.moves.append(i)
				y.parent = root
				if gamestatus(y.moves) != 0:
					y.status = gamestatus(y.moves)
					root.children = []
					root.children.append(y)
					break
				root.children.append(y)
	else:
		for child in root.children:
			add_new_layer(child)


def gamestatus(input):
	array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i,j in enumerate(input):
		if i%2 == 0:
			array[j-1] = 1
		else:
			array[j-1] = 2
	for i in range(0, 3): #(i = 0; i <= 2; ++i) {
		if (array[3*i] == 1 and array[3*i + 1] == 1 and array[3*i + 2] == 1): 
			return 1;
		
		if (array[3*i] == 2 and array[3*i + 1] == 2 and array[3*i + 2] == 2): 
			return 2;
	for i in range(0, 3): #(i = 0; i <= 2; ++i) {
		if (array[i] == 1 and array[i + 3] == 1 and array[i + 6] == 1):
			return 1;
		
		if (array[i] == 2 and array[i+3] == 2 and array[i + 6] == 2): 
			return 2;
	if (array[0] == 1 and array[4] == 1 and array[8] == 1): 
		return 1;
	if (array[0] == 2 and array[4] == 2 and array[8] == 2):
		return 2;
	if (array[2] == 1 and array[4] == 1 and array[6] == 1):
		return 1;
	if (array[2] == 2 and array[4] == 2 and array[6] == 2):
		return 2;
	return 0;

def print_tree(root):
	print(root.winningpercentage)
	print (root.moves)
	if not root.children:
		return
	else:
		for child in root.children:
			print_tree(child)

def size_of_tree(root):
	output = 1
	if not root.children:
		return output
	else:
		for child in root.children:
			output += size_of_tree(child)
		return output

def game_endings(root):
	if not root.children:
		if root.status == 1:
			root.winningpercentage = 0.0
			return
		if root.status == 2:
			root.winningpercentage = 1.0
			return
		if root.status == 0:
			root.winningpercentage = 0.5
			return

	for child in root.children:
		game_endings(child)

def calculate_winning_percentages(root):
	if not root.children:
		return

	for child in root.children:
		calculate_winning_percentages(child)
	
	output = 0
	for child in root.children:
		output += child.winningpercentage
	

	output = output/len(root.children)
	
	root.winningpercentage = output



def printboard(input):
	array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i,j in enumerate(input):
		if i%2 == 0:
			array[j-1] = 1
		else:
			array[j-1] = 2
	
	for i in range(0, 9):
		if (array[i] == 1):
			sys.stdout.write('X')
		
		if (array[i] == 0): 
			sys.stdout.write('_')
		
		if (array[i] == 2): 
			sys.stdout.write('O')
		
		if (i % 3 == 2): 
			sys.stdout.write('\n')
		



def print_winning_percentages(root):
	print(root.winningpercentage)
	if not root.children:
		return
	else:
		for child in root.children:
			print_winning_percentages(child)

def player_goes_first(y):
	movearray = []
	gamewon = 0
	while gamewon == 0:
		move = raw_input("Enter the square of your move: ")
		move = int(move)
		if move in movearray:
			print ("not a legal move!")
			break
		movearray.append(move)
		print ("Your move:")
		printboard(movearray)
		gamewon = gamestatus(movearray)
		if (gamewon != 0):
			print ("congratulations! you win!")
			break
		if len(movearray) == 9:
			print ("the game is a tie!")
			break
		for i in movearray:
			for child in y.children:
				if child.move == i:
					y = child
					break
		bestmove = -1
		maxwinningpercentage = -1
		for child in y.children:
			if child.winningpercentage > maxwinningpercentage:
				maxwinningpercentage = child.winningpercentage
				bestmove = child.move
		movearray.append(bestmove)
		print("Computer's move:")
		printboard(movearray)
		gamewon = gamestatus(movearray)
		if (gamewon != 0):
			print("sorry! you lose!")
			break
		if len(movearray) == 9:
			print ("the game is a tie!")
			break

def computer_goes_first(y):
	movearray = []
	gamewon = 0
	while gamewon == 0:

		if movearray:
			for i in movearray:
				for child in y.children:
					if child.move == i:
						y = child
						break
		bestmove = -1
		maxwinningpercentage = 2
		print (movearray)
		for child in y.children:
			if child.winningpercentage < maxwinningpercentage:
				maxwinningpercentage = child.winningpercentage
				bestmove = child.move
		movearray.append(bestmove)
		print("Computer's move:")
		printboard(movearray)
		gamewon = gamestatus(movearray)
		if (gamewon != 0):
			print("sorry! you lose!")
			break
		if len(movearray) == 9:
			print ("the game is a tie!")
			break

		move = raw_input("Enter the square of your move: ")
		move = int(move)
		if move in movearray:
			print ("not a legal move!")
			break
		movearray.append(move)
		print ("Your move:")
		printboard(movearray)
		gamewon = gamestatus(movearray)
		if (gamewon != 0):
			print ("congratulations! you win!")
			break
		if len(movearray) == 9:
			print ("the game is a tie!")
			break
print ("Loading...")
y = Node(0)


for i in range(1, 10):
	add_new_layer(y)

game_endings(y)
calculate_winning_percentages(y)


firstorsecond = raw_input("Type 1 if you want to first, or 2 if you want to go second: ")
firstorsecond = int(firstorsecond)
if (firstorsecond == 1):
	player_goes_first(y)
elif (firstorsecond == 2):
	computer_goes_first(y)
else:
	print ("You must enter 1 or 2")


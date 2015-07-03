import sys
import random
class Player4:
	def __init__(self):
		self.WINCOMBOS = [[[0,0],[0,1],[0,2]],
				 [[1,0],[1,1],[1,2]],
				 [[2,0],[2,1],[2,2]],
				 [[0,0],[1,0],[2,0]],
				 [[0,1],[1,1],[2,1]],
				 [[0,2],[1,2],[2,2]],
				 [[0,0],[1,1],[2,2]],
				 [[0,2],[1,1],[2,0]]]

		self.bestmove = -1
		self.maxdepth = 6
		self.ar_index = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]] 
		self.convert = [[0,1,2],[3,4,5],[6,7,8]]

	def move(self, current_board_game, board_stat, move_by_opponent, flag):
		if self.check_move(move_by_opponent) == 1:
			a = (4,4)
			return a
		else:
			sys.exit(1)

	
	def check_move(self, move_by_opponent):
		if type(move_by_opponent) is not tuple:
			print "Opponent's move is not a tuple"
			sys.exit(1)

		if len(move_by_opponent) != 2:
			print "Opponents's move is not of length 2"
			sys.exit(1)
			
		a = move_by_opponent[0]
		b = move_by_opponent[1]

		if type(a) is not int or type(b) is not int:
			print "Opponent's move is not a int"
			sys.exit(1)

		if a == -1 and b == -1:
			return 0

		if a < 0 or a > 8 or b < 0 or b > 8:
			print "Opponent's move is outside the 9X9 matrix."
			sys.exit(1)
			
		return 1

	def buildtree(self, array):
		self.bestmove = -1
		alpha = self.recurse_tree(array, 'X',0)
		print alpha
		print self.bestmove
		print self.ar_index[self.bestmove]

	def recurse_tree(self, array, player, depth):
		if depth > self.maxdepth:
			return 0
		if player == 'X':
			otherplayer = 'O'
		else:
			otherplayer = 'X'
		if self.winner(array) != None:
		#	print self.winner(array)
		#	print "In this if"
		#	print self.score(array)
		#	print 'vikram ahuja'
			return self.score(array)
		#print "going ahead bitches"
		#print self.winner(array)

		movelist = self.GetPossibleMoves(array)  #This has to be changed tomorrow for the 9X9 matrix :)
		#print movelist
		alpha = -999999

		salist = []
		import copy
		for i in movelist:
			array1 = copy.deepcopy(array)
			#print array
			a = self.ar_index[i]
			#print a
			array1[a[0]][a[1]] = player
			#print array
			#print array1 

			subalpha = -self.recurse_tree(array1, otherplayer, depth+1)
			if alpha < subalpha:
				alpha = subalpha;
			if depth == 0: salist.append(subalpha)

		if depth == 0:
			candidate = []
			for i in range(len(salist)):
				if salist[i] == alpha:
					candidate.append(movelist[i])
			#print alpha
			self.bestmove = random.choice(candidate)

		return alpha


	def score(self, array):
		if self.winner(array) == 'X':
			return 999999
		elif self.winner(array) == 'O':
			return -999999
		elif self.winner(array) == '-':
			return 0


	def winner(self , array):
		for a, b, c in self.WINCOMBOS:
			
			if array[a[0]][a[1]] == array[b[0]][b[1]] == array[c[0]][c[1]] != '-':
			#	print array[a[0]][a[1]]
			#	print 'Hello'
				return array[a[0]][a[1]]
		for i in range(0,3):
			for j in range(0,3):
				if array[i][j] == '-':
			#		print 'None'
					return None
		#print '-'
		return '-'

	def GetPossibleMoves(self, array):
		clist=[]
		for i in range(0,3):
			for j in range(0,3):
				if array[i][j] == '-':
					clist.append(self.convert[i][j])
		return clist

obj=Player4()
a=[['-','-','-'],['-','-','-'],['-','-','-']]
print type(a)
obj.buildtree(a)
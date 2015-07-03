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
		self.maxdepth = 4
		self.ar_index = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]] 
		self.convert = [[0,1,2],[3,4,5],[6,7,8]]
		self.subs = [[0,0],[0,3], [0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
		self.name ="vikram"
		print self.name

	def move(self, current_board_game, board_stat, move_by_opponent, flag):
		
		if self.check_move(move_by_opponent) == 0:
			a = (4,4)
			return a

		else:
			allocated_block = self.select_block(move_by_opponent,current_board_game)
			array_index = self.ar_index[allocated_block]
			if board_stat[allocated_block] == "-":
				print "allocated_block",
				print allocated_block
				array = [[0,0,0],[0,0,0],[0,0,0]]
				ai = array_index[0]*3
				aj = array_index[1]*3
				u =0
				v =0
				for i in range(ai, ai + 3):
					v = 0 
					for j in range(aj, aj +3):
						array[u][v] = current_board_game[i][j]
						v +=1
					u +=1
			#sys.exit(1)
				for i in range(0,3):
					for j in range(0,3):
						print array[i][j],
					print
				self.buildtree(array, flag)
				a = self.ar_index[self.bestmove]
				a = (self.ar_index[self.bestmove][0] +ai , self.ar_index[self.bestmove][1] + aj)

				return a
			else:
				ar = [0,0,0,0,0,0,0,0,0]
				for i in range(0,9):
					if board_stat[i] != '-':
						ar[i] = -1
				array = [['-','-','-'],['-','-','-'],['-','-','-']]
				v =0
				u = 0
				
				if flag == 'X':
					flag1 = 'O'
				else:
					flag1 = 'X'
				for i in range(0,3):
					for j in range(0,3):
						v=0
						u=0
						for k in range(3*i,(3*i)+3):
						 	v = 0
						 	for l in range(3*j,(3*j)+3):
						 		
						 		array[u][v] = current_board_game[k][l]
						 	
						 		print array[u][v],
						 		v +=1
						 	u +=1
						 	print
						for x in range(0,3):
							for z in range(0,3):
								if array[x][z] == flag and ar[self.convert[i][j]] !=-1:
									ar[self.convert[i][j]] = 1
									break
						for x in range(0,3):
							for z in range(0,3):
								for a,b,c in self.WINCOMBOS:
									if array[c[0]][c[1]] != array[a[0]][a[1]] and  array[a[0]][a[1]]== array[b[0]][b[1]] and array[a[0]][a[1]] == flag and array[c[0]][c[1]] != flag1:
										#print "case1"
										if ar[self.convert[i][j]] !=-1:
											ar[self.convert[i][j]] = 2
										break

									if array[b[0]][b[1]] != array[a[0]][a[1]] and  array[a[0]][a[1]]== array[c[0]][c[1]] and array[a[0]][a[1]] == flag and array[b[0]][b[1]] != flag1:
										#print "case2"
										if ar[self.convert[i][j]] !=-1:
											ar[self.convert[i][j]] = 2
										
										break

									if array[c[0]][c[1]] != array[a[0]][a[1]] and  array[c[0]][c[1]]== array[b[0]][b[1]] and array[b[0]][b[1]]  == flag and array[a[0]][a[1]] != flag1:
										#print "case3"
										if ar[self.convert[i][j]] !=-1:
											ar[self.convert[i][j]] = 2
										
										break
						print
					print
				print
						 		#for a,b,c in self.WINCOMBOS:
						 		#	if a[]
						 		#if current_board_game[k][l] == flag:
						 		#	ar[self.convert[i][j]] = 1
				print ar
				for i in range(0,9):
					if ar[i] == 2:
						ma = i
						print ma
						break

				for i in range(0,9):
					if ar[i] == 1:
						ma = i
						print ma
						break



				for i in range(0,9):
					if ar[i] == 0:
						ma = i
						print ma
						break


				
				d = self.ar_index[ma]
				ai = d[0]*3
				aj = d[1]*3
				u =0
				v =0
				for i in range(ai, ai + 3):
					v = 0 
					for j in range(aj, aj +3):
						array[u][v] = current_board_game[i][j]
						v +=1
					u +=1
			#sys.exit(1)
				self.buildtree(array, flag)
				a = self.ar_index[self.bestmove]
				a = (self.ar_index[self.bestmove][0] +ai , self.ar_index[self.bestmove][1] + aj)

				return a
				sys.exit(1)



	


	def select_block(self, move_by_opponent,current_board_game):
		a = move_by_opponent[0]
		b = move_by_opponent[1]

		a1 =a/3
		b1 =b/3
		print self.convert[a1][b1]
		a -= self.subs[self.convert[a1][b1]][0]
		b -= self.subs[self.convert[a1][b1]][1]
		
		box = self.convert[a][b]
		print box
		if box in [1,3,4,5,7]:
			allocated_block = box
			return allocated_block

		elif box in [0,2,6,8]:
			allocated_block = box
			if box == 0:
				allocated_list = [0,1,3]

			elif box == 2:
				allocated_list = [2,1,5]

			elif box == 6:
				allocated_list = [6,3,7]

			elif box == 8:
				allocated_list = [8,7,5]
			
			array = [['-','-','-'],['-','-','-'],['-','-','-']]
			for i in allocated_list:
				num = self.ar_index[i]
				y =0
				z =0
				for u in range(num[0]*3,num[0]*3 +3):
					
					for v in range(num[1]*3,num[1]*3 +3):
						array[y][z] = current_board_game[u][v]
						print array[y][z],
						z +=1
					z =0
					y +=1
					print 
				for a1,b1,c1 in self.WINCOMBOS:
					if array[a1[0]][a1[1]] == array[b1[0]][b1[1]] == array[c1[0]][c1[1]] != '-':
						break
					for i1 in range(0,3):
						for j in range(0,3):
							if array[i1][j] == '-':
			#		print 'None'
								return i
					break
			return i


		return allocated_block


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

	def buildtree(self, array, flag):
		self.bestmove = -1
		alpha = self.recurse_tree(array, flag,0)
		print alpha
		print self.bestmove
		return self.bestmove

	def recurse_tree(self, array, player, depth):
		if depth > self.maxdepth:
			return 0
		if player == 'X':
			otherplayer = 'O'
		else:
			otherplayer = 'X'
		if self.winner(array) == player or self.winner(array) == otherplayer:
			a = self.score(array, player, otherplayer)
			print a
			return a
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
			if subalpha == None:
				print "subalpha is none"
			
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
		if alpha == None:
			print "alpha is none"

		return alpha
	

	def score(self, array, player, otherplayer):
		if self.winner(array) == player:
			print player
			print "We win"
			return 999999
		elif self.winner(array) == otherplayer:
			print otherplayer
			print "Otherplayer win"
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
					return 'w'
		#print '-'
		return '-'

	def GetPossibleMoves(self, array):
		clist=[]
		for i in range(0,3):
			for j in range(0,3):
				if array[i][j] == '-':
					clist.append(self.convert[i][j])
		return clist




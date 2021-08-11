# tic tac toe multi player 1 Vs 1
array=[[' ' for x in range(3)]for y in range(3)]
class tictactoe():
	array=[[]]
	symbols=[]
	def __init__(self):
		print("object created")
	def setarray(self,arr):
		self.array=arr
	def display(self):
		counter=0
		for x in self.array:
			print(x[0]+'|'+x[1]+'|'+x[2])
			counter+=1
			if counter!=3:
				print('-----')
	def updatearray(self,location,symbol):
		self.array[location[0]][location[1]]=symbol
	def setsymbols(self,s):
		self.symbols=s
	def checkfree(self,x,y):
		if array[x][y]==' ':
			return True
		return False
	def takeinput(self,turn):
		print("player "+turn+" turn Enter Location")
		while(1):
			x=int(input('Enter x'))
			y=int(input('Enter y'))
			inps=[0,1,2]
			if x in inps and y in inps and self.checkfree(x,y):
				break
			else:
				print("Enter Valid input try again")
		self.updatearray([x,y],turn)
	def checkwin(self,turn):
		if self.array[0][0]==turn and self.array[1][1]==turn and self.array[2][2]==turn:
			print("diagonal")
			return True
		if self.array[0][2]==turn and self.array[1][1]==turn and self.array[2][0]==turn:
			print("diagonal")
			return True
		for x in range(3):
			if self.array[0][x]==turn and self.array[1][x]==turn and self.array[2][x]==turn:
				print("col")
				return True
			if self.array[x][0]==turn and self.array[x][1]==turn and self.array[x][2]==turn:
				print("row")
				return True
		return False
	def isboardfull(self):
		counter=0
		for x in self.array:
			for y in x:
				if y==' ':
					counter+=1
		if counter==0:
			return True
		return False



def switch(turn):
	if turn=='O':
		return'X'
	return 'O'
#main
obj=tictactoe()
obj.setarray(array)
turn='O'
check,check1=0,0
while(check==0 and check1==0):
	obj.takeinput(turn)
	check=obj.checkwin(turn)
	check1=obj.isboardfull()
	turn=switch(turn)
	obj.display()
	
if (check!=0):
	print("Player "+switch(turn)+" wins")
else:
	print("Game Drawn")	

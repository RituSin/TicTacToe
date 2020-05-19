#from IPython.display import clear_output
import random

def display_board(mylist):
	#clear_output()
	print('\n'*100)
	print('    |     |    ')
	print('  '+mylist[7] + ' |  '+mylist[8]+'  | '+mylist[9]+'  ')
	print('    |     |    ')
	print('-----------------')
	print('    |     |    ')
	print('  '+mylist[4] + ' |  '+mylist[5]+'  | '+mylist[6]+'  ')
	print('    |     |    ')
	print('-----------------')
	print('    |     |    ')
	print('  '+mylist[1] + ' |  '+mylist[2]+'  | '+mylist[3]+'  ')
	print('    |     |    ')
	
def player_input():
	marker= False
	while marker not in ['X','O']:
		print('Player 1: Do You want X or O? ')
		marker = input()
	if(marker == 'X'):
		return ('X','O')
	else:
		return ('O','X')	
			
def place_marker(Test_board,marker,position):	
	Test_board[position]= marker
	display_board(Test_board)	

def win_check(board,mark):
	return (
	(board[1] == board[2] == board[3] == mark)or   #row
	(board[4] == board[5] == board[6] == mark)or   #row
	(board[7] == board[8] == board[9] == mark)or   #row
	(board[1] == board[4] == board[7] == mark)or   #column
	(board[2] == board[5] == board[8] == mark)or   #column
	(board[3] == board[6] == board[9] == mark)or   #column
	(board[7] == board[5] == board[3] == mark)or   #dig
	(board[1] == board[5] == board[9] == mark)   #dig
	)	
	
def choose_first():
	flip = random.randint(0,1)
	if(flip == 0):
		return 'Player 1'
	else:
		return 'Player 2'


#if space in the board is freely available
def space_check(board,position):
	return board[position] == ' ' 
	
#if the board full return true
def full_board_check(board):
	for i in range(1,10):
		if(space_check(board,i)):
			return False
		
	return True	
	
#Player's move	
def player_choice(board,turn):
	pos = 0
	while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board,pos):
		pos = int(input(turn + ' choose num between 1-9: '))
	return pos	
			
#ask player if they want to play again
def reply():
	return input('want to play again? select Yes otherwise No : ')	== 'Yes'	


#while loop to keep running the game
print('Welcome to Tic Tac Toe\n')

while True:
	#Play the game.

	##Set everything up-> board<choose marker<whose first
	the_board = [' ']*10
	Player1marker, Player2marker = player_input()
	turn = choose_first()
	
	print(turn + ' Goes first!!!\n')
	PlayGame = input('Ready to play? y or n: ')
	if(PlayGame == 'y'):
		GameON = True
	else:
		GameON = False
		
	#Game play
	while GameON:
		if turn == 'Player 1':
			##Player one turn
			
			#show the board
			display_board(the_board)
			
			#choose a position
			pos = player_choice(the_board,turn)
			
			#place the marker on the position
			place_marker(the_board,Player1marker,pos)
			
			#check if they won
			if win_check(the_board,Player1marker):
				display_board(the_board)
				print(turn + ' wins\n')
				GameON = False
			else:
				#or check if there is  a tie			
				if(full_board_check(the_board)):
					display_board(the_board)
					print('Tie Game\n')
					break
				else:
					#no tie and no win ? then next player's turn
					turn = 'Player 2'				 
		else:
			## Player Two turn
			
			#show the board
			display_board(the_board)
			
			#choose a position
			pos = player_choice(the_board,turn)
			
			#place the marker on the position
			place_marker(the_board,Player2marker,pos)
			
			#check if they won
			if win_check(the_board,Player2marker):
				display_board(the_board)
				print(turn + ' wins\n')
				GameON = False
			else:
				#or check if there is  a tie			
				if(full_board_check(the_board)):
					display_board(the_board)
					print('Tie Game\n')
					break
				else:
					#no tie and no win ? then next player's turn
					turn = 'Player 1'	
		
	if(not reply()):
		break
					
	
		
		

	
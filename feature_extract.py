#empty 0 white 1 black 2
# AAAAA
def five(board, i, j, stone):
	own = 0
	other = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	#horizental direction
	if 4 <= j <= 14 & board[i][j-4:j+1] = [own,own,own,own,empty]:
		return True
	if 3 <= j <= 13 & board[i][j-3:j+2] = [own,own,own,empty,own]:
		return True
	if 2 <= j <= 12 & board[i][j-2:j+3] = [own,own,empty,own,own]:
		return True
	if 1 <= j <= 11 & board[i][j-1:j+4] = [own,empty,own,own,own]:
		return True
	if 0 <= j <= 10 & board[i][j:j+5] = [empty,own,own,own,own]:
		return True

	#vertical direction
	if 4 <= i <= 14 & board[i-4:i+1][j] = [own,own,own,own,empty]:
		return True
	if 3 <= i <= 13 & board[i-3:i+2][j] = [own,own,own,empty,own]:
		return True
	if 2 <= i <= 12 & board[i-2:i+3][j] = [own,own,empty,own,own]:
		return True
	if 1 <= i <= 11 & board[i-1:i+4][j] = [own,empty,own,own,own]:
		return True
	if 0 <= i <= 10 & board[i:i+5][j] = [empty,own,own,own,own]:
		return True

	#left oblique direction
	if 4 <= i <= 14 & 4 <= j <= 14 & [board[i-4][j-4], board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j]] == [own,own,own,own,empty]:
		return True
	if 3 <= i <= 13 & 3 <= j <= 13 & [board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1]] == [own,own,own,empty,own]:
		return True
	if 2 <= i <= 12 & 2 <= j <= 12 & [board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2]] == [own,own,empty,own,own]:
		return True
	if 1 <= i <= 11 & 1 <= j <= 11 & [board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3]] == [own,empty,own,own,own]:
		return True
	if 0 <= i <= 10 & 0 <= j <= 10 & [board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3], board[i+4][j+4]] == [empty,own,own,own,own]:
		return True

	#right oblique direction
	if 0 <= i <= 10 & 4 <= j <= 14 & [board[i][j], board[i+1][j-1], board[i+2][j-2], board[i+3][j-3], board[i+4][j-4]] == [empty,own,own,own,own]:
		return True
	if 1 <= i <= 11 & 3 <= j <= 13 & [board[i-1][j+1], board[i][j], board[i+1][j-1], board[i+2][j-2], board[i+3][j-3]] == [own,empty,own,own,own]:
		return True
	if 2 <= i <= 12 & 2 <= j <= 12 & [board[i-2][j+2], board[i-1][j+1], board[i][j], board[i+1][j-1], board[i+2][j-2]] == [own,own,empty,own,own]:
		return True
	if 3 <= i <= 13 & 1 <= j <= 11 & [board[i-3][j+3], board[i-2][j+2], board[i-1][j+1], board[i][j], board[i+1][j-1]] == [own,own,own,empty,own]:
		return True
	if 4 <= i <= 14 & 0 <= j <= 10 & [board[i-4][j+4], board[i-3][j+3], board[i-2][j+2], board[i-1][j+1], board[i][j]] == [own,own,own,own,empty]:
		return True

	return False

# EAAAAE
def liveFour(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	#horizontal direction
	if 4 <= j <= 13 & board[i][j-4:j+2] == [empty,own,own,own,empty,empty]:
		return True
	if 3 <= j <= 12 & board[i][j-3:j+3] == [empty,own,own,empty,own,empty]:
		return True
	if 2 <= j <= 11 & board[i][j-2:j+4] == [empty,own,empty,own,own,empty]:
		return True
	if 1 <= j <= 10 & board[i][j-1:j+5] == [empty,empty,own,own,own,empty]:
		return True

	#vertical direction
	if 4 <= i <= 13 & board[i-4:i+2][j] == [empty,own,own,own,empty,empty]:
		return True
	if 3 <= i <= 12 & board[i-3:i+3][j] == [empty,own,own,empty,own,empty]:
		return True
	if 2 <= i <= 11 & board[i-2:i+4][j] == [empty,own,empty,own,own,empty]:
		return True
	if 1 <= i <= 10 & board[i-1:i+5][j] == [empty,empty,own,own,own,empty]:
		return True

	#left oblique direction
	if 1 <= i <= 10 & 1 <= j <= 10 & [board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3], board[i+4][j+4]] == [empty,empty,own,own,own,empty]:
		return True
	if 2 <= i <= 11 & 2 <= j <= 11 & [board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3]] == [empty,own,empty,own,own,empty]:
		return True
	if 3 <= i <= 12 & 3 <= j <= 12 & [board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2]] == [empty,own,own,empty,own,empty]:
		return True
	if 4 <= i <= 13 & 4 <= j <= 13 & [board[i-4][j-4], board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1]] == [empty,own,own,own,empty,empty]:
		return True

	#right oblique direction
	if 1 <= i <= 10 & 4 <= j <= 13 & [board[i-1][j+1], board[i][j], board[i+1][j-1], board[i+2][j-2], board[i+3][j-3], board[i+4][j-4]] == [empty,empty,own,own,own,empty]:
		return True
	if 2 <= i <= 11 & 3 <= j <= 12 & [board[i-2][j+2], board[i-1][j+1], board[i][j], board[i+1][j-1], board[i+2][j-2], board[i+3][j-3]] == [empty,own,empty,own,own,empty]:
		return True
	if 3 <= i <= 12 & 2 <= j <= 11 & [board[i-3][j+3], board[i-2][j+2], board[i-1][j+1], board[i][j], board[i+1][j-1], board[i+2][j-2]] == [empty,own,own,empty,own,empty]:
		return True
	if 4 <= i <= 13 & 1 <= j <= 10 & [board[i-4][j+4], board[i-3][j+3], board[i-2][j+2], board[i-1][j+1], board[i][j], board[i+1][j-1]] == [empty,own,own,own,empty,empty]:
		return True

	return False

def four_horizental(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if j == 4 & (board[i][j-4:j+1] == [own,own,own,empty,empty] | board[i][j-4:j+1] == [own,own,empty,own,empty] | board[i][j-4:j+1] == [own,empty,own,own,empty]):
		return True
	if j == 10 & (board[i][j:j+5] == [empty,empty,own,own,own] | board[i][j:j+5] == [empty,own,empty,own,own] | board[i][j:j+5] == [empty,own,own,empty,own]):
		return True

	if j == 3 & board[i][j-3:j+2] == [own,own,own,empty,empty]:
		return True
	if j == 2 & board[i][j-2:j+3] == [own,own,empty,own,empty]:
		return True
	if j == 1 & board[i][j-1:j+4] == [own,empty,own,own,empty]:
		return True
	if j == 0 & board[i][j:j+5] == [empty,own,own,own,empty]:
		return True

	if j == 11 & board[i][j-1:j+4] == [empty,empty,own,own,own]:
		return True
	if j == 12 & board[i][j-2:j+3] == [empty,own,empty,own,own]:
		return True
	if j == 13 & board[i][j-3:j+2] == [empty,own,own,empty,own]:
		return True
	if j == 14 & board[i][j-4:j+1] == [empty,own,own,own,empty]:
		return True

	if 4 <= j <= 13 & (board[i][j-4:j+2] == [other,own,own,own,empty,empty] | board[i][j-4:j+2] == [empty,own,own,own,empty,other]):
		return True
	if 3 <= j <= 12 & (board[i][j-3:j+3] == [other,own,own,empty,own,empty] | board[i][j-3:j+3] == [empty,own,own,empty,own,other]):
		return True
	if 2 <= j <= 11 & (board[i][j-2:j+4] == [other,own,empty,own,own,empty] | board[i][j-2:j+4] == [empty,own,empty,own,own,other]):
		return True
	if 1 <= j <= 10 & (board[i][j-1:j+5] == [other,empty,own,own,own,empty] | board[i][j-1:j+5] == [empty,empty,own,own,own,other]):
		return True

	if 5 <= j <= 14 & (board[i][j-5:j+1] == [other,own,own,own,empty,empty] | board[i][j-5:j+1] == [other,own,own,empty,own,empty] | board[i][j-5:j+1] == [other,own,empty,own,own,empty]):
		return True
	if 0 <= j <= 9 & (board[i][j:j+6] == [empty,empty,own,own,own,other] | board[i][j:j+6] == [empty,own,empty,own,own,other] | board[i][j:j+6] == [empty,own,own,empty,own,other]):
		return True

	return False

def four_vertical(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if i == 4 & (board[i-4:i+1][j] == [own,own,own,empty,empty] | board[i-4:i+1][j] == [own,own,empty,own,empty] | board[i-4:i+1][j] == [own,empty,own,own,empty]):
		return True
	if i == 10 & (board[i:i+5][j] == [empty,empty,own,own,own] | board[i:i+5][j] == [empty,own,empty,own,own] | board[i:i+5][j] == [empty,own,own,empty,own]):
		return True

	if i == 3 & board[i-3:i+2][j] == [own,own,own,empty,empty]:
		return True
	if i == 2 & board[i-2:i+3][j] == [own,own,empty,own,empty]:
		return True
	if i == 1 & board[i-1:i+4][j] == [own,empty,own,own,empty]:
		return True
	if i == 0 & board[i:i+5][j] == [empty,own,own,own,empty]:
		return True

	if i == 11 & board[i-1:i+4][j] == [empty,empty,own,own,own]:
		return True
	if i == 12 & board[i-2:i+3][j] == [empty,own,empty,own,own]:
		return True
	if i == 13 & board[i-3:i+2][j] == [empty,own,own,empty,own]:
		return True
	if i == 14 & board[i-4:i+1][j] == [empty,own,own,own,empty]:
		return True

	if 4 <= i <= 13 & (board[i-4:i+2][j] == [other,own,own,own,empty,empty] | board[i-4:i+2][j] == [empty,own,own,own,empty,other]):
		return True
	if 3 <= i <= 12 & (board[i-3:i+3][j] == [other,own,own,empty,own,empty] | board[i-3:i+3][j] == [empty,own,own,empty,own,other]):
		return True
	if 2 <= i <= 11 & (board[i-2:i+4][j] == [other,own,empty,own,own,empty] | board[i-2:i+4][j] == [empty,own,empty,own,own,other]):
		return True
	if 1 <= i <= 10 & (board[i-1:i+5][j] == [other,empty,own,own,own,empty] | board[i-1:i+5][j] == [empty,empty,own,own,own,other]):
		return True

	if 5 <= i <= 14 & (board[i-5:i+1][j] == [other,own,own,own,empty,empty] | board[i-5:i+1][j] == [other,own,own,empty,own,empty] | board[i-5:i+1][j] == [other,own,empty,own,own,empty]):
		return True
	if 0 <= i <= 9 & (board[i:i+6][j] == [empty,empty,own,own,own,other] | board[i:i+6][j] == [empty,own,empty,own,own,other] | board[i:i+6][j] == [empty,own,own,empty,own,other]):
		return True

	return False

def four_left_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if i == 4 & j == 4:
		temp_list = [board[i-4][j-4], board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j]]
		if temp_list == [own,own,own,empty,empty] | temp_list == [own,own,empty,own,empty] | temp_list == [own,empty,own,own,empty] | temp_list == [empty,own,own,own,empty]:
			return True
	if i == 10 & j == 10:
		temp_list = [board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3], board[i+4][j+4]]
		if temp_list == [empty,empty,own,own,own] | temp_list == [empty,own,empty,own,own] | temp_list == [empty,own,own,empty,own] | temp_list == [empty,own,own,own,empty]:
			return True

	if i == 3 & j == 3 & [board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1]] == [own,own,own,empty,empty]:
		return True
	if i == 2 & j == 2 & [board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+1][j+1]] == [own,own,empty,own,empty]:
		return True
	if i == 1 & j == 1 & [board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+1][j+1], board[i+2][j+2]] == [own,empty,own,own,empty]:
		return True
	if i == 0 & j == 0 & [board[i][j], board[i+1][j+1], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3]] == [empty,own,own,own,empty]:
		return True

	if i == 11 & j == 11 & [board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3]] == [empty,empty,own,own,own]:
		return True
	if i == 12 & j == 12 & [board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2]] == [empty,own,empty,own,own]:
		return True
	if i == 13 & j == 13 & [board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1]] == [empty,own,own,empty,own]:
		return True
	if i == 14 & j == 14 & [board[i-4][j-4], board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j]] == [empty,own,own,own,empty]:
		return True

	if 4 <= i <= 13 & 4 <= j <= 13:
		temp_list = [board[i-4][j-4], board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1]]
		if temp_list == [other,own,own,own,empty,empty] | temp_list == [empty,own,own,own,empty,other]:
			return True
	if 3 <= i <= 12 & 3 <= j <= 12:
		temp_list = [board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2]]
		if temp_list == [other,own,own,empty,own,empty] | temp_list == [empty,own,own,empty,own,other]:
			return True
	if 2 <= i <= 11 & 2 <= j <= 11:
		temp_list = [board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3]]
		if temp_list == [other,own,empty,own,own,empty] | temp_list == [empty,own,empty,own,own,other]:
			return True
	if 1 <= i <= 10 & 1 <= j <= 10:
		temp_list = [board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3], board[i+4][j+4]]
		if temp_list == [other,empty,own,own,own,empty] | temp_list == [empty,empty,own,own,own,other]:
			return True

	if 5 <= i <= 14 & 5 <= j <= 14:
		temp_list = [board[i-5][j-5], board[i-4][j-4], board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j]]
		if temp_list == [other,own,own,own,empty,empty] | temp_list == [other,own,own,empty,own,empty] | temp_list == [other,own,empty,own,own,empty]:
			return True
	if 0 <= i <= 9 & 0 <= j <= 9:
		temp_list = [board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3], board[i+4][j+4], board[i+5][j+5]]
		if temp_list == [empty,empty,own,own,own,other] | temp_list == [empty,own,empty,own,own,other] | temp_list == [empty,own,own,empty,own,other]:
			return True

	return False

# BAAAAB or BAAABA or BAABAA or BABAAA 
def sealFour(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	#left direction
	if j >= 4 & board[i][j-4:j+1] == [other,other,other,other,empty]:
		return True
	if j >= 3 & board[i][j-3:j+2] == [other,other,other,empty,other]:
		return True
	if j >= 2 & board[i][j-2:j+3] == [other,other,empty,other,other]:
		return True
	if j >= 1 & board[i][j-1:j+4] == [other,empty,other,other,other]:
		return True

	#right direction
	if j <= 10 & board[i][j:j+5] == [empty,other,other,other,other]:
		return True
	if j <= 11 & board[i][j-1:j+4] == [other,empty,other,other,other]:
		return True
	if j <= 12 & board[i][j-2:j+3] == [other,other,empty,other,other]:
		return True
	if j <= 13 & board[i][j-3:j+2] == [other,other,other,empty,other]:
		return True

	#upward direction
	if i >= 4 & board[i-4:i+1][j] == [other,other,other,other,empty]:
		return True
	if i >= 3 & board[i-3:i+2][j] == [other,other,other,empty,other]:
		return True
	if i >= 2 & board[i-2:i+3][j] == [other,other,empty,other,other]:
		return True
	if i >= 1 & board[i-1:i+4][j] == [other,empty,other,other,other]:
		return True

	#downward direction
	if i <= 10 & board[i:i+5][j] == [empty,other,other,other,other]:
		return True
	if i <= 11 & board[i-1:i+4][j] == [other,empty,other,other,other]:
		return True
	if i <= 12 & board[i-2:i+3][j] == [other,other,empty,other,other]:
		return True
	if i <= 13 & board[i-3:i+2][j] == [other,other,other,empty,other]:
		return True

	#left-up direction
	if i >= 4 & j >= 4 & [board[i-4][j-4], board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j]] == [other,other,other,other,empty]:
		return True
	if i >= 3 & j >= 3 & [board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1]] == [other,other,other,empty,other]:
		return True
	if i >= 2 & j >= 2 & [board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2]] == [other,other,empty,other,other]:
		return True
	if i >= 1 & j >= 1 & [board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3]] == [other,empty,other,other,other]:
		return True

	#right-up direction
	if i >= 4 & j <= 10 & [board[i][j], board[i-1][j+1], board[i-2][j+2], board[i-3][j+3], board[i-4][j+4]] == [empty,other,other,other,other]:
		return True
	if i >= 3 & j <= 11 & [board[i+1][j-1], board[i][j], board[i-1][j+1], board[i-2][j+2], board[i-3][j+3]] == [other,empty,other,other,other]:
		return True
	if i >= 2 & j <= 12 & [board[i+2][j-2], board[i+1][j-1], board[i][j], board[i-1][j+1], board[i-2][j+2]] == [other,other,empty,other,other]:
		return True
	if i >= 1 & j <= 13 & [board[i+3][j-3], board[i+2][j-2], board[i+1][j-1], board[i][j], board[i-1][j+1]] == [other,other,other,empty,other]:
		return True

	#left-down direction
	if i <= 10 & j >= 4 & [board[i][j], board[i+1][j-1], board[i+2][j-2], board[i+3][j-3], board[i+4][j-4]] == [empty,other,other,other,other]:
		return True
	if i <= 11 & j >= 3 & [board[i-1][j+1], board[i][j], board[i+1][j-1], board[i+2][j-2], board[i+3][j-3]] == [other,empty,other,other,other]:
		return True
	if i <= 12 & j >= 2 & [board[i-2][j+2], board[i-1][j+1], board[i][j], board[i+1][j-1], board[i+2][j-2]] == [other,other,empty,other,other]:
		return True
	if i <= 13 & j >= 1 & [board[i-3][j+3], board[i-2][j+2], board[i-1][j+1], board[i][j], board[i+1][j-1]] == [other,other,other,empty,other]:
		return True

	#right-down direction
	if i <= 10 & j <= 10 & [board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3], board[i+4][j+4]] == [empty,other,other,other,other]:
		return True
	if i <= 11 & j <= 11 & [board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3]] == [other,empty,other,other,other]:
		return True
	if i <= 12 & j <= 12 & [board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1], board[i+2][j+2]] == [other,other,empty,other,other]:
		return True
	if i <= 13 & j <= 13 & [board[i-3][j-3], board[i-2][j-2], board[i-1][j-1], board[i][j], board[i+1][j+1]] == [other,other,other,empty,other]:
		return True

	return False

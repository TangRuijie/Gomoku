#empty 0 white 1 black 2
def oblique_list(board, istart, jstart, iend, jend):
	_list = []
	i = istart
	j = jstart
	if istart < iend & jstart < jend:
		while i <= iend:
			_list.append(board[i][j])
			i += 1
			j += 1
	elif istart < iend & jstart > jend:
		while i <= iend:
			_list.append(board[i][j])
			i += 1
			j -= 1
	elif istart > iend & jstart < jend:
		while i >= iend:
			_list.append(board[i][j])
			i -= 1
			j += 1
	else:
		while i >= iend:
			_list.append(board[i][j])
			i -= 1
			j -= 1
	return _list

def five(board, i, j, stone):
	if board[i][j] != 0:
		return False
	own = 0
	other = 0
	empty = 0
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
	if 4 <= i <= 14 & 4 <= j <= 14 & oblique_list(board, i-4, j-4, i, j) == [own,own,own,own,empty]:
		return True
	if 3 <= i <= 13 & 3 <= j <= 13 & oblique_list(board, i-3, j-3, i+1, j+1) == [own,own,own,empty,own]:
		return True
	if 2 <= i <= 12 & 2 <= j <= 12 & oblique_list(board, i-2, j-2, i+2, j+2) == [own,own,empty,own,own]:
		return True
	if 1 <= i <= 11 & 1 <= j <= 11 & oblique_list(board, i-1, j-1, i+3, j+3) == [own,empty,own,own,own]:
		return True
	if 0 <= i <= 10 & 0 <= j <= 10 & oblique_list(board, i, j, i+4, j+4) == [empty,own,own,own,own]:
		return True

	#right oblique direction
	if 0 <= i <= 10 & 4 <= j <= 14 & oblique_list(board, i, j, i+4, j-4) == [empty,own,own,own,own]:
		return True
	if 1 <= i <= 11 & 3 <= j <= 13 & oblique_list(board, i-1, j+1, i+3, j-3) == [own,empty,own,own,own]:
		return True
	if 2 <= i <= 12 & 2 <= j <= 12 & oblique_list(board, i-2, j+2, i+2, j-2) == [own,own,empty,own,own]:
		return True
	if 3 <= i <= 13 & 1 <= j <= 11 & oblique_list(board, i-3, j+3, i+1, j-1) == [own,own,own,empty,own]:
		return True
	if 4 <= i <= 14 & 0 <= j <= 10 & oblique_list(board, i-4, j+4, i, j) == [own,own,own,own,empty]:
		return True

	return False

def live_four(board, i, j, stone):
	if board[i][j] != 0:
		return False
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
	if 1 <= i <= 10 & 1 <= j <= 10 & oblique_list(board, i-1, j-1, i+4, j+4) == [empty,empty,own,own,own,empty]:
		return True
	if 2 <= i <= 11 & 2 <= j <= 11 & oblique_list(board, i-2, j-2, i+3, j+3) == [empty,own,empty,own,own,empty]:
		return True
	if 3 <= i <= 12 & 3 <= j <= 12 & oblique_list(board, i-3, j-3, i+2, j+2) == [empty,own,own,empty,own,empty]:
		return True
	if 4 <= i <= 13 & 4 <= j <= 13 & oblique_list(board, i-4, j-4, i+1, j+1) == [empty,own,own,own,empty,empty]:
		return True

	#right oblique direction
	if 1 <= i <= 10 & 4 <= j <= 13 & oblique_list(board, i-1, j+1, i+4, j-4) == [empty,empty,own,own,own,empty]:
		return True
	if 2 <= i <= 11 & 3 <= j <= 12 & oblique_list(board, i-2, j+2, i+3, j-3) == [empty,own,empty,own,own,empty]:
		return True
	if 3 <= i <= 12 & 2 <= j <= 11 & oblique_list(board, i-3, j+3, i+2, j-2) == [empty,own,own,empty,own,empty]:
		return True
	if 4 <= i <= 13 & 1 <= j <= 10 & oblique_list(board, i-4, j+4, i+1, j-1) == [empty,own,own,own,empty,empty]:
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

	if (i == 4 & 4 <= j <= 14) | (j == 4 & 4 <= i <= 14):
		temp_list = oblique_list(board, i-4, j-4, i, j)
		if temp_list == [own,own,own,empty,empty] | temp_list == [own,own,empty,own,empty] | temp_list == [own,empty,own,own,empty] | temp_list == [empty,own,own,own,empty]:
			return True
	if (i == 10 & 10 >= j >= 0) | (j == 10 & 10 >= i >= 0):
		temp_list = oblique_list(board, i, j, i+4, j+4)
		if temp_list == [empty,empty,own,own,own] | temp_list == [empty,own,empty,own,own] | temp_list == [empty,own,own,empty,own] | temp_list == [empty,own,own,own,empty]:
			return True

	if ((i == 3 & 3 <= j <= 13) | (j == 3 & 3 <= i <= 13)) & oblique_list(board, i-3, j-3, i+1, j+1) == [own,own,own,empty,empty]:
		return True
	if ((i == 2 & 2 <= j <= 12) | (j == 2 & 2 <= i <= 12)) & oblique_list(board, i-2, j-2, i+2, j+2) == [own,own,empty,own,empty]:
		return True
	if ((i == 1 & 1 <= j <= 11) | (j == 1 & 1 <= i <= 11)) & oblique_list(board, i-1, j-1, i+3, j+3) == [own,empty,own,own,empty]:
		return True
	if ((i == 0 & 0 <= j <= 10) | (j == 0 & 0 <= i <= 10)) & oblique_list(board, i, j, i+4, j+4) == [empty,own,own,own,empty]:
		return True

	if ((i == 11 & 11 >= j >= 1) | (j == 11 & 11 >= i >= 1)) & oblique_list(board, i-1, j-1, i+3, j+3) == [empty,empty,own,own,own]:
		return True
	if ((i == 12 & 12 >= j >= 2) | (j == 12 & 12 >= i >= 2)) & oblique_list(board, i-2, j-2, i+2, j+2) == [empty,own,empty,own,own]:
		return True
	if ((i == 13 & 13 >= j >= 3) | (j == 13 & 13 >= i >= 3)) & oblique_list(board, i-3, j-3, i+1, j+1) == [empty,own,own,empty,own]:
		return True
	if ((i == 14 & 14 >= j >= 4) | (j == 14 & 14 >= i >= 4)) & oblique_list(board, i-4, j-4, i, j) == [empty,own,own,own,empty]:
		return True

	if 4 <= i <= 13 & 4 <= j <= 13:
		temp_list = oblique_list(board, i-4, j-4, i+1, j+1)
		if temp_list == [other,own,own,own,empty,empty] | temp_list == [empty,own,own,own,empty,other]:
			return True
	if 3 <= i <= 12 & 3 <= j <= 12:
		temp_list = oblique_list(board, i-3, j-3, i+2, j+2)
		if temp_list == [other,own,own,empty,own,empty] | temp_list == [empty,own,own,empty,own,other]:
			return True
	if 2 <= i <= 11 & 2 <= j <= 11:
		temp_list = oblique_list(board, i-2, j-2, i+3, j+3)
		if temp_list == [other,own,empty,own,own,empty] | temp_list == [empty,own,empty,own,own,other]:
			return True
	if 1 <= i <= 10 & 1 <= j <= 10:
		temp_list = oblique_list(board, i-1, j-1, i+4, j+4)
		if temp_list == [other,empty,own,own,own,empty] | temp_list == [empty,empty,own,own,own,other]:
			return True

	if 5 <= i <= 14 & 5 <= j <= 14:
		temp_list = oblique_list(board, i-5, j-5, i, j)
		if temp_list == [other,own,own,own,empty,empty] | temp_list == [other,own,own,empty,own,empty] | temp_list == [other,own,empty,own,own,empty]:
			return True
	if 0 <= i <= 9 & 0 <= j <= 9:
		temp_list = oblique_list(board, i, j, i+5, j+5)
		if temp_list == [empty,empty,own,own,own,other] | temp_list == [empty,own,empty,own,own,other] | temp_list == [empty,own,own,empty,own,other]:
			return True

	return False

def four_right_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if (i == 10 & 4 <= j <= 14) | (j == 4 & 10 >= i >= 0):
		temp_list = oblique_list(board, i, j, i+4, j-4)
		if temp_list == [empty,empty,own,own,own] | temp_list == [empty,own,empty,own,own] | temp_list == [empty,own,own,empty,own]:
			return True
	if (i == 4 & 10 >= j >= 0) | (j == 10 & 4 <= i <= 14):
		temp_list = oblique_list(board, i, j, i-4, j+4)
		if temp_list == [empty,empty,own,own,own] | temp_list == [empty,own,empty,own,own] | temp_list == [empty,own,own,empty,own]:
			return True

	if ((i == 11 & 3 <= j <= 13) | (j == 3 & 11 >= i >= 1)) & oblique_list(board, i-1, j+1, i+3, j-3) == [empty,empty,own,own,own]:
		return True
	if ((i == 12 & 2 <= j <= 12) | (j == 2 & 12 >= i >= 2)) & oblique_list(board, i-2, j+2, i+2, j-2) == [empty,own,empty,own,own]:
		return True
	if ((i == 13 & 1 <= j <= 11) | (j == 1 & 13 >= i >= 3)) & oblique_list(board, i-3, j+3, i+1, j-1) == [empty,own,own,empty,own]:
		return True
	if ((i == 14 & 0 <= j <= 10) | (j == 0 & 14 >= i >= 4)) & oblique_list(board, i-4, j+4, i, j) == [empty,own,own,own,empty]:
		return True

	if ((i == 3 & 11 >= j >= 1) | (j == 11 & 3 <= i <= 13)) & oblique_list(board, i+1, j-1, i-3, j+3) == [empty,empty,own,own,own]:
		return True
	if ((i == 2 & 12 >= j >= 2) | (j == 12 & 2 <= i <= 12)) & oblique_list(board, i+2, j-2, i-2, j+2) == [empty,own,empty,own,own]:
		return True
	if ((i == 1 & 13 >= j >= 3) | (j == 13 & 1 <= i <= 11)) & oblique_list(board, i+3, j-3, i-1, j+1) == [empty,own,own,empty,own]:
		return True
	if ((i == 0 & 14 >= j >= 4) | (j == 14 & 0 <= i <= 10)) & oblique_list(board, i+4, j-4, i, j) == [empty,own,own,own,empty]:
		return True

	if 1 <= i <= 10 & 4 <= j <= 13:
		temp_list = oblique_list(board, i-1, j+1, i+4, j-4)
		if temp_list == [empty,empty,own,own,own,other] | temp_list == [other,empty,own,own,own,empty]:
			return True
	if 2 <= i <= 11 & 3 <= j <= 12:
		temp_list = oblique_list(board, i-2, j+2, i+3, j-3)
		if temp_list == [empty,own,empty,own,own,other] | temp_list == [other,own,empty,own,own,empty]:
			return True
	if 3 <= i <= 12 & 2 <= j <= 11:
		temp_list = oblique_list(board, i-3, j+3, i+2, j-2)
		if temp_list == [empty,own,own,empty,own,other] | temp_list == [other,own,own,empty,own,empty]:
			return True
	if 4 <= i <= 12 & 1 <= j <= 10:
		temp_list = oblique_list(board, i-4, j+4, i+1, j-1)
		if temp_list == [empty,own,own,own,empty,other] | temp_list == [other,own,own,own,empty,empty]:
			return True

	if 0 <= i <= 9 & 5 <= j <= 14:
		temp_list = oblique_list(board, i, j, i+5, j-5)
		if temp_list == [empty,empty,own,own,own,other] | temp_list == [empty,own,empty,own,own,other] | temp_list == [empty,own,own,empty,own,other]:
			return True
	if 5 <= i <= 14 & 0 <= j <= 9:
		temp_list = oblique_list(board, i, j, i-5, j+5)
		if temp_list == [empty,empty,own,own,own,other] | temp_list == [empty,own,empty,own,own,other] | temp_list == [empty,own,own,empty,own,other]:
			return True

	return False

def four(board, i, j, stone):
	if board[i][j] != 0:
		return False
	count = 0
	if four_horizental(board, i, j, stone) == True:
		count += 1
	if four_vertical(board, i, j, stone) == True:
		count += 1
	if four_left_oblique(board, i, j, stone) == True:
		count += 1
	if four_right_oblique(board, i, j, stone) == True:
		count += 1
	if count == 1:
		return True
	else:
		return False

def double_four(board, i, j, stone):
	if board[i][j] != 0:
		return False
	count = 0
	if four_horizental(board, i, j, stone) == True:
		count += 1
	if four_vertical(board, i, j, stone) == True:
		count += 1
	if four_left_oblique(board, i, j, stone) == True:
		count += 1
	if four_right_oblique(board, i, j, stone) == True:
		count += 1
	if count > 1:
		return True
	else:
		return False

def seal_four(board, i, j, stone):
	if board[i][j] != 0:
		return False
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	#horizonal direction
	if j == 4 & board[i][j-4:j+1] == [other,other,other,other,empty]:
		return True
	if j == 3 & board[i][j-3:j+2] == [other,other,other,empty,other]:
		return True
	if j == 2 & board[i][j-2:j+3] == [other,other,empty,other,other]:
		return True
	if j == 1 & board[i][j-1:j+4] == [other,empty,other,other,other]:
		return True
	if j == 10 & board[i][j:j+5] == [empty,other,other,other,other]:
		return True
	if j == 11 & board[i][j-1:j+4] == [other,empty,other,other,other]:
		return True
	if j == 12 & board[i][j-2:j+3] == [other,other,empty,other,other]:
		return True
	if j == 13 & board[i][j-3:j+2] == [other,other,other,empty,other]:
		return True

	if 5 <= j <= 14 & board[i][j-5:j+1] == [own,other,other,other,other,empty]:
		return True
	if 4 <= j <= 13 & board[i][j-4:j+2] == [own,other,other,other,empty,other]:
		return True
	if 3 <= j <= 12 & (board[i][j-3:j+3] == [own,other,other,empty,other,other] | board[i][j-3:j+3] == [other,other,other,empty,other,own]):
		return True
	if 2 <= j <= 11 & (board[i][j-2:j+4] == [own,other,empty,other,other,other] | board[i][j-2:j+4] == [other,other,empty,other,other,own]):
		return True
	if 1 <= j <= 10 & board[i][j-1:j+5] == [other,empty,other,other,other,own]:
		return True
	if 0 <= j <= 9 & board[i][j:j+6] == [empty,other,other,other,other,own]:
		return True

	#vertical direction
	if i == 4 & board[i-4:i+1][j] == [other,other,other,other,empty]:
		return True
	if i == 3 & board[i-3:i+2][j] == [other,other,other,empty,other]:
		return True
	if i == 2 & board[i-2:i+3][j] == [other,other,empty,other,other]:
		return True
	if i == 1 & board[i-1:i+4][j] == [other,empty,other,other,other]:
		return True
	if i == 10 & board[i:i+5][j] == [empty,other,other,other,other]:
		return True
	if i == 11 & board[i-1:i+4][j] == [other,empty,other,other,other]:
		return True
	if i == 12 & board[i-2:i+3][j] == [other,other,empty,other,other]:
		return True
	if i == 13 & board[i-3:i+2][j] == [other,other,other,empty,other]:
		return True

	if 5 <= i <= 14 & board[i-5:i+1][j] == [own,other,other,other,other,empty]:
		return True
	if 4 <= i <= 13 & board[i-4:i+2][j] == [own,other,other,other,empty,other]:
		return True
	if 3 <= i <= 12 & (board[i-3:i+3][j] == [own,other,other,empty,other,other] | board[i-3:i+3][j] == [other,other,other,empty,other,own]):
		return True
	if 2 <= i <= 11 & (board[i-2:i+4][j] == [own,other,empty,other,other,other] | board[i-2:i+4][j] == [other,other,empty,other,other,own]):
		return True
	if 1 <= i <= 10 & board[i-1:i+5][j] == [other,empty,other,other,other,own]:
		return True
	if 0 <= i <= 9 & board[i:i+6][j] == [empty,other,other,other,other,own]:
		return True

	#left oblique direction
	if ((i == 4 & 0 <= j <= 10) | (j == 4 & 0 <= i <= 10)) & oblique_list(board, i, j, i-4, j-4) == [empty,other,other,other,other]:
		return True
	if ((i == 3 & 1 <= j <= 11) | (j == 3 & 1 <= i <= 11)) & oblique_list(board, i+1, j+1, i-3, j-3) == [other,empty,other,other,other]:
		return True
	if ((i == 2 & 2 <= j <= 12) | (j == 2 & 2 <= i <= 12)) & oblique_list(board, i+2, j+2, i-2, j-2) == [other,other,empty,other,other]:
		return True
	if ((i == 1 & 3 <= j <= 13) | (j == 1 & 3 <= i <= 13)) & oblique_list(board, i+3, j+3, i-1, j-1) == [other,other,other,empty,other]:
		return True
	if ((i == 10 & 10 >= j >= 0) | (j == 10 & 10 >= i >= 0)) & oblique_list(board, i, j, i+4, j+4) == [empty,other,other,other,other]:
		return True
	if ((i == 11 & 11 >= j >= 1) | (j == 11 & 11 >= i >= 1)) & oblique_list(board, i-1, j-1, i+3, j+3) == [other,empty,other,other,other]:
		return True
	if ((i == 12 & 12 >= j >= 2) | (j == 12 & 12 >= i >= 2)) & oblique_list(board, i-2, j-2, i+2, j+2) == [other,other,empty,other,other]:
		return True
	if ((i == 13 & 13 >= j >= 3) | (j == 13 & 13 >= i >= 3)) & oblique_list(board, i-3, j-3, i+1, j+1) == [other,other,other,empty,other]:
		return True

	if 5 <= i <= 14 & 5 <= j <= 14 & oblique_list(board, i, j, i-5, j-5) == [empty,other,other,other,other,own]:
		return True
	if 4 <= i <= 13 & 4 <= j <= 13 & oblique_list(board, i+1, j+1, i-4, j-4) == [other,empty,other,other,other,own]:
		return True
	if 3 <= i <= 12 & 3 <= j <= 12:
		temp_list = oblique_list(board, i+2, j+2, i-3, j-3)
		if temp_list == [other,other,empty,other,other,own] | temp_list == [own,other,empty,other,other,other]:
			return True
	if 2 <= i <= 11 & 2 <= j <= 11:
		temp_list = oblique_list(board, i+3, j+3, i-2, j-2)
		if temp_list == [other,other,other,empty,other,own] | temp_list == [own,other,other,empty,other,other]:
			return True
	if 1 <= i <= 10 & 1 <= j <= 10 & oblique_list(board, i+4, j+4, i-1, j-1) == [own,other,other,other,empty,other]:
		return True
	if 0 <= i <= 9 & 0 <= j <= 9 & oblique_list(board, i, j, i+5, j+5) == [empty,other,other,other,other,own]:
		return True

	#right oblique direction
	if ((i == 10 & 4 <= j <= 14) | (j == 4 & 10 >= i >= 0)) & oblique_list(board, i, j, i+4, j-4) == [empty,other,other,other,other]:
		return True
	if ((i == 11 & 3 <= j <= 13) | (j == 3 & 11 >= i >= 1)) & oblique_list(board, i-1, j+1, i+3, j-3) == [other,empty,other,other,other]:
		return True
	if ((i == 12 & 2 <= j <= 12) | (j == 2 & 12 >= i >= 2)) & oblique_list(board, i-2, j+2, i+2, j-2) == [other,other,empty,other,other]:
		return True
	if ((i == 13 & 1 <= j <= 11) | (j == 1 & 13 >= i >= 3)) & oblique_list(board, i-3, j+3, i+1, j-1) == [other,other,other,empty,other]:
		return True
	if ((i == 4 & 10 >= j >= 0) | (j == 10 & 4 <= i <= 14)) & oblique_list(board, i, j, i-4, j+4) == [empty,other,other,other,other]:
		return True
	if ((i == 3 & 11 >= j >= 1) | (j == 11 & 3 <= i <= 13)) & oblique_list(board, i+1, j-1, i-3, j+3) == [other,empty,other,other,other]:
		return True
	if ((i == 2 & 12 >= j >= 2) | (j == 12 & 2 <= i <= 12)) & oblique_list(board, i+2, j-2, i-2, j+2) == [other,other,empty,other,other]:
		return True
	if ((i == 1 & 13 >= j >= 3) | (j == 13 & 1 <= i <= 11)) & oblique_list(board, i+3, j-3, i-1, j+1) == [other,other,other,empty,other]:
		return True

	if 0 <= i <= 9 & 5 <= j <= 14 & oblique_list(board, i, j, i+5, j-5) == [empty,other,other,other,other,own]:
		return True
	if 1 <= i <= 10 & 4 <= j <= 13 & oblique_list(board, i-1, j+1, i+4, j-4) == [other,empty,other,other,other,own]:
		return True
	if 2 <= i <= 11 & 3 <= j <= 12:
		temp_list = oblique_list(board, i-2, j+2, i+3, j-3)
		if temp_list == [other,other,empty,other,other,own] | temp_list == [own,other,empty,other,other,other]:
			return True
	if 3 <= i <= 12 & 2 <= j <= 11:
		temp_list = oblique_list(board, i-3, j+3, i+2, j-2)
		if temp_list == [other,other,other,empty,other,own] | temp_list == [own,other,other,empty,other,other]:
			return True
	if 4 <= i <= 13 & 1 <= j <= 10 & oblique_list(board, i+1, j-1, i-4, j+4) == [other,empty,other,other,other,own]:
		return True
	if 5 <= i <= 14 & 0 <= j <= 9 & oblique_list(board, i, j, i-5, j+5) == [empty,other,other,other,other,own]:
		return True

	return False

def live_three_horizontal(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if 4 <= j <= 13 & (board[i][j-4:j+2] == [empty,empty,own,own,empty,empty] | board[i][j-4:j+2] == [empty,own,own,empty,empty,empty] | board[i][j-4:j+2] == [empty,own,empty,own,empty,empty]):
		return True
	if 3 <= j <= 12 & (board[i][j-3:j+3] == [empty,own,own,empty,empty,empty] | board[i][j-3:j+3] == [empty,empty,own,empty,own,empty] | board[i][j-3:j+3] == [empty,own,empty,empty,own,empty]):
		return True
	if 2 <= j <= 11 & (board[i][j-2:j+4] == [empty,own,empty,own,empty,empty] | board[i][j-2:j+4] == [empty,empty,empty,own,own,empty] | board[i][j-2:j+4] == [empty,own,empty,empty,own,empty]):
		return True
	if 1 <= j <= 10 & (board[i][j-1:j+5] == [empty,empty,own,own,empty,empty] | board[i][j-1:j+5] == [empty,empty,empty,own,own,empty] | board[i][j-1:j+5] == [empty,empty,own,empty,own,empty]):
		return True

	return False

def live_three_vertical(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if 4 <= i <= 13 & (board[i-4:i+2][j] == [empty,empty,own,own,empty,empty] | board[i-4:i+2][j] == [empty,own,own,empty,empty,empty] | board[i-4:i+2][j] == [empty,own,empty,own,empty,empty]):
		return True
	if 3 <= i <= 12 & (board[i-3:i+3][j] == [empty,own,own,empty,empty,empty] | board[i-3:i+3][j] == [empty,empty,own,empty,own,empty] | board[i-3:i+3][j] == [empty,own,empty,empty,own,empty]):
		return True
	if 2 <= i <= 11 & (board[i-2:i+4][j] == [empty,own,empty,own,empty,empty] | board[i-2:i+4][j] == [empty,empty,empty,own,own,empty] | board[i-2:i+4][j] == [empty,own,empty,empty,own,empty]):
		return True
	if 1 <= i <= 10 & (board[i-1:i+5][j] == [empty,empty,own,own,empty,empty] | board[i-1:i+5][j] == [empty,empty,empty,own,own,empty] | board[i-1:i+5][j] == [empty,empty,own,empty,own,empty]):
		return True

	return False

def live_three_left_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if 4 <= i <= 13 & 4 <= j <= 13:
		temp_list = oblique_list(board, i-4, j-4, i+1, j+1)
		if temp_list == [empty,empty,own,own,empty,empty] | temp_list == [empty,own,own,empty,empty,empty] | temp_list == [empty,own,empty,own,empty,empty]:
			return True
	if 3 <= i <= 12 & 3 <= j <= 12:
		temp_list = oblique_list(board, i-3, j-3, i+2, j+2)
		if temp_list == [empty,own,own,empty,empty,empty] | temp_list == [empty,empty,own,empty,own,empty] | temp_list == [empty,own,empty,empty,own,empty]:
			return True
	if 2 <= i <= 11 & 2 <= j <= 11:
		temp_list = oblique_list(board, i-2, j-2, i+3, j+3)
		if temp_list == [empty,own,empty,own,empty,empty] | temp_list == [empty,empty,empty,own,own,empty] | temp_list == [empty,own,empty,empty,own,empty]:
			return True
	if 1 <= i <= 10 & 1 <= j <= 10:
		temp_list = oblique_list(board, i-1, j-1, i+4, j+4)
		if temp_list == [empty,empty,own,own,empty,empty] | temp_list == [empty,empty,empty,own,own,empty] | temp_list == [empty,empty,own,empty,own,empty]:
			return True

	return False

def live_three_right_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if 1 <= i <= 10 & 4 <= j <= 13:
		temp_list = oblique_list(board, i+4, j-4, i-1, j+1)
		if temp_list == [empty,empty,own,own,empty,empty] | temp_list == [empty,own,own,empty,empty,empty] | temp_list == [empty,own,empty,own,empty,empty]:
			return True
	if 2 <= i <= 11 & 3 <= j <= 12:
		temp_list = oblique_list(board, i+3, j-3, i-2, j+2)
		if temp_list == [empty,own,own,empty,empty,empty] | temp_list == [empty,empty,own,empty,own,empty] | temp_list == [empty,own,empty,empty,own,empty]:
			return True
	if 3 <= i <= 12 & 2 <= j <= 11:
		temp_list = oblique_list(board, i+2, j-2, i-3, j+3)
		if temp_list == [empty,own,empty,own,empty,empty] | temp_list == [empty,empty,empty,own,own,empty] | temp_list == [empty,own,empty,empty,own,empty]:
			return True
	if 4 <= i <= 13 & 1 <= j <= 10:
		temp_list = oblique_list(board, i+1, j-1, i-4, j+4)
		if temp_list == [empty,empty,own,own,empty,empty] | temp_list == [empty,empty,empty,own,own,empty] | temp_list == [empty,empty,own,empty,own,empty]:
			return True

	return False

def live_three(board, i, j, stone):
	if board[i][j] != 0:
		return False
	count = 0
	if live_three_horizontal(board, i, j, stone) == True:
		count += 1
	if live_three_vertical(board, i, j, stone) == True:
		count += 1
	if live_three_left_oblique(board, i, j, stone) == True:
		count += 1
	if live_three_right_oblique(board, i, j, stone) == True:
		count += 1

	if count == 1:
		return True
	else:
		return False

def double_live_three(board, i, j, stone):
	if board[i][j] != 0:
		return False
	count = 0
	if live_three_horizontal(board, i, j, stone) == True:
		count += 1
	if live_three_vertical(board, i, j, stone) == True:
		count += 1
	if live_three_left_oblique(board, i, j, stone) == True:
		count += 1
	if live_three_right_oblique(board, i, j, stone) == True:
		count += 1

	if count > 1:
		return True
	else:
		return False

def three_horizontal(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if j == 0:
		temp_list = board[i][j:j+5]
		if temp_list == [empty,own,own,empty,empty] | temp_list == [empty,own,empty,own,empty] | temp_list == [empty,empty,own,own,empty]:
			return True
	if j == 1:
		temp_list = board[i][j-1:j+4]
		if temp_list == [own,empty,own,,empty,empty] | temp_list == [own,empty,empty,own,empty]:
			return True
	if j == 2:
		temp_list = board[i][j-2:j+3]
		if temp_list == [own,own,empty,empty,empty] | temp_list == [own,empty,empty,own,empty]:
			return True
	if j == 3:
		temp_list = board[i][j-3:j+2]
		if temp_list == [own,own,empty,empty,empty] | temp_list == [own,empty,own,empty,empty]:
			return True
	if j == 14:
		temp_list = board[i][j-4:j+1]
		if temp_list == [empty,empty,own,own,empty] | temp_list == [empty,own,empty,own,empty] | temp_list == [empty,own,own,empty,empty]:
			return True
	if j == 13:
		temp_list = board[i][j-3:j+2]
		if temp_list == [empty,empty,own,empty,own] | temp_list == [empty,own,empty,empty,own]:
			return True
	if j == 12:
		temp_list = board[i][j-2:j+3]
		if temp_list == [empty,empty,empty,own,own] | temp_list == [empty,own,empty,empty,own]:
			return True
	if j == 11:
		temp_list = board[i][j-1:j+4]
		if temp_list == [empty,empty,empty,own,own] | temp_list == [empty,empty,own,empty,own]:
			return True

	if 1 <= j <= 10:
		temp_list = board[i][j-1:+5]
		if temp_list == [other,empty,own,own,empty,empty] | temp_list == [other,empty,own,empty,own,empty] | temp_list == [empty,empty,empty,own,own,other] | temp_list == [other,empty,empty,own,own,empty] | temp_list == [empty,empty,own,empty,own,other]:
			return True
	if 2 <= j <= 11:
		temp_list = board[i][j-2:j+4]
		if temp_list == [other,own,empty,own,empty,empty] | temp_list == [empty,empty,empty,own,own,other] | temp_list == [other,own,empty,empty,own,empty] | temp_list == [empty,own,empty,empty,own,other]:
			return True
	if 3 <= j <= 12:
		temp_list = board[i][j-3:j+3]
		if temp_list == [other,own,own,empty,empty,empty] | temp_list == [empty,empty,own,empty,own,other] | temp_list == [empty,own,empty,empty,own,other] | temp_list == [other,own,empty,empty,own,empty]:
			return True
	if 4 <= j <= 13:
		temp_list = board[i][j-4:j+2]
		if temp_list == [empty,empty,own,own,empty,other] | temp_list == [other,own,own,empty,empty,empty] | temp_list == [empty,own,empty,own,empty,other] | temp_list == [other,own,empty,own,empty,empty] | temp_list == [empty,own,own,empty,empty,other]:
			return True

	return False

def three_vertical(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if i == 0:
		temp_list = board[i:i+5][j]
		if temp_list == [empty,own,own,empty,empty] | temp_list == [empty,own,empty,own,empty] | temp_list == [empty,empty,own,own,empty]:
			return True
	if i == 1:
		temp_list = board[i-1:i+4][j]
		if temp_list == [own,empty,own,,empty,empty] | temp_list == [own,empty,empty,own,empty]:
			return True
	if i == 2:
		temp_list = board[i-2:i+3][j]
		if temp_list == [own,own,empty,empty,empty] | temp_list == [own,empty,empty,own,empty]:
			return True
	if i == 3:
		temp_list = board[i-3:i+2][j]
		if temp_list == [own,own,empty,empty,empty] | temp_list == [own,empty,own,empty,empty]:
			return True
	if i == 14:
		temp_list = board[i-4:i+1][j]
		if temp_list == [empty,empty,own,own,empty] | temp_list == [empty,own,empty,own,empty] | temp_list == [empty,own,own,empty,empty]:
			return True
	if i == 13:
		temp_list = board[i-3:i+2][j]
		if temp_list == [empty,empty,own,empty,own] | temp_list == [empty,own,empty,empty,own]:
			return True
	if i == 12:
		temp_list = board[i-2:i+3][j]
		if temp_list == [empty,empty,empty,own,own] | temp_list == [empty,own,empty,empty,own]:
			return True
	if i == 11:
		temp_list = board[i-1:i+4][j]
		if temp_list == [empty,empty,empty,own,own] | temp_list == [empty,empty,own,empty,own]:
			return True

	if 1 <= i <= 10:
		temp_list = board[i-1:i+5][j]
		if temp_list == [other,empty,own,own,empty,empty] | temp_list == [other,empty,own,empty,own,empty] | temp_list == [empty,empty,empty,own,own,other] | temp_list == [other,empty,empty,own,own,empty] | temp_list == [empty,empty,own,empty,own,other]:
			return True
	if 2 <= i <= 11:
		temp_list = board[i-2:i+4][j]
		if temp_list == [other,own,empty,own,empty,empty] | temp_list == [empty,empty,empty,own,own,other] | temp_list == [other,own,empty,empty,own,empty] | temp_list == [empty,own,empty,empty,own,other]:
			return True
	if 3 <= i <= 12:
		temp_list = board[i-3:i+3][j]
		if temp_list == [other,own,own,empty,empty,empty] | temp_list == [empty,empty,own,empty,own,other] | temp_list == [empty,own,empty,empty,own,other] | temp_list == [other,own,empty,empty,own,empty]:
			return True
	if 4 <= i <= 13:
		temp_list = board[i-4:i+2][j]
		if temp_list == [empty,empty,own,own,empty,other] | temp_list == [other,own,own,empty,empty,empty] | temp_list == [empty,own,empty,own,empty,other] | temp_list == [other,own,empty,own,empty,empty] | temp_list == [empty,own,own,empty,empty,other]:
			return True

	return False

def three_left_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if (i == 0 & 0 <= j <= 10) | (j == 0 & 0 <= i <= 10):
		temp_list = oblique_list(board, i, j, i+4, j+4)
		if temp_list == [empty,own,own,empty,empty] | temp_list == [empty,own,empty,own,empty] | temp_list == [empty,empty,own,own,empty]:
			return True
	if (i == 1 & 1 <= j <= 11) | (j == 1 & 1 <= i <= 11):
		temp_list = oblique_list(board, i-1, j-1, i+3, j+3)
		if temp_list == [own,empty,own,,empty,empty] | temp_list == [own,empty,empty,own,empty]:
			return True
	if (i == 2 & 2 <= j <= 12) | (j == 2 & 2 <= i <= 12):
		temp_list = oblique_list(board, i-2, j-2, i+2, j+2)
		if temp_list == [own,own,empty,empty,empty] | temp_list == [own,empty,empty,own,empty]:
			return True
	if (i == 3 & 3 <= j <= 13) | (j == 3 & 3 <= i <= 13):
		temp_list = oblique_list(board, i-3, j-3, i+1, j+1)
		if temp_list == [own,own,empty,empty,empty] | temp_list == [own,empty,own,empty,empty]:
			return True
	if (i == 14 & 14 >= j >= 4) | (j == 14 & 14 >= i >= 4):
		temp_list = oblique_list(board, i-4, j-4, i, j)
		if temp_list == [empty,empty,own,own,empty] | temp_list == [empty,own,empty,own,empty] | temp_list == [empty,own,own,empty,empty]:
			return True
	if (i == 13 & 13 >= j >= 3) | (j == 13 & 13 >= i >= 3):
		temp_list = oblique_list(board, i-3, j-3, i+1, j+1)
		if temp_list == [empty,empty,own,empty,own] | temp_list == [empty,own,empty,empty,own]:
			return True
	if (i == 12 & 12 >= j >= 2) | (j == 12 & 12 >= i >= 2):
		temp_list = oblique_list(board, i-2, j-2, i+2, j+2)
		if temp_list == [empty,empty,empty,own,own] | temp_list == [empty,own,empty,empty,own]:
			return True
	if (i == 11 & 11 >= j >= 1) | (j == 11 & 11 >= i >= 1):
		temp_list = oblique_list(board, i-1, j-1, i+3, j+3)
		if temp_list == [empty,empty,empty,own,own] | temp_list == [empty,empty,own,empty,own]:
			return True

	if 1 <= i <= 10 & 1 <= j <= 10:
		temp_list = oblique_list(board, i-1, j-1, i+4, j+4)
		if temp_list == [other,empty,own,own,empty,empty] | temp_list == [other,empty,own,empty,own,empty] | temp_list == [empty,empty,empty,own,own,other] | temp_list == [other,empty,empty,own,own,empty] | temp_list == [empty,empty,own,empty,own,other]:
			return True
	if 2 <= i <= 11 & 2 <= j <= 11:
		temp_list = oblique_list(board, i-2, j-2, i+3, j+3)
		if temp_list == [other,own,empty,own,empty,empty] | temp_list == [empty,empty,empty,own,own,other] | temp_list == [other,own,empty,empty,own,empty] | temp_list == [empty,own,empty,empty,own,other]:
			return True
	if 3 <= i <= 12 & 3 <= j <= 12:
		temp_list = oblique_list(board, i-3, j-3, i+2, j+2)
		if temp_list == [other,own,own,empty,empty,empty] | temp_list == [empty,empty,own,empty,own,other] | temp_list == [empty,own,empty,empty,own,other] | temp_list == [other,own,empty,empty,own,empty]:
			return True
	if 4 <= i <= 13 & 4 <= j <= 13:
		temp_list = oblique_list(board, i-4, j-4, i+1, j+1)
		if temp_list == [empty,empty,own,own,empty,other] | temp_list == [other,own,own,empty,empty,empty] | temp_list == [empty,own,empty,own,empty,other] | temp_list == [other,own,empty,own,empty,empty] | temp_list == [empty,own,own,empty,empty,other]:
			return True

	return False

def three_right_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if (i == 14 & 0 <= j <= 10) | (j == 0 & 14 >= i >= 4):
		temp_list = oblique_list(board, i, j, i-4, j+4)
		if temp_list == [empty,own,own,empty,empty] | temp_list == [empty,own,empty,own,empty] | temp_list == [empty,empty,own,own,empty]:
			return True
	if (i == 13 & 1 <= j <= 11) | (j == 1 & 13 >= i >= 3):
		temp_list = oblique_list(board, i+1, j-1, i-3, j+3)
		if temp_list == [own,empty,own,,empty,empty] | temp_list == [own,empty,empty,own,empty]:
			return True
	if (i == 12 & 2 <= j <= 12) | (j == 2 & 12 >= i >= 2):
		temp_list = oblique_list(board, i+2, j-2, i-2, j+2)
		if temp_list == [own,own,empty,empty,empty] | temp_list == [own,empty,empty,own,empty]:
			return True
	if (i == 11 & 3 <= j <= 13) | (j == 3 & 11 >= i >= 1):
		temp_list = oblique_list(board, i+3, j-3, i-1, j+1)
		if temp_list == [own,own,empty,empty,empty] | temp_list == [own,empty,own,empty,empty]:
			return True
	if (i == 0 & 14 >= j >= 4) | (j == 14 & 0 <= i <= 10):
		temp_list = oblique_list(board, i+4, j-4, i, j)
		if temp_list == [empty,empty,own,own,empty] | temp_list == [empty,own,empty,own,empty] | temp_list == [empty,own,own,empty,empty]:
			return True
	if (i == 1 & 13 >= j >= 3) | (j == 13 & 1 <= i <= 11):
		temp_list = oblique_list(board, i+3, j-3, i-1, j+1)
		if temp_list == [empty,empty,own,empty,own] | temp_list == [empty,own,empty,empty,own]:
			return True
	if (i == 2 & 12 >= j >= 2) | (j == 12 & 2 <= i <= 12):
		temp_list = oblique_list(board, i+2, j-2, i-2, j+2)
		if temp_list == [empty,empty,empty,own,own] | temp_list == [empty,own,empty,empty,own]:
			return True
	if (i == 3 & 11 >= j >= 1) | (j == 11 & 3 <= i <= 13):
		temp_list = oblique_list(board, i+1, j-1, i-3, j+3)
		if temp_list == [empty,empty,empty,own,own] | temp_list == [empty,empty,own,empty,own]:
			return True

	if 4 <= i <= 13 & 1 <= j <= 10:
		temp_list = oblique_list(board, i+1, j-1, i-4, j+4)
		if temp_list == [other,empty,own,own,empty,empty] | temp_list == [other,empty,own,empty,own,empty] | temp_list == [empty,empty,empty,own,own,other] | temp_list == [other,empty,empty,own,own,empty] | temp_list == [empty,empty,own,empty,own,other]:
			return True
	if 3 <= i <= 12 & 2 <= j <= 11:
		temp_list = oblique_list(board, i+2, j-2, i-3, j+3)
		if temp_list == [other,own,empty,own,empty,empty] | temp_list == [empty,empty,empty,own,own,other] | temp_list == [other,own,empty,empty,own,empty] | temp_list == [empty,own,empty,empty,own,other]:
			return True
	if 2 <= i <= 11 & 3 <= j <= 12:
		temp_list = oblique_list(board, i+3, j-3, i-2, j+2)
		if temp_list == [other,own,own,empty,empty,empty] | temp_list == [empty,empty,own,empty,own,other] | temp_list == [empty,own,empty,empty,own,other] | temp_list == [other,own,empty,empty,own,empty]:
			return True
	if 1 <= i <= 10 & 4 <= j <= 13:
		temp_list = oblique_list(board, i+4, j-4, i-1, j+1)
		if temp_list == [empty,empty,own,own,empty,other] | temp_list == [other,own,own,empty,empty,empty] | temp_list == [empty,own,empty,own,empty,other] | temp_list == [other,own,empty,own,empty,empty] | temp_list == [empty,own,own,empty,empty,other]:
			return True

	return False

def three(board, i, j, stone):
	if board[i][j] != 0:
		return False
	count = 0
	if three_horizontal(board, i, j, stone) == True:
		count += 1
	if three_vertical(board, i, j, stone) == True:
		count += 1
	if three_left_oblique(board, i, j, stone) == True:
		count += 1
	if three_right_oblique(board, i, j, stone) == True:
		count += 1

	if count == 1:
		return True
	else:
		return False

def double_three(board, i, j, stone):
	if board[i][j] != 0:
		return False
	count = 0
	if three_horizontal(board, i, j, stone) == True:
		count += 1
	if three_vertical(board, i, j, stone) == True:
		count += 1
	if three_left_oblique(board, i, j, stone) == True:
		count += 1
	if three_right_oblique(board, i, j, stone) == True:
		count += 1

	if count > 1:
		return True
	else:
		return False

def seal_live_three_horizontal(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if 0 <= j <= 10:
		temp_list = board[i][j:j+5]
		if temp_list == [empty,other,other,other,empty]:
			return True
	if 4 <= j <= 14:
		temp_list = board[i][j-4:j+1]
		if temp_list == [empty,other,other,other,empty]:
			return True

	if 0 <= j <= 9:
		temp_list = board[i][j:j+6]
		if temp_list == [empty,other,other,empty,other,empty] | temp_list == [empty,other,empty,other,other,empty]:
			return True
	if 2 <= j <= 11:
		temp_list = board[i][j-2:j+4]
		if temp_list == [empty,other,empty,other,other,empty]:
			return True
	if 3 <= j <= 12:
		temp_list = board[i][j-3:j+3]
		if temp_list == [empty,other,other,empty,other,empty]:
			return True
	if 5 <= j <= 14:
		temp_list = board[i][j-5:j+1]
		if temp_list == [empty,other,empty,other,other,empty]:
			return True

	return False

def seal_live_three_vertical(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if 0 <= i <= 10:
		temp_list = board[i:i+5][j]
		if temp_list == [empty,other,other,other,empty]:
			return True
	if 4 <= i <= 14:
		temp_list = board[i-4:i+1][j]
		if temp_list == [empty,other,other,other,empty]:
			return True

	if 0 <= i <= 9:
		temp_list = board[i:i+6][j]
		if temp_list == [empty,other,other,empty,other,empty] | temp_list == [empty,other,empty,other,other,empty]:
			return True
	if 2 <= i <= 11:
		temp_list = board[i-2:i+4][j]
		if temp_list == [empty,other,empty,other,other,empty]:
			return True
	if 3 <= i <= 12:
		temp_list = board[i-3:i+3][j]
		if temp_list == [empty,other,other,empty,other,empty]:
			return True
	if 5 <= i <= 14:
		temp_list = board[i-5:i+1][j]
		if temp_list == [empty,other,empty,other,other,empty]:
			return True

	return False

def seal_live_three_left_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if 0 <= i <= 10 & 0 <= j <= 10:
		temp_list = oblique_list(board, i, j, i+4, j+4)
		if temp_list == [empty,other,other,other,empty]:
			return True
	if 4 <= i <= 14 & 4 <= j <= 14:
		temp_list = oblique_list(board, i-4, j-4, i, j)
		if temp_list == [empty,other,other,other,empty]:
			return True

	if 0 <= i <= 9 & 0 <= j <= 9:
		temp_list = oblique_list(board, i, j, i+5, j+5)
		if temp_list == [empty,other,other,empty,other,empty] | temp_list == [empty,other,empty,other,other,empty]:
			return True
	if 2 <= i <= 11 & 2 <= j <= 11:
		temp_list = oblique_list(board, i-2, j-2, i+3, j+3)
		if temp_list == [empty,other,empty,other,other,empty]:
			return True
	if 3 <= i <= 12 & 3 <= j <= 12:
		temp_list = oblique_list(board, i-3, j-3, i+2, j+2)
		if temp_list == [empty,other,other,empty,other,empty]:
			return True
	if 5 <= i <= 14 & 5 <= j <= 14:
		temp_list = oblique_list(board, i-5, j-5, i, j)
		if temp_list == [empty,other,empty,other,other,empty]:
			return True

	return False

def seal_live_three_right_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if 4 <= i <= 14 & 0 <= j <= 10:
		temp_list = oblique_list(board, i, j, i-4, j+4)
		if temp_list == [empty,other,other,other,empty]:
			return True
	if 0 <= i <= 10 & 4 <= j <= 14:
		temp_list = oblique_list(board, i+4, j-4, i, j)
		if temp_list == [empty,other,other,other,empty]:
			return True

	if 5 <= i <= 14 & 0 <= j <= 9:
		temp_list = oblique_list(board, i, j, i-5, j+5)
		if temp_list == [empty,other,other,empty,other,empty] | temp_list == [empty,other,empty,other,other,empty]:
			return True
	if 3 <= i <= 12 & 2 <= j <= 11:
		temp_list = oblique_list(board, i+2, j-2, i-3, j+3)
		if temp_list == [empty,other,empty,other,other,empty]:
			return True
	if 2 <= i <= 11 & 3 <= j <= 12:
		temp_list = oblique_list(board, i+3, j-3, i-2, j+2)
		if temp_list == [empty,other,other,empty,other,empty]:
			return True
	if 0 <= i <= 9 & 5 <= j <= 14:
		temp_list = oblique_list(board, i+5, j-5, i, j)
		if temp_list == [empty,other,empty,other,other,empty]:
			return True

	return False

def seal_live_three(board, i, j, stone):
	if board[i][j] != 0:
		return False
	count = 0
	if seal_live_three_horizontal(board, i, j, stone) == True:
		count += 1
	if seal_live_three_vertical(board, i, j, stone) == True:
		count += 1
	if seal_live_three_left_oblique(board, i, j, stone) == True:
		count += 1
	if seal_live_three_right_oblique(board, i, j, stone) == True:
		count += 1

	if count == 1:
		return True
	else:
		return False

def seal_double_live_three(board, i, j, stone):
	if board[i][j] != 0:
		return False
	count = 0
	if seal_live_three_horizontal(board, i, j, stone) == True:
		count += 1
	if seal_live_three_vertical(board, i, j, stone) == True:
		count += 1
	if seal_live_three_left_oblique(board, i, j, stone) == True:
		count += 1
	if seal_live_three_right_oblique(board, i, j, stone) == True:
		count += 1

	if count > 1:
		return True
	else:
		return False

def seal_three_horizontal(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if j == 1:
		temp_list = board[i][j-1:j+4]
		if temp_list == [other,empty,other,other,empty]:
			return True
	if j == 2:
		temp_list = board[i][j-2:j+3]
		if temp_list == [other,other,empty,other,empty]:
			return True
	if j == 3:
		temp_list = board[i][j-3:j+2]
		if temp_list == [other,other,other,empty,empty]:
			return True
	if j == 4:
		temp_list = board[i][j-4:j+1]
		if temp_list == [other,other,empty,other,empty] | temp_list == [other,empty,other,other,empty] | temp_list == [other,other,other,empty,empty]:
			return True
	if j == 10:
		temp_list = board[i][j:j+5]
		if temp_list == [empty,other,empty,other,other] | temp_list == [empty,other,other,empty,other] | temp_list == [empty,empty,other,other,other]:
			return True
	if j == 11:
		temp_list = board[i][j-1:j+4]
		if temp_list == [empty,empty,other,other,other]:
			return True
	if j == 12:
		temp_list = board[i][j-2:j+3]
		if temp_list == [empty,other,empty,other,other]:
			return True
	if j == 13:
		temp_list = board[i][j-3:j+2]
		if temp_list == [empty,other,other,empty,other]:
			return True

	if 0 <= j <= 9:
		temp_list = board[i][j:j+6]
		if temp_list == [empty,empty,other,other,other,own] | temp_list == [empty,other,empty,other,other,own] | temp_list == [empty,other,other,empty,other,own]:
			return True
	if 1 <= j <= 10:
		temp_list = board[i][j-1:j+5]
		if temp_list == [empty,empty,other,other,other,own]:
			return True
	if 2 <= j <= 11:
		temp_list = board[i][j-2:j+4]
		if temp_list == [own,other,empty,other,other,empty] | temp_list == [empty,other,empty,other,other,own]:
			return True
	if 3 <= j <= 12:
		temp_list = board[i][j-3:j+3]
		if temp_list == [own,other,other,empty,other,empty] | temp_list == [empty,other,other,empty,other,own]:
			return True
	if 4 <= j <= 13:
		temp_list = board[i][j-4:j+2]
		if temp_list == [own,other,other,other,empty,empty]:
			return True
	if 5 <= j <= 14:
		temp_list = board[i][j-5:j+1]
		if temp_list == [own,other,other,other,empty,empty] | temp_list == [own,other,other,empty,other,empty] | temp_list == [own,other,empty,other,other,empty]:
			return True

	return False

def seal_three_vertical(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if i == 1:
		temp_list = board[i-1:i+4][j]
		if temp_list == [other,empty,other,other,empty]:
			return True
	if i == 2:
		temp_list = board[i-2:i+3][j]
		if temp_list == [other,other,empty,other,empty]:
			return True
	if i == 3:
		temp_list = board[i-3:i+2][j]
		if temp_list == [other,other,other,empty,empty]:
			return True
	if i == 4:
		temp_list = board[i-4:i+1][j]
		if temp_list == [other,other,empty,other,empty] | temp_list == [other,empty,other,other,empty] | temp_list == [other,other,other,empty,empty]:
			return True
	if i == 10:
		temp_list = board[i:i+5][j]
		if temp_list == [empty,other,empty,other,other] | temp_list == [empty,other,other,empty,other] | temp_list == [empty,empty,other,other,other]:
			return True
	if i == 11:
		temp_list = board[i-1:i+4][j]
		if temp_list == [empty,empty,other,other,other]:
			return True
	if i == 12:
		temp_list = board[i-2:i+3][j]
		if temp_list == [empty,other,empty,other,other]:
			return True
	if i == 13:
		temp_list = board[i-3:i+2][j]
		if temp_list == [empty,other,other,empty,other]:
			return True

	if 0 <= i <= 9:
		temp_list = board[i:i+6][j]
		if temp_list == [empty,empty,other,other,other,own] | temp_list == [empty,other,empty,other,other,own] | temp_list == [empty,other,other,empty,other,own]:
			return True
	if 1 <= i <= 10:
		temp_list = board[i-1:i+5][j]
		if temp_list == [empty,empty,other,other,other,own]:
			return True
	if 2 <= i <= 11:
		temp_list = board[i-2:i+4][j]
		if temp_list == [own,other,empty,other,other,empty] | temp_list == [empty,other,empty,other,other,own]:
			return True
	if 3 <= i <= 12:
		temp_list = board[i-3:i+3][j]
		if temp_list == [own,other,other,empty,other,empty] | temp_list == [empty,other,other,empty,other,own]:
			return True
	if 4 <= i <= 13:
		temp_list = board[i-4:i+2][j]
		if temp_list == [own,other,other,other,empty,empty]:
			return True
	if 5 <= i <= 14:
		temp_list = board[i-5:i+1][j]
		if temp_list == [own,other,other,other,empty,empty] | temp_list == [own,other,other,empty,other,empty] | temp_list == [own,other,empty,other,other,empty]:
			return True

	return False

def seal_three_left_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if (i == 1 & 1 <= j <= 11) | (j == 1 & 1 <= i <= 11):
		temp_list = oblique_list(board, i-1, j-1, i+3, j+3)
		if temp_list == [other,empty,other,other,empty]:
			return True
	if (i == 2 & 2 <= j <= 12) | (j == 2 & 2 <= i <= 12):
		temp_list = oblique_list(board, i-2, j-2, i+2, j+2)
		if temp_list == [other,other,empty,other,empty]:
			return True
	if (i == 3 & 3 <= j <= 13) | (j == 3 & 3 <= i <= 13):
		temp_list = oblique_list(board, i-3, j-3, i+1, j+1)
		if temp_list == [other,other,other,empty,empty]:
			return True
	if (i == 4 & 4 <= j <= 14) | (j == 4 & 4 <= i <= 14):
		temp_list = oblique_list(board, i-4, j-4, i, j)
		if temp_list == [other,other,empty,other,empty] | temp_list == [other,empty,other,other,empty] | temp_list == [other,other,other,empty,empty]:
			return True
	if (i == 10 & 0 <= j <= 10) | (j == 10 & 0 <= i <= 10):
		temp_list = oblique_list(board, i, j, i+4, j+4)
		if temp_list == [empty,other,empty,other,other] | temp_list == [empty,other,other,empty,other] | temp_list == [empty,empty,other,other,other]:
			return True
	if (i == 11 & 1 <= j <= 11) | (j == 11 & 1 <= i <= 11):
		temp_list = oblique_list(board, i-1, j-1, i+3, j+3)
		if temp_list == [empty,empty,other,other,other]:
			return True
	if (i == 12 & 2 <= j <= 12) | (j == 12 & 2 <= i <= 12):
		temp_list = oblique_list(board, i-2, j-2, i+2, j+2)
		if temp_list == [empty,other,empty,other,other]:
			return True
	if (i == 13 & 3 <= j <= 13) | (j == 13 & 3 <= i <= 13):
		temp_list = oblique_list(board, i-3, j-3, i+1, j+1)
		if temp_list == [empty,other,other,empty,other]:
			return True

	if 0 <= i <= 9 & 0 <= j <= 9:
		temp_list = oblique_list(board, i, j, i+5, j+5)
		if temp_list == [empty,empty,other,other,other,own] | temp_list == [empty,other,empty,other,other,own] | temp_list == [empty,other,other,empty,other,own]:
			return True
	if 1 <= i <= 10 & 1 <= j <= 10:
		temp_list = oblique_list(board, i-1, j-1, i+4, j+4)
		if temp_list == [empty,empty,other,other,other,own]:
			return True
	if 2 <= i <= 11 & 2 <= j <= 11:
		temp_list = oblique_list(board, i-2, j-2, i+3, j+3)
		if temp_list == [own,other,empty,other,other,empty] | temp_list == [empty,other,empty,other,other,own]:
			return True
	if 3 <= i <= 12 & 3 <= j <= 12:
		temp_list = oblique_list(board, i-3, j-3, i+2, j+2)
		if temp_list == [own,other,other,empty,other,empty] | temp_list == [empty,other,other,empty,other,own]:
			return True
	if 4 <= i <= 13 & 4 <= j <= 13:
		temp_list = oblique_list(board, i-4, j-4, i+1, j+1)
		if temp_list == [own,other,other,other,empty,empty]:
			return True
	if 5 <= i <= 14 & 5 <= j <= 14:
		temp_list = oblique_list(board, i-5, j-5, i, j)
		if temp_list == [own,other,other,other,empty,empty] | temp_list == [own,other,other,empty,other,empty] | temp_list == [own,other,empty,other,other,empty]:
			return True

	return False

def seal_three_right_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1

	if (i == 13 & 1 <= j <= 11) | (j == 1 & 3 <= i <= 13):
		temp_list = oblique_list(board, i+1, j-1, i-3, j+3)
		if temp_list == [other,empty,other,other,empty]:
			return True
	if (i == 12 & 2 <= j <= 12) | (j == 2 & 2 <= i <= 12):
		temp_list = oblique_list(board, i+2, j-2, i-2, j+2)
		if temp_list == [other,other,empty,other,empty]:
			return True
	if (i == 11 & 3 <= j <= 13) | (j == 3 & 1 <= i <= 11):
		temp_list = oblique_list(board, i+3, j-3, i-1, j+1)
		if temp_list == [other,other,other,empty,empty]:
			return True
	if (i == 10 & 4 <= j <= 14) | (j == 4 & 0 <= i <= 10):
		temp_list = oblique_list(board, i+4, j-4, i, j)
		if temp_list == [other,other,empty,other,empty] | temp_list == [other,empty,other,other,empty] | temp_list == [other,other,other,empty,empty]:
			return True
	if (i == 4 & 0 <= j <= 10) | (j == 10 & 4 <= i <= 14):
		temp_list = oblique_list(board, i, j, i-4, j+4)
		if temp_list == [empty,other,empty,other,other] | temp_list == [empty,other,other,empty,other] | temp_list == [empty,empty,other,other,other]:
			return True
	if (i == 3 & 1 <= j <= 11) | (j == 11 & 3 <= i <= 13):
		temp_list = oblique_list(board, i+1, j-1, i-3, j+3)
		if temp_list == [empty,empty,other,other,other]:
			return True
	if (i == 2 & 2 <= j <= 12) | (j == 12 & 2 <= i <= 12):
		temp_list = oblique_list(board, i+2, j-2, i-2, j+2)
		if temp_list == [empty,other,empty,other,other]:
			return True
	if (i == 1 & 3 <= j <= 13) | (j == 13 & 1 <= i <= 11):
		temp_list = oblique_list(board, i+3, j-3, i-1, j+1)
		if temp_list == [empty,other,other,empty,other]:
			return True

	if 5 <= i <= 14 & 0 <= j <= 9:
		temp_list = oblique_list(board, i, j, i-5, j+5)
		if temp_list == [empty,empty,other,other,other,own] | temp_list == [empty,other,empty,other,other,own] | temp_list == [empty,other,other,empty,other,own]:
			return True
	if 4 <= i <= 13 & 1 <= j <= 10:
		temp_list = oblique_list(board, i+1, j-1, i-4, j+4)
		if temp_list == [empty,empty,other,other,other,own]:
			return True
	if 3 <= i <= 12 & 2 <= j <= 11:
		temp_list = oblique_list(board, i+2, j-2, i-3, j+3)
		if temp_list == [own,other,empty,other,other,empty] | temp_list == [empty,other,empty,other,other,own]:
			return True
	if 2 <= i <= 11 & 3 <= j <= 12:
		temp_list = oblique_list(board, i+3, j-3, i-2, j+2)
		if temp_list == [own,other,other,empty,other,empty] | temp_list == [empty,other,other,empty,other,own]:
			return True
	if 1 <= i <= 10 & 4 <= j <= 13:
		temp_list = oblique_list(board, i+4, j-4, i-1, j+1)
		if temp_list == [own,other,other,other,empty,empty]:
			return True
	if 0 <= i <= 9 & 5 <= j <= 14:
		temp_list = oblique_list(board, i+5, j-5, i, j)
		if temp_list == [own,other,other,other,empty,empty] | temp_list == [own,other,other,empty,other,empty] | temp_list == [own,other,empty,other,other,empty]:
			return True

	return False

def seal_three(board, i, j, stone):
	if board[i][j] != 0:
		return False
	count = 0
	if seal_three_horizontal(board, i, j, stone) == True:
		count += 1
	if seal_three_vertical(board, i, j, stone) == True:
		count += 1
	if seal_three_left_oblique(board, i, j, stone) == True:
		count += 1
	if seal_three_right_oblique(board, i, j, stone) == True:
		count += 1

	if count == 1:
		return True
	else:
		return False

def seal_double_three(board, i, j, stone):
	if board[i][j] != 0:
		return False
	count = 0
	if seal_three_horizontal(board, i, j, stone) == True:
		count += 1
	if seal_three_vertical(board, i, j, stone) == True:
		count += 1
	if seal_three_left_oblique(board, i, j, stone) == True:
		count += 1
	if seal_three_right_oblique(board, i, j, stone) == True:
		count += 1

	if count > 1:
		return True
	else:
		return False

def live_two_horizental(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	if 2 <= j <= 12 & board[i][j-2:j+3] == [empty, empty, empty, own, empty]:
		return True
	if 2 <= j <= 12 & board[i][j-2:j+3] == [empty, own, empty, empty, empty]:
		return True
	if 1 <= j <= 11 & board[i][j-1:j+4] == [empty, empty, empty, own, empty]:
		return True
	if 3 <= j <= 13 & board[i][j-3:j+2] == [empty, own, empty, empty, empty]:
		return True
	if 1 <= j <= 10 & board[i][j-1:j+5] == [empty, empty, empty, empty, own, empty]:
		return True
	if 4 <= j <= 13 & board[i][j-4:j+2] == [empty, own, empty, empty, empty, empty]:
		return True

	return False

def live_two_vertical(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	if 2 <= i <= 12 & board[i-2:i+3][j] == [empty, empty, empty, own, empty]:
		return True
	if 2 <= i <= 12 & board[i-2:i+3][j] == [empty, own, empty, empty, empty]:
		return True
	if 1 <= i <= 11 & board[i-1:i+4][j] == [empty, empty, empty, own, empty]:
		return True
	if 3 <= i <= 13 & board[i-3:i+2][j] == [empty, own, empty, empty, empty]:
		return True
	if 1 <= i <= 10 & board[i-1:i+5][j] == [empty, empty, empty, empty, own, empty]:
		return True
	if 4 <= i <= 13 & board[i-4:i+2][j] == [empty, own, empty, empty, empty, empty]:
		return True

	return False

def live_two_left_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	if 2 <= i <= 12 & 2 <= j <= 12 & oblique_list(board, i-2, j-2, i+2, j+2) == [empty, empty, empty, own, empty]:
		return True
	if 2 <= i <= 12 & 2 <= j <= 12 & oblique_list(board, i-2, j-2, i+2, j+2) == [empty, own, empty, empty, empty]:
		return True
	if 1 <= i <= 11 & 1 <= j <= 11 & oblique_list(board, i-1, j-1, i+3, j+3) == [empty, empty, empty, own, empty]:
		return True
	if 3 <= i <= 13 & 3 <= j <= 13 & oblique_list(board, i-3, j-3, i+1, j+1) == [empty, own, empty, empty, empty]:
		return True
	if 1 <= i <= 10 & 1 <= j <= 10 & oblique_list(board, i-1, j-1, i+4, j+4) == [empty, empty, empty, empty, own, empty]:
		return True
	if 4 <= i <= 13 & 4 <= j <= 13 & oblique_list(board, i-4, j-4, i+1, j+1) == [empty, own, empty, empty, empty, empty]:
		return True

	return False

def live_two_right_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	if 2 <= i <= 12 & 2 <= j <= 12 & oblique_list(board, i-2, j+2, i+2, j-2) = [empty, empty, empty, own, empty]:
		return True
	if 2 <= i <= 12 & 2 <= j <= 12 & oblique_list(board, i-2, j+2, i+2, j-2) = [empty, own, empty, empty, empty]:
		return True
	if 1 <= i <= 11 & 3 <= j <= 13 & oblique_list(board, i-1, j+1, i+3, j-3) = [empty, empty, empty, own, empty]:
		return True
	if 3 <= i <= 13 & 1 <= j <= 11 & oblique_list(board, i-3, j+3, i+1, j-1) = [empty, own, empty, empty, empty]:
		return True
	if 1 <= i <= 10 & 4 <= j <= 13 & oblique_list(board, i-1, j+1, i+4, j-4) = [empty, empty, empty, empty, own, empty]:
		return True
	if 4 <= i <= 13 & 1 <= j <= 10 & oblique_list(board, i-4, j+4, i+1, j-1) = [empty, own, empty, empty, empty, empty]:
		return True

	return False
	
def  single_live_two(board, i, j, stone):
	count = 0
	if live_two_vertical(board, i, j, stone) == True:
		count += 1
	if live_two_horizental(board, i, j, stone) == True:
		count += 1
	if live_two_left_oblique(board, i, j, stone) == True:
		count += 1
	if live_two_right_oblique(board, i, j, stone) == True:
		count += 1
	if count == 1:
		return True
	else:
		return False

def double_live_two(board, i, j, stone):
	count = 0
	if live_two_vertical(board, i, j, stone) == True:
		count += 1
	if live_two_horizental(board, i, j, stone) == True:
		count += 1
	if live_two_left_oblique(board, i, j, stone) == True:
		count += 1
	if live_two_right_oblique(board, i, j, stone) == True:
		count += 1
	if count > 1:
		return True
	else:
		return False

def sleep_two_horizental(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	if 2 <= j <= 11 & board[i][j-2:j+4] == [other, own, empty, empty, empty, empty]:
		return True
	if 3 <= j <= 12 & board[i][j-3:j+3] == [other, own, empty, empty, empty, empty]:
		return True
	if 4 <= j <= 13 & board[i][j-4:j+2] == [other, own, empty, empty, empty, empty]:
		return True
	if 1 <= j <= 10 & board[i][j-1:j+5] == [empty, empty, empty, empty, own, other]:
		return True
	if 2 <= j <= 11 & board[i][j-2:j+4] == [empty, empty, empty, empty, own, other]:
		return True
	if 3 <= j <= 12 & board[i][j-3:j+3] == [empty, empty, empty, empty, own, other]:
		return True
	if (j == 1 | j == 2 | j ==3) & board[i][0:5] == [own, empty, empty, empty, empty]:
		return True
	if (j == 13 | j == 12 | j == 11) & board[i][10:15] = [empty, empty, empty, empty, own]:
		return True	

	return False

def sleep_two_vertical(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	if 2 <= i <= 11 & board[i-2:i+4][j] == [other, own, empty, empty, empty, empty]:
		return True
	if 3 <= i <= 12 & board[i-3:i+3][j] == [other, own, empty, empty, empty, empty]:
		return True
	if 4 <= i <= 13 & board[i-4:i+2][j] == [other, own, empty, empty, empty, empty]:
		return True
	if 1 <= i <= 10 & board[i-1:i+5][j] == [empty, empty, empty, empty, own, other]:
		return True
	if 2 <= i <= 11 & board[i-2:i+4][j] == [empty, empty, empty, empty, own, other]:
		return True
	if 3 <= i <= 12 & board[i-3:i+3][j] == [empty, empty, empty, empty, own, other]:
		return True
	if (i == 1 | i == 2 | i ==3) & board[0:5][j] == [own, empty, empty, empty, empty]:
		return True
	if (i == 13 | i == 12 | i == 11) & board[10:15][j] = [empty, empty, empty, empty, own]:
		return True	

	return False

def sleep_two_left_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	if 2 <= i <= 11 & 2 <= j <= 11 & oblique_list(board, i-2, j-2, i+3, j+3) == [other, own, empty, empty, empty, empty]:
		return True
	if 3 <= i <= 12 & 3 <= j <= 12 & oblique_list(board, i-3, j-3, i+2, j+2) == [other, own, empty, empty, empty, empty]:
		return True
	if 4 <= i <= 13 & 4 <= j <= 13 & oblique_list(board, i-4, j-4, i+1, j+1) == [other, own, empty, empty, empty, empty]:
		return True
	if 1 <= i <= 10 & 1 <= j <= 10 & oblique_list(board, i-1, j-1, i+4, j+4) == [empty, empty, empty, empty, own, other]:
		return True
	if 2 <= i <= 11 & 2 <= j <= 11 & oblique_list(board, i-2, j-2, i+3, j+3) == [empty, empty, empty, empty, own, other]:
		return True
	if 3 <= i <= 12 & 3 <= j <= 12 & oblique_list(board, i-3, j-3, i+2, j+2) == [empty, empty, empty, empty, own, other]:
		return True
	if ((i == 1 & j == 1) | (i == 2 & j == 2) | (i == 3 & j == 3)) & oblique_list(board, 0, 0, 4, 4) == [own, empty, empty, empty, empty]:
		return True
	if ((i == 13 & j == 13) | (i == 12 & j == 12) | (i == 11 & j == 11)) & oblique_list(board, 10, 10, 14, 14) == [empty, empty, empty, empty, own]:
		return True

	return False

def sleep_two_right_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	if 2 <= i <= 11 & 3 <= j <= 12 & oblique_list(board, i-2, j+2, i+3, j-3) == [other, own, empty, empty, empty, empty]:
		return True
	if 3 <= i <= 12 & 2 <= j <= 11 & oblique_list(board, i-3, j+3, i+2, j-2) == [other, own, empty, empty, empty, empty]:
		return True
	if 4 <= i <= 13 & 1 <= j <= 10 & oblique_list(board, i-4, j+4, i+1, j-1) == [other, own, empty, empty, empty, empty]:
		return True
	if 1 <= i <= 10 & 4 <= j <= 13 & oblique_list(board, i-1, j+1, i+4, j-4) == [empty, empty, empty, empty, own, other]:
		return True
	if 2 <= i <= 11 & 3 <= j <= 12 & oblique_list(board, i-2, j+2, i+3, j-3) == [empty, empty, empty, empty, own, other]:
		return True
	if 3 <= i <= 12 & 2 <= j <= 11 & oblique_list(board, i-3, j+3, i+2, j-2) == [empty, empty, empty, empty, own, other]:
		return True
	if ((i == 1 & j == 13) | (i == 2 & j == 12) | (i == 3 & j == 11)) & oblique_list(board, 0, 14, 4, 10) == [own, empty, empty, empty, empty]:
		return True
	if ((i == 13 & j == 13) | (i == 12 & j == 12) | (i == 11 & j == 11)) & oblique_list(board, 10, 4, 14, 0) == [empty, empty, empty, empty, own]:
		return True

	return False

def single_sleep_two(board, i, j, stone):
	count = 0
	if sleep_two_vertical(board, i, j, stone):
		count += 1
	if sleep_two_horizental(board, i, j, stone):
		count += 1
	if sleep_two_left_oblique(board, i, j, stone):
		count += 1
	if sleep_two_right_oblique(board, i, j, stone):
		count += 1
	if count == 1:
		return True
	else:
		return False

def double_sleep_two(board, i, j, stone):
	count = 0
	if sleep_two_vertical(board, i, j, stone):
		count += 1
	if sleep_two_horizental(board, i, j, stone):
		count += 1
	if sleep_two_left_oblique(board, i, j, stone):
		count += 1
	if sleep_two_right_oblique(board, i, j, stone):
		count += 1
	if count > 1:
		return True
	else:
		return False

def seal_livetwo_horizental(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	if 1 <= j <= 10 & board[i][j-1:j+5] == [empty, empty, other, other, empty, empty]:
		return True
	if 4 <= j <= 13 & board[i][j-4:j+2] == [empty, empty, other, other, empty, empty]:
		return True

	if 0 <= j <= 10 & board[i][j:j+5] == [empty, other, empty, other, empty]:
		return True
	if 2 <= j <= 12 & board[i][j-2:j+3] == [empty, other, empty, other, empty]:
		return True
	if 4 <= j <= 14 & board[i][j-4:j] == [empty, other, empty, other, empty]:
		return True

	if 0 <= j <= 9 & board[i][j:j+6] == [empty, other, empty, empty, other, empty]:
		return True
	if 2 <= j <= 11 & board[i][j-2:j+4] == [empty, other, empty, empty, other, empty]:
		return True
	if 3 <= j <= 12 & board[i][j-3:j+3] == [empty, other, empty, empty, other, empty]:
		return True
	if 5 <= j <= 14 & board[i][j-5:j+1] == [empty, other, empty, empty, other, empty]:
		return True

	return False

def seal_livetwo_vertical(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	if 1 <= i <= 10 & board[i-1:i+5][j] == [empty, empty, other, other, empty, empty]:
		return True
	if 4 <= i <= 13 & board[i-4:i+2][j] == [empty, empty, other, other, empty, empty]:
		return True

	if 0 <= i <= 10 & board[i:i+5][j] == [empty, other, empty, other, empty]:
		return True
	if 2 <= i <= 12 & board[i-2:i+3][j] == [empty, other, empty, other, empty]:
		return True
	if 4 <= i <= 14 & board[i-4:i][j] == [empty, other, empty, other, empty]:
		return True

	if 0 <= i <= 9 & board[i:i+6][j] == [empty, other, empty, empty, other, empty]:
		return True
	if 2 <= i <= 11 & board[i-2:i+4][j] == [empty, other, empty, empty, other, empty]:
		return True
	if 3 <= i <= 12 & board[i-3:i+3][j] == [empty, other, empty, empty, other, empty]:
		return True
	if 5 <= i <= 14 & board[i-5:i+1][j] == [empty, other, empty, empty, other, empty]:
		return True

	return False

def seal_livetwo_left_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	if 1 <= i <= 10 & 1 <= j <= 10 & oblique_list(board, i-1, j-1, i+4, j+4) == [empty, empty, other, other, empty, empty]:
		return True
	if 4 <= i <= 13 & 4 <= i <= 13 & oblique_list(board, i-4, j-4, i+1, j+1) == [empty, empty, other, other, empty, empty]:
		return True

	if 0 <= i <= 10 & 0 <= i <= 10 & oblique_list(board, i, j, i+4, j+4) == [empty, other, empty, other, empty]:
		return True
	if 2 <= i <= 12 & 2 <= i <= 12 & oblique_list(board, i-2, j-2, i+2, j+2) == [empty, other, empty, other, empty]:
		return True
	if 4 <= i <= 14 & 4 <= i <= 14 & oblique_list(board, i-4, j-4, i, j) == [empty, other, empty, other, empty]:
		return True

	if 0 <= i <= 9 & 0 <= i <= 9 & oblique_list(board, i, j, i+5, j+5) == [empty, other, empty, empty, other, empty]:
		return True
	if 2 <= i <= 11 & 2 <= i <= 11 & oblique_list(board, i-2, j-2, i+3, j+3) == [empty, other, empty, empty, other, empty]:
		return True
	if 3 <= i <= 12 & 3 <= i <= 12 & oblique_list(board, i-3, j-3, i+2, j+2) == [empty, other, empty, empty, other, empty]:
		return True
	if 5 <= i <= 14 & 5 <= i <= 14 & oblique_list(board, i-5, j-5, i, j) == [empty, other, empty, empty, other, empty]:
		return True

	return False

def seal_livetwo_right_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	if 1 <= i <= 10 & 4 <= j <= 13 & oblique_list(board, i-1, j+1, i+4, j-4) == [empty, empty, other, other, empty, empty]:
		return True
	if 4 <= i <= 13 & 1 <= i <= 11 & oblique_list(board, i-4, j+4, i+1, j-1) == [empty, empty, other, other, empty, empty]:
		return True

	if 0 <= i <= 10 & 4 <= i <= 14 & oblique_list(board, i, j, i+4, j+4) == [empty, other, empty, other, empty]:
		return True
	if 2 <= i <= 12 & 2 <= i <= 12 & oblique_list(board, i-2, j-2, i+2, j+2) == [empty, other, empty, other, empty]:
		return True
	if 4 <= i <= 14 & 0 <= i <= 10 & oblique_list(board, i-4, j-4, i, j) == [empty, other, empty, other, empty]:
		return True

	if 0 <= i <= 9 & 5 <= i <= 14 & oblique_list(board, i, j, i+5, j-5) == [empty, other, empty, empty, other, empty]:
		return True
	if 2 <= i <= 11 & 3 <= i <= 12 & oblique_list(board, i-2, j+2, i+3, j-3) == [empty, other, empty, empty, other, empty]:
		return True
	if 3 <= i <= 12 & 2 <= i <= 11 & oblique_list(board, i-3, j+3, i+2, j-2) == [empty, other, empty, empty, other, empty]:
		return True
	if 5 <= i <= 14 & 0 <= i <= 9 & oblique_list(board, i-5, j+5, i, j) == [empty, other, empty, empty, other, empty]:
		return True

	return False

def single_seal_livetwo(board, i, j, stone):
	count = 0
	if seal_livetwo_horizental(board, i, j, stone):
		count += 1
	if seal_livetwo_vertical(board, i, j, stone):
		count += 1
	if seal_livetwo_left_oblique(board, i, j, stone):
		count += 1
	if seal_livetwo_right_oblique(board, i, j, stone):
		count += 1

	if count == 1:
		return True
	else:
		return False

def double_seal_livetwo(board, i, j, stone):
	count = 0
	if seal_livetwo_horizental(board, i, j, stone):
		count += 1
	if seal_livetwo_vertical(board, i, j, stone):
		count += 1
	if seal_livetwo_left_oblique(board, i, j, stone):
		count += 1
	if seal_livetwo_right_oblique(board, i, j, stone):
		count += 1

	if count > 1:
		return True
	else:
		return False

def seal_sleep_two_horizental(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	#BAAOOO
	if 3 <= j <= 12 & board[i][j-3:j+3] == [own, other, other, empty, empty, empty]:
		return True
	if 4 <= j <= 13 & board[i][j-4:j+2] == [own, other, other, empty, empty, empty]:
		return True
	if 5 <= j <= 14 & board[i][j-5:j+1] == [own, other, other, empty, empty, empty]:
		return True
	#BAOAOO
	if 2 <= j <= 11 & board[i][j-2:j+4] == [own, other, empty, other, empty, empty]:
		return True
	if 4 <= j <= 13 & board[i][j-4:j+2] == [own, other, empty, other, empty, empty]:
		return True
	if 5 <= j <= 14 & board[i][j-5:j+1] == [own, other, empty, other, empty, empty]:
		return True
	#BAOOAO
	if 2 <= j <= 11 & board[i][j-2:j+4] == [own, other, empty, empty, other, empty]:
		return True
	if 3 <= j <= 12 & board[i][j-3:j+3] == [own, other, empty, empty, other, empty]:
		return True
	if 5 <= j <= 14 & board[i][j-5:j+1] == [own, other, empty, empty, other, empty]:

	#OOOAAB
	if 0 <= j <= 9 & board[i][j:j+6] == [empty, empty, empty, other, other, own]:
		return True
	if 1 <= j <= 10 & board[i][j-1:j+5] == [empty, empty, empty, other, other, own]:
		return True
	if 2 <= j <= 11 & board[i][j-2:j+4] == [empty, empty, empty, other, other, own]:
		return True
	#OOAOAB
	if 0 <= j <= 9 & board[i][j:j+6] == [empty, empty, other, empty, other, own]:
		return True
	if 1 <= j <= 10 & board[i][j-1:j+5] == [empty, empty, other, empty, other, own]:
		return True
	if 3 <= j <= 12 & board[i][j-3:j+3] == [empty, empty, other, empty, other, own]:
		return True
	#OAOOAB
	if 0 <= j <= 9 & board[i][j:j+6] == [empty, other, empty, empty, other, own]:
		return True
	if 2 <= j <= 11 & board[i][j-2:j+4] == [empty, other, empty, empty, other, own]:
		return True
	if 3 <= j <= 12 & board[i][j-3:j+3] == [empty, other, empty, empty, other, own]:
		return True

	#|AAOOO	|AOAOO 	|AOOAO
	if 2 <= j <= 4  & board[i][0:5] == [other, other, empty, empty, empty]:
		return True
	if (j == 1 | 3 <= j <= 4) & board[i][0:5] == [other, empty, other, empty, empty]:
		return True
	if (1 <= j <= 2 | j == 4) & board[i][0:5] == [other, empty, empty, other, empty]:
		return True

	#OOOAA|	OOAOA|	OAOOA|
	if 10 <= j <= 12 & board[i][10:15] == [empty, empty, empty, other, other]:
		return True
	if (10 <= j <= 11 | j == 13) & board[i][10:15] == [empty, empty, other, empty, other]:
		return True
	if (j == 10 | 12 <= j <= 13) & board[i][10:15] == [empty, other, empty, empty, other]:
		return True

	return False

def seal_sleep_two_vertical(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	#BAAOOO
	if 3 <= i <= 12 & board[i-3:i+3][j] == [own, other, other, empty, empty, empty]:
		return True
	if 4 <= i <= 13 & board[i-4:i+2][j] == [own, other, other, empty, empty, empty]:
		return True
	if 5 <= i <= 14 & board[i-5:i+1][j] == [own, other, other, empty, empty, empty]:
		return True
	#BAOAOO
	if 2 <= i <= 11 & board[i-2:i+4][j] == [own, other, empty, other, empty, empty]:
		return True
	if 4 <= i <= 13 & board[i-4:i+2][j] == [own, other, empty, other, empty, empty]:
		return True
	if 5 <= i <= 14 & board[i-5:i+1][j] == [own, other, empty, other, empty, empty]:
		return True
	#BAOOAO
	if 2 <= i <= 11 & board[i-2:i+4][j] == [own, other, empty, empty, other, empty]:
		return True
	if 3 <= i <= 12 & board[i-3:i+3][j] == [own, other, empty, empty, other, empty]:
		return True
	if 5 <= i <= 14 & board[i-5:i+1][j] == [own, other, empty, empty, other, empty]:

	#OOOAAB
	if 0 <= i <= 9 & board[i:i+6][j] == [empty, empty, empty, other, other, own]:
		return True
	if 1 <= i <= 10 & board[i-1:i+5][j] == [empty, empty, empty, other, other, own]:
		return True
	if 2 <= i <= 11 & board[i-2:i+4][j] == [empty, empty, empty, other, other, own]:
		return True
	#OOAOAB
	if 0 <= i <= 9 & board[i:i+6][j] == [empty, empty, other, empty, other, own]:
		return True
	if 1 <= i <= 10 & board[i-1:i+5][j] == [empty, empty, other, empty, other, own]:
		return True
	if 3 <= i <= 12 & board[i-3:i+3][j] == [empty, empty, other, empty, other, own]:
		return True
	#OAOOAB
	if 0 <= i <= 9 & board[i:i+6][j] == [empty, other, empty, empty, other, own]:
		return True
	if 2 <= i <= 11 & board[i-2:i+4][j] == [empty, other, empty, empty, other, own]:
		return True
	if 3 <= i <= 12 & board[i-3:i+3][j] == [empty, other, empty, empty, other, own]:
		return True

	#|AAOOO	|AOAOO 	|AOOAO
	if 2 <= i <= 4  & board[0:5][j] == [other, other, empty, empty, empty]:
		return True
	if (i == 1 | 3 <= i <= 4) & board[0:5][j] == [other, empty, other, empty, empty]:
		return True
	if (1 <= i <= 2 | i == 4) & board[0:5][j] == [other, empty, empty, other, empty]:
		return True

	#OOOAA|	OOAOA|	OAOOA|
	if 10 <= i <= 12 & board[10:15][j] == [empty, empty, empty, other, other]:
		return True
	if (10 <= i <= 11 | i == 13) & board[10:15][j] == [empty, empty, other, empty, other]:
		return True
	if (i == 10 | 12 <= i <= 13) & board[10:15][j] == [empty, other, empty, empty, other]:
		return True

def seal_sleep_two_left_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	#BAAOOO
	if 3 <= i <= 12 & 3 <= j <= 12 & oblique_list(board, i-3, j-3, i+2, j+2) == [own, other, other, empty, empty, empty]:
		return True
	if 4 <= i <= 13 & 4 <= j <= 13 & oblique_list(board, i-4, j-4, i+1, j+1) == [own, other, other, empty, empty, empty]:
		return True
	if 5 <= i <= 14 & 5 <= j <= 14 & oblique_list(board, i-5, j-5, i, j) == [own, other, other, empty, empty, empty]:
		return True
	#BAOAOO
	if 2 <= i <= 11 & 2 <= j <= 11 & oblique_list(board, i-2, j-2, i+3, j+3) == [own, other, empty, other, empty, empty]:
		return True
	if 4 <= i <= 13 & 4 <= j <= 13 & oblique_list(board, i-4, j-4, i+2, j+2) == [own, other, empty, other, empty, empty]:
		return True
	if 5 <= i <= 14 & 5 <= j <= 14 & oblique_list(board, i-5, j-5, i, j) == [own, other, empty, other, empty, empty]:
		return True
	#BAOOAO
	if 2 <= i <= 11 & 2 <= j <= 11 & oblique_list(board, i-2, j-2, i+3, j+3) == [own, other, empty, empty, other, empty]:
		return True
	if 3 <= i <= 12 & 3 <= j <= 12 & oblique_list(board, i-3, j-3, i+2, j+2) == [own, other, empty, empty, other, empty]:
		return True
	if 5 <= i <= 14 & 5 <= j <= 14 & oblique_list(board, i-5, j-5, i, j) == [own, other, empty, empty, other, empty]:

	#OOOAAB
	if 0 <= i <= 9 & 0 <= j <= 9 & oblique_list(board, i, j, i+5, j+5) == [empty, empty, empty, other, other, own]:
		return True
	if 1 <= i <= 10 & 1 <= j <= 10 & oblique_list(board, i-1, j-1, i+4, j+4) == [empty, empty, empty, other, other, own]:
		return True
	if 2 <= i <= 11 & 2 <= j <= 11 & oblique_list(board, i-2, j-2, i+3, j+3) == [empty, empty, empty, other, other, own]:
		return True
	#OOAOAB
	if 0 <= i <= 9 & 0 <= j <= 9 & oblique_list(board, i, j, i+5, j+5) == [empty, empty, other, empty, other, own]:
		return True
	if 1 <= i <= 10 & 1 <= j <= 10 & oblique_list(board, i-1, j-1, i+4, j+4) == [empty, empty, other, empty, other, own]:
		return True
	if 3 <= i <= 12 & 3 <= j <= 12 & oblique_list(board, i-3, j-3, i+2, j+2) == [empty, empty, other, empty, other, own]:
		return True
	#OAOOAB
	if 0 <= i <= 9 & 0 <= j <= 9 & oblique_list(board, i, j, i+5, j+5) == [empty, other, empty, empty, other, own]:
		return True
	if 2 <= i <= 11 & 2 <= j <= 11 & oblique_list(board, i-2, j-2, i+3, j+3) == [empty, other, empty, empty, other, own]:
		return True
	if 3 <= i <= 12 & 3 <= j <= 12 & oblique_list(board, i-3, j-3, i+2, j+2) == [empty, other, empty, empty, other, own]:
		return True

	# |AAOOO
	if ((i == 2 & 2 <= j <= 12) | (j == 2 & 2 <= i <= 12)) & oblique_list(board, i-2, j-2, i+2, j+2) == [other, other, empty, empty, empty]:
		return True
	if ((i == 3 & 3 <= j <= 13) | (j == 3 & 3 <= i <= 13)) & oblique_list(board, i-3, j-3, i+1, j+1) == [other, other, empty, empty, empty]:
		return True
	if ((i == 4 & 4 <= j <= 14) | (j ==4 & 4 <= i <= 14)) & oblique_list(board, i-4, j-4, i, j) == [other, other, empty, empty, empty]:
		return True
	# |AOAOO
	if ((i == 1 & 1 <= j <= 11) | (j == 1 & 1 <= i <= 11)) & oblique_list(board, i-1, j-1, i+3, j+3) == [other, empty, other, empty, empty]:
		return True
	if ((i == 3 & 3 <= j <= 13) | (j == 3 & 3 <= i <= 13)) & oblique_list(board, i-3, j-3, i+1, j+1) == [other, empty, other, empty, empty]:
		return True
	if ((i == 4 & 4 <= j <= 14) | (j == 4 & 4 <= i <= 14)) & oblique_list(board, i-4, j-4, i, j) == [other, empty, other, empty, empty]:
		return True
	# |AOOAO
	if ((i == 1 & 1 <= j <= 11) | (j == 1 & 1 <= i <= 11)) & oblique_list(board, i-1, j-1, i+3, j+3) == [other, empty, empty, other, empty]:
		return True
	if ((i == 2 & 2 <= j <= 12) | (j == 2 & 2 <= i <= 12)) & oblique_list(board, i-2, j-2, i+2, j+2) == [other, empty, empty, other, empty]:
		return True
	if ((i == 4 & 4 <= j <= 14) | (j == 4 & 4 <= i <= 14)) & oblique_list(board, i-4, j-4, i, j) == [other, empty, empty, other, empty]:
		return True

	#OOOAA|
	if ((i == 10 & 0 <= j <= 10) | (j == 10 & 0 <= i <= 10)) & oblique_list(board, i, j, i+4, j+4) == [empty, empty, empty, other, other]:
		return True
	if ((i == 11 & 1 <= j <= 11) | (j == 11 & 1 <= i <= 11)) & oblique_list(board, i-1, j-1, i+3, j+3) == [empty, empty, empty, other, other]:
		return True
	if ((i == 12 & 2 <= j <= 12) | (j == 12 & 2 <= j <= 12)) & oblique_list(board, i-2, j-2, i+2, j+2) == [empty, empty, empty, other, other]:
		return True
	#OOAOA|
	if ((i == 10 & 0 <= j <= 10) | (j == 10 & 0 <= i <= 10)) & oblique_list(board, i, j, i+4, j+4) == [empty, empty, other, empty, other]:
		return True
	if ((i == 11 & 1 <= j <= 11) | (j == 11 & 1 <= i <= 11)) & oblique_list(board, i-1, j-1, i+3, j+3) == [empty, empty, other, empty, other]:
		return True
	if ((i == 13 & 3 <= j <= 13) | (j == 13 & 3 <= i <= 13)) & oblique_list(board, i-3, j-3, i+1, j+1) == [empty, empty, other, empty, other]:
		return True
	#OAOOA|
	if ((i == 10 & 0 <= j <= 10) | (j == 10 & 0 <= i <= 10)) & oblique_list(board, i, j, i+4, j+4) == [empty, other, empty, empty, other]:
		return True
	if ((i == 12 & 2 <= j <= 12) | (j == 12 & 2 <= j <= 12)) & oblique_list(board, i-2, j-2, i+2, j+2) == [empty, other, empty, empty, other]:
		return True
	if ((i == 13 & 3 <= j <= 13) | (j == 13 & 3 <= i <= 13)) & oblique_list(board, i-3, j-3, i+1, j+1) == [empty, other, empty, empty, other]:
		return True

	return False

def seal_sleep_two_right_oblique(board, i, j, stone):
	own = 0
	other = 0
	empty = 0
	if stone == 'w':
		own = 1
		other = 2
	else:
		own = 2
		other = 1
	#BAAOOO
	if 3 <= i <= 12 & 2 <= j <= 11 & oblique_list(board, i-3, j+3, i+2, j-2) == [own, other, other, empty, empty, empty]:
		return True
	if 4 <= i <= 13 & 1 <= j <= 10 & oblique_list(board, i-4, j+4, i+1, j-1) == [own, other, other, empty, empty, empty]:
		return True
	if 5 <= i <= 14 & 0 <= j <= 9 & oblique_list(board, i-5, j+5, i, j) == [own, other, other, empty, empty, empty]:
		return True
	#BAOAOO
	if 2 <= i <= 11 & 3 <= j <= 12 & oblique_list(board, i-2, j+2, i+3, j-3) == [own, other, empty, other, empty, empty]:
		return True
	if 4 <= i <= 13 & 1 <= j <= 10 & oblique_list(board, i-4, j+4, i+2, j-2) == [own, other, empty, other, empty, empty]:
		return True
	if 5 <= i <= 14 & 0 <= j <= 9 & oblique_list(board, i-5, j+5, i, j) == [own, other, empty, other, empty, empty]:
		return True
	#BAOOAO
	if 2 <= i <= 11 & 3 <= j <= 12 & oblique_list(board, i-2, j+2, i+3, j-3) == [own, other, empty, empty, other, empty]:
		return True
	if 3 <= i <= 12 & 2 <= j <= 11 & oblique_list(board, i-3, j+3, i+2, j-2) == [own, other, empty, empty, other, empty]:
		return True
	if 5 <= i <= 14 & 0 <= j <= 9 & oblique_list(board, i-5, j+5, i, j) == [own, other, empty, empty, other, empty]:

	#OOOAAB
	if 0 <= i <= 9 & 5 <= j <= 14 & oblique_list(board, i, j, i+5, j-5) == [empty, empty, empty, other, other, own]:
		return True
	if 1 <= i <= 10 & 4 <= j <= 13 & oblique_list(board, i-1, j+1, i+4, j-4) == [empty, empty, empty, other, other, own]:
		return True
	if 2 <= i <= 11 & 3 <= j <= 12 & oblique_list(board, i-2, j+2, i+3, j-3) == [empty, empty, empty, other, other, own]:
		return True
	#OOAOAB
	if 0 <= i <= 9 & 5 <= j <= 14 & oblique_list(board, i, j, i+5, j-5) == [empty, empty, other, empty, other, own]:
		return True
	if 1 <= i <= 10 & 4 <= j <= 13 & oblique_list(board, i-1, j+1, i+4, j-4) == [empty, empty, other, empty, other, own]:
		return True
	if 3 <= i <= 12 & 2 <= j <= 11 & oblique_list(board, i-3, j+3, i+2, j-2) == [empty, empty, other, empty, other, own]:
		return True
	#OAOOAB
	if 0 <= i <= 9 & 5 <= j <= 14 & oblique_list(board, i, j, i+5, j+5) == [empty, other, empty, empty, other, own]:
		return True
	if 2 <= i <= 11 & 3 <= j <= 12 & oblique_list(board, i-2, j+2, i+3, j-3) == [empty, other, empty, empty, other, own]:
		return True
	if 3 <= i <= 12 & 2 <= j <= 11 & oblique_list(board, i-3, j+3, i+2, j-2) == [empty, other, empty, empty, other, own]:
		return True

	# |AAOOO
	if ((i == 2 & 2 <= j <= 12) | (j == 12 & 2 <= i <= 12)) & oblique_list(board, i-2, j+2, i+2, j-2) == [other, other, empty, empty, empty]:
		return True
	if ((i == 3 & 1 <= j <= 11) | (j == 11 & 3 <= i <= 13)) & oblique_list(board, i-3, j+3, i+1, j-1) == [other, other, empty, empty, empty]:
		return True
	if ((i == 4 & 0 <= j <= 10) | (j == 10 & 4 <= i <= 14)) & oblique_list(board, i-4, j+4, i, j) == [other, other, empty, empty, empty]:
		return True
	# |AOAOO
	if ((i == 1 & 3 <= j <= 13) | (j == 13 & 1 <= i <= 11)) & oblique_list(board, i-1, j+1, i+3, j-3) == [other, empty, other, empty, empty]:
		return True
	if ((i == 3 & 1 <= j <= 11) | (j == 11 & 3 <= i <= 13)) & oblique_list(board, i-3, j+3, i+1, j-1) == [other, empty, other, empty, empty]:
		return True
	if ((i == 4 & 0 <= j <= 10) | (j == 10 & 4 <= i <= 14)) & oblique_list(board, i-4, j+4, i, j) == [other, empty, other, empty, empty]:
		return True
	# |AOOAO
	if ((i == 1 & 3 <= j <= 13) | (j == 13 & 1 <= i <= 11)) & oblique_list(board, i-1, j+1, i+3, j-3) == [other, empty, empty, other, empty]:
		return True
	if ((i == 2 & 2 <= j <= 12) | (j == 12 & 2 <= i <= 12)) & oblique_list(board, i-2, j+2, i+2, j-2) == [other, empty, empty, other, empty]:
		return True
	if ((i == 4 & 0 <= j <= 10) | (j == 10 & 4 <= i <= 14)) & oblique_list(board, i-4, j+4, i, j) == [other, empty, empty, other, empty]:
		return True

	#OOOAA|
	if ((i == 10 & 4 <= j <= 14) | (j == 4 & 0 <= i <= 10)) & oblique_list(board, i, j, i+4, j-4) == [empty, empty, empty, other, other]:
		return True
	if ((i == 11 & 3 <= j <= 13) | (j == 3 & 1 <= i <= 11)) & oblique_list(board, i-1, j+1, i+3, j-3) == [empty, empty, empty, other, other]:
		return True
	if ((i == 12 & 2 <= j <= 12) | (j == 2 & 2 <= j <= 12)) & oblique_list(board, i-2, j+2, i+2, j-2) == [empty, empty, empty, other, other]:
		return True
	#OOAOA|
	if ((i == 10 & 4 <= j <= 14) | (j == 4 & 0 <= i <= 10)) & oblique_list(board, i, j, i+4, j-4) == [empty, empty, other, empty, other]:
		return True
	if ((i == 11 & 3 <= j <= 13) | (j == 3 & 1 <= i <= 11)) & oblique_list(board, i-1, j+1, i+3, j-3) == [empty, empty, other, empty, other]:
		return True
	if ((i == 13 & 1 <= j <= 11) | (j == 1 & 3 <= i <= 13)) & oblique_list(board, i-3, j+3, i+1, j-1) == [empty, empty, other, empty, other]:
		return True
	#OAOOA|
	if ((i == 10 & 4 <= j <= 14) | (j == 4 & 0 <= i <= 10)) & oblique_list(board, i, j, i+4, j-4) == [empty, other, empty, empty, other]:
		return True
	if ((i == 12 & 2 <= j <= 12) | (j == 2 & 2 <= j <= 12)) & oblique_list(board, i-2, j+2, i+2, j-2) == [empty, other, empty, empty, other]:
		return True
	if ((i == 13 & 1 <= j <= 11) | (j == 1 & 3 <= i <= 13)) & oblique_list(board, i-3, j+3, i+1, j-1) == [empty, other, empty, empty, other]:
		return True

	return False 

def single_seal_sleep_two(board, i, j, stone):
	count = 0
	if seal_sleep_two_horizental(board, i, j, stone):
		count += 1
	if seal_sleep_two_vertical(board, i, j, stone):
		count += 1
	if seal_sleep_two_left_oblique(board, i, j, stone):
		count += 1
	if seal_sleep_two_right_oblique(board, i, j, stone):
		count += 1
	if count == 1:
		return True
	else:
		return False

def double_seal_sleep_two(board, i, j, stone):
	count = 0
	if seal_sleep_two_horizental(board, i, j, stone):
		count += 1
	if seal_sleep_two_vertical(board, i, j, stone):
		count += 1
	if seal_sleep_two_left_oblique(board, i, j, stone):
		count += 1
	if seal_sleep_two_right_oblique(board, i, j, stone):
		count += 1
	if count > 1:
		return True
	else:
		return False

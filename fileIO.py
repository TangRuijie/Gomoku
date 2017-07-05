def handle_file(No):
	board = []
	row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(0, 15):
		board.append(row)
	filename = 'sgf/list' + str(No) + '.txt'
	fo = open(filename)
	feature_file = open('feature.txt', 'w+')
	choice_file = open('choice.txt', 'w+')
	chess = fo.read()
	# now chess includes the string
	index = 0
	var = 1
	while var == 1:
		index = chess.find('B', index)
		if index == -1:
			break
		i = chess[index+2] - 'a'
		j = chess[index+3] - 'a'
		board[i][j] = 2

		suffix = chess.find('W', index)
		if suffix == -1:
			break
		i = chess[suffix+2] - 'a'
		j = chess[suffix+3] - 'a'
		feature_vector = handle_feature(board, 'w')
		feature_file.write(' '.join(feature_vector))
		feature_file.write('\n')
		choice_file.write(str(i)+' '+str(j))
		choice_file.write('\n')

		index = chess.find('W', index)
		if index == -1:
			break
		i = chess[index+2] - 'a'
		j = chess[index+3] - 'a'
		board[i][j] = 1

		suffix = chess.find('B', index)
		if suffix == -1:
			break
		i = chess[suffix+2] - 'a'
		j = chess[suffix+3] - 'a'
		feature_vector = handle_feature(board, 'b')
		feature_file.write(' '.join(feature_vector))
		feature_file.write('\n')
		choice_file.write(str(i)+' '+str(j))
		choice_file.write('\n')

def handle_feature(board, stone):
	feature_vector = []
	for i in range(0, 15):
		for j in range(0, 15):
			if five(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if live_four(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if four(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if double_four(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if seal_four(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if live_three(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if double_live_three(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if three(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if double_three(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if seal_live_three(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if seal_double_live_three(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if seal_three(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if seal_double_three(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if single_live_two(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if double_live_two(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if single_sleep_two(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if double_sleep_two(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if single_seal_livetwo(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if double_seal_livetwo(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if single_seal_sleeptwo(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)

			if double_seal_sleeptwo(board, i, j, stone):
				feature_vector.append(1)
			else:
				feature_vector.append(0)
	return feature_vector
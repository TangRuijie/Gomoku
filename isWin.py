def isWin(l):
	blank_type = 0
	white_type = 1
	black_type = 2

	for i in range(15):
		cur_type = blank_type
		max_chain = 0
		for j in range(15):
			if (l[i][j] == blank_type):
				cur_type = blank_type
				max_chain = 0
			elif (l[i][j] == cur_type):
				max_chain += 1
				if (max_chain == 5):
					if (j+1 >= 15):
						return cur_type
					elif (l[i][j+1] != cur_type):
						return cur_type
			elif (l[i][j] != cur_type and l[i][j] == black_type):
				cur_type = black_type
				max_chain = 1
			elif (l[i][j] != cur_type and l[i][j] == white_type):
				cur_type = white_type
				max_chain = 1

	for i in range(15):
		cur_type = blank_type
		max_chain = 0
		for j in range(15):
			if (l[j][i] == blank_type):
				cur_type = blank_type
				max_chain = 0
			elif (l[j][i] == cur_type):
				max_chain += 1
				if (max_chain == 5):
					if (j+1 >= 15):
						return cur_type
					elif (l[j+1][i] != cur_type):
						return cur_type
			elif (l[j][i] != cur_type and l[j][i] == black_type):
				cur_type = black_type
				max_chain = 1
			elif (l[j][i] != cur_type and l[j][i] == white_type):
				cur_type = white_type
				max_chain = 1

	# j = i + z
	for z in range(21):
		cur_type = blank_type
		max_chain = 0
		z -= 10
		if (z < 0):
			for j in range(z + 15):
				if (l[j-z][j] == blank_type):
					cur_type = blank_type
					max_chain = 0
				elif (l[j-z][j] == cur_type):
					max_chain += 1
					if (max_chain == 5):
						if ((j+1-z) >= 15):
							return cur_type
						elif(l[j+1-z][j+1] != cur_type):
							return cur_type
				elif (l[j-z][i] != cur_type and l[j-z][i] == black_type):
					cur_type = black_type
					max_chain = 1
				elif (l[j-z][i] != cur_type and l[j-z][i] == white_type):
					cur_type = white_type
					max_chain = 1
		elif (z >= 0):
			for i in range(15 - z):
				if (l[i][i+z] == blank_type):
					cur_type = blank_type
					max_chain = 0
				elif (l[i][i+z] == cur_type):
					max_chain += 1
					if (max_chain == 5):
						if ((i+1+z) >= 15):
							return cur_type
						elif (l[i+1][i+1-z] != cur_type):
							return cur_type
				elif (l[i][i+z] != cur_type and l[i][i+z] == black_type):
					cur_type = black_type
					max_chain = 1
				elif (l[i][i+z] != cur_type and l[i][i+z] == white_type):
					cur_type = white_type
					max_chain = 1

	# j = z - i
	for z in range(21):
		cur_type = blank_type
		max_chain = 0
		z += 4
		if (z < 14):
			for j in range(z + 1):
				if (l[z-j][j] == blank_type):
					cur_type = blank_type
					max_chain = 0
				elif (l[z-j][j] == cur_type):
					max_chain += 1
					if (max_chain == 5):
						if(z-j-1 < 0):
							return cur_type
						elif (l[z-j-1][j+1] != cur_type):
							return cur_type
				elif (l[z-j][j] != cur_type and l[z-j][j] == black_type):
					cur_type = black_type
					max_chain = 1
				elif (l[z-j][j] != cur_type and l[z-j][j] == white_type):
					cur_type = white_type
					max_chain = 1
		elif (z >= 14):
			for i in range(29-z):
				if (l[14-i][z+i-14] == blank_type):
					cur_type = blank_type
					max_chain = 0
				elif (l[14-i][z+i-14] == cur_type):
					max_chain += 1
					if (max_chain == 5):
						if (z+i-13 >= 15):
							return cur_type
						elif (l[13-i][z+i-13] != cur_type):
							return cur_type
				elif (l[14-i][z+i-14] != cur_type and l[14-i][z+i-14] == black_type):
					cur_type = black_type
					max_chain = 1
				elif (l[14-i][z+i-14] != cur_type and l[14-i][z+i-14] == white_type):
					cur_type = white_type
					max_chain = 1
	return blank_type
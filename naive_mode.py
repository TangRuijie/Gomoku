import random
import re
from feature_extract import *

def handle_score(board, i, j, type):
	stone = 0
	score = 0
	if type == 2:
		stone = 'b'
	else:
		stone = 'w'

	if five(board, i, j, stone):
		score += 10000000

	if seal_four(board, i, j, stone):
		score += 1000000

	if live_four(board, i, j, stone):
		score += 500000

	if double_four(board, i, j, stone):
		score += 500000

	if four_and_live_three(board, i, j, stone):
		score += 100000

	if seal_double_three(board, i, j, stone):
		score += 50000

	if seal_three_and_live_two(board, i, j, stone):
		score += 30000

	if seal_live_three(board, i, j, stone):
		score += 20000

	if double_live_three(board, i, j, stone):
		score += 8000

	if live_three(board, i, j, stone):
		score += 5000

	if four(board, i, j, stone):
		score += 4900

	if double_seal_livetwo(board, i, j, stone):
		score += 2000

	if seal_three(board, i, j, stone):
		score += 100

	if single_seal_livetwo(board, i, j, stone):
		score += 90

	if double_three(board, i, j, stone):
		score += 80

	if double_seal_sleep_two(board, i, j, stone):
		score += 70

	if three(board, i, j, stone):
		score += 60

	if single_seal_sleep_two(board, i, j, stone):
		score += 50

	if double_live_two(board, i, j, stone):
		score += 40

	if single_live_two(board, i, j, stone):
		score += 30

	if double_sleep_two(board, i, j, stone):
		score += 20

	if single_sleep_two(board, i, j, stone):
		score += 10

	return score


def naive_mode(l, ai_num):
	blank_type = 0
	fir_step = 0
	sec_step = 1
	thi_step = 2
	fou_step = 3
	fiv_step = 4
	six_step = 5
	sev_step = 6
	eig_step = 7
	point = [[fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step],
	[fir_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,fir_step],
	[fir_step,sec_step,thi_step,thi_step,thi_step,thi_step,thi_step,thi_step,thi_step,thi_step,thi_step,thi_step,thi_step,sec_step,fir_step],
	[fir_step,sec_step,thi_step,fou_step,fou_step,fou_step,fou_step,fou_step,fou_step,fou_step,fou_step,fou_step,thi_step,sec_step,fir_step],
	[fir_step,sec_step,thi_step,fou_step,fiv_step,fiv_step,fiv_step,fiv_step,fiv_step,fiv_step,fiv_step,fou_step,thi_step,sec_step,fir_step],
	[fir_step,sec_step,thi_step,fou_step,fiv_step,six_step,six_step,six_step,six_step,six_step,fiv_step,fou_step,thi_step,sec_step,fir_step],
	[fir_step,sec_step,thi_step,fou_step,fiv_step,six_step,sev_step,sev_step,sev_step,six_step,fiv_step,fou_step,thi_step,sec_step,fir_step],
	[fir_step,sec_step,thi_step,fou_step,fiv_step,six_step,sev_step,eig_step,sev_step,six_step,fiv_step,fou_step,thi_step,sec_step,fir_step],
	[fir_step,sec_step,thi_step,fou_step,fiv_step,six_step,sev_step,sev_step,sev_step,six_step,fiv_step,fou_step,thi_step,sec_step,fir_step],
	[fir_step,sec_step,thi_step,fou_step,fiv_step,six_step,six_step,six_step,six_step,six_step,fiv_step,fou_step,thi_step,sec_step,fir_step],
	[fir_step,sec_step,thi_step,fou_step,fiv_step,fiv_step,fiv_step,fiv_step,fiv_step,fiv_step,fiv_step,fou_step,thi_step,sec_step,fir_step],
	[fir_step,sec_step,thi_step,fou_step,fou_step,fou_step,fou_step,fou_step,fou_step,fou_step,fou_step,fou_step,thi_step,sec_step,fir_step],
	[fir_step,sec_step,thi_step,thi_step,thi_step,thi_step,thi_step,thi_step,thi_step,thi_step,thi_step,thi_step,thi_step,sec_step,fir_step],
	[fir_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,sec_step,fir_step],
	[fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step,fir_step]]

	#score
	for i in range(15):
		for j in range(15):
			if (l[i][j] == blank_type):
				point[i][j] += handle_score(l, i, j, ai_num)
			else:
				point[i][j] -= 10000

	max_point = 0
	max_i = -1
	max_j = -1
	for i in range(15):
		for j in range(15):
			if (point[i][j] > max_point):
				max_point = point[i][j]
				max_i = i
				max_j = j
			elif (point[i][j] == max_point):
				temp_rand = random.randint(0, 1)
				if (temp_rand == 1):
					max_point = point[i][j]
					max_i = i
					max_j = j

	return [max_i, max_j]


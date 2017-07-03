import random
import re


def m_search(l, i, j):
	l[i][j] = 'A'
	add_score = 0
	feature_num = 13
	feature_list = []
	for x in range(feature_num):
		feature_list.append(0)
	model_list = ['EAAAAE', 'AAAAE','AAAEA', 'AAEAA', 'EEAAAEE', 'AAAEE', 'EAEAAE', 'AEEAA', 'AEAEA', 'EEEAAEEE', 'AAEEE', 'EEAEAEE', 'EAEEAE']
	score_list = [300000, 2500, 3000, 2600, 3000, 500, 800, 600, 550, 650, 150, 250, 200]
	# if (x >= 4 and x <= 10 and x >= 4 and x <= 10):
	# 	#-|/\
	# 	str1 = ''.join(l[i][(j-4):(j+5)])
	# 	str2 = ''.join(l[(i-4):(i+5)][j])
	# 	str3_list = []
	# 	str4_list = []
	# 	for x in range(9):
	# 		x -= 4
	# 		str3_list.append(l[i+x][j-x])
	# 		str4_list.append(l[i+x][j+x])
	# 	str3 = ''.join(str3_list)
	# 	str4 = ''.join(str4_list)
	# elif():
	#-|/\
	str1 = ''.join(l[i][:])
	str2 = ''.join(l[:][j])
	str3_list = []
	str4_list = []
	#/
	temp_i = i
	temp_j = j
	while(temp_i < 14 and temp_j > 0):
		temp_i += 1
		temp_j -= 1
	while(temp_i >= 0 and temp_j <= 14):
		str3_list.append(l[temp_i][temp_j])
		temp_i -= 1
		temp_j += 1
	str3 = ''.join(str3_list)
	#\
	temp_i = i
	temp_j = j
	while(temp_i > 0 and temp_j > 0):
		temp_i -= 1
		temp_j -= 1
	while(temp_i <= 14 and temp_j <= 14):
		str4_list.append(l[temp_i][temp_j])
		temp_i += 1
		temp_j += 1
	str4 = ''.join(str4_list)

	#search
	for x in range(feature_num):
		if (re.search(model_list[x], str1)):
			feature_list[x] += 1
		if (re.search(model_list[x], str2)):
			feature_list[x] += 1
		if (re.search(model_list[x], str3)):
			feature_list[x] += 1
		if (re.search(model_list[x], str4)):
			feature_list[x] += 1
		add_score += feature_list[x] * score_list[x]
	return add_score



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

	#change l to l_new
	l_new = []
	for i in range(15):
		l_new.append([])
	for i in range(15):
		for j in range(15):
			if (l[i][j] == blank_type):
				l_new[i].append('E')
			elif (l[i][j] == ai_num):
				l_new[i].append('A')
			else:
				l_new[i].append('B')

	#score
	for i in range(15):
		for j in range(15):
			if (l[i][j] == blank_type):
				point[i][j] += m_search(l_new, i, j)

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


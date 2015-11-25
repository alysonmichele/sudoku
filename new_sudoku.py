# -*- coding: UTF-8 -*-
import pdb, copy
import itertools, collections

def find(target, sets):
    for i,lst in enumerate(sets):
        for j,color in enumerate(lst):
            if color == target:
                return (i)
    return (None, None)


def squares(x,y):
	if 0 <= x <= 2:
		if 0 <= y <= 2:
			for i in range(3):
				for j in range(3):
					square.append(sudoku[i][j])
		if 3 <= y <= 5:
			for i in range(3):
				for j in range(3,6):
					square.append(sudoku[i][j])
		if 6 <= y <= 8:
			for i in range(3):
				for j in range(6,9):
					square.append(sudoku[i][j])
	if 3 <= x <= 5:
		if 0 <= y <= 2:
			for i in range(3,6):
				for j in range(3):
					square.append(sudoku[i][j])
		if 3 <= y <= 5:
			for i in range(3,6):
				for j in range(3,6):
					square.append(sudoku[i][j])
		if 6 <= y <= 8:
			for i in range(3,6):
				for j in range(6,9):
					square.append(sudoku[i][j])
	if 6 <= x <= 8:
		if 0 <= y <= 2:
			for i in range(6,9):
				for j in range(3):
					square.append(sudoku[i][j])
		if 3 <= y <= 5:
			for i in range(6,9):
				for j in range(3,6):
					square.append(sudoku[i][j])
		if 6 <= y <= 8:
			for i in range(6,9):
				for j in range(6,9):
					square.append(sudoku[i][j])
	return square

def pop_columns(sudoku):
	columns=[ [ 0 for i in range(9) ] for j in range(9) ]
	for x in range(9):
		for y in range(9):
			columns[x][y]=sudoku[y][x]
	return columns

# def populate_cols(columns,sudoku):
# 	columns=[ [ 0 for i in range(9) ] for j in range(9) ]
# 	for m in range(9):
# 		for n in range(9):
# 			columns[m][n]=sudoku[n][m]
# 	return columns

rowOne=[7,0,0,3,4,0,0,5,0]
rowTwo=[0,0,5,0,2,0,0,8,0]
rowThree=[0,8,0,0,0,0,0,0,2]
rowFour=[0,0,0,9,5,0,0,0,3]
rowFive=[9,0,0,0,8,0,0,0,1]
rowSix=[5,0,0,0,1,7,0,0,0]
rowSeven=[8,0,0,0,0,0,0,6,0]
rowEight=[0,3,0,0,9,0,2,0,0]
rowNine=[0,9,0,0,6,2,0,0,7]

# rowOne=[3,0,0,1,9,0,0,5,8]
# rowTwo=[9,0,0,8,0,4,0,7,0]
# rowThree=[0,0,7,0,2,0,1,9,0]
# rowFour=[0,7,6,0,0,2,5,0,0]
# rowFive=[0,0,5,0,0,0,3,0,0]
# rowSix=[0,0,9,4,0,0,8,2,0]
# rowSeven=[0,9,8,0,3,0,4,0,0]
# rowEight=[0,1,0,2,0,6,0,0,5]
# rowNine=[4,6,0,0,5,8,0,0,1]

# rowOne=[0,1,0,4,8,0,0,0,0]
# rowTwo=[0,0,0,0,7,0,0,0,2]
# rowThree=[0,3,2,6,9,5,0,0,0]
# rowFour=[1,8,0,0,2,0,0,0,0]
# rowFive=[3,4,0,0,1,0,0,6,8]
# rowSix=[0,0,0,0,6,0,0,4,5]
# rowSeven=[0,0,0,2,4,7,8,3,0]
# rowEight=[7,0,0,0,3,0,0,0,0]
# rowNine=[0,0,0,0,5,6,0,2,0]

# rowOne=[6,3,5,4,0,0,0,0,0]
# rowTwo=[9,0,1,5,0,8,0,7,0]
# rowThree=[7,4,0,0,0,0,0,1,0]
# rowFour=[2,0,0,1,8,0,0,6,0]
# rowFive=[0,8,0,0,4,0,0,9,0]
# rowSix=[0,5,0,0,7,9,0,0,2]
# rowSeven=[0,7,0,0,0,0,0,3,6]
# rowEight=[0,1,0,6,0,2,4,0,7]
# rowNine=[0,0,0,0,0,4,1,8,9]

choices=set([1,2,3,4,5,6,7,8,9])

#start in row one, with the first index and grab all numbers in that row and in that column

sudoku=[rowOne, rowTwo, rowThree, rowFour, rowFive, rowSix, rowSeven, rowEight, rowNine]


columns=pop_columns(sudoku)
second_choice=False
x=0
index=0
total_count=0
trial=[]
#start in row 1
counts=collections.Counter(itertools.chain(*sudoku))
total_zeroes=counts[0]
prev_count=total_zeroes
round_inner=1
round=1
original_sudoku=[]
try_again=False
while total_zeroes > 0:
	#check if count has changed
	if x==9:
		x=0
		total_count=0
	for x in range(9):
		#count how many 0s are in the row
		zero_count=sudoku[x].count(0)
		#reset position to 0
		position=0
		#set row choices to empty list
		row_choices=[]
		no_dupes=set()
		#step through each space to check if it's empty
		y=0
		u=0
		for y in range(9):
			#pdb.set_trace()
			used=[]
			square=[]
			#if it's not empty, put dummy 99 in row_choices to hold index, then go to next space
			if sudoku[x][y] != 0:
				row_choices.append([99])
				y=y+1
			#if it is empty then grab all numbers in the row and in the column and square
			else:
				position=position+1
				#numbers in row
				used.append(sudoku[x])
				#numbers in column
				used.append(columns[y])
				#numbers in square
				#if row is between 0 and 2, then grab first
				square=squares(x,y)
				used.append(square)
				#grab each used number
				no_dupes=used[0]+used[1]+used[2]
				no_dupes=[u for u in no_dupes if u !=0]
				no_dupes=set(no_dupes)
				available=choices-no_dupes
				available=list(available)
				#if there's only one possible number that can go there, then insert it
				if len(available)==1:
					num=available.pop()
					sudoku[x][y]=num
					row_choices.append([num])
					if sudoku[x].count(0)==0:
						y=y+1
				else:
				#if there's more than one, add the possibilities to the row's list of sets
					row_choices.append(available)
					#if this is the last empty space in the row, then check if any numbers can be placed in
					if	position==zero_count:
						#c=Counter(row_choices)
						counter = collections.Counter(itertools.chain(*row_choices))
						for z in choices:
							if counter[z]==1:
							#if number only appears once, then place it where it belongs
								pos=find(z, row_choices)
								sudoku[x][pos]=z
						y=y+1
						counts=collections.Counter(itertools.chain(*sudoku))
						#count how many zeroes are left
						total_zeroes=counts[0]
						if total_zeroes==0:
							print 'SOLVED!'
							break
					else:
						#go to next space 
						y=y+1
			#pdb.set_trace()
			if y==9:
				#at the end of a row, count how many zeroes are left, if it's the same as before, increase round
				counts=collections.Counter(itertools.chain(*sudoku))
				total_zeroes=counts[0]
				#pdb.set_trace()
				if prev_count==total_zeroes:
					round=round+1
				else:
					prev_count=total_zeroes

				if round >=25:
					#pdb.set_trace()
					print 'NO GOOD'
					original_sudoku=copy.deepcopy(sudoku)
					original_columns=copy.deepcopy(columns)
					print round, total_zeroes, prev_count
					first_trial=1
					prev_count=total_zeroes

################### TRIAL ##########################################
					#start at first line, check if it has zeroes
					while total_zeroes > 0:
						#if the first round didn't work then reset and try next number

						if try_again==True:
							try_again=False
							sudoku=copy.deepcopy(original_sudoku)
							columns=copy.deepcopy(original_columns)
							second_choice=True
							first_trial=1
							round_inner=0
							#pdb.set_trace()


						for d in range(9):
							counts=collections.Counter(itertools.chain(*sudoku))
							total_zeroes=counts[0]
							row_choices=[]
							no_dupes=set()
							position=0
							row_zeroes=sudoku[d].count(0)
							#if it has zeroes, collect all available number list
							if row_zeroes!=0:
								#step through each space to check if it's empty
								for c in range(9):
									used=[]
									square=[]
								#if it's not empty, put dummy 99 in row_choices to hold index, then go to next space
									if sudoku[d][c] != 0:
										row_choices.append([99])
										c=c+1
								#if it is empty then grab all numbers in the row and in the column and square
									else:
										position=position+1
										#numbers in row
										used.append(sudoku[d])
										#numbers in column
										used.append(columns[c])
										#numbers in square
										#if row is between 0 and 2, then grab first
										square=squares(d,c)
										#pdb.set_trace()
										#pdb.set_trace()
										used.append(square)
										#grab each used number
										no_dupes=used[0]+used[1]+used[2]
										no_dupes=[u for u in no_dupes if u !=0]
										no_dupes=set(no_dupes)
										available=choices-no_dupes
										available=list(available)
										#if there's only one possible number that can go there, then insert it

										if len(available)==1:
											num=available.pop()
											sudoku[d][c]=num
											row_choices.append([num])
											if sudoku[d].count(0)==0:
												c=c+1
											#create a list of indices that we are trying
											#trial.append([d,c])
										else:
										#if there's more than one, add the possibilities to the row's list of sets
											row_choices.append(available)
											#if this is the last empty space in the row, then check if any numbers can be placed in
											if	position==row_zeroes:
												#find the square with fewest choices
												if first_trial==1:
													first_trial=9
													non_choices=[]
													for z in row_choices:
														if z[0]!=99:
															non_choices.append(z)
													smallest=min(non_choices, key=len)
													if second_choice==False:
														opt=smallest[0]
													else:
														opt=smallest[1]
													placed=find(opt, row_choices)
													sudoku[d][placed]=opt
													c=c+1
													#trial.append[d,c]
												else:
												#c=Counter(row_choices)
													counter = collections.Counter(itertools.chain(*row_choices))
													for z in choices:
														if counter[z]==1:
														#if number only appears once, then place it where it belongs
															pos=find(z, row_choices)
															sudoku[d][pos]=z
															#trial.append[d,c]
													c=c+1
													counts=collections.Counter(itertools.chain(*sudoku))
												#count how many zeroes are left
													total_zeroes=counts[0]
													if total_zeroes==0:
														print 'SOLVED!'
														break
											else:
												#go to next space 
												c=c+1
											#if prev_count==total_zeroes:
											#	round_inner=round_inner+1
											#else:
											#	prev_count=total_zeroes
											#if round_inner > 10:
											#	print trial
											#	exit()
									if c==9:
										pdb.set_trace()

										columns=pop_columns(sudoku)
						#if the row doesn't have zeroes, go to next row
										d=d+1
										counts=collections.Counter(itertools.chain(*sudoku))
										total_zeroes=counts[0]
										if prev_count==total_zeroes:
											round_inner=round_inner+1
										else:
											prev_count=total_zeroes
											print prev_count
											#pdb.set_trace()
											break


										if round_inner>=10:
											#if it gets here, reset all the zeroes 
											d=0
											c=0
											try_again=True
											print prev_count, total_zeroes

############## TRIAL ########################################

					#find space in row that has fewest options
					#select one of the numbers and insert it
					print sudoku
					exit()
				print 'do i get here'
				columns=pop_columns(sudoku)
				x=x+1
				counts=collections.Counter(itertools.chain(*sudoku))
				total_zeroes=counts[0]
				#pdb.set_trace()
				if total_zeroes==0:
					#print sudoku
					print 'SOLVED'
					break



print sudoku, round

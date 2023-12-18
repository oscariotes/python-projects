

# print(f'{row1}\n{row2}\n{row3}\n{row4}')

# Move the using the position column and row
# ex. 23 is column 2 and row 3


# moveSplit = list(move)
# print(moveSplit)



position = input('Where to you want to move? ')

row1 = ['◻️','◻️,','◻️','◻️']
row2 = ['◻️','◻️,','◻️','◻️']
row3 = ['◻️','◻️,','◻️','◻️']
row4 = ['◻️','◻️,','◻️','◻️']

map = [row1, row2, row3, row4]
print(f'{row1}\n{row2}\n{row3}\n{row4}')

horizontal = int(position[0])
vertical = int(position[1])

selectedRow = map[vertical -1]
selectedRow [horizontal -1] = 'X'

print(selectedRow)



#newMap = map[vertical -1][horizontal -1]








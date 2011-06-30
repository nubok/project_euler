spiral_size = 1001

spiral = { }
"""direction:
0: right
1: down
2: left
3: up
"""
direction = 0

row = (spiral_size-1)/2
col = (spiral_size-1)/2

delta_row = [0, 1, 0, -1]
delta_col = [1, 0, -1, 0]

current_len = 1
current_number = 1

while current_number != (spiral_size*spiral_size+1):
    for j in range(current_len):
        spiral[(row, col)] = current_number
        current_number += 1
        row += delta_row[direction]
        col += delta_col[direction]

    if direction % 2 == 1:
        current_len += 1

    direction = (direction + 1) % 4

result = -1 # The number in the middle is 1 - it is counted twice

for i in range(spiral_size):
    result += spiral[(i, i)]
    result += spiral[(spiral_size-1-i, i)]

print result

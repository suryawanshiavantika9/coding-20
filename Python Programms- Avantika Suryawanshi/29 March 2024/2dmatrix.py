
Matrix = [[0, 0, 0, 1],
          [0, 1, 1, 1],
          [1, 1, 1, 1],
          [0, 0, 0, 0]]

max_count, row = 0, -1

for i in range(4):

    count = 0
    for j in range(4):
        if Matrix[i][j] == 1:
            count += 1

    if count > max_count:
        max_count = count
        row = i

print("Row with maximum 1's is :", row+1)
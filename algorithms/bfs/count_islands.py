"""
This is a bfs-version of counting-islands problem in dfs section.
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands.
An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3

Example 3:
111000
110000
100001
001101
001100
Answer: 3

Example 4:
110011
001100
000001
111100
Answer: 5
"""


def count_islands(grid, flags):
	# 1
	row = len(grid)
	col = len(grid[0])

	num_islands = 0
	# 2
	visited = [[0] * col for i in range(row)]
	directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	queue = []

	# 3
	for i in range(row):
		flags[0] = True
		# 4
		for j, num in enumerate(grid[i]):
			flags[1] = True
			# 5, 6
			if num == 1 and visited[i][j] != 1:
				flags[2] = True
				visited[i][j] = 1
				queue.append((i, j))
				# 7
				while queue:
					flags[4] = True
					x, y = queue.pop(0)
					# 8
					for k in range(len(directions)):
						flags[5] = True
						nx_x = x + directions[k][0]
						nx_y = y + directions[k][1]
						# 9, 10, 11, 12
						if nx_x >= 0 and nx_y >= 0 and nx_x < row and nx_y < col:
							flags[6] = True
							# 13, 14
							if visited[nx_x][nx_y] != 1 and grid[nx_x][nx_y] == 1:
								flags[8] = True
								queue.append((nx_x, nx_y))
								visited[nx_x][nx_y] = 1
							else:
								flags[9] = True
						else:
							flags[7] = True
				num_islands += 1
			else:
				flags[3] = True

	return num_islands

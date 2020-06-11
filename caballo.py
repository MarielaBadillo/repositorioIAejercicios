import copy

g = [[1,0,1],
	[0,0,0],
	[-1,0,-1]]
	
for i in range(3):
	for j in range(3):
		print(g[i][j], end = ' ')
	print()
print()

m = copy.deepcopy(g)

for e in range(4):
	if g[0][0] != 0:
		m[1][-1] = copy.deepcopy(g[0][0])
		m[0][0] = copy.deepcopy(g[1][-1])
	if g[0][1] != 0:
		m[-1][-1] = copy.deepcopy(g[0][1])
		m[0][1] = copy.deepcopy(g[-1][-1])
	if g[0][-1] != 0:
		m[-1][1] = copy.deepcopy(g[0][-1])
		m[0][-1] = copy.deepcopy(g[-1][1])
	if g[1][0] != 0:
		m[0][-1] = copy.deepcopy(g[1][0])
		m[1][0] = copy.deepcopy(g[0][-1])
	if g[1][-1] != 0:
		m[-1][0] = copy.deepcopy(g[1][-1])
		m[1][-1] = copy.deepcopy(g[-1][0])
	if g[-1][0] != 0:
		m[0][1] = copy.deepcopy(g[-1][0])
		m[-1][0] = copy.deepcopy(g[1][-1])
	if g[-1][1] != 0:
		m[0][0] = copy.deepcopy(g[-1][1])
		m[-1][1] = copy.deepcopy(g[0][0])
	if g[-1][-1] != 0:
		m[1][0] = copy.deepcopy(g[-1][-1])
		m[-1][-1] = copy.deepcopy(g[1][0])
	
	g = copy.deepcopy(m)
	
	for i in range(3):
		for j in range(3):
			print(m[i][j], end = ' ')
		print()
	print()

import math
# This is 2-dimension Leduction Algorithm

def norm(v):
	return int(math.sqrt(v[0]**2 + v[1]**2))

def inner_product(v1, v2):
	return v1[0]*v2[0] + v1[1]*v2[1] 

def solve(v1, v2):
	m = 1	
	while m != 0:
		v1Size = norm(v1)
		v2Size = norm(v2)
		if v2Size < v1Size:
			v1, v2 = v2, v1
		m = inner_product(v1, v2) // (norm(v1)**2)
		if m == 0:
			return [v1, v2]
		v2[1] = v2[1] - m * v1[1]
		v2[0] = v2[0] - m * v1[0]


v1, v2 = [66586820, 65354729], [6513996, 6393464]
ans = (solve(v1, v2))
print(ans)


import numpy as np

np.set_printoptions(suppress=True) # remove exponential notation!

v = np.array([[1, -1, 1], [1, 0, 1], [1, 1, 2]], dtype='float')
def gram_schmidt(v):
	x = np.zeros(v.shape)
	x[0] = v[0]
	for i in range(1,len(x)):
		u = np.zeros(len(x))
		for j in range(i):
			u[j] = np.inner(v[i], x[j]) / (np.linalg.norm(x[j])**2	)
		x[i] = v[i] - sum([u[j] * x[j] for j in range(i)])
	return x
print(gram_schmidt(v))

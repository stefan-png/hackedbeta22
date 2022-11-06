grid = np.ones(shape=(11, 11), dtype = object)
for q in range(0, 11):
    for r in range(0, 11):
        if q + r >= 5 and q + r <= 15:
            grid[q, r] = 0
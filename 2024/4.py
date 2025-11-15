
s = open("./4.in").read().strip()

grid = s.split("\n")
R = len(grid)
C = len(grid[0])

def has_xmas(r, c, dr, dc):
    for i, v in enumerate("XMAS"):
        nr = r + i*dr
        nc = c + i*dc
        if not (0 <= nr < R and 0 <= nc < C):
            return False
        if grid[nr][nc] != v:
            return False
    return True

def has_x_mas(r, c):
    if not (1 <= r < R-1 and 1 <= c < C-1):
        return False
    if grid[r][c] != 'A':
        return False
    diag1 = grid[r+1][c-1] + grid[r-1][c+1]
    diag2 = grid[r-1][c-1] + grid[r+1][c+1]
    return diag1 in ["MS", "SM"] and diag2 in ["MS", "SM"]

p1 = 0
p2 = 0
for r in range(R):
    for c in range(C):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if has_xmas(r, c, dr, dc):
                    p1 += 1
        if has_x_mas(r, c):
            p2 += 1

print(p1)
print(p2)




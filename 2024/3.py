import re

DO = "do()"
DO_NOT = "don't"
MUL = "mul("

p1 = 0
p2 = 0

s = open("./3.in").read().strip()

enable = True
for i in range(len(s)):
	if s[i: i + len(DO)] == DO:
		enable = True
	if s[i: i + len(DO_NOT)] == DO_NOT:
		enable = False
	if s[i: i + len(MUL)] == MUL:
		j = i + 4
		while s[j] != ')':
			j += 1
		if not s[j - 1].isdigit():
			continue
		try:
			x, y = map(int, re.findall("\d+", s[i:j + 1]))
			p1 += x * y
			if enable:
				p2 += x * y
		except:
			pass

print(p1)
print(p2)


import collections


def cal_distance():
    left = []
    right = []
    with open("./2024_d1/input", "r") as f:
        for line in f:
            num1, num2 = map(int, line.strip().split())
            left.append(num1)
            right.append(num2)
    left.sort()
    right.sort()
    total = 0
    for l, r in zip(left, right):
        total += abs(l-r)
    
    print(total)

def cal_similarity_score():
    left = []
    right = collections.defaultdict(int)
    with open("./2024_d1/input", "r") as f:
        for line in f:
            num1, num2 = map(int, line.strip().split())
            left.append(num1)
            right[num2] += 1
    score = 0
    for l in left:
        if l in right:
            score += l * right[l]
    print(score)
    
            

cal_distance()
cal_similarity_score()

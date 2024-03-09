dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

letter = input()
time = 0
for l in letter:
    for idx, ls in enumerate(dial):
        if l in ls:
            time += (idx +3)

print(time)

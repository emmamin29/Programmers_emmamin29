hrs, min = map(int, input().split())
min2 = int(input())

total_minute = min + min2
hrs += total_minute // 60
min = total_minute % 60

if hrs > 23:
    hrs -= 24

print(hrs, min)
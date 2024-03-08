subject = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)

new_list = []
for score in score_list:
    new_list.append(score/max_score * 100)

test_avg = sum(new_list)/subject
print(test_avg)
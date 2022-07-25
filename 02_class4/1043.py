import sys

input = sys.stdin.readline
n, cnt_party = map(int, input().split())
know = set(map(int, input().split()[1:]))  # 진실을 아는사람
party_list = [set(map(int, input().split()[1:])) for _ in range(cnt_party)]
#
# 남은 배열에서 n*n 횟수 만큼 반복
for i in range(len(party_list)):
    j = 0
    while j < len(party_list):
        if know.intersection(party_list[j]):
            know=know.union(party_list[j])
            # 진실을 말하는 파티 참석한 사람들-> 진실아는사람들로
            del party_list[j]
        else:  # 파티를 삭제안했을때만 j++되게
            j += 1
print(len(party_list)) #거짓말을 해도 될 남은 파티수 출력
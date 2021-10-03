# 標準入力を受け付ける。
N = int(input())

# 0~N人ログインしていたユーザーの日数を格納する。
ans = [0] * (N + 1)
query = []
for _ in range(N):
    A, B = map(int, input().split())
    # ログイン開始日を記録する。
    start = A
    # ログイン終了日を記録する。
    end = A + B
    query.append((start, 1))
    query.append((end, -1))

# ログイン開始日 or ログイン終了日を基準にしてソートする。
query.sort()

loginNum = 0
# ひとつ前のログイン日開始日 or ログイン終了日を格納する。
last = -1

for (A, B) in query:
    # queryの内容が重複していても問題ない。日付間隔がないため。
    ans[loginNum] += A - last
    last = A
    loginNum += B

for i in range(1, N + 1):
    print(str(ans[i]) + ' ', end='')

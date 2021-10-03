# 標準入力を受け付ける。
S = input()
T = input()

# Sを操作することなく、S = Tになる場合は、即座にYesを出力する。
if S == T:
    print('Yes')
    exit()

S = list(S)
for i in range(len(S) - 1):
    # S[0]とS[1]を入れ替え、S[1]とS[2]を入れ替え、S[2]とS[3]を入れ替え、、、の場合を検証する。
    tmp = S[i + 1]
    S[i + 1] = S[i]
    S[i] = tmp

    # 入れ替えた場合にS = Tになるか検証する。
    if ''.join(S) == T:
        print('Yes')
        exit()

    # 入れ替えてS = Tを検証した後は、一度元のSに戻すことを忘れない。
    tmp = S[i + 1]
    S[i + 1] = S[i]
    S[i] = tmp

print('No')

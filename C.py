# 標準入力を受け付ける。
N = input()

N = list(N)

ans = 0
# bit全探索を行う。計算量 : 2のN乗
for i in range(2 ** len(N)):
    a = []
    b = []
    # bitをjの値ぶん右シフトさせて、1であるbitを探す。
    for j in range(len(N)):
        if i >> j & 1:
            a.append(N[j])
        else:
            b.append(N[j])
    # aが[] or bが[] ⏩ 片方が正整数になっていないため、後続処理を行うことなく、continueする。
    if a == [] or b == []:
        continue

    # 選んだ数字の中で最大値になるのは、左の桁へ大きい数字がくる場合なので、降順ソートを行う。
    a.sort(reverse=True)
    b.sort(reverse=True)

    ans = max(ans, int(''.join(a)) * int(''.join(b)))

print(ans)

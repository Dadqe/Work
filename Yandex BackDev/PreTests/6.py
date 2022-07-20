J = input()
S = input()
result = 0
prev_ch = []
for ch in J:
    if ch not in prev_ch:
        result += S.count(ch)
    else:
        continue
    prev_ch.append(ch)
print(result)
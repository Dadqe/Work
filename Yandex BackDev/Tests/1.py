S1 = "COVER"
Q1 = "CLEAR"

ch_dict = {}

for i in range(0, len(S1)):
    ch_dict[S1[i]] = Q1.count(S1[i])

for i in range(0, len(S1)):
    if Q1[i] == S1[i]:
        print("correct")
        ch_dict[S1[i]] -= 1
    elif Q1[i] in S1 and ch_dict[S1[i]] != 0 and ch_dict[Q1[i]] != 0:
        print("present")
        ch_dict[S1[i]] -= 1
    elif Q1[i] != S1[i]:
        print("absent")
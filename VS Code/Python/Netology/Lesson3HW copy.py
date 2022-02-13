def count_letter(words,letter):
  n = 0
  for word in words:
    if letter in word:
      n = n + 1
  return n
words=["pyton","c++","c","java","scala"]
letter="c"
print(count_letter(words,letter))
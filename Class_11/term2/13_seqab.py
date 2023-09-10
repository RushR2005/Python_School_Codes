
seq_a=(1,2,3,4)
seq_b=(1,3,5,7)

n = True
for i in seq_a:
    if i not in seq_b:
        n = False
        break

print(n)


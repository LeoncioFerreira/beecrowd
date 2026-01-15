i = 1
j = 7

while True:
    j = 8
    for _ in range(3):
        j -= 1
        print(f"I={i} J={j}")
        if i==9 and j==5:
            break
    if i==9 and j==5:
            break
    i += 2

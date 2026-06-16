rr = [1, 3, 4, 5, 6, 41, 789, -1]
stop_index = len(rr) - 1

for _ in range(len(rr) - 1):
    swap = False
    for j in range(stop_index):

        if rr[j] > rr[j + 1]:
            rr[j], rr[j + 1] = rr[j + 1], rr[j]
            swap = True

    if not swap:
        break

    stop_index += -1
    print(rr)
print(rr)

def find_max(arr):
#    maxes = [max(enumerate(arr), key=lambda x: x[1])]
#    while True:
#        next_max = max(enumerate(arr[maxes[-1][0] + 1:]), key=lambda x: x[1])
#        print(maxes, maxes[-1][0], next_max)
#        time.sleep(2)
#        if next_max[1] == maxes[-1][1]:
#            maxes.append((next_max[0] + maxes[-1][0], next_max[1]))
#        else:
#            break
#    distances = [abs(i - len(arr) / 2) for i, v in maxes]
#    return min(enumerate(maxes), key=lambda x: distances[x[0]])[1]
#    return max(enumerate())
   return max(enumerate(arr), key=lambda x: x[1])

def capacity(arr):
    if not arr: return 0
    i, v = find_max(arr)  # get max closest to center
    count = 0
    curr_i, curr_v = i, v
    while curr_i != 0:
        if arr[curr_i - 1] <= curr_v:
            curr_i -= 1
            curr_v = arr[curr_i]
        else:
            arr[curr_i] += 1
            count += 1
            curr_i, curr_v = i, v

    curr_i, curr_v = i, v

    while curr_i != len(arr) - 1:
        if arr[curr_i + 1] <= curr_v:
            curr_i += 1
            curr_v = arr[curr_i]
        else:
            arr[curr_i] += 1
            count += 1
            curr_i, curr_v = i, v
    return count

def capacity2(height):
    if not height: return 0
    ans = 0;
    size = len(height);
    left_max, right_max = [0] * size,[0] * size
    left_max[0] = height[0];
    for i in range(1, size):
        left_max[i] = max(height[i], left_max[i - 1])
    right_max[size - 1] = height[size - 1];
    for i in range(size - 2, 0, -1):
        right_max[i] = max(height[i], right_max[i + 1])
    for i in range(1, size - 1):
        ans += min(left_max[i], right_max[i]) - height[i];
    return ans;

def main():
    sol1 = capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    sol2 = capacity2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

    assert(sol1 == 6)
    assert(sol2 == 6)
    print(sol1)
    print(sol2)

main()

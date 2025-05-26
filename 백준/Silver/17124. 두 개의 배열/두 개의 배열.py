T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    c_list = []

    m_list.sort()

    def search(target, m_list):
        low = 0
        high = len(m_list) - 1

        while (low <= high):
            mid = (low + high) // 2
            if (target == m_list[mid]):
                return m_list[mid]
            if (target > m_list[mid]):
                low = mid + 1
            else:
                high = mid - 1

        if (low == len(m_list)):
            return m_list[high]
        elif (high == -1):
            return m_list[low]
        else:
            if (abs(target - m_list[low]) < abs(target - m_list[high])):
                return m_list[low]
            else:
                return m_list[high]

    for i in range(len(n_list)):
        c_list.append(search(n_list[i], m_list))


    print(sum(c_list))
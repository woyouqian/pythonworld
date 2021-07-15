# 1、实现一些排序算法，冒泡排序、选择排序、插入排序、快速排序；
# 2、实现二分法查找有序列表；
# 3、数据结构及其他算法暂不实现；
import time


def decorate(func):
    def warper(list0, item):
        first = time.time()
        result = func(list0, item)
        time.sleep(1)
        end = time.time()
        print(func.__name__, end='\t')
        print("programme running cost: %s sec..." % (end-first-1))
        return result

    return warper


def count_time(func, list0):
    first = time.time()
    func(list0)
    time.sleep(1)
    end = time.time()
    print(func.__name__, end='\t')
    print("programme running cost: %s sec..." % (end - first - 1))
    print(list0)


# 1、实现一些排序算法，冒泡排序、选择排序、插入排序；
def list_sort_bubble(list0):
    n = len(list0)
    flag = False
    for i in range(n):
        for j in range(1, n-i):
            # print(list0[j])
            if list0[j] < list0[j-1]:
                list0[j], list0[j-1] = list0[j-1], list0[j]
                flag = True
        if not flag:
            break


def list_sort_choose(list0):
    n = len(list0)
    for i in range(-1, n-2):
        for j in range(i+1, n-1):
            if list0[j] < list0[j+1]:
                list0[j], list0[j+1] = list0[j+1], list0[j]
            else:
                pass
        list0[i+1], list0[-1] = list0[-1], list0[i+1]


def list_sort_insert(list0):
    n = len(list0)
    for j in range(n-1):
        i = j + 1
        # print(list0[i])
        b = 0
        for k in range(j, -1, -1):
            if list0[k] > list0[i-b]:
                list0[k], list0[i-b] = list0[i-b], list0[k]
                b += 1
            else:
                break


def quick_sort(list0, first, last):
    low = first
    height = last
    if first >= last:
        return
    mid_var = list0[first]
    while low < height:
        while low < height and list0[height] >= mid_var:
                height -= 1
        list0[low] = list0[height]

        while low < height and list0[low] < mid_var:
                low += 1
        list0[height] = list0[low]
    list0[low] = mid_var

    # before var
    quick_sort(list0, first, last=low-1)
    # last var
    quick_sort(list0, first=low+1, last=last)


def list_sort(list0):
    if list0:
        list0.sort()


# 2、实现二分法查找有序列表；
@decorate
def find_one(list0, item):
    if list0:
        for a in list0:
            if a == item:
                print("item: %d in list..." % item)
                return a
    print("item: %d not in list..." % item)
    return False


@decorate
def find_half(list0, item):
    n = len(list0)
    if n > 0:
        first = 0
        end = n-1
        while first <= end:
            middle = (first + end) // 2
            if list0[middle] == item:
                print("item: %d in list..." % item)
                return list0[middle]
            elif item < list0[middle]:
                end = middle - 1
            else:
                first = middle + 1
        print("item: %d not in list..." % item)
        return False


@decorate
def find_half_recur(list0, item):
    n = len(list0)
    if n > 0:
        middle = n//2
        if list0[middle] == item:
            print("item: %d in list..." % item)
            return list0[middle]
        elif item < list0[middle]:
            return find_half_recur(list0[:middle], item)
        else:
            return find_half_recur(list0[middle+1:], item)
    print("item: %d not in list..." % item)
    return False


if __name__ == '__main__':
    list0 = [2, 1, 3, 6, 9, 12, 5, 7, 14, 15, 8, 11]
    list1 = [2, 1, 3, 6, 9, 12, 5, 7, 14, 15, 8, 11]
    print(list1)
    # count_time(list_sort, list0)
    # count_time(list_sort_bubble, list1)
    # count_time(list_sort_insert, list1)
    # count_time(list_sort_choose, list1)
    quick_sort(list1, 0, len(list1)-1)
    print(list1)
    # find_half_recur(list1, 5)
    # find_half(list1, 20)
    # find_one(list1, 20)



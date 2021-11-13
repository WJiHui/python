
def merge_sort(l1, l2):
    """
    归并排序,对已有顺序的两个列表进行排序
    """

    n = []
    while a and b:
        if a[0] <= b[0]:
            n.append(a.pop(0))
        else:
            n.append(b.pop(0))
    if a:
        n.extend(a)
    if b:
        n.extend(b)
    return n


def bubble_sort(test_list):
    """
    冒泡排序
    从左向右，如果相邻的两个数，前面的数比后面的数大，就互换位置
    每一轮for j 都把最大的放在最后
    """
    for i in range(len(test_list)):
        for j in range(len(test_list)-i-1):
            if test_list[j] > test_list[j+1]: # >从小到大排序 <从大到小
                test_list[j], test_list[j+1] = test_list[j+1], test_list[j]
            #print(test_list)
    return test_list

def bubble_sort2(test_list):
    for i in range(len(test_list)):
        for j in range(i+1, len(test_list)):
            if test_list[i] > test_list[j]:
                test_list[i], test_list[j] = test_list[j], test_list[i]
            #print(test_list)
    return test_list

if __name__ == '__main__':
    a = [1,4,6,8,9]
    b = [2,3,5,6,7]
    merge_sort(a, b)
    test_list = [1, 34, 22, 45, 11, 99, 0, 8, 2]
    bubble_sort(test_list.copy())
    #bubble_sort2(test_list.copy())

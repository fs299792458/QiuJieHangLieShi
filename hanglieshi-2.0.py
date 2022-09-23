#  Made by fs299792458
#You can find me at https://space.bilibili.com/1094622618
#-*- coding: utf-8 -*-
restart = True
while restart:
    A = []
    input_numbers = 0
    Round = 1
    while input_numbers != ' ':
        print('请输入行列式的各个元素，结束输入请输入空格，在此输入您的第', Round, '个数:  ')
        input_numbers = input()
        A.append(input_numbers)
        Round += 1
    del A[-1]
    length = len(A)
    n = length ** 0.5
    if n - int(n) != 0:
        print('error')
    else:
        i3 = 0
        temp_list = []
        while i3 < length:
            temp_list.append(float(A[i3]))
            i3 += 1
        A = temp_list
        D = []
        for temp in range(0, int(n)):
            D.append([])
        i1 = 0
        i2 = 0
        while i1 < length:
            a = A[i1]
            list1 = D[i2]
            i3 = len(list1)
            if i3 <= n - 1:
                list1.append(a)
                i1 += 1
            else:
                i2 += 1
        end = False
        answer = 1
        while not end:
            end = False
            if n == 1:
                C = D[0]
                k = C[0]
                end = True
                answer = answer * k
            else:
                list2 = D[int(n - 1)]
                i4 = 0
                while i4 < n - 1:
                    list3 = D[i4]
                    x1 = list2[0]
                    x2 = list3[0]
                    p = -x2 / x1
                    i5 = 0
                    templist = []
                    i4 += 1
                    while i5 < n:
                        x3 = list2[i5]
                        x4 = list3[i5]
                        y = x4 + x3 * p
                        i5 += 1
                        templist.append(y)
                    else:
                        D[int(i4 - 1)] = templist
                else:
                    f = (-1) ** (1 + n)
                    k = list2[0] * f
                    answer = answer * k
                    for list4 in D:
                        if list4 == []:
                            pass
                        else:
                            del list4[0]
                    D[int(n - 1)] = []
                    n -= 1
    print(answer)
    Finish = input("运算已结束，重新开始请在此输入r,或按任意键退出：  ")
    restart = False
    if Finish == 'r':
        restart = True

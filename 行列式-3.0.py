#  Made by fs299792458
#You can find me at https://space.bilibili.com/1094622618
#-*- coding: utf-8 -*-
def work_out_determinant(inputlist):   #计算行列式的值
    if type(inputlist)!=list:
        return  'error'
    n=len(inputlist)**0.5
    if n-int(n):
        return 'error'
    D=[]
    for i1 in range(0,int(n)):
        D.append(inputlist[i1*int(n):(i1+1)*int(n)])
    answer=1
    while len(D)-1:
        if not D[0][0]:
            answer*=-1
            i2=0
            while i2 < len(D)-1:
                i2+=1
                if D[i2][0]:
                    D.insert(0,D[i2])
                    del (D[i2+1])
                    break
            else:
                return 0

        if  D[0][0]-1:
            answer*=D[0][0]
            list4=[]
            for i4 in D[0]:
                list4.append(i4/D[0][0])
            del D[0]
            D.insert(0,list4)
        list1=D[0]
        i3=0
        while i3<len(D)-1:
            i3+=1
            list2=D[i3]
            k=list2[0]
            for i4 in range(0,int(len(D[i3]))):
                list2.append(list2[0]-k*list1[i4])
                del list2[0]
        del D[0]
        for list3 in D:
            del list3[0]

    answer*=D[0][0]
    return answer


while True:
    inputlist=[]
    input_numbers = 0
    Round = 1
    while input_numbers != ' ':
        print('请输入行列式的各个元素，结束输入请输入空格，在此输入您的第', Round, '个数:  ')
        input_numbers = input()
        inputlist.append(input_numbers)
        Round += 1
    del inputlist[-1]
    for i in range(0,len(inputlist)):
        inputlist.append(int(inputlist[0]))
        del inputlist[0]
    answer=str(work_out_determinant(inputlist))
    whether_finish=input('运算已结束，结果为：'+ answer +'  重新开始请在此输入r,或按任意键退出： ')
    if whether_finish != 'r':
        break
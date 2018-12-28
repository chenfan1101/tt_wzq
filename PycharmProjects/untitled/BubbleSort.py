

# 冒泡排序算法
# 第一步，将每一组的进行比对，数字大的放在后面，
# 第二部，重复第一步的步骤，一直到最后一组的比对完成为止
def maopao():
    temp = [56, 54, 3243, 323, 3, 82, 121, 33, 4, 1]
    for j in range(1,len(temp)):
        found = False
        for i in range(len(temp)-j):
            if(temp[i]>temp[i+1]):  #将满足条件的数组的值进行替换
                lists = temp[i]
                temp[i] = temp[i+1]
                temp[i+1] = lists
            else:
                found = True     # 做的优化，当所有相邻的数组内的数值均满足条件时，已经排序完成，不需要继续比对了
        if not found:
            break
    print(temp)

# 知识点，range(3) 为数组0，1，2    range(1,3) 为数组 1，2





if __name__=='__main__':
    maopao()




'''
链接：
【【自学用】算法实例精讲——Python语言实现】 
https://www.bilibili.com/video/BV1M3411Y7DA/?share_source=copy_web&vd_source=eb4147d10330b93c14171bf2d069eb41
待排序数组A=(50, 36, 66, 76, 95, 12, 25),使用直接插入排序法实现升序排列.
'''
# def insertSort(arr):
#     for i in range(0,len(arr)):
#         key = arr[i]
#         j = i-1 
#         while( j >= 0 and arr[j] > key ):
#             temp = arr[j]
#             arr[j] = key 
#             arr[j+1] = temp
#             j = j-1 

#     return arr 

# arr = [10,32,10,1,112,2,34,1,9]
# insertSort(arr)
# print(arr)

# 直接插入排序算法
def insertSort(arr):
    for i in range(1, len(arr)):
        target = arr[i]   # 此处用于保存当前需要插入的变量
        j = i-1 # j 是用于遍历已排好序列的数组a 

        # 此处的while循环是用来给需要插入的数字开辟位置
        while( j>=0 and target<arr[j]): # 当我还没遍历完已经排好的数组 a 同时 需要插入的数字还没找到需要插入的地方的时候
            arr[j+1] = arr[j]  # 把所有的数先往后移动
            j -=1   # 然后角标继续往前

        ## 当前面处理好需要安放的位置后，再将
        arr[j+1] = target # 因为前一步执行了 j-1  ,此处的 j+1 就代表着 arr[j] 
        # 把这个数安放好之后，就可以继续考虑下一个需要插入的变量了。

    return arr 

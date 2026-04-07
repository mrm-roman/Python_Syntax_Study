#列表练习
# 1. 输入 5 个数字，存入列表，输出最大值和最小值
number_list = []
for i in range(1,6):
    number_list.append(int(input(f"请输入第{i}个数字:")))
number_list.sort()
print(f"最大值是{number_list[4]}")
print(f"最小值是{number_list[0]}")


# 2. 删除列表中的重复元素
##方法一：转成集合，再变回列表，但列表顺序可能改变
raw_list = [1, 2, 2, 3, 3, 3]
print(list(set(raw_list)))
#方法二：通过循环判断，可保留顺序，但大数据量时运行速度较慢
raw_list = [3, 1, 2, 1, 3, 2]
clean_list = []
for item in raw_list:
    if item not in clean_list:
        clean_list.append(item)
print(clean_list)


# 3. 将一个列表反转
raw_list = [1, 2, 2, 3, 3, 3]
raw_list.reverse()
print(raw_list)


# 4. 统计列表中每个元素出现的次数
raw_list = [3, 1, 2, 1, 3, 2]
set_list = set(raw_list)
for item in set_list:
    print(f"元素{item}出现的次数为：{raw_list.count(item)}")


# 5. 把一组成绩按从高到低排序
score = [12,52,75,67,97,67,89,43,78,56,90,99,78,98]
score.sort(reverse=True)
print(score)


# ### 元组练习

# 1. 创建一个包含姓名、年龄、城市的元组并输出
info = ("name", "age", "city")
print(info)

# 2. 比较列表和元组的区别：尝试修改元素，观察报错
info = ("name", "age", "city")
info[0] = "a"



# ### 集合练习

# 1. 对列表去重
# 2. 求两个集合的交集、并集、差集
# 3. 判断两个列表中有哪些共同元素
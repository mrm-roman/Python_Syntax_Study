### 练习 1：统计字符串长度
string1 = input("请输入想统计长度的字符串：")
print(len(string1))


### 练习 2：判断回文字符串
# 如 `"level"`、`"上海自来水来自海上"`（可先做英文简单版）
string2 = input("请输入字符串：")
#方法1：前后对比法
length = len(string2)
for i in range(length):
    if string2[i] != string2[length-i-1]:
        print("这不是回文字符串！")
        break
    elif i == length-1:
        print("这是回文字符串！")
#方法2：翻转对比法
    if string2 == string2[::-1]:
        print("这是回文字符串！")
    else:
        print("这不是回文字符串！")

### 练习 3：统计元音字母个数
# 输入一个字符串，统计 `a e i o u` 的数量。
string3 = input("请输入字符串：")
print(string3.count("a"))
print(string3.count("e"))
print(string3.count("i"))
print(string3.count("o"))
print(string3.count("u"))


### 练习 4：把一句英文的每个单词首字母大写
string4 = input("请输入字符串：")
print(string4.title())


### 练习 5：去掉字符串首尾空格，并把中间多个空格变成一个空格
raw_text = "   这   是一段    非常   混乱的   文字   "
clean_text = " ".join(raw_text.split())
print(f"清洗后: '{clean_text}'")   #清洗后: '这 是一段 非常 混乱的 文字'
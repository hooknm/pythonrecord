def add(x, y):
  return x + y
result = add(3, 4)
print(result)

def jian(a, b):
  return a - b
result1 = jian(7, 3)
print(result1)
end_result = result + result1
print(end_result)



"""
累加器 v1.0
"""

s = 0

x = int(input('输入整数：'))
s += x

x = int(input('输入整数：'))
s += x

x = int(input('输入整数：'))
s += x

print('总和：%d' % s)


"""
判断奇偶数
"""

in_x = int(input('输入整数：'))

if in_x % 2 == 0:
    print('偶数')
else:
    print('奇数')


language = "python"
reversed_language = language[::-1]
print(reversed_language) # nohtyp

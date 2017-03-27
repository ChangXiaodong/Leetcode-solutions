12. 打印1最大的n位数

    考虑大数问题，转换成字符串计算
    0到9全排列问题，用dfs完成。
```
def print1ton(n, s, length):
	if length > n:
		return
	print(s)
	for i in range(10):
		print1ton(n, s + str(i), length + 1)
	
```
    
13. 
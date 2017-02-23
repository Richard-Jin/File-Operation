##Python<br>
###2017/2/22
1.获取当前进程工作目录（操作的目录）。
```python
os.getcwd()　　　#get current work direction
```
###2017/2/23
1.正则表达式元符<br>
　　\d:一个数字；<br>
　　\w：一个字母或数字；<br>
　　\s：一个空格；<br>
　　\S：匹配任意非空字符；
　　.：一个任意字符；<br>
　　*：任意个任意字符；<br>
　　+：一个或以上个任意字符；<br>
　　?：0个或1个任意字符<br>
　　\d+?：加个问号→非贪婪匹配；<br>
　　{n}：n个字符<br>
　　{n,m}：n-m个字符<br>
　　[]：一个范围。
<br>
2.正则表达式分组提取<br>
　　在表达式上加()，第一个括号为第一组。<br>
```python
m.group(0)  #原始字符串
m.group(1)  #第一个字符串
```
3.正则表达式编译后直接匹配
```python
re_telephone=re.compile(r'^(\d{3})\-(\d{3-8})$')
re_telephone.match(string)
```
[伯乐在线-正则表达式](http://www.runoob.com/python/python-reg-expressions.html)
<br>
4.字符串find
　找到字符返回找到位置索引，未找到返回-1。

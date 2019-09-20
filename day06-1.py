# pyquery本身就是css选择器
# 选择div时用"#"号
# class "."
# 其他标签，啥都不用填

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
# 初始化
# 字符串初始化 这里的字符串指的是html
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('li'))

# url初始化 这里传入一个url，他会去请求这个url然后对返回结果进行选择
# from pyquery import PyQuery as pq
# doc = pq(url='http://www.baidu.com')
# print(doc('head'))

# 文件初始化 这里我就没创建文件了
# from pyquery import PyQuery as pq
# doc = pq(filename='demo.html')
# print(doc('li'))

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
# 获取信息

# 获取属性
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.attr('href'))
# print(a.attr.href)

# 获取文本
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.text())

# 获取html
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# print(li.html())
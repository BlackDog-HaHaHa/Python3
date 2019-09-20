html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

# 基本css选择器
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('#container .list li')) # 由外到内的选择元素

# 查找元素
# 子元素
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)

# 父元素和祖父元素
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# parents = items.parents()
# print(type(parents))
# print(parents)


# 兄弟元素
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
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li.siblings())
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li.siblings('.active'))
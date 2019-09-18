# re.search
# import re
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.search('Hello.*?(\d+).*?',content)
# print(result)
# print(result.group(1))

# re.findall

# re.sub 替换
# import re
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.sub('(\d+)','',content)
# print(result)

# import re
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.sub('(\d+)',r'\1 89',content) # \1是将前面匹配到的结果拿过来了
# print(result)
# 替换可以用来删掉一些不好匹配的标签，方便后面的提取

# re.compile
# import re
# content = '''Hello 1234567 World_This
# is a Regex Demo'''
# pattern = re.compile('Hello.*Demo',re.S)
# result = re.match(pattern,content) # 我的理解就是将正则赋值给变量，方便复用
# print(result)
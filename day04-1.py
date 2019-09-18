# 常规匹配
# import re
# content = 'Hello 123 4567 world_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
# print(result)
# print(result.group())
# print(result.span())

# 泛匹配
# import re
# content = 'Hello 123 4567 world_This is a Regex Demo'
# result = re.match('^Hello.*Demo$',content)
# print(result)
# print(result.group())
# print(result.span())

# 匹配目标
# import re
# content = 'Hello 1234567 world_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sworld.*Demo$',content)
# print(result)
# print(result.group())
# print(result.group(1)) # 输出小括号里你匹配的东西
# print(result.span())

# 贪婪匹配
# import re
# content = 'Hello 1234567 world_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$',content)
# print(result)
# print(result.group(1))
# print(result.span())

# 非贪婪匹配
# import re
# content = 'Hello 1234567 world_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$',content)
# print(result)
# print(result.group(1))
# print(result.span())

# 匹配模式
# import re
# content = '''Hello 1234567 world_This
# is a Regex Demo'''
# result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
# print(result)
# print(result.group(1))
# print(result.span())
# 正则表达式中，“.”的作用是匹配除“\n”以外的任何字符，而re.S则是还能匹配“\n”

# 转义
# import re
# content = 'price is $5.00'
# result = re.match('price is \$5\.00',content)
# print(result)
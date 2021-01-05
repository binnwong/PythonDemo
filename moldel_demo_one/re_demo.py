import re


# match_result = re.match(r"We", "We read the world wrong and say that it deceives us.")
# print(match_result)
# print(match_result.group())
#
# search_result = re.search(r"read", "We read the world wrong and say that it deceives us.")
# print(search_result)
# print(search_result.group())

# findall_result = re.findall(r'\d+', 'We read the world wrong 777 and 2 say that it deceives 007 us.')
# print(findall_result)
# print(type(findall_result))

# sub_result = re.sub(r'a', 'A', 'We read the world wrong and say that it deceives us.')
# print(sub_result)

result1 = re.search(r'\d+', 'We read the world wrong 7777777 and 2 say that it deceives 007 us.')
print(result1.group())

result2 = re.search(r'\d+?', 'We read the world wrong 7777777 and 2 say that it deceives 007 us.')
print(result2.group())

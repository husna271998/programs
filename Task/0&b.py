import re
def text_to_check(text):
        patterns = '^a+b*$'
        if re.search(patterns,  text):
                return 'true!'
        else:
                return('false!')
print(text_to_check("ac"))
print(text_to_check("a"))
print(text_to_check("aaaa"))
print(text_to_check("aaabbbbbbbb"))
print(text_to_check("ab"))

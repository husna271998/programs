import re
def text_to_check(text):
        string = '^[a-z]+_[a-z]+$'
        if re.search(string,  text):
                return 'True'
        else:
                return('False')

print(text_to_check("amm_mbrrrbbc"))
print(text_to_check("aab_Abbbc"))
print(text_to_check("aababbbc"))
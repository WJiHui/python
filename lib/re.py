import re

# 分割字符串，删除无用的字符
def re_findall(text):
    words = re.findall('\w+', text)
    print(words) # ['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']

def re_sub(text):
    words = re.sub('\"|\s+|\'|,', ' ', text)
    print(words) #  "The time has come   the Walrus said"
    
    words = words.split()
    print(words) # ['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']

def re_split(text):
    words = re.split('\"|\s+|\'|,', text)
    print(words)  # ['', 'The', 'time', 'has', 'come', '', '', 'the', 'Walrus', 'said', '']

def re_finditer(text):
    RE_WORD = re.compile('\w+')
    words = RE_WORD.finditer(text)
    print(type(words)) # <class 'callable_iterator'>
    
    for i in words:
        # <re.Match object; span=(1, 4), match='The'> ...
        print(i)         
        
        # The ...
        print(i.group())
#         print(dir(i))

def main():
    re_findall('"The time has come," the Walrus said,')
    re_sub('"The time has come," the Walrus said,')
    re_split('"The time has come," the Walrus said,')
    re_finditer('"The time has come," the Walrus said,')

if __name__ == "__main__":
    main()
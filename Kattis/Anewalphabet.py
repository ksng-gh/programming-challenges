import sys

def Anewalphabet():
    sentence = input()
    sentence = sentence.lower()
    for x in sentence:
        print(LetterTranslation(x), end="", flush=True)

def LetterTranslation(inp):
    translate = {'a':'@','b':'8','c':'{','d':'|)','e':'3','f':'#','g':'6','h':'[-]','i':'|','j':'_|','k':'|<','l':'1','m':'[]\/[]','n':'[]\[]','o':'0','p':'|D','q':'(,)','r':'|Z','s':'$','t':'\'][\'','u':'|_|','v':'\/','w':'\/\/','x':'}{','y':'`/','z':'2'}
    for x in translate:
        if x == inp:
            return translate.get('{}'.format(x))
    return inp

Anewalphabet()

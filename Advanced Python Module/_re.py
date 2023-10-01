import re

# result = dir(re)

# re module

str = 'Python course: Python Programming Guide | 40 hours'

# re.findall()
# result = re.findall("Python", str)
# result = len(result)

#re.split()
# result= re.split(" ", str)
# result= re.split("R", str)

#re.syb()
# result= re.sub(" ", "-", str)

#re.search()
# result= re.search("Python", str)
# result= result.span()
# result= result.start()
# result= result.end()
# result= result.group()
# result= result.string

# Regular Expression

"""


    [] - Köşeli parantezler arasına yazılan tüm karakterler aranır.(All characters written between square brackets are searched.)

        [abc] => a     : 1 match 
                 b     : 2 match 
                 Python: no match

        [a-e] => [abcde]
        [1-5] => [12345]
        [0-39]=> [012...39]

        [^abc]=> characters other than abc
        [^1-9]=> non-digits characters

"""

result = re.findall("[abc]", str)
result = re.findall("[sat]", str)
result = re.findall("[a-e]", str)
result = re.findall("[a-z]", str)
result = re.findall("[1-4]", str)
result = re.findall("[^abc]", str)
result = re.findall("[^0-3]", str)



"""
    . - Specifies any single attribute.
        .. => a   : no matches
              ab  : 1 matches
              abc : 1 matches
              abcd: 2 matches
"""

result = re.findall("...", str)
result = re.findall("Py..on", str)

"""
        ^ - Does it start with the specified characters?
        ^a => a  : 1 matches
              abc: 1 matches
              bac: no matches
"""
result = re.findall("^a", str)
result = re.findall("^P", str)


"""
        $ - Does it end with the specified characters?
        a$ => a     : 1 matches
              lamba : 1 matches
              Python: no matches
"""

result = re.findall("t$",str)
result = re.findall("hours$",str)
result = re.findall("hourss$",str)

"""
     * - Checks if a character is zero or more
         ma*n => mn   : 1 matches
                 man  : 1 matches
                 maaan: 1 matches
                 main : no matches (a'nın arkasından n gelmiyor.)
"""

result = re.findall("hour*s", str)


"""
     + - Checks if a character is one or more
         ma+n => mn   : no matches
                 man  : 1 matches
                 maaan: 1 matches
                 main : no matches (a'nın arkasından n gelmiyor.)
"""

result = re.findall("Program*ing", str)

"""
     ? - Checks if a character is zero or one
         ma+n => mn   : no matches
                 man  : 1 matches
                 maaan: 1 matches
                 main : no matches (a'nın arkasından n gelmiyor.)
"""

result = re.findall("Program?ing", str)
result = re.findall("hour?s", str)


"""
    {} - Checks the number of characters
        a1{2}    => a karakterinin arkasına 1 karakteri 2 kez tekrarlamalı.
        a1{2,3}  => a karakterinin arkasına 1 karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""
result = re.findall("m{2}",str)
result = re.findall("[0-9]{2}",str)

"""
    |  - used to realize one of the alternative options.

        a|b => a  or  b

            cde    =>     no match
            ade    =>     1 match
            acdbea =>     3 match

"""

"""
    () - is used to group

        (a|b|c)xz => a,b,c karakterlerinin arkasına z gelmelidir.
"""




"""

            1 - özel karakterleri aramamizi saglar.
                \$a => $ karakterinin arkasina a karakterinin arar. Yani 
                       $ regular exp. engine tarafindan yorumlanmaz.
            
            \A - Belirtilen karakter string in basinda mi ?
                \Athe => the string in basindam1
            
            \Z - Belirtilen karakter string in sonunda mi ?
                the\Z =>  the string in sonunda mı
            result = re. findal1("APython",str)
            result = re. findal1("hours\Z",str)

            \b - Belirtilen karakter kelimenin in basinda ya da sonunda mi ?
                \bthe => the kelimenin in basinda mi?
                the\b => the kelimenin in sonunda mi?

            \B - Belirtilen karakter kelimenin in basinda ya da sonunda desil mI ?
                \Bthe =› the kelimenin in basinda degil mi? 
                the\B => the kelimenin in sonunda degil mi?

            \d - [0-91 ile ayni anlama gelir yani rakamlari arar.
                |\d => 12abc34

            \D - [^9-9] ile ayni anlama gelir yani rakam olmayanlari arar.
                \D => 1ab44_50

            \s - Boşluk karakterlerini arar
            \S - Boşluk karakterleri dışındakileri arar.
            \w - Alfabetik karakterler, rakamlar ve alt çicgi karakteri.
            \W - \w nün tam tersi



"""













print(result) 

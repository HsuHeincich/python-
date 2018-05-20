# -*- coding: utf-8 -*-
strings=['foo','card','bar','aaaa','abab']
strings.sort(key=lambda x:len(set(list(x))))    #可以直接set(x)
print strings
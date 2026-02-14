import re
h = open('index.html','r',encoding='utf-8').read()
D = []
def q(t,a,b,c,d,x):
    D.append({"s":"Electronics Information","q":t,"o":[a,b,c,d],"a":x})

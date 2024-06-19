#WAP that count the frequency of each character in a string
str="abracadabra"
d={}
for i in str:
    a=i
    count=0
    for i in str:
        if i==a:
            count+=1
    d.update({a:count})
print(d)

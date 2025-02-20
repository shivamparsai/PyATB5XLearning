# count the frequency of each character in String

string = "automation"

# a:2, u:1, t:2, o:2, m:1, i:1, n:1

dict4 = {}

for i in string:
    dict4[i] = dict4.get(i,0)+1

print(dict4)
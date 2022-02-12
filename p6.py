# You are given n words. Some words may repeat.
#  For each word, output its number of occurrences.
#  The output order should correspond with the input order of appearance of the word.
#  See the sample input/output for clarification. 
import collections;
n= int(input())
d=collections.OrderedDict()

for  i in range(n):
    word=input()
    if word in d:
        d[word]+=1
    else:
        d[word]=1
print(len(d))
for k,v in d.items():
    print(v ,end =" ")
print("this program is prepared by om and id :d21ce176")  
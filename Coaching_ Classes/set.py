
"""
1.set is unordered data collection 
2. ste is not accept duplicate value
3.set is a mutable data collection
4.set is hetrogeneous data collection
5.set is created set() but value are  sorted
6. set are update by only two methods these are add(),update() method
6.1. add() method used for single value insertion
6.2. update() method used for add multiple data but data are in the form of list []
7. set have pop(),remove(),discard(),clear()
7.1. pop()- remove random value and return deleted value  ut in case of idle it remove first element
7.2. remove()- delete given value and it can't return any value if no data found then it return keyerror
7.3 discard()- remove given value and it also not return value if no data found then it can't return any error
7.4 clear()- remove all data at once

set Operations

union()-combined one or more |
intersection()-common in 2 sets &
difference()-only in first set -
symmetric_diffrence()- uncommom in 2 sets ^

difference_update()-output of deffirence are stored in first set
symmetric_difference_update()-output of deffirence are stored in first set
intersection_difference_update()-output of deffirence are stored in first set

frozenset()- it create read only set
"""


s=(1,2,3,3,4,9,4,5,6,7,8,9)


print(set(s))


s1={1,2,3,5,7,9,5,7}
s2={2,3,6,5,8,7,0}

a=s1.union(s2)
print(a)

b=s1.intersection(s2)
print(b)

c=s1.difference(s2)
print(c)

d=s1.symmetric_difference(s2)
print(d)


e=s1.difference_update(s2)
print(e)

f=s1.symmetric_difference_update(s2)
print(f)

g=s1.intersection_update(s2)
print(g)

c1={'Apple','Microsoft','Banana','Mango'}
c2={'Apple','Mango'}
c3={'Mango','TCS'}

x=c1.issuperset(c2)
print(x)

y=c1.issubset(c2)
print(y)

y=c1.isdisjoint(c2)
print(y)

w=c1.issuperset(c3)
print(w)


li=['Ram','chand','poor','rich','rtiolk']

age={12,45,34,23,12,87,65}

for n,a in zip(li,age):
    print("Name",n,"Age",a)


li=['Ram','chand','poor','rich','chand','poor','rich','rtiolk','ahbf','ghjkid']

s1=set()
s2=set()

for name in li:
    if name not in s1:
        s1.add(name)
    else:
        s2.add(name)

print(s1)
print(s2)
print(li)


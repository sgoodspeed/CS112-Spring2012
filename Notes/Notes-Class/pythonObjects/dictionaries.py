#!usr/bin/env python

people ={'Jonah':"stupid",
         'Alec' : "smelly",
         "Jack":"ugly",
         "Paul":"awesome"}

name = raw_input("Your name: ")
if name in people:
    print name, "is", people[name]
else:
    print "I don't know you", name

print people.keys()
print people.values()
print len(people)


eng2sp = {}
eng2sp['one']='uno'
eng2sp['two']='dos'
print eng2sp['one']
for k,v in eng2sp.items():
    print k,v

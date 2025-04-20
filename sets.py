SMPLE_LIST=[1,3,2,5,4,7,6,9,8,10,9]
print(SMPLE_LIST)
sam=set(SMPLE_LIST)
print(sam)
pee=[1,2,3,4,5,6,7,8,9]
poo=[10,11,12,13,14,15,16,17,18,19,1,2,3,4,5]
setpee=set(pee)
setpoo=set(poo)
print(setpee.union(setpoo))
print(setpee | setpoo)
print(setpoo.intersection(setpee))
print(setpoo&setpee)
print(setpoo.difference(setpee))
print(setpoo-setpee)
print(setpee.symmetric_difference(setpoo))
print(setpoo^setpee)
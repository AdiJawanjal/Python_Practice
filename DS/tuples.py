# tuples are ordered and Immutable
tu=(1,2)
a,b = tu
print(a)
print(b)
print(a,b)

'''
1
2
1 2
'''
#---------------------------------------------------

tu=(1,2,2,4,2)
a,b,c,d,e= tu
print(tu.count(2))

'''
O/P
3
'''

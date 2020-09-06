arg=select(4,1,2,3,4,5,6,7,8,9)
print(arg)
a={1,2,3,4}
print(ipairs(a))
-- iterate to first absent integer.
print(pairs(a))
-- able to scan through the table.
a[2.5]=5777
print(a[2.5])
a,b=233,334
print(a,b)

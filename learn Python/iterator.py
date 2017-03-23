nums = [1, 2]

i=[i for i in nums]
print i[0]
i={i:i**2 for i in range(3)}
print i
print i[2]
i=(i for i in nums)
print next(i)
if(next(i)!=None):
	print next(i)

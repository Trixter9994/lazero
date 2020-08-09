-- cutting method: check with differential?
-- check with integral?
-- hope you like math haha...

function ct(ax,b)
	local s=0
	for a,k in ipairs(ax) do
		if k == b then
			s=s+1
		end
	end
	return s
end

function verify(list0)
	local t2 = list0[1]
	local Count = ct(list0,t2)
	if Count == #list0 then
		return true
	else
		return false
	end
end

rape={1,1,1,1,1}
print(verify(rape))
rape0={1,2,1,1,1,1}
-- no direct approach.
-- consider partial or grouping or putting into a range
print('-i will rape you-')
print(verify(rape0))

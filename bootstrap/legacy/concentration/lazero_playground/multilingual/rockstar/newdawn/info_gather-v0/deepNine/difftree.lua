-- cutting method: check with differential?
-- check with integral?
-- hope you like math haha...

function range(from, to, step)
  step = step or 1
  return function(_, lastvalue)
    local nextvalue = lastvalue + step
    if step > 0 and nextvalue <= to or step < 0 and nextvalue >= to or
       step == 0
    then
      return nextvalue
    end
  end, nil, from - step
end

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

function takeAct(list0)
	local mk = {}
	local mv = #list0-1
	-- greater than one
	for vk in range(1, mv,1) do
		mk[#mk+1]=list0[vk+1]-list0[vk]
	end
	return mk
end

nuke={1,2,3,4,5}

for so,sive in ipairs(takeAct(nuke)) do
	print(so,sive)
end
--[[
rape={1,1,1,1,1}
print(verify(rape))
rape0={1,2,1,1,1,1}
-- no direct approach.
-- consider partial or grouping or putting into a range
print('-i will rape you-')
print(verify(rape0))]]
-- hell

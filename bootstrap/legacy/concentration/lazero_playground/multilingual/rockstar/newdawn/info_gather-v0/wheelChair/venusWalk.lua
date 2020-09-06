-- cutting method: check with differential?
-- check with integral?
-- hope you like math haha...
function round(float)
    return math.floor(float + .5)
end

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


function takeOver(list0,stacks)
	local blowJob = false
	if #list0>1 and verify(list0) == true then
		blowJob = true
--		print("mark I")
--		print(blowJob)
--[[		print(stacks)
		for np,mp in ipairs(stacks) do
			print(mp)
			for nvk, mvk in ipairs(mp) do
				print(mvk)
			end
		end]]
--		fury={blowJob,stacks}
		return blowJob,stacks
--		print(blowjob)
	elseif #list0 ==1 then
--		print("mark II")
		return blowJob,stacks
	else
		mvp = takeAct(list0)
		stacks[#stacks+1]=mvp
--[[		for np,mp in ipairs(mvp) do
			print(mp)
		end]]
		return takeOver(mvp,stacks)
	end
end
nuke={}
for vm,argv in ipairs(arg) do
	nuke[#nuke+1]=round(argv)
end
--bank=takeOver(nuke,{})
prt,wrt=takeOver(nuke,{})
print(prt)
--print(wrt)
for rk,rn in ipairs(wrt) do
--	print(rk,rn)
--	print("--spliter--")
	for rad, run in ipairs(rn) do
		if rad<#rn then
			io.write(run.." ")
		else
			print(run)
		end
	end
end

-- greater than two.
--[[for so,sive in ipairs(takeAct(nuke)) do
	print(so,sive)
end]]
-- stop it. do it in python.
-- yeah.
--[[
rape={1,1,1,1,1}
print(verify(rape))
rape0={1,2,1,1,1,1}
-- no direct approach.
-- consider partial or grouping or putting into a range
print('-i will rape you-')
print(verify(rape0))]]
-- hell

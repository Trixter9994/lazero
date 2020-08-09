-- this <pairs> means key - value pair.
tab1 = { key1 = "val1", key2 = "val2", "val3" }
for k, v in pairs(tab1) do
    print(k .. " - " .. v)
end
 
tab1.key1 = nil
for k, v in pairs(tab1) do
    print(k .. " - " .. v)
end

-- this fuck really works
tab2={}
tab2.locate="fuck"
print(tab2["locate"])

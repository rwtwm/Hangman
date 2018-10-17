def isIsogram(inStr):
        charDict = {}
        for char in inStr:
                if char in charDict:
                        return False
                else:
                        charDict[char] = True
        return True

with open("sowpods.txt","r") as spds:
	with open("sowpods_iso.txt","w") as isopds:
		
		for line in spds.readlines():
			if isIsogram(line):
				isopds.write(line)


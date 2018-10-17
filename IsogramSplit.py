with open("sowpods_iso.txt","r") as isopds:

        files = {}
                
        for line in isopds.readlines():
                seenLen = []
                
                size = len(line)
                if size not in seenLen:
                        newFileStr = "isograms{}.txt".format(size)
                        newFile = open(newFileStr,"a")
                        files.update({size: newFile})
                        seenLen.append(size)

                files[size].write(line) 

        for file in files:
                file.close()

        

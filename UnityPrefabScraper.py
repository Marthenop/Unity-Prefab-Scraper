import os, glob

mlist = os.listdir("Metas")
melist = os.listdir("Materials")
#Really wanted to just use wildcards, but I'm not allowed to do that when I open a file.
p = glob.glob("Prefab/*.*")

finds = []
findm = []
findme = []

f = open(p[0], "r")
find2 = f.readlines()
f.close


for line in find2:
    line = line.split(", ")

    if "m_Mesh" in line[0]:
        find3 = findm.append(line[1])
    findm = [*set(findm)]

    if "m_Script" in line[0]:
        find3 = finds.append(line[1])

    #Mat files start on a new line, so this will have to do.
    if "fileID: 2100000" in line[0]:
        find3 = findme.append(line[1])
    #Gotta get rid of dupes
    findme = [*set(findme)]
    
p = p[0].split('\\')

#Extra if, but it saves the program a bit of work if nothing is there.
print(p[1]+" has "+str(len(finds))+" scripts, "+str(len(findm))+" meshes, and "+str(len(findme))+" materials attached:\n")

if len(finds) != 0:
    for item in mlist:
        f = open("Metas/"+item, "r")
        llist = f.readlines()
        f.close
        for item2 in finds:
            if item2 in llist[1]:
                item = item.split('.')
                print(item2+" - "+item[0]+"."+item[1])

#Really didn't need to do this, but it looks nicer and it's easier to read for people who don't know.
if len(findm) != 0:
    print("")
    for item in mlist:
        f = open("Metas/"+item, "r")
        llist = f.readlines()
        f.close
        for item2 in findm:
            if item2 in llist[1]:
                item = item.split('.')
                print(item2+" - "+item[0]+"."+item[1])

if len(findme) != 0:
    print("")
    for item in mlist:
        f = open("Metas/"+item, "r")
        llist = f.readlines()
        f.close
        for item2 in findme:
            if item2 in llist[1]:
                item = item.split('.')
                print(item2+" - "+item[0]+"."+item[1])

input("\nNote: If there are any discrepancies in the numbers, you might have missed a few meta files.\n")


#test in python 3.6.4

import sys, os
import hashlib

#find duplicate file in dir
spath = "D:\\QQFiles\\332189413"
pathDict = {}


def findDuplicateFile(dirPath):
    allsub = os.listdir(dirPath)
    for sub in allsub:
        subPath = "%s/%s" % (dirPath, sub)
        if os.path.isfile(subPath):
        	md5 = getFileMd5(subPath)
        	if isDuplicateFile(subPath, md5):
        		doWithDuplicateFile(subPath, md5, pathDict[md5])
        	else:
        		pathDict[md5] = subPath
        if os.path.isdir(subPath):
            findDuplicateFile(subPath)

def getFileMd5(filePath):
	md5 = hashlib.md5()
	file = open(filePath, "rb")
	while True:
		buff = file.read(8096)
		if not buff:
			break;
		md5.update(buff)
	file.close()
	return md5.hexdigest()

def isDuplicateFile(filePath, md5):
	#you can do endwith operation in here, eg:
	#if md5 in pathDict and filePath.endswith("png"):
	if md5 in pathDict:
		return True
	return False

def doWithDuplicateFile(filePath, md5, sameFile):
	#print duplicate file info
	print("%s is same as %s, md5:%s" % (filePath, sameFile, md5))

	#delete duplicate file
	#try:
	#	os.remove(filePath)
	#except Exception as e:
	#	print("delete %s error:%s" % (filePath, e))



if __name__ == '__main__':
    findDuplicateFile(spath)
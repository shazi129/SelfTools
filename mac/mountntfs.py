#!/usr/bin/env python
#encoding: utf-8

import os

ret = os.popen("mount").readlines()

ntfsList = []
for line in ret:
    if line.find("ntfs") >= 0:
        ntfsList.append(line)

if len(ntfsList) == 0:
    print "没有ntfs设备"
    exit(0)

print "要重新挂载的设备:"
for index, line in enumerate(ntfsList):
    print "[%s] %s" % (index, line)

index = raw_input("序号:")
mount_info = ntfsList[int(index)].split()

password = raw_input("管理员密码: ")

ret = os.popen("echo password | sudo -S umount %s" % (passwword, mount_info[0]).readlines())
print ret
ret = os.popen("mkdir %s" % mount_info[2]).readlines()
print ret
ret = os.popen("echo Shazi129 | sudo -S mount_ntfs -o rw,nobrowse %s %s" % (mount_info[0], mount_info[2])).readlines()
print ret

ret = os.popen("open %s" % mount_info[2]).readlines()
print ret

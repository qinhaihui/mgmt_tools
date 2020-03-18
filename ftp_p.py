#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : python3.7
# @Time    : 2020/3/17 18:30
# @Author  : qhh
# @Site    : hztest
# @File    : ftp_p.py
# @Software: PyCharm
import time
import ftputil
# https://blog.51cto.com/walkerqt/2299304
FtpHost = r''  # FTP 主机
SubDir = r''   # 最后的斜线有无不影响，根目录用单斜线即可
FtpUser = r''
FtpPwd = r''
FtpEncoding = r'utf-8'


def Main():
    r"""
        遍历 ftp 目录，列出单个文件大小，统计目录个数、文件个数、文件总大小。
    """
    fileCnt = 0
    fileSize = 0
    dirCnt = 0
    with ftputil.FTPHost(host=FtpHost, user=FtpUser, passwd=FtpPwd) as host:
        for parent, dirnames, filenames in host.walk(SubDir):
            for filename in filenames:
                fileCnt += 1
                pathfile = host.path.join(parent, filename)
                singleFileSize = host.path.getsize(pathfile)
                fileSize += singleFileSize
                print('\tfile: %s, %d bytes' %
                      (pathfile.encode('utf-8').decode(FtpEncoding), singleFileSize))

            for dirname in dirnames:
                dirCnt += 1
                pathdir = host.path.join(parent, dirname)
                print('\tdir: %s' % pathdir.encode(
                    'utf-8').decode(FtpEncoding))

            print('fileCnt: %d, fileSize: %d B/%.2f KB/%.2f MB/%.2f GB, dirCnt: %d'
                  % (fileCnt, fileSize, fileSize/1024, fileSize/1024/1024, fileSize/1024/1024/1024, dirCnt))

    print('fileCnt: %d, fileSize: %d B/%.2f KB/%.2f MB/%.2f GB, dirCnt: %d'
          % (fileCnt, fileSize, fileSize/1024, fileSize/1024/1024, fileSize/1024/1024/1024, dirCnt))


if __name__ == '__main__':
    Main()
    print('current time: %s\n'
          % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

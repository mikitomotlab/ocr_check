#!/usr/bin/env python3

import sys
import glob
import os
import numpy as np

def inputfile_list():
    cwd = os.getcwd()	#current working directory
    dirs = []
    for x in os.listdir(cwd):
        if os.path.isdir(x):
            dirs.append(x)

    path = cwd+"/file" 

	#ディレクトリ内をチェックし csv ファイルをfilesに追加
    files = []
    print(files)

    for f in os.listdir(path):
		#print("f: {}".format(f))
        base, ext = os.path.splitext(f)
        if ext=='.md':
            files.append(path + "/" + f)
	
    number_files =np.arange(len(files))
    files_with_no = np.hstack([np.vstack(number_files), np.vstack(files)])
    return files_with_no

def content(filename):
    with open(filename) as freader, open('try1.md', 'w') as writer:
        for line in freader:
            # print(line)
            rete = r'#' + ' '

            if r'### ' in line:
                print(line)
                line = '<style font-size: 8px;>' + line + '</style>\n'
            elif r'## 'in line:
                line = '<style font-size: 10px;>' + line + '</style>\n'
            elif r'# 'in line:
                line = '<style font-size: 15px;>' + line + '</style>\n'
            
            writer.write(line)


if __name__ == "__main__":
    # file_list = []
    get_file_list = inputfile_list()
    
    for x in range(len(get_file_list[:,0])):
        print(get_file_list[x,0], get_file_list[x,1])

    print("Insert -1 to stop the proce")
    print("Select the No.: ", end='')
    qn=int(input())

    choose_file = get_file_list[qn,1]

    content(choose_file) 

    print('finish')

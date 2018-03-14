import os
from pathlib import Path
import platform
import glob
import shutil
import string



print("1. Top 10 biggest files.")
print("2. Clean Desktop")
print("Enter Choice : ",end='')
choice=int(input())
if(choice==1):
####################
#
#   Getting top 10 Largest files.
#
####################
    top_10=[]
    file_info=[]
    #get system information
    sys_info=platform.system()

    def swap(a,i,k):
        temp=a[i]
        a[i]=a[k]
        a[k]=temp

    def sorting_file(file_info,top_10):
        for i in range(len(top_10)):
            temp=top_10[i]
            k=i
            for j in range(i+1,len(top_10),1):
                if(top_10[j]>temp):
                    temp=top_10[j]
                    k=j
            swap(top_10,i,k)
            swap(file_info,i,k)

    if(sys_info=="Windows"):
        a_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        print("Enter Drive no. to scan")
        for i in range(len(a_drives)):
            print((i+1),". ",a_drives[i],sep='')

        d=int(input())
        nameDrive=a_drives[d-1]+"\\"

    elif(sys_info=="Linux"):
        nameDrive=os.path.expanduser("~")

    #Scan and search files in given drive=>nameDrive
    for root,dirs,files in os.walk(nameDrive):
            for f in files:
                try:
                    fpath=os.path.join(root,f)
                    file_size=os.stat(fpath).st_size/1024
                    file_size /= 1024.0
                    if(len(top_10)<10):
                        top_10.append(file_size)
                        file_info.append(fpath)
                    else:
                        x=min(top_10)
                        if(file_size>x):
                            for i in range(10):
                                if(x==top_10[i] and x!=0):
                                    top_10[i]=file_size
                                    file_info[i]=fpath
                except:
                    pass

    print("Drives scanned....!")
    print("Here are top 10 largest files :")
    sorting_file(file_info,top_10)#sort the files Ascending order
    for i in range(len(top_10)):
        print(file_info[i],"   :   %0.2f MB"%top_10[i])
    
elif(choice==2):
    ####################
    #
    #   Desktop Path Directory
    #
    ####################
    #get desktop path
    deskHome=str(Path.home())
    home = os.path.join(deskHome,"Desktop")

    #list to contain file names and root name
    roots=[]
    #directories=[]
    fileNames=[]
    for r,d,f in os.walk(home):
        roots.append(r)
        #directories.append(d)
        fileNames.append(f)

    #####################
    #
    #  Getting Files
    #
    #####################

    #extensions for files to move to document folder
    img_files=['.gif','.png','.jpeg','.jpg']
    img_files+=[img_files[i].upper() for i in range(len(img_files))]
    img_files=tuple(img_files)
    office_files=['.pptx','.ppt','.xls','.xlsx','.docx','.odt','.ods','.xlr']
    office_files+=[office_files[i].upper() for i in range(len(office_files))]
    office_files=tuple(office_files)
    pdf_files=['.pdf']
    pdf_files+=[pdf_files[i].upper() for i in range(len(pdf_files))]
    pdf_files=tuple(pdf_files)
    video_files=['.mp4','.mpg','.mpeg','.mkv','.3gp','.mpg','.wmv']
    video_files+=[video_files[i].upper() for i in range(len(video_files))]
    video_files=tuple(video_files)
    music_files=['.mp3','.wav']
    music_files+=[music_files[i].upper() for i in range(len(music_files))]
    music_files=tuple(music_files)
    txt_files=['.txt']
    txt_files+=[txt_files[i].upper() for i in range(len(txt_files))]
    txt_files=tuple(txt_files)
    code_files=['.html','.htm','.js','.php','.cpp','.c','.py','.java',]
    code_files+=[code_files[i].upper() for i in range(len(code_files))]
    code_files=tuple(code_files)
    compressed_files=['.7z','.rar','.zip','.tar.gz']
    compressed_files+=[compressed_files[i].upper() for i in range(len(compressed_files))]
    compressed_files=tuple(compressed_files)

    extension_files=img_files+office_files+pdf_files+video_files+music_files+txt_files+code_files+compressed_files
    #print("EXTENSion : ",extension_files)

    #get the files in reqfiles[] if they have above given extensions
    reqfiles=[]
    for i in range(len(fileNames[0])):
        #print(fileNames[0][i])
        if(fileNames[0][i].endswith(extension_files)):
            reqfiles.append(fileNames[0][i])

    ####################
    #
    #   Creating Directories
    #
    ####################
    
    #get Documents folder
    docFolder=os.path.join(deskHome,"Documents")

    #Creating folders
    for i in range(len(reqfiles)):
        newPath=docFolder
        if(reqfiles[i].endswith(img_files)):
            newPath=os.path.join(newPath,"Image_Files")
        elif(reqfiles[i].endswith(office_files)):
            newPath=os.path.join(newPath,"MSOffice_Files")
        elif(reqfiles[i].endswith(pdf_files)):
            newPath=os.path.join(newPath,"PDF_Files")
        elif(reqfiles[i].endswith(video_files)):
            newPath=os.path.join(newPath,"Video_Files")
        elif(reqfiles[i].endswith(txt_files)):
            newPath=os.path.join(newPath,"Text_Files")
        elif(reqfiles[i].endswith(music_files)):
            newPath=os.path.join(newPath,"Music_Files")
        elif(reqfiles[i].endswith(code_files)):
            newPath=os.path.join(newPath,"Code_Files")
        elif(reqfiles[i].endswith(compressed_files)):
            newPath=os.path.join(newPath,"Compressed_Files")
        if not os.path.isdir(newPath):
            os.makedirs(newPath)

    ####################
    #
    #   Moving Files
    #
    ####################
    for i in range(len(reqfiles)):
        source=roots[0]
        destination=docFolder
        if(reqfiles[i].endswith(music_files)):
            source=os.path.join(roots[0],reqfiles[i])
            destination=os.path.join(docFolder,"Music_Files")
        elif(reqfiles[i].endswith(img_files)):
            source=os.path.join(roots[0],reqfiles[i])
            destination=os.path.join(docFolder,"Image_Files")
        elif(reqfiles[i].endswith(office_files)):
            source=os.path.join(roots[0],reqfiles[i])
            destination=os.path.join(docFolder,"MSOffice_Files")
        elif(reqfiles[i].endswith(pdf_files)):
            source=os.path.join(roots[0],reqfiles[i])
            destination=os.path.join(docFolder,"PDF_Files")
        elif(reqfiles[i].endswith(video_files)):
            source=os.path.join(roots[0],reqfiles[i])
            destination=os.path.join(docFolder,"Video_Files")
        elif(reqfiles[i].endswith(txt_files)):
            source=os.path.join(roots[0],reqfiles[i])
            destination=os.path.join(docFolder,"Text_Files")
        elif(reqfiles[i].endswith(code_files)):
            source=os.path.join(roots[0],reqfiles[i])
            destination=os.path.join(docFolder,"Code_Files")
        elif(reqfiles[i].endswith(compressed_files)):
            source=os.path.join(roots[0],reqfiles[i])
            destination=os.path.join(docFolder,"Compressed_Files")
        destination=os.path.join(destination,reqfiles[i])
        shutil.move(source,destination)
        
    docFolder=os.path.join(deskHome,"Documents")
    print("Desktop Cleaned....!")
    print("Files moved to : ",docFolder)
else:
    print("Wrong Input")
print("Press Enter")
input()

from os import listdir
from os.path import isfile, join
import os.path, time
import datetime
import os

if __name__ == '__main__':
    os.system('cls')

    myPath = "d:\\Lars\\Python_Test_Directory"

    currentTime = time.time()

    for fil in listdir(myPath):
        fullPath = join(myPath, fil)
        if isfile(fullPath):
            print(fullPath + " --> "+ fil)
            print("Last modified : " + time.ctime(os.path.getmtime(fullPath)))
            print("File created : " + time.ctime((os.path.getctime(fullPath))))
            fileTime = os.path.getctime(fullPath)
            #print("Filetime : "+ str(fileTime))
            print("Tid i dage mellem i dag og fil oprettelse dag : " + str((currentTime - fileTime) // (24 * 3600)))
            if ((currentTime - fileTime) // (24 * 3600)) >= 30:
                print(fil + " skal slettes !!!")
            else:
                fileInfo, fileExtension = os.path.splitext(fullPath)
                fileExtension = fileExtension.lower()
                if (((currentTime - fileTime) // (24 * 3600)) >= 7) and ( (".zip" == fileExtension) or (".rar" == fileExtension)):
                    print(fil + " er en pakket fil og skal slettes !!!")

            #os.remove()
            print("")

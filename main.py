#-Write_Read_Disk-#
import time
import os
import subprocess

def main():

    def test(sTime, path):
        testFile = os.path.join('Users/agishanimalthas/Downloads', 'File-j0o84.txt') 
        f = open('Users/agishanimalthas/Downloads','wb+')
        print ('getestet ...')
        for i in range(0,1600000):
           f.write('Schreibgeschwindigkeit im Prozess.')
        f.close()
        diff = time.clock() - sTime
        speed = (os.stat(testFile).st_size/1048576)/diff
        os.unlink(testFile)
        startTime = time.clock()
        return speed

    def selectPath():
        path = os.path.curdir
        # path option provided after detecting operating system
        if os.name == 'posix':
            print (subprocess.check_output("df"))
            path = raw_input("Möglichen Dateipfad anwählen bsp. ABC/User/Doc")
        if os.name == 'nt':
            path = raw_input("Enter the Drive Letter of Removale Drive. e.g I ")
            path= path.split(":")
    
        if not os.path.exists(path):
            print ('validen Pfad angeben')
            selectPath()
            
        return path

    path = selectPath()
    testFile = path+":/speedTest"
    print ("Geschwindigkeit wird berechnet")
    startTime = time.clock()
    speed = test(startTime, path)
    print ("Your disk drive speed is %s mb/sec" %speed)


if __name__ == "__main__":
    main()
    
#Dines Nimalthas
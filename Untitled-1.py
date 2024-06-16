import os
import subprocess
import zipfile

def brutecrack():
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                for d in range(1,10):
                    for e in range(1,10):
                        for f in range(1,10):
                            password=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                            
                            print(password)
                            
                            command= 'C:\\Program Files\\7-Zip\\7z.exe -p '+ password + ' t D:\\Temp\\111\\D.zip'

                            child = subprocess.call(command)

                            print(child)

                            if child == 0:
                                print("相册密码为：" + password)
                                return
if __name__ == '__main__':
    brutecrack()

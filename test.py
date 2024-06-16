# import sqlite3

# def connectDB():
#     sql3= sqlite3.connect(r"D:\\example.sqlite3")
#     print("Successful!!!")
def calc(D1,D2,H,P):
    D1=D1+10

    if D2 >=10 :
        D2=D2-10
    else:
        D2 = 0 
    
    H = H+10

    V = 3.1415*(D1*D1-D2*D2)*H/4.0

    ZhiLiang = V * P / 1000000
    
    
    print("质量=",ZhiLiang)

if __name__ == '__main__' :
    # connectDB()
    calc(460,240,30,8.5)



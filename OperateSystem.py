from BankSystem import BankSystem

BankSys=BankSystem()
while True:
    print("""***********欢迎使用ZT卡片管理系统***********
               1.显示卡片信息；
               2.新增卡片信息；
               3.删除卡片信息；
               4.修改卡片信息；
               5.保存卡片信息；
               6.退出系统；
               """)
    num=int(input("please enter 1-6:"))
    if num==1:
        BankSys.showCardInfo()
    elif num==2:
        BankSys.addCardInfo()
    elif num==3:
        BankSys.delCardInfo()
    elif num==4:
        BankSys.changeCardInfo()
    elif num==5:
        BankSys.isRecoder()
    elif num==6:
        print("thanks for using ZT system!")
        break
    else:
        pass


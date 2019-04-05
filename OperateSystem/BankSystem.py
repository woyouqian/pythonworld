import os
"""
编写一个卡片管理系统：
1.卡片信息包含卡片种类（kind），卡号（number），密码（password）；
2.每个卡片要有唯一的身份识别id；
3.对卡片可实现增加删除更改查找功能；
4.并要有相应的文本存档记录。
"""

class BankSystem(object):
    def __init__(self):
        self.banckCards=[]
        # 卡片信息文档存放路径！
        self.savePath="D:\\codefiles\\proj01\\cardinfo.txt"
        self.getRecoder()

    def addCardInfo(self):
        card={}
        cid=input("please enter idteny id:")
        ckind=input("please enter the bank'name:")
        cnum=input("please enter the card'number:")
        cpassword=input("please enter password:")
        # card={'id':cid,'kind':ckind,'num':cnum,'password':cpassword}
        card['id']=cid
        card['kind']=ckind
        card['num']=cnum
        card['password']=cpassword
        if card:
            # print(card)
            self.banckCards.append(card)

    def showCardInfo(self):
        # cardTxt=open("D:\\codefiles\\proj01\\cardinfo.txt", 'r')
        # allInfo=cardTxt.readlines()
        # if allInfo:
        #     for info in allInfo:
        #         if info != '\n':
        #             msg=info.split('\t')
        #             card = {
        #                     'id':msg[0],
        #                     'kind':msg[1],
        #                     'num':msg[2],
        #                     'password':msg[3].rstrip('\n')
        #                     }
        #             self.banckCards.append(card)
        # cardTxt.close()
        if self.banckCards:
            for card in self.banckCards:
                print(card)
        else:
            print('there is no any card recoder!' )

    def delCardInfo(self):
        if self.banckCards:
            cid=input("please enter idteny id which one you would delete:")
            flag = True
            for i in range(len(self.banckCards)):
                if self.banckCards[i]['id']==cid:
                    print(self.banckCards[i]['kind'],end='\t')
                    print(self.banckCards[i]['num'])
                    psd=input("are you sure del this card? enter the password:")
                    if self.banckCards[i]['password']==psd:
                        # card.clear()
                        del self.banckCards[i]
                        # print(self.banckCards)
                        flag=False
                    else:
                        print("you have give up!")
                    break
            if flag:
                print("please confirm again!")
        else:
            print('there is no any card recoder!' )

    def changeCardInfo(self):
        if self.banckCards:
            cid=input("please enter idteny id which one you would change:")
            flag = True
            for card in self.banckCards:
                if card['id']==cid:
                    ckind = input("please enter the bank'name:")
                    cnum = input("please enter the card'number:")
                    cpassword = input("please enter password:")
                    if ckind:
                        card['kind']=ckind
                    if cnum:
                        card['num']=cnum
                    if cpassword:
                        card['password']=cpassword
                    flag=False
                    break
            if flag:
                print("please confirm again!")
        else:
            print('there is no any card recoder!' )


    def isRecoder(self):
        if self.banckCards:
            with open(self.savePath,'w') as cardTxt:
                for card in self.banckCards:
                    info='\n'+card['id']+'\t'+card['kind']+'\t'+card['num']+'\t'+card['password']
                    cardTxt.write(info)
        else:
            print('there is no any card recoder!' )

    def getRecoder(self):
        # cardTxt = open("D:\\codefiles\\proj01\\cardinfo.txt", 'r')
        isExists=os.path.exists(self.savePath)
        if not isExists:
        # if isExist==False:
            open(self.savePath,'w')
        with open(self.savePath, 'r') as cardTxt:
            allInfo = cardTxt.readlines()
            if allInfo:
                for info in allInfo:
                    if info != '\n':
                        msg=info.split('\t')
                        card={
                              'id': msg[0],
                              'kind': msg[1],
                              'num': msg[2],
                              'password': msg[3].rstrip('\n')
                              }
                        self.banckCards.append(card)
        # cardTxt.close()


'''
BankSys=BankSystem()
# BankSys.addCardInfo()
BankSys.showCardInfo()
# BankSys.delCardInfo()
# BankSys.showCardInfo()
# BankSys.isRecoder()
# BankSys.changeCardInfo()
# BankSys.showCardInfo()
'''
if __name__=='__main__':
    pass



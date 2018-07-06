# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180705","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# 로그인 처리 모듈 만들어보기
#
# - 회원가입으로 아이디, 패스워드, 이름 입력받기
# - 아이디는 이메일 형식
# - 패스워드는 길이 6~12자, 영문자와 숫자를 포함해야함, 영문 대문자는 불허용
# - 로그인버튼으로 아이디와 패스워드 입력하면 "{이름}님 환영합니다!

class DATABASE:
    __accountlist = []
    __accountnum = 0

    def newaccount(self,d):
        self.__accountlist.append(d)
        self.__accountnum += 1

    def showall(self):
        print("회원 수 :",self.__accountnum)
        idx = 0
        for i in self.__accountlist:
            print("[%d]"%(idx+1),i)
            idx+=1

    def login(self):
        inputid = input("이메일를 입력하세요 : ")
        if inputid.count('@') == 0:
            print("(Error) 이메일을 입력하세요")
            self.login()
        else:
            pass
        temp = re.findall("(\w+[\w\.]*)@(\w+[\w\.]*)", inputid)

        for i in self.__accountlist:
            if i.get('ID') == temp[0][0] and i.get('HOST')==temp[0][1]:
                inputpw = input("패스워드를 입력하세요 : ")
                if i.get('PWD')==inputpw :
                    print("\n# "+i.get('NAME')+"님이 로그인하셨습니다.")
                    return

                else:
                    print("(Error) 패스워드가 틀렸습니다.")
                    return

        else:
            print("(Error) 일치하는 회원 정보가 없습니다.")

    def BACKUP(self):
        with open("list_backup.bin","wb") as f:
            for i in self.__accountlist:
                pickle.dump(i,f)
        with open("count_backup.bin","wb") as f:
            pickle.dump(self.__accountnum,f)

    def LOAD(self):
        with open("list_backup.bin","rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
                self.__accountlist.append(data)
        with open("count_backup.bin","rb") as f:
            self.__accountnum=pickle.load(f)

    def DELETE(self,choice):
        while True:
            choice = input("# 삭제할 회원 번호 (없으면 0) : ")
            if (choice == "0"):
                break

            elif choice.isdigit() == False:
                print("(Error) 번호를 입력해야 합니다.")
                continue

            elif (int)(choice) >= 1 and (int)(choice) <= self.__accountnum:
                print("# {0} 회원의 {1}@{2} 계정 정보가 삭제되었습니다.\n".format(self.__accountlist[(int)(choice)-1].get('NAME'),
                                                                   self.__accountlist[((int)(choice))-1].get('ID'),
                                                                   self.__accountlist[((int)(choice)) - 1].get('HOST')))
                del self.__accountlist[((int)(choice))-1]
                self.__accountnum -= 1
                self.showall()
            else:
                print("(Error) 유효하지 않은 번호입니다.")
                continue

class ACCOUNT(DATABASE):
    ID = str()
    ID_host = str()
    __PW = str()
    __NAME = str()

    def set_ID(self):
        id = input("[ID] 이메일 입력 : ")
        if id.count('@') == 0:
            print("(Error) 이메일을 입력하세요")
            self.set_ID()
        else:
            temp = re.findall("(\w+[\w\.]*)@(\w+[\w\.]*)",id)
            self.ID = temp[0][0]
            self.ID_host = temp[0][1]

    def set_PW(self):
        pw = input("[PW] 패스워드 입력(6~12자리) : ")
        if len(pw)<6:
            print("(Error) 비밀번호가 너무 짧습니다.")
            self.set_PW()
        elif len(pw) > 12:
            print("(Error) 비밀번호가 너무 깁니다")
            self.set_PW()
        elif re.search("[^a-z0-9]",pw):
            print("(Error) 소문자와 숫자만 사용가능합니다")
            self.set_PW()
        else:
            pwagain = input("[PW] 패스워드 재입력 : ")
            if pwagain != pw :
                print("(Error) 비밀번호가 일치하지 않습니다.")
                self.set_PW()
            else:
                self.__PW = pw
    def set_NAME(self):
        name = input("[NAME] 이름 입력 : ")
        self.__NAME = name

    def complete(self):
        keys = ('ID','HOST','PWD','NAME')
        values = (self.ID, self.ID_host, self.__PW, self.__NAME)
        d = dict(zip(keys,values))
        print("\n# \'"+self.__NAME + "\'님 회원가입을 축하드립니다.")
        return d







import re
import pickle
#with open("backup.json","rb") as f:
#    DB = DATABASE()
#    DB = json.load(f)

DB = DATABASE()
DB.LOAD()




while True:
    print("-------------------------------------------------")
    print("1. 회원가입", "2. 로그인", "3. 관리모드", "4. 종료", sep="\n")
    choice = input(">> ")
    if choice == "회원가입" or choice == "1":
        print("# 회원가입을 시작합니다.")
        newuser = ACCOUNT()
        newuser.set_ID()
        newuser.set_PW()
        newuser.set_NAME()
        DB.newaccount(newuser.complete())
    elif  choice == "로그인" or choice == "2":
        DB.login()
        pass
    elif  choice == '관리모드' or choice == "3":
        DB.showall()
        DB.DELETE(choice)

    elif choice == "종료" or choice == "4":
        DB.BACKUP()
        print("백업 후, 종료합니다.")
        break

    else:
        print("잘못된 입력입니다.")
        continue
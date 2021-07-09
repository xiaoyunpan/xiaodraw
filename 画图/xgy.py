import easygui,xjh,main
def xgy():
    choice=easygui.buttonbox("""                      程序由上晋编写及编译
                      语言:Python
                      模块:turtle,easygui
                      感谢大家的支持！
                      官方网站:https://soft.xiaoyunpan.cn""",
            choices = ['OK'])
    if choice == 'OK':
        main.main()

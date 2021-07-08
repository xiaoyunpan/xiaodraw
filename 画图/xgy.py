import easygui,xjh,main
def xgy():
    choice=easygui.buttonbox("""                      程序由上晋编写及编译
                      语言:Python
                      模块:turtle,easygui
                      感谢大家的支持！
                      官方网站:https://soft.xiaoyunpan.cn""",
            choices = ['激活','返回主菜单'])
    if choice == '激活':
        xjh.jh()
    if choice == '返回主菜单':
        main.main()

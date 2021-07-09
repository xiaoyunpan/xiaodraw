#***********************************************
#本主程序由上晋开发                          *
#上晋的软件官方网站: https://soft.xiaoyunpan.cn*
#***********************************************
import easygui,xdq,xgy,xht
def main():
    h_c=easygui.buttonbox("欢迎使用由上晋开发的画图程序！请问您要进行哪一种操作?",
                choices = ['画图','关于','退出'])
    if h_c == '退出':
        xdq.xdq()
    if h_c == '关于':
        xgy.xgy()
    if h_c == '画图':
        xht.xht()


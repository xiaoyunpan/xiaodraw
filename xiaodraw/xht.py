#***********************************************
#本画图主程序程序由上晋开发                    *
#上晋的软件官方网站: https://soft.xiaoyunpan.cn*
#***********************************************
import easygui,xht_k,main
def xht():
        d_c = easygui.choicebox("请选择一种操作",
                      choices = ['画矩形','画方形','自定义','返回主菜单'])
        if d_c == '返回主菜单':
                main.main()
        if d_c == '画矩形':
                xht_k.hux()
        if d_c == '画方形':
                xht_k.fx()
        if d_c == '自定义':
                xht_k.hx()

#***********************************************
#本画图主程序程序由上晋开发                    *
#上晋的软件官方网站: https://soft.xiaoyunpan.cn*
#***********************************************
import easygui,xht_k,main,xjh
def xht():
        d_c = easygui.choicebox("请选择一种操作",
                      choices = ['画圆形','画方形','自定义','返回主菜单'])
        if d_c == '返回主菜单':
                main.main()
        if d_c == '自定义':
                try:
                        f2=open('htjh.ini','r')
                        jh=f2.readline()
                        f2.close
                except:
                        jh=False
                if jh=='True':
                        xht_k.hx()
                else:
                        xjh.jh()
                        

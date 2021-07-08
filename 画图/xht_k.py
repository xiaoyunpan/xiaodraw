"""
本代码模块由上晋开发
上晋的软件官方网站: https://soft.xiaoyunpan.cn
"""
import turtle,easygui,xht
t=turtle
def hx():
    hx_f=easygui.enterbox("请问您需要多长的横线?")
    t.forward(int(hx_f))

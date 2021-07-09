"""
本代码模块由上晋开发
上晋的软件官方网站: https://soft.xiaoyunpan.cn
"""
import turtle,easygui,xht
def hx():
    hx_c=easygui.choicebox("请选择画笔颜色...",
                 choices = ['红','蓝','黄','黑'])
    if hx_c=='红':
        turtle.color('red')
    if hx_c=='蓝':
        turtle.color('blue')
    if hx_c=='黄':
        turtle.color('yellow')
    if hx_c=='黑':
        turtle.color('black')
    try:
        hx_ch=easygui.enterbox("请输入横线长度...")
        hx_ich=int(hx_ch)
        turtle.forward(hx_ich)
    except:
        easygui.msgbox("错误！请输入不含单位的数字！并确保您没有进行违规操作！")
 

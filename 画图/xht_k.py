"""
本代码模块由上晋开发
上晋的软件官方网站: https://soft.xiaoyunpan.cn
"""
import turtle,easygui,xht
def hx():
    hx_c=easygui.choicebox("请选择画笔颜色... / Please choose a brush color...",
                 choices = ['Red','Blue','Yellow','Black'])
    if hx_c=='红':
        turtle.color('red')
    if hx_c=='蓝':
        turtle.color('blue')
    if hx_c=='黄':
        turtle.color('yellow')
    if hx_c=='黑':
        turtle.color('black')
    try:
        hx_xc=easygui.enterbox("请输入横线粗度... / Please enter the thickness of the horizontal line...")
        hx_ixc=int(hx_xc)
        turtle.turtlesize(hx_ixc)
    except Exception as error:
        easygui.msgbox("Error！请输入不含单位的数字！并确保您没有进行违规操作！",error)
    try:
        hx_ch=easygui.enterbox("请输入横线长度... / Please enter the length of the horizontal line...")
        hx_ich=int(hx_ch)
        turtle.forward(hx_ich)
    except Exception as error:
        easygui.msgbox("Error！请输入不含单位的数字！并确保您没有进行违规操作！",error)
    try:
        hx_zj=easygui.enterbox("请输入转角角度(左)... / Please enter the corner angle(left)...")
        hx_izj=int(hx_zj)
        turtle.left(hx_izj)
    except Exception as error:
        easygui.msgbox("Error！请输入不含单位的数字！并确保您没有进行违规操作！",error)

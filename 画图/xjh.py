"""
本代码模块由上晋开发
上晋的软件官方网站: https://soft.xiaoyunpan.cn
"""
import turtle,easygui,xht
pen=turtle
def hx():
    try:
        hx_xc=easygui.enterbox("请输入横线粗度... / Please enter the thickness of the horizontal line...")
        hx_ixc=int(hx_xc)
        pen.pensize(hx_ixc)
    except Exception as error:
        easygui.msgbox("Error！请输入不含单位的数字！并确保您没有进行违规操作！",error)

    hx_c=easygui.choicebox("请选择画笔颜色... / Please choose a brush color...",
                 choices = ['Red','Blue','Yellow','Black'])
    if hx_c=='Red':
        pen.pencolor('red')
    if hx_c=='Blue':
        pen.pencolor('blue')
    if hx_c=='Yellow':
        pen.pencolor('yellow')
    if hx_c=='Black':
        pen.pencolor('black')
    try:
        hx_ch=easygui.enterbox("请输入横线长度... / Please enter the length of the horizontal line...")
        hx_ich=int(hx_ch)
        pen.forward(hx_ich)
    except Exception as error:
        easygui.msgbox("Error！请输入不含单位的数字！并确保您没有进行违规操作！",error)
    try:
        hx_zj=easygui.enterbox("请输入转角角度(左)... / Please enter the corner angle(left)...")
        hx_izj=int(hx_zj)
        pen.left(hx_izj)
    except Exception as error:
        easygui.msgbox("Error！请输入不含单位的数字！并确保您没有进行违规操作！",error)

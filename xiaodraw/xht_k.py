"""
本代码模块由上晋开发
上晋的软件官方网站: https://soft.xiaoyunpan.cn
"""
import turtle,easygui,xht
pen=turtle

#横线库
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

#弧线库
def hux():
    try:
        hux_xc=easygui.enterbox("请输入横线粗度... / Please enter the thickness of the horizontal line...")
        hux_ixc=int(hux_xc)
        pen.pensize(hux_ixc)
    except Exception as error:
        easygui.msgbox("Error！请输入不含单位的数字！并确保您没有进行违规操作！",error)

    hux_c=easygui.choicebox("请选择画笔颜色... / Please choose a brush color...",
                 choices = ['Red','Blue','Yellow','Black'])
    if hux_c=='Red':
        pen.pencolor('red')
    if hux_c=='Blue':
        pen.pencolor('blue')
    if hux_c=='Yellow':
        pen.pencolor('yellow')
    if hux_c=='Black':
        pen.pencolor('black')
    try:
        hux_bj=easygui.enterbox("请输入弧线半径... / Please enter the length of the horizontal line...")
        hux_ibj=int(hux_bj)
    except Exception as error:
        easygui.msgbox("Error！请输入不含单位的数字！并确保您没有进行违规操作！",error)
    try:
        hux_hd=easygui.enterbox("请输入弧线弧度... / Please enter the length of the horizontal line...")
        hux_ihd=int(hux_hd)
        pen.circle(hux_ibj,hux_ihd)
    except Exception as error:
        easygui.msgbox("Error！请输入不含单位的数字！并确保您没有进行违规操作！",error)

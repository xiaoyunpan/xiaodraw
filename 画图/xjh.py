import easygui,urllib.request,main,openkey
def jh():
    try:
        f=open('_jh_.key','r')
        wbjh=f.readline()
        f.close()
    except:
        f=open('_jh_.key','w')
        f=open('_jh_.key','r')
        wbjh=f.readline()
        f.close()
    try:
        wjh=urllib.request.urlopen('https://oss.shandianpan.com/b908ee1249ecba86b6309dad811b119c.doc')
        rjh=wjh.read().decode('utf-8')
    except:
        choice=easygui.buttonbox("网络错误，无法从服务器获取激活信息！",
                       choices = ['确定'])
        if choice == '确定':
            main.main()
    try:
        if wbjh == 'eb2e0a6306fbfbaff264b5315fb17a434124e4f296b1452276932':
            choice=easygui.buttonbox("您已激活，可以使用全部功能，感谢您对上晋的支持！",
                    choices = ['确定'])
            if choice == '确定':
                main.main()
        else:
            sjh=easygui.enterbox("""                            您尚未激活，请立即输入密钥激活以确保所有功能可用！
                                密钥是免费的，您可以从《上晋的生活记录》丛书中寻
                                找或通过上晋的云盘获取""")
            if sjh == rjh:
                openkey.open_key_jh()
                choice=easygui.buttonbox("激活成功！",
                               choices = ['确定'])
                if choice == '确定':
                    main.main()
            else:
                choice=easygui.buttonbox("密钥错误！",
                               choices = ['确定'])
                if choice == '确定':
                    main.main()
    except Exception as error:
        easygui.msgbox("""                          警告
                          发生错误，程序被迫终止！错误代码详见错误提示程序标题栏。
                          请确保您没有进行违规操作，稍后您可以自行关闭程序。
                          如果您无法关闭程序，请强制关闭。如果以后仍然出现错误，请联系我们。
                          如果您要联系技术支持人员，请将错误代码告知他们。""",error)


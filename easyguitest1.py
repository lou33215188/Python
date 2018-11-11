import easygui as easy

msg = "请输入您的信息"
title = "账户中心"
fields_name = ["*用户名",  "*真实姓名", "固定电话", "*手机号码", "QQ", "*E—mail"]
fields_value = easy.multenterbox(msg, title, fields_name)

while True:
    if fields_value is None:
        break
    errmsg = ""
    for i in range(len(fields_name)):
        option = fields_name[i].strip()
        if fields_value[i].strip() == "" and option[0] == "*":
            errmsg += ("[%s]为必须填\n\n" % fields_name[i])
    if errmsg == "":
        break
    else:
        easy.msgbox("%s" % errmsg)
    easy.msgbox("请重新输入！\n")
    fields_value = easy.multenterbox(msg, title, fields_name)
easy.msgbox("保存成功，用户资料如下：%s" % str(fields_value))

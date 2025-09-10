label start:
    # 显示欧洲形势地图和旁白
    scene europe_map
    show cover_image
    hide cover_image with fade
    "1933年，德国法西斯上台后，对周边国家采取蚕食吞并政策，严重威胁英国、法国、苏联等国家的边防安全。"
    "经济和政治局势的动荡导致谋杀率大幅增加，绑架案四处频发。西欧各国对德国采取绥靖政策，牺牲小国家、商人和贫民利益换取并不长久的国家安全。"
    "西装革履的英法贵族为保全自身，不断签订各种条约，将周边小国推入法西斯的血盆大口。"
    "而沦陷区的国家支离破碎，人民流离失所，难以维生，匪盗猖獗。"

    # 显示列车视频和旁白
    scene black
    show expression Movie(play="video/train_running.webm", loop=True, size=(1920, 1080)) as movie
    with fade
    "1938年1月15日，由苏联莫斯科开往法国南林克港的列车正疾行在波兰平原上。车上载满官员、贵族和刚刚签订完《英苏-法苏合作条约》的外交官们。"
    "刚处理完苏联的一桩法律案件，疲惫不堪的你乘坐这趟车准备回英国享受假期。"
    stop movie
    hide movie
    "正当你准备休息时，一张从你口袋中滑落的旧照片让你陷入了回忆..."

    call screen clickable_calgary_image

label detective_background:
    show expression "images/Calgary_Ham_old.jpeg" at truecenter
    "你是一名来自英国约克郡的侦探，名叫卡尔加利·海姆(Calgary Ham)。"
    "你出生于侦探世家，从小拜读夏洛克福尔摩斯的著作。"
    "1921年，你进入伦敦警探专门学校学习，并在毕业后经营一家小侦探所。"
    menu:
        "继续":
            jump night

label night:
    # 显示夜间车厢和旁白
    scene background2 with fade
    "夜间，由于愈发强烈的暴风雪，列车只得临时停车，并熄灭大多数煤气灯以保证仅剩燃料的持续供应。"
    "昏暗而逼仄的车厢内，被困的人们焦虑而又恐惧地等待。"
    "当车厢中的不安气氛达到顶峰时，第十四与十五节车厢的连接处传来一声尖叫，然后是两三声沉闷的枪响。"
    "本就不安的乘客中，尖叫声此起彼伏，惊慌地四散奔逃。"

    # 显示死者图片和旁白
    show expression Movie(play="video/detective_inspecting.webm", loop=False, size=(1920, 1080)) as movie
    with fade
    "你以最快的速度奔向枪声响起的地方，但是太迟了……"
    stop movie
    hide movie
    scene victim_blood with fade
    "中弹者倒在血泊中，毛发散乱，瞳孔放大，苍白的脸扭曲而惊愕，伸手探去早已没了鼻息。"
    pause 2.0
    "由于案件发生突然，车厢狭窄拥挤，你断定凶手仍在现场不远处。"
    scene suspects_lineup with fade
    "通过简单取证与对比，你锁定了邻近3节车厢内的5名嫌疑人，准备进一步进行审问。可直觉告诉你，这件谋杀案的背后根本没有你想的那么简单......."

label main_menu_1:
    hide screen interrogation_controls
    scene background2 with fade
    menu:
        "调查死者信息":
            jump victim_info
        "查看嫌疑人信息":
            jump suspect_info
        "审讯嫌疑人":
            jump interrogation_menu
        "指认凶手":
            jump accuse_culprit

label victim_info:
    show victim_blood with fade
    "经过调查，死者名为萨缪尔(Samiur)，是一个臭名昭著的罪犯。1935年罗霍姆绑架案的凶手，截至被害前仍在四处潜逃。"
    "他原为奥地利莱姆尼安家族长子，后家道中落，故乡沦陷，父母遭遇意外死亡，贫困潦倒，不得不通过绑架索取赎金为生。"
    menu:
        "返回":
            jump main_menu_1

# 嫌疑人信息查看界面
label suspect_info:
    scene suspects_lineup with fade
    menu:
        "蒙特夫(Monteff)":
            show monteff at center with dissolve
            "范德·蒙特夫(Fond Monteff) - 法国外交大臣阿兰德·蒙特夫的妻子，著名戏剧演员弗洛尼亚的女儿。女儿黛西·蒙特夫是当年罗霍姆绑架案的受害人之一，她在交付 15 万英镑的赎金之后，看到的是女儿的尸体，她至少已经死了一个多星期。"
            hide monteff with dissolve
            jump suspect_info
        "霍夫曼(Hoffman)":
            show hoffman at center with dissolve
            "拉杰特·杨·霍夫曼(Rhajeat young Hoffman) - 英国激进派议员，极度反对社会上蔓延的妥协思潮，据他所述，'需要制造一场令人震惊的案件，才能让反对我的那些蠢人警醒'。"
            hide hoffman with dissolve
            jump suspect_info
        "克里姆塔涅夫斯基(Kremtanivsky)":
            show kremtanivsky at center with dissolve
            "克里姆塔涅夫斯基(Kremtanivsky) - 原苏联列宁格勒第三区警察局长，因管辖区发生重大绑架撕票案而遭到免职。只希望抓到凶手严惩以报仇雪恨，可碍于凶手身份扑朔迷离至今未果。"
            hide kremtanivsky with dissolve
            jump suspect_info
        "约翰(John)":
            show john at center with dissolve
            "约翰·曼尼普尔(John Manipur) - 原英属印度军官，三年前被调回欧洲应对即将爆发的战争。在一年前的巴伐利亚冲突中，他的父亲、弟弟、姐姐均葬身于德国统领下的莱姆尼安雇佣军的炮火中。"
            hide john with dissolve
            jump suspect_info
        "苏和华(Sok)":
            show sok at center with dissolve
            "苏和华(Sok Tor Hof) - 法属越南商人，12 年前西贡走私大案，三岁的儿子在港口玩耍时被装上货船带走，至今下落不明。寻子心切的他在得到线索后只身赶赴欧洲寻子，等来的却是儿子早已遇害的消息。"
            hide sok with dissolve
            jump suspect_info
        "返回":
            jump main_menu_1

# 审讯选择菜单
label interrogation_menu:
    scene background2 with fade
    "请选择要审讯的嫌疑人:"
    menu:
        "提示: 在审讯过程中，你可以随时点击右上角\"返回主菜单\"按钮"
        "蒙特夫(Monteff)":
            jump interrogate_monteff
        "霍夫曼(Hoffman)":
            jump interrogate_hoffman
        "克里姆塔涅夫斯基(Kremtanivsky)":
            jump interrogate_kremtanivsky
        "约翰(John)":
            jump interrogate_john
        "苏和华(Sok)":
            jump interrogate_sok
        "返回":
            jump main_menu_1

label accuse_culprit:
    scene suspects_lineup with fade
    "请选择要指控的嫌疑人:"
    menu:
        "蒙特夫(Monteff)":
            jump ending_monteff
        "霍夫曼(Hoffman)":
            jump ending_hoffman
        "克里姆塔涅夫斯基(Kremtanivsky)":
            jump ending_kremtanivsky
        "约翰(John)":
            jump ending_john
        "苏和华(Sok)":
            jump ending_sok
        "返回":
            jump main_menu_1

label finish:
    window hide
    scene finish with dissolve
    pause 2.0
    scene black with dissolve
    return


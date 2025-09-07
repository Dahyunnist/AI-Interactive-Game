label start:
    scene cover_image with fade
    show text "{size=150}伊维利亚列车大劫案{/size}" at truecenter with dissolve
    pause
    hide text with dissolve

    # 显示欧洲形势地图和旁白
    scene europe_map with fade

    "1933年，德国法西斯上台后，对周边国家采取蚕食吞并政策，严重威胁英国、法国、苏联等国家的边防安全。"
    "经济和政治局势的动荡导致谋杀率大幅增加，绑架案四处频发。西欧各国对德国采取绥靖政策，牺牲小国家、商人和贫民利益换取并不长久的国家安全。"
    "西装革履的英法贵族为保全自身，不断签订各种条约，将周边小国推入法西斯的血盆大口。"
    "而沦陷区的国家支离破碎，人民流离失所，难以维生，匪盗猖獗。"

    # 显示列车视频和旁白
    scene black
    show expression Movie(play="video/train.webm", loop=True, size=(1920, 1080)) as movie
    with fade

    "1938年1月15日，由苏联莫斯科开往法国南林克港的列车正疾行在波兰平原上。车上载满官员、贵族和刚刚签订完《英苏-法苏合作条约》的外交官们。"
    "刚处理完苏联的一桩法律案件，疲惫不堪的你乘坐这趟车准备回英国享受假期。"

    stop movie
    hide movie

    # 显示夜间车厢和旁白
    scene background2 with fade
    "夜间，由于愈发强烈的暴风雪，列车只得临时停车，并熄灭大多数煤气灯以保证仅剩燃料的持续供应。"
    "昏暗而逼仄的车厢内，被困的人们焦虑而又恐惧地等待。"
    "当车厢中的不安气氛达到顶峰时，第十四与十五节车厢的连接处传来一声尖叫，然后是两三声沉闷的枪响。"
    "本就不安的乘客中，尖叫声此起彼伏，惊慌地四散奔逃。"

    # 显示死者图片和旁白
    scene victim_blood with fade
    "当你赶到时，只见到中弹者倒在血泊中，毛发散乱，瞳孔放大，苍白的脸扭曲而惊愕，伸手探去早已没了鼻息。"

    scene suspects_lineup
    "经过调查，死者名为萨缪尔，是一个臭名昭著的罪犯。由于案件发生突然，车厢狭窄拥挤，你断定凶手仍在现场不远处。"
    "通过简单取证与对比，你锁定了邻近3节车厢内的5名嫌疑人，准备进一步进行审问。可直觉告诉你，这件谋杀案的背后根本没有你想的那么简单......."


label main_menu_1:
    scene background2 with fade
    menu:
        "查看嫌疑人信息":
            jump suspect_info
        "开始审讯":
            jump interrogation_menu
        "给出推理":
            jump accuse_culprit

# 嫌疑人信息查看界面
label suspect_info:
    scene suspects_lineup with fade
    menu:
        "范德蒙特夫":
            show fond at center with dissolve
            "范德蒙特夫 - 法国外交大臣阿兰德·蒙特夫的妻子，著名戏剧演员弗洛尼亚的女儿。女儿黛西·蒙特夫是当年罗霍姆绑架案的受害人之一。"
            hide fond with dissolve
            jump suspect_info
        "霍夫曼":
            show hoffman at center with dissolve
            "拉杰特·杨·霍夫曼 - 英国激进派议员，极度反对社会上蔓延的妥协思潮，据他所述，'需要制造一场令人震惊的案件，才能让反对我的那些蠢人警醒'。"
            hide hoffman with dissolve
            jump suspect_info
        "克里姆塔涅夫斯基":
            show kremtanivsky at center with dissolve
            "克里姆塔涅夫斯基 - 原苏联列宁格勒第三区警察局长，因管辖区发生重大绑架撕票案而遭到免职。只希望抓到凶手严惩以报仇雪恨。"
            hide kremtanivsky with dissolve
            jump suspect_info
        "约翰":
            show john at center with dissolve
            "约翰·曼尼普尔 - 原英属印度军官，三年前被调回欧洲应对即将爆发的战争。在一年前的巴伐利亚冲突中，他的父亲、弟弟、姐姐均葬身于德国统领下的莱姆尼安雇佣军的炮火中。"
            hide john with dissolve
            jump suspect_info
        "苏和华":
            show sok at center with dissolve
            "苏和华 - 法属越南商人，12年前西贡走私大案，三岁的儿子在港口玩耍时被装上货船带走，至今下落不明。寻子心切的他在得到线索后只身赶赴欧洲寻子，等来的却是儿子早已遇害的消息。"
            hide sok with dissolve
            jump suspect_info
        "返回":
            jump main_menu_1

    # 审讯选择菜单
    label interrogation_menu:
        scene background2 with fade
        "请选择要审讯的嫌疑人:"
        menu:
            "范德蒙特夫(monteff)":
                jump to_do
            "霍夫曼(Hoffman)":
                jump interrogate_hoffman
            "克里姆塔涅夫斯基":
                jump to_do
            "约翰(john)":
                jump to_do
            "苏和华":
                jump to_do
            "返回":
                jump main_menu_1

# ==== 审讯霍夫曼 ====
label interrogate_hoffman:
    
    scene empty_room with fade
    show hoffman at center with dissolve

    hoffman "（双手交叉）侦探先生，您随便问，但我只能回答您五个问题"
    
    # 5-round dialogue loop
    python: 
        # hoffman_states = {
        #         "平静": "video/hoffman_idle.webm",
        #         "谨慎": "video/hoffman_serious.webm",
        #         "慌张": "video/hoffman_nervous.webm",
        #         "愤怒": "video/hoffman_angry.webm"
        #     }
        round_num = 0
        while round_num < 5:  
            renpy.say(calgary, f"第{round_num+1}/5轮：你要问hoffman什么？")
            question = renpy.input(f"问题 {round_num+1}: ", length = 100).strip()
            if not question:
                renpy.say(None, "请输入有效问题")
                continue

            # 角色一边做出回答，一边播放情绪对应的动画
            current_emotion, clean_response = interrogate(question, "hoffman")
            renpy.say(hoffman, clean_response)
            round_num += 1
            # narration_queue = [clean_response]
            # character_saying(hoffman_states[current_emotion], hoffman)
            # renpy.pause(0.3)
    
    # 结束审讯
    # $ narration_queue = [
    #     "好了，侦探先生，我对这些感到厌烦了，我相信我们都需要休息一下"
    # ]
    # python:
    #     character_saying("video/hoffman_standing.webm", hoffman)
    hoffman "好了，侦探先生，我对这些感到厌烦了，我相信我们都需要休息一下"
    
    # 霍夫曼离开
    # pause(1.5)
    # $ renpy.movie_cutscene("video/hoffman_leaving.webm") 
    show hoffman:
        easeout 1.0 xoffset 2000
    with dissolve
    pause 3.0
    
    "霍夫曼离开了审讯室。"

    jump main_menu_1

    $ interrogated_suspects.add("hoffman")

label to_do:
    "待完成"
    menu:
        "返回":
            jump main_menu_1

# ==== Culprit accusation (trigger after all interrogations) ====
label accuse_culprit:
    scene background1 with fade
    "请选择要指控的嫌疑人:"
    menu:
        "范德蒙特夫(monteff)":
            jump ending_wrong
        "霍夫曼(Hoffman)":
            jump ending_correct
        "克里姆塔涅夫斯基":
            jump ending_wrong
        "约翰(john)":
            jump ending_wrong
        "苏和华":
            jump ending_wrong
        "返回":
            jump main_menu_1

label ending_correct:
    calgary "真相只有一个————Hoffman, 你就是凶手！"
    hoffman "（脸色惨白）是的，他毁掉了我的生活……"
    "案件解决，你抓住了真凶！"
    return

label ending_wrong:
    "你做出了错误的推理，真凶顺利逍遥法外……"
    return

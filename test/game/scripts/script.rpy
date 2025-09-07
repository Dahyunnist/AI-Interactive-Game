##### 角色
# 约翰·曼尼普尔上校 John Manipur
define manipur = Character("约翰·曼尼普尔上校", what_size = 75, who_size = 45, color="#ff99cc")    # Pink dialogue
# 拉杰特·杨·霍夫曼 Rhajeat young Hoffman
define hoffman = Character("拉杰特·杨·霍夫曼", color="#99ccff", image = "hoffman")  # Blue dialogue
# 范德蒙特夫Fond Monteff
define monteff = Character("范德蒙特夫", color="#ccff99", image = "monteff")    # Green dialogue
# 卡尔加利·海姆 Calgary Ham
define detective = Character("卡尔加利·海姆", color="#ffff99")  # Yellow dialogue
# 旁白
define back = Character("旁白", what_prefix='"', what_suffix='"', what_slow_cps=20)

# 已审讯过的嫌疑人
$ interrogated_suspects = []

# 功能：播放动画时渐次展示旁白
default narration_queue = []
default current_narration = ""
label play_animated_narration(video_path, character):
    # 显示视频
    show expression Movie(
        play = video_path,
        size = (config.screen_width, config.screen_height),
    ) as video_player
    # 使用角色对话系统显示旁白
    python:
        for text in narration_queue:
            character(text, interact=False)
            renpy.pause(len(text)/20.0 + 5)  # 句间间隔5秒
    # 清理
    hide video_player
    return



image cover: 
    "images/train.png"  # Main background (东方快车车厢)
    zoom 2.5
image carriage: 
    "images/carriage.png"
    zoom 3.7

image carriage_dark:
    "images/carriage_dark.png"
    zoom 3.7

image map:
    "images/map.png"

image manipur_idle: 
    "images/manipur_idle.png"
    zoom 0.2
image hoffman_idle: 
    "images/hoffman_idle.png"
    zoom 0.3
image monteff_idle: 
    "images/monteff_idle.png"
    zoom 0.4
    




init python:
    from scripts.ai_dialogue import call_ai_model, extract_emotion

    def renpy_profile_loader(name):
        with renpy.file(f"character_profiles/{name}.txt") as f:
            return f.read().decode("utf-8").strip()
    
    def interrogate(question, name):
        raw_response = call_ai_model(question, name, renpy_profile_loader)
        return extract_emotion(raw_response)

    def character_saying(video_path, character):
        renpy.show("video_player", 
            at_list=[Transform(size=(config.screen_width, config.screen_height))],
            what=Movie(play=video_path)
        )
        for text in narration_queue:
            character(text, interact=False)
            renpy.pause(len(text)/20.0 + 5)
        renpy.hide("video_player")


# Main game flow
label start:
    scene cover
    "欢迎本次列车，侦探先生！"
    scene map
    back "1933年，德国法西斯上台后，对周边国家采取蚕食吞并政策，严重威胁英国、法国、苏联等国家的边防安全。"
    back "经济和政治局势的动荡导致谋杀率大幅增加，绑架案四处频发。西欧各国对德国采取绥靖政策，牺牲小国家、商人和贫民利益换取并不长久的国家安全。"
    back "西装革履的英法贵族为保全自身，不断签订各种条约，将周边小国推入法西斯的血盆大口。"
    back "而沦陷区的国家支离破碎，人民流离失所，难以维生，匪盗猖獗。"


    $ narration_queue = [
        "1938年1月15日，由苏联莫斯科开往法国南林克港的列车正疾行在波兰平原上。车上载满官员、贵族和刚刚签订完《英苏-法苏合作条约》的外交官们。",
        "刚处理完苏联的一桩法律案件，疲惫不堪的你乘坐这趟车准备回英国享受假期。",
        "第三句"
    ]
    call play_animated_narration("video/manipur.webm", back)

    scene carriage_dark # 待优化：可以换成多幅动画
    back "夜间，由于愈发强烈的暴风雪，列车只得临时停车，并熄灭大多数煤气灯以保证仅剩燃料的持续供应。"
    back "昏暗而逼仄的车厢内，被困的人们焦虑而又恐惧地等待。"
    back "当车厢中的不安气氛达到顶峰时，第十四与十五节车厢的连接处传来一声尖叫，然后是两三声沉闷的枪响。"
    back "本就不安的乘客中，尖叫声此起彼伏，惊慌地四散奔逃。"


    scene samiur_lying
    back "当你赶到时，只见到中弹者倒在血泊中，毛发散乱，瞳孔放大，苍白的脸扭曲而惊愕，伸手探去早已没了鼻息。"

    scene suspects_standing
    back "经过调查，死者名为萨缪尔，是一个臭名昭著的罪犯。由于案件发生突然，车厢狭窄拥挤，你断定凶手仍在现场不远处。"
    back "通过简单取证与对比，你锁定了邻近3节车厢内的5名嫌疑人，准备进一步进行审问。可直觉告诉你，这件谋杀案的背后根本没有你想的那么简单......."

    menu:
        "查看嫌疑人信息":
            jump show_suspect_info
        "开始审讯":
            menu:
                "manipur":
                    jump interrogate_manipur
                "Hoffman":
                    jump interrogate_hoffman
                "monteff":
                    jump interrogate_monteff


    menu:
        "Interrogate manipur":
            jump interrogate_manipur
        "Interrogate hoffman":
            jump interrogate_hoffman
        "Interrogate monteff":
            jump interrogate_monteff

label proceed:
    "请选择下一个审讯的对象"  
    menu:  
        "manipur" if "manipur" not in interrogated_suspects:  
            jump interrogate_manipur  
        "hoffman" if "hoffman" not in interrogated_suspects:  
            jump interrogate_hoffman  
        "monteff" if "monteff" not in interrogated_suspects:  
            jump interrogate_monteff



# ==== 审讯曼尼普尔 ====
label interrogate_manipur:
    
    show manipur_idle
    manipur "（表情紧张）侦探先生，我什么都不知道..."
    detective "Where were you last night?"
    # ...
    # ... 


# ==== 审讯霍夫曼 ====
label interrogate_hoffman:
    scene hoffman_idle

    hoffman "（双手交叉）侦探先生，您随便问，但我只能回答您五个问题"
    
    # 5-round dialogue loop
    python: 
        hoffman_states = {
                "平静": "video/hoffman_idle.webm",
                "谨慎": "video/hoffman_serious.webm",
                "慌张": "video/hoffman_nervous.webm",
                "愤怒": "video/hoffman_angry.webm"
            }

        for round_num in range(1, 6):  
            renpy.say(detective, f"第{round_num}/5轮：你要问hoffman什么？")
            question = renpy.input(f"问题 {round_num}: ", length = 100).strip()
            if not question:
                renpy.say(detective, "请输入有效问题")
                continue

            # 角色一边做出回答，一边播放情绪对应的动画
            current_emotion, clean_response = interrogate(question, "hoffman")
            narration_queue = [clean_response]
            character_saying(hoffman_states[current_emotion], hoffman)
            renpy.pause(0.3)
    
    # End interrogation
    hoffman "（站起身）好了，侦探先生，我对这些感到厌烦了，我相信我们都需要休息一下"

    detective "审讯结束"
    $ interrogated_suspects.add("hoffman")
    menu:  
        "继续审讯":  
            jump proceed  # 返回嫌疑人选择界面  
        "指认凶手":  
            jump accuse_culprit  # 直接进入指认环节  


# ==== Branch 3: Interrogate monteff (5 rounds of AI dialogue) ====
label interrogate_monteff:  
    $ dialogue_round = 0  # 重置对话轮次（RenPy脚本变量）  
    # hide manipur_idle hoffman_idle  
    # show monteff_idle at truecenter with dissolve  
    monteff "（微笑）侦探先生，您好！我不打算隐瞒什么，昨天晚上我的确经过了车厢，但我什么都没听到看到"  
    
    
    $ char_profile = """  
    You are monteff, a passenger on the Orient Express, NOT the murderer.  
    Alibi: Passed victim's carriage at 10 PM, heard a door slam but saw no one.  
    """  

     
    python:  
          
        while renpy.store.dialogue_round < 5:  
            renpy.store.dialogue_round += 1  
              
            renpy.say(renpy.store.detective, f"Round {renpy.store.dialogue_round}/5: What do you ask monteff?")  
              
            player_question = renpy.input(f"Question {renpy.store.dialogue_round}: ", length=100).strip()  
            if not player_question:    
                renpy.say(renpy.store.detective, "Please ask a valid question!")  
                continue   
             
            monteff_response = renpy.store.call_ai_model(player_question, renpy.store.char_profile)  
             
            renpy.say(renpy.store.monteff, monteff_response)  
            renpy.pause(0.5)   

    # 审问结束（回到RenPy脚本）  
    hide monteff_idle with dissolve 
    monteff "(站起来) 侦探先生，我想我已经说得够清楚了，我什么都没有做！您无休止的质疑使我厌烦，我要回去休息一下" 
    detective "审讯结束" 
    $ interrogated_suspects.add("monteff") 
    menu:  
        "继续审讯":  
            jump proceed  # 返回嫌疑人选择界面  
        "指认凶手":  
            jump accuse_culprit  # 直接进入指认环节 


# ==== Culprit accusation (trigger after all interrogations) ====
label accuse_culprit:
    scene carriage
    "All suspects interrogated. Now accuse the murderer!"
    menu:
        "Accuse manipur":
            jump ending_wrong
        "Accuse hoffman":
            jump ending_correct
        "Accuse monteff":
            jump ending_wrong

label ending_correct:
    detective "hoffman, your military background and alibi contradictions give you away!"
    hoffman "（脸色惨白）Yes... I did it! He ruined my life!"  # ✅ 正确：使用定义好的hoffman变量  
    "Case solved! You caught the murderer!"
    return

label ending_wrong:
    detective "Wrong accusation! hoffman has escaped during the chaos..."
    "Game Over. Better luck next time!"
    return

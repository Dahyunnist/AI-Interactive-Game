# Define characters with color coding
# 约翰·曼尼普尔上校 John Manipur
define manipur = Character("manipur", what_size = 75, who_size = 45, color="#ff99cc", image = "manipur")    # Pink dialogue
# 拉杰特·杨·霍夫曼 Rhajeat young Hoffman
define hoffman = Character("hoffman", color="#99ccff", image = "hoffman")  # Blue dialogue
# 范德蒙特夫Fond Monteff
define monteff = Character("monteff", color="#ccff99", image = "monteff")    # Green dialogue

define detective = Character("Detective", color="#ffff99")  # Yellow dialogue
# 旁白
define back = Character("旁白", what_prefix='"', what_suffix='"', what_slow_cps=20)

# 定义视频背景（Movie对象会自动适应屏幕）
image video_background = Movie(
    play="video/manipur.webm",  # 视频路径
    loop=False,  # 不循环播放（根据需求调整）
    size=(1920, 1080)  # 视频原始分辨率（需与实际视频一致）
)

# 旁白变量
default narration_queue = []
default current_narration = ""

# label play_animated_narration(video_path):
#     # 显示视频（Movie 对象会自动播放）
#     show expression Movie(
#         play=video_path,
#         size=(1920, 1080)  # 根据实际分辨率调整
#     ) as video_player
    
#     # 显示旁白
#     show screen dynamic_narration
    
#     python:
#         # # 方案变更：不再检测视频时长，直接按旁白时间暂停
#         # total_duration = 0.0
#         # for text, duration in narration_queue:
#         #     current_narration = text
#         #     renpy.pause(duration)
#         #     total_duration += duration
        
#         # # 固定额外暂停（确保视频播完）
#         # renpy.pause(1.0)  # 默认追加1秒缓冲时间
#         for text in narration_queue:
#             current_narration = ""
#             renpy.pause(0.01)
#             current_narration = text
#             # renpy.restart_interaction()
#             # required_time = len(text)/10 + 0.5
#             renpy.pause(len(text)/20 + 0.5)
    
#     # 清理
#     hide screen dynamic_narration
#     hide video_player
#     return

label play_animated_narration(video_path):
    # 显示视频
    show expression Movie(
        play = video_path,
        size = (config.screen_width, config.screen_height),
    ) as video_player
    
    # 使用角色对话系统显示旁白
    python:
        for text in narration_queue:
            back(text, interact=False)  # 关键：直接调用角色对话函数
            renpy.pause(len(text)/20.0 + 5)  # 句间间隔
    
    # 清理
    hide video_player
    return






image side manipur:
    "images/figure/manipur.png"
    zoom 0.3

image side hoffman:
    "images/figure/hoffman.png"
    zoom 0.3

image side monteff:
    "images/figure/monteff.png"
    zoom 0.3

# Image assets definition (place in game/images/)
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
    from scripts.ai_dialogue import call_ai_model

    def renpy_profile_loader(name):
        with renpy.file(f"character_profiles/{name}.txt") as f:
            return f.read().decode("utf-8").strip()
    
    def interrogate(question, name):
        return call_ai_model(question, name, renpy_profile_loader)

    # config.preload_videos = True

# Main game flow
label start:
    scene cover  # Maintain background image p1
    "欢迎本次列车，侦探先生！"
    scene map
    back "1933年，德国法西斯上台后，对周边国家采取蚕食吞并政策，严重威胁英国、法国、苏联等国家的边防安全。"
    back "经济和政治局势的动荡导致谋杀率大幅增加，绑架案四处频发。西欧各国对德国采取绥靖政策，牺牲小国家、商人和贫民利益换取并不长久的国家安全。"
    back "西装革履的英法贵族为保全自身，不断签订各种条约，将周边小国推入法西斯的血盆大口。"
    back "而沦陷区的国家支离破碎，人民流离失所，难以维生，匪盗猖獗。"

    # $ renpy.start_predict("video/manipur.webm")
    $ narration_queue = [
        "1938年1月15日，由苏联莫斯科开往法国南林克港的列车正疾行在波兰平原上。车上载满官员、贵族和刚刚签订完《英苏-法苏合作条约》的外交官们。",
        "刚处理完苏联的一桩法律案件，疲惫不堪的你乘坐这趟车准备回英国享受假期。",
        "第三句"
    ]

    call play_animated_narration("video/manipur.webm")

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
    # menu:  
    #     "manipur" if "manipur" not in interrogated_suspects:  
    #         jump interrogate_manipur  
    #     "hoffman" if "hoffman" not in interrogated_suspects:  
    #         jump interrogate_hoffman  
    #     "monteff" if "monteff" not in interrogated_suspects:  
    #         jump interrogate_monteff
    menu:
        "Interrogate manipur":
            jump interrogate_manipur
        "Interrogate hoffman":
            jump interrogate_hoffman
        "Interrogate monteff":
            jump interrogate_monteff



# ==== Branch 1: Interrogate manipur (Play animation then return) ====
label interrogate_manipur:
    
    # show manipur_idle at truecenter with dissolve
    manipur "（表情紧张）侦探先生，我什么都不知道..."
    detective "Where were you last night?"
    "（Playing manipur's alibi animation...）"
    
    # Play animation (place in game/video/)
    # play music "audio/love.mp3"
    # hide manipur_idle with dissolve
    # $ renpy.movie_cutscene("video/manipur.webm") 
    show screen video_with_narration
    
    # 第1句旁白（0秒时显示）
    $ current_narration = "旁白1：故事发生在1934年的东方快车..."
    pause 3.0  # 持续3秒
    
    # 第2句旁白（3秒时切换）
    $ current_narration = "旁白2：车上载着来自世界各地的乘客..."
    pause 4.5  # 持续4.5秒
    
    # 第3句旁白（7.5秒时切换）
    $ current_narration = "旁白3：他们之中，隐藏着一个凶手..."
    pause 3.0  # 持续3秒
    
    # 结束：隐藏屏幕
    hide screen video_with_narration

    pause 5
    menu: 
        "继续审讯":  
            jump proceed  # 返回嫌疑人选择界面  
        "指认凶手":  
            jump accuse_culprit  # 直接进入指认环节  


# ==== Branch 2: Interrogate hoffman (5 rounds of AI dialogue) ====
label interrogate_hoffman:
    scene hoffman_sitting

    hoffman "（双手交叉）侦探先生，您随便问，但我只能回答您五个问题"
    
    # 5-round dialogue loop
    python: 
        # 在Python块内访问RenPy变量需用renpy.store  
        for round_num in range(1, 6):  
            renpy.say(detective, f"第{round_num}/5轮：你要问hoffman什么？")

            question = renpy.input(f"问题 {round_num}: ", length = 100).strip()
            if not question:
                renpy.say(detective, "请输入有效问题")
                continue

            response = interrogate(question, "hoffman")
            renpy.say(hoffman, response)
            renpy.pause(0.3)
    
    # End interrogation
    hoffman "（站起身）好了，侦探先生，我对这些感到厌烦了，我相信我们都需要休息一下"
    hide hoffman_idle with dissolve
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
    
    # monteff的角色设定（传递给AI模型）  
    $ char_profile = """  
    You are monteff, a passenger on the Orient Express, NOT the murderer.  
    Alibi: Passed victim's carriage at 10 PM, heard a door slam but saw no one.  
    """  

    # ==== 关键：用python:块包裹循环逻辑 ====  
    python:  
        # 在Python块内访问RenPy变量需用renpy.store  
        while renpy.store.dialogue_round < 5:  
            renpy.store.dialogue_round += 1  
            # 1. 显示侦探台词（调用RenPy的say函数）  
            renpy.say(renpy.store.detective, f"Round {renpy.store.dialogue_round}/5: What do you ask monteff?")  
            # 2. 获取玩家输入（调用RenPy的input函数）  
            player_question = renpy.input(f"Question {renpy.store.dialogue_round}: ", length=100).strip()  
            if not player_question:  # 若输入为空  
                renpy.say(renpy.store.detective, "Please ask a valid question!")  
                continue  # ✅ 在Python块内可用continue  
            # 3. 调用AI模型生成回答  
            monteff_response = renpy.store.call_ai_model(player_question, renpy.store.char_profile)  
            # 4. 显示monteff的AI回答  
            renpy.say(renpy.store.monteff, monteff_response)  
            renpy.pause(0.5)  # 暂停0.5秒  

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
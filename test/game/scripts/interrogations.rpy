screen interrogation_controls():
    frame:
        xalign 0.95
        yalign 0.05
        background None
        vbox:
            # 添加边框的按钮
            frame:
                background "#FFD700"
                padding (6, 6)  # 边框宽度
                xminimum 208  # 按钮宽度 + 边框宽度
                yminimum 68   # 按钮高度 + 边框宽度

                textbutton "返回主菜单":
                    action Jump("main_menu_1")
                    text_size 35
                    text_color "#FFFFFF"
                    text_hover_color "#FFFFFF"
                    background "#487d17"  # 亮红色背景
                    hover_background "#1c4f0c"  # 悬停时更亮的红色
                    xminimum 200
                    yminimum 60
                    padding (20, 15)


label interrogate_monteff:

    scene empty_room with fade

    if monteff_asked >= 5:
        "你已经问过蒙特夫太太5个问题了，不能再继续询问了。"
        jump main_menu_1

    show monteff at center with dissolve

    show screen interrogation_controls

    if monteff_asked == 0:
        monteff "（微微低头，声音轻柔）尊敬的侦探先生，请问您有什么需要我协助的吗？我会尽力配合您的调查。"

    # 5-round dialogue loop
    python: 
        monteff_states = {
                "平静": "video/monteff_idle.webm",
                "谨慎": "video/monteff_serious.webm",
                "慌张": "video/monteff_nervous.webm",
                "愤怒": "video/monteff_angry.webm"
            }
        while monteff_asked < 5:  
            renpy.say(calgary, f"第{monteff_asked+1}/5轮：你要问蒙特夫太太什么？")
            question = renpy.input(f"问题 {monteff_asked+1}: ", length = 100).strip()
            if not question:
                renpy.say(None, "请输入有效问题")
                continue

            # 角色一边做出回答，一边播放情绪对应的动画
            current_emotion, clean_response = interrogate(question, "monteff")
            monteff_asked += 1
            narration_queue = [clean_response]
            character_saying(monteff_states[current_emotion], monteff)
            renpy.pause(0.3)

    hide screen interrogation_controls with fade
    $ narration_queue = [
        "侦探先生，如果您没有其他问题，请允许我回去休息了。这一切让我感到非常不适。"
    ]
    python:
        character_saying("video/monteff_leaving.webm", monteff)
    
    # 蒙特夫离开
    pause(1.5)
    show monteff:
        easeout 1.0 xoffset 2000
    with dissolve
    pause 3.0
    
    "蒙特夫太太优雅地离开了审讯室。"

    $ interrogated_suspects.add("monteff")
    jump main_menu_1

label interrogate_hoffman:

    scene empty_room with fade

    if hoffman_asked >= 5:
        "你已经问过霍夫曼议员5个问题了，不能再继续询问了。"
        jump main_menu_1

    show hoffman at center with dissolve

    show screen interrogation_controls

    if hoffman_asked == 0:
        hoffman "（双手交叉）侦探先生，您随便问，但我只能回答您五个问题"
    
    # 5-round dialogue loop
    python: 
        hoffman_states = {
                "平静": "video/hoffman_idle.webm",
                "谨慎": "video/hoffman_serious.webm",
                "慌张": "video/hoffman_nervous.webm",
                "愤怒": "video/hoffman_angry.webm"
            }
        while hoffman_asked < 5:  
            renpy.say(calgary, f"第{hoffman_asked+1}/5轮：你要问hoffman什么？")
            question = renpy.input(f"问题 {hoffman_asked+1}: ", length = 100).strip()
            if not question:
                renpy.say(None, "请输入有效问题")
                continue

            # 角色一边做出回答，一边播放情绪对应的动画
            current_emotion, clean_response = interrogate(question, "hoffman")
            hoffman_asked += 1
            narration_queue = [clean_response]
            character_saying(hoffman_states[current_emotion], hoffman)
            renpy.pause(0.3)
    
    hide screen interrogation_controls with fade
    $ narration_queue = [
        "好了，侦探先生，我对这些感到厌烦了，我相信我们都需要休息一下"
    ]
    python:
        character_saying("video/hoffman_standing.webm", hoffman)
    
    # 霍夫曼离开
    pause(1.5)
    $ renpy.movie_cutscene("video/hoffman_leaving.webm") 
    show hoffman:
        easeout 1.0 xoffset 2000
    with dissolve
    pause 3.0
    
    "霍夫曼离开了审讯室。"

    jump main_menu_1

    $ interrogated_suspects.add("hoffman")

label interrogate_kremtanivsky:

    scene empty_room with fade

    if kremtanivsky_asked >= 5:
        "你已经问过克里姆塔涅夫斯基5个问题了，不能再继续询问了。"
        jump main_menu_1

    show kremtanivsky at center with dissolve

    show screen interrogation_controls

    if kremtanivsky_asked == 0:
        kremtanivsky "（双手抱胸，微微仰头）侦探同志，请抓紧时间。苏联警察机关有严格的纪律，我不会隐瞒任何事实。"
    
    # 5-round dialogue loop
    python: 
        kremtanivsky_states = {
                "平静": "video/kremtanivsky_idle.webm",
                "谨慎": "video/kremtanivsky_serious.webm",
                "慌张": "video/kremtanivsky_nervous.webm",
                "愤怒": "video/kremtanivsky_angry.webm"
            }
        while kremtanivsky_asked < 5:  
            renpy.say(calgary, f"第{kremtanivsky_asked+1}/5轮：你要问克里姆塔涅夫斯基什么？")
            question = renpy.input(f"问题 {kremtanivsky_asked+1}: ", length = 100).strip()
            if not question:
                renpy.say(None, "请输入有效问题")
                continue

            # 角色一边做出回答，一边播放情绪对应的动画
            current_emotion, clean_response = interrogate(question, "kremtanivsky")
            kremtanivsky_asked += 1
            narration_queue = [clean_response]
            character_saying(kremtanivsky_states[current_emotion], kremtanivsky)
            renpy.pause(0.3)

    hide screen interrogation_controls with fade
    $ narration_queue = [
        "侦探同志，如果调查结束，我建议你关注真正的威胁，而不是在我这里浪费时间。"
    ]
    python:
        character_saying("video/kremtanivsky_leaving.webm", kremtanivsky)
    
    # 克里姆塔涅夫斯基离开
    pause(1.5)
    show kremtanivsky:
        easeout 1.0 xoffset 2000
    with dissolve
    pause 3.0
    
    "克里姆塔涅夫斯基大步离开了审讯室。"

    $ interrogated_suspects.add("kremtanivsky")
    jump main_menu_1

label interrogate_john:
    scene empty_room with fade

    if john_asked >= 5:
        "你已经问过约翰上校5个问题了，不能再继续询问了。"
        jump main_menu_1

    show john at center with dissolve

    show screen interrogation_controls

    if john_asked == 0:
        john "（不耐烦地看着手表）侦探先生，我时间有限，请您尽快。我还有军务要处理。"
    
    # 5-round dialogue loop
    python: 
        john_states = {
                "平静": "video/john_idle.webm",
                "谨慎": "video/john_serious.webm",
                "慌张": "video/john_nervous.webm",
                "愤怒": "video/john_angry.webm"
            }
        while john_asked < 5:  
            renpy.say(calgary, f"第{john_asked+1}/5轮：你要问约翰上校什么？")
            question = renpy.input(f"问题 {john_asked+1}: ", length = 100).strip()
            if not question:
                renpy.say(None, "请输入有效问题")
                continue

            # 角色一边做出回答，一边播放情绪对应的动画
            current_emotion, clean_response = interrogate(question, "john")
            john_asked += 1
            narration_queue = [clean_response]
            character_saying(john_states[current_emotion], john)
            renpy.pause(0.3)
    
    hide screen interrogation_controls with fade
    $ narration_queue = [
        "侦探先生，如果您没有确凿证据，请不要再浪费我的时间。我还有更重要的事情要处理。"
    ]
    python:
        character_saying("video/john_leaving.webm", john)
    
    # 约翰离开
    pause(1.5)
    show john:
        easeout 1.0 xoffset 2000
    with dissolve
    pause 3.0
    
    "约翰上校头也不回地离开了审讯室。"

    $ interrogated_suspects.add("john")
    jump main_menu_1

label interrogate_sok:

    scene empty_room with fade

    if sok_asked >= 5:
        "你已经问过苏和华5个问题了，不能再继续询问了。"
        jump main_menu_1

    show sok at center with dissolve

    show screen interrogation_controls

    if sok_asked == 0:
        sok "（叹气）侦探先生，我只是个普通商人，来这里做生意的。请问您有什么需要了解的？"
    
    # 5-round dialogue loop
    python: 
        sok_states = {
                "平静": "video/john_idle.webm",
                "谨慎": "video/john_serious.webm",
                "慌张": "video/john_nervous.webm",
                "愤怒": "video/john_angry.webm"
            }
        while sok_asked < 5:  
            renpy.say(calgary, f"第{sok_asked+1}/5轮：你要问苏和华什么？")
            question = renpy.input(f"问题 {sok_asked+1}: ", length = 100).strip()
            if not question:
                renpy.say(None, "请输入有效问题")
                continue

            # 角色一边做出回答，一边播放情绪对应的动画
            current_emotion, clean_response = interrogate(question, "sok")
            sok_asked += 1
            narration_queue = [clean_response]
            character_saying(sok_states[current_emotion], sok)
            renpy.pause(0.3)
    
    hide screen interrogation_controls with fade
    $ narration_queue = [
        "侦探先生，如果您没有其他问题，请允许我回去休息了。这趟旅程让我感到非常疲惫。"
    ]
    python:
        character_saying("video/sok_leaving.webm", sok)
    
    # 苏和华离开
    pause(1.5)
    show sok:
        easeout 1.0 xoffset 2000
    with dissolve
    pause 3.0
    
    "苏和华微微鞠躬后离开了审讯室。"

    $ interrogated_suspects.add("sok")
    jump main_menu_1
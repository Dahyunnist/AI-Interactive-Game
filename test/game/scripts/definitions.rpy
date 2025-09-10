init python:
    import random
    from scripts.ai_dialogue import call_ai_model, extract_emotion
    from scripts.memory_manager import clear_all_memories

    # 旁白样式
    style.narrator_style = Style(style.default)
    style.narrator_style.size = 28
    style.narrator_style.color = "#e0e0e0"

    def renpy_profile_loader(name):
        with renpy.file(f"character_profiles/{name}.txt") as f:
            return f.read().decode("utf-8").strip()
    
    def interrogate(question, name):
        raw_response = call_ai_model(question, name, renpy_profile_loader)
        return extract_emotion(raw_response)

    # 使用函数的形式实现动画+旁白，功能与之前的play_animated_narration相同
    def character_saying(video_path, character):
        renpy.show("video_player", 
            at_list=[Transform(size=(config.screen_width, config.screen_height))],
            what=Movie(play=video_path)
        )
        for text in narration_queue:
            character(text, interact=False)
            renpy.pause(len(text)/20.0 + 5)
        renpy.hide("video_player")

    # 在游戏开始时调用清空函数，清空所有角色的记忆
    clear_all_memories()

    interrogated_suspects = set()
    monteff_asked = 0
    hoffman_asked = 0
    kremtanivsky_asked = 0
    john_asked = 0
    sok_asked = 0

init:
    image cover_image:
        "cover.png"
        size(1920, 1080)
    image europe_map:
        "map.png"
        size(1920, 1080)
    image background1:
        "background1.png"
        size(1920, 1080)
    image background2:
        "background2.png"
        size(1920, 1080)
    image empty_room:
        "empty_room.png"
        size(1920, 1080)
    image hoffman_sitting:
        "hoffman_sitting.png"
        size(1920, 1080)
    image john_sitting:
        "john_sitting.png"
        size(1920, 1080)
    image krem_sitting:
        "krem_sitting.png"
        size(1920, 1080)
    image monteff_sitting:
        "monteff_sitting.png"
        size(1920, 1080)
    image sok_sitting:
        "sok_sitting.png"
        size(1920, 1080)
    
    image interrogation_room = Solid("#ecf0f1")
    
    image victim_blood:
        "victim_blood.png"
        size(1920, 1080)
    image suspects_lineup:
        "suspects_lineup.png"
        size(1920, 1080)
    image finish:
        "finish.jpeg"
        size(1920, 1080)

    image hoffman:
        "Rhajeat_Young_Hoffman.png"
        zoom(0.65)
    image calgary:
        "Calgary_Ham.png"
        zoom(0.75)
    image monteff:
        "Fond_Monteff.png"
        zoom(0.75)
    image john:
        "John_Manipur.png"
        zoom(0.75)
    image kremtanivsky:
        "Kremtanivsky.png"
        zoom(0.75)
    image sok:
        "Sok_Tor_Hof.png"
        zoom(0.75)

    image side hoffman:
        "Rhajeat_Young_Hoffman_head.png"
        zoom(0.3)
    image side calgary:
        "Calgary_Ham_head.png"
        zoom(0.25)
    image side monteff:
        "Fond_Monteff_head.png"
        zoom(0.4)
    image side john:
        "John_Manipur_head.png"
        zoom(0.35)
    image side kremtanivsky:
        "Kremtanivsky_head.png"
        zoom(0.6)
    image side sok:
        "Sok_Tor_Hof_head.png"
        zoom(0.45)


    define hoffman = Character("Hoffman", image = "hoffman", who_color="#98da8c")
    define calgary = Character("Calgary", image = "calgary", who_color="#0929c7")
    define monteff = Character("Monteff", image = "monteff", who_color="#ee09c0")
    define john = Character("John", image = "john", who_color="#6b65d3")
    define kremtanivsky = Character("Kremtanivsky", image = "kremtanivsky", who_color="#c9b2be")
    define sok = Character("Sok", image = "sok", who_color="#d8e5d2")

    image monteff_idle:
        "images/character_gestures/monteff_idle.png"
        zoom 0.75
    image monteff_serious:
        "images/character_gestures/monteff_serious.png"
        zoom 0.75
    image monteff_nervous:
        "images/character_gestures/monteff_nervous.png"
        zoom 0.75
    image monteff_angry:
        "images/character_gestures/monteff_angry.png"
        zoom 0.75

    image hoffman_idle:
        "images/character_gestures/hoffman_idle.png"
        zoom 0.75
    image hoffman_serious:
        "images/character_gestures/hoffman_serious.png"
        zoom 0.75
    image hoffman_nervous:
        "images/character_gestures/hoffman_nervous.png"
        zoom 0.75
    image hoffman_angry:
        "images/character_gestures/hoffman_angry.png"
        zoom 0.75
    
    image john_idle:
        "images/character_gestures/john_idle.png"
        zoom 0.75
    image john_serious:
        "images/character_gestures/john_serious.png"
        zoom 0.75
    image john_nervous:
        "images/character_gestures/john_nervous.png"
        zoom 0.75
    image john_angry:
        "images/character_gestures/john_angry.png"
        zoom 0.75

    image krem_idle:
        "images/character_gestures/krem_idle.png"
        zoom 0.75
    image krem_serious:
        "images/character_gestures/krem_serious.png"
        zoom 0.75
    image krem_nervous:
        "images/character_gestures/krem_nervous.png"
        zoom 0.75
    image krem_angry:
        "images/character_gestures/krem_angry.png"
        zoom 0.75

    image sok_idle:
        "images/character_gestures/sok_idle.png"
        zoom 0.75
    image sok_serious:
        "images/character_gestures/sok_serious.png"
        zoom 0.75
    image sok_nervous:
        "images/character_gestures/sok_nervous.png"
        zoom 0.75
    image sok_angry:
        "images/character_gestures/sok_angry.png"
        zoom 0.75

    

    define hoffman = Character("Hoffman", image = "hoffman")
    define calgary = Character("Calgary", image = "calgary")
    define monteff = Character("Monteff", image = "fond")
    define john = Character("John", image = "john")
    define kremtanivsky = Character("Kremtanivsky", image = "kremtanivsky")
    define sok = Character("Sok", image = "sok")


    # 功能：播放动画时渐次展示旁白
    default narration_queue = []
    default current_narration = ""

    # # 使用label的形式定义动画旁白播放函数，通过call调用
    # label play_animated_narration(video_path, character):
    #     # 显示视频
    #     show expression Movie(
    #         play = video_path,
    #         size = (config.screen_width, config.screen_height),
    #     ) as video_player
    #     # 使用角色对话系统显示旁白
    #     python:
    #         for text in narration_queue:
    #             character(text, interact=False)
    #             renpy.pause(len(text)/20.0 + 5)  # 句间间隔5秒
    #     # 清理
    #     hide video_player
    #     return

init python:
    import random
    from scripts.ai_dialogue import call_ai_model, extract_emotion

    # 游戏配置
    config.name = _("伊维利亚列车大劫案")
    config.version = "1.0"
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

init:
    # 角色定义
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
    image interrogation_room = Solid("#ecf0f1")
    image victim_blood:
        "victim_blood.png"
        size(1920, 1080)
    image suspects_lineup = Solid("#212128")

    image hoffman:
        "Rhajeat_Young_Hoffman.png"
        zoom(0.60)
    image calgary:
        "Calgary_Ham.png"
        zoom(0.75)
    image fond:
        "Fond_Monteff.png"
        zoom(0.75)
    image john:
        "John_Manipur.png"
        zoom(0.65)
    image kremtanivsky:
        "Kremtanivsky.png"
        zoom(0.75)
    image sok:
        "Sok_Tor_Hof.png"
        zoom(0.75)

    image side hoffman:
        "Rhajeat_Young_Hoffman_head.png"
        zoom(0.25)
    image side calgary:
        "Calgary_Ham_head.png"
        zoom(0.5)
    image side fond:
        "Fond_Monteff_head.png"
        zoom(0.25)
    image side john:
        "John_Manipur_head.png"
        zoom(0.30)
    image side kremtanivsky:
        "Kremtanivsky_head.png"
        zoom(0.25)
    image side sok:
        "Sok_Tor_Hof_head.png"
        zoom(0.25)

    define hoffman = Character("hoffman", image = "hoffman")
    define calgary = Character("calgary", image = "calgary")
    define fond = Character("fond", image = "fond")
    define john = Character("john", image = "john")
    define kremtanivsky = Character("kremtanivsky", image = "kremtanivsky")
    define sok = Character("sok", image = "sok")

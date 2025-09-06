# Define characters with color coding
define irene = Character("Irene", what_size = 75, who_size = 45, color="#ff99cc", image = "irene")    # Pink dialogue
define seulgi = Character("Seulgi", color="#99ccff", image = "seulgi")  # Blue dialogue
define wendy = Character("Wendy", color="#ccff99", image = "wendy")    # Green dialogue
define detective = Character("Detective", color="#ffff99")  # Yellow dialogue

# 定义视频背景（Movie对象会自动适应屏幕）
image video_background = Movie(
    play="video/irene.webm",  # 视频路径
    loop=False,  # 不循环播放（根据需求调整）
    size=(1920, 1080)  # 视频原始分辨率（需与实际视频一致）
)

# 旁白变量
default narration_queue = []
default current_narration = ""

label play_animated_narration:
    play movie video_path
    show screen dynamic_narration
    python:
        while len(narration_queue) > 0:
            text, duration = narration_queue.pop(0)
            current_narration = text
            renpy.pause(duration)

    hide screen dynamic_narration
    stop movie
    return




image side irene:
    "images/figure/irene.png"
    zoom 0.3

image side seulgi:
    "images/figure/seulgi.png"
    zoom 0.3

image side wendy:
    "images/figure/wendy.png"
    zoom 0.3

# Image assets definition (place in game/images/)
image train: 
    "images/train.png"  # Main background (东方快车车厢)
    zoom 2.5
image carriage: 
    "images/carriage.png"
    zoom 3.7


image irene_idle: 
    "images/irene_idle.png"
    zoom 0.2
image seulgi_idle: 
    "images/seulgi_idle.png"
    zoom 0.3
image wendy_idle: 
    "images/wendy_idle.png"
    zoom 0.4
    


# AI model API integration (initialize on game start)
init python:
    import requests  # Install requests via pip first (see note below)
    import json
    import os
    from scripts.memory_manager import load_memory, save_memory

    MODEL_CONFIGS = {
        "irene": {"api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "model": "qwen-plus", "temperature": 0.5},  
        "seulgi": {"api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "model": "qwen-turbo", "temperature": 0.8},  
        "wendy": {"api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "model": "qwen-turbo", "temperature": 0.6}, 
    }

    
    interrogated_suspects = set()

    # Global variable to track dialogue rounds
    dialogue_round = 0

    def call_ai_model(question, character_name):
        """
        调用指定角色的大模型，自动加载/更新记忆
        :param character_name: 角色名 ("irene"/"seulgi"/"wendy")
        """
        # ==== API Configuration ====
        # 阿里巴巴通义千问API
        API_KEY = "sk-c7785f6decc94b28a30ae01c5c65090b"  # Replace with actual API key
        # API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
        # MODEL_NAME = "qwen-turbo"  # 模型名称（轻量版，可选qwen-plus/qwen-max）

        # ==== 构建请求参数（严格按官方API格式）====
        # 1. 构造对话历史（角色设定+玩家问题，符合OpenAI兼容格式）
        with renpy.file(f"character_profiles/{character_name}.txt") as f:
            system_prompt = f.read().decode("utf-8").strip()
        
        history = load_memory(character_name)

        config = MODEL_CONFIGS[character_name]

        messages = [
            {"role": "system", "content": system_prompt},  # 角色设定（系统提示）
            *history,
            {"role": "user", "content": question}               # 玩家问题
        ]

        # 2. 完整请求体（参考官方教程的兼容模式格式）
        payload = {
            "model": config["model"],                # 必须指定模型名称
            "messages": messages,               # 对话历史（包含角色设定和问题）
            "max_tokens": 150,                  # 生成回答的最大长度（约3-5句话）
            "temperature": config["temperature"]                  # 随机性（0.7适中，符合游戏角色个性）
        }

        # 3. 请求头（包含API Key认证）
        headers = {
            "Authorization": f"Bearer {API_KEY}",  # 固定格式："Bearer " + API Key
            "Content-Type": "application/json"
        }
        
        # API call with error handling (offline fallback)
        # ==== 发送请求并处理响应 ====
        try:
            # 发送POST请求到官方教程指定的Base URL
            response = requests.post(
                url = config["api_url"] + "/chat/completions",  # 兼容模式的对话接口路径
                headers=headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()  # 检查HTTP错误（如401密钥错误）

            # 解析响应（官方教程兼容OpenAI格式）
            character_response = response.json()["choices"][0]["message"]["content"].strip()  # 提取回答文本

            # 更新记忆（追加当前问答内容）并保存
            history.append({"role": "user", "content": question})
            history.append({"role": "assistant", "content": character_response})
            save_memory(character_name, history)

            return character_response

        except Exception as e:
            # 错误处理：返回友好提示（玩家无感知，开发时可打印错误日志）
            print(f"API调用失败: {str(e)}")  # RenPy控制台可查看错误详情
            return "你在胡言乱语些什么？"  # 游戏内显示的默认回答




# Main game flow
label start:
    scene cover  # Maintain background image p1
    "欢迎本次列车，侦探先生！"
    scene map
    "昨晚列车上发生了一起凶案，我们初步锁定了三名有嫌疑的乘客"
    show irene_idle at left
    show seulgi_idle at center
    show wendy_idle at right
    # 嵌入超链接
    "您可以一个一个审问他们，或者也可以选择使用您超乎常人的直觉{a=jump:accuse_culprit}直接指认凶手{/a}" # a=后面也可以加网址，就像真的超链接那样
    # 选择审讯对象
    hide irene_idle
    hide seulgi_idle
    hide wendy_idle

    menu:
        "Interrogate Irene":
            jump interrogate_irene
        "Interrogate Seulgi":
            jump interrogate_seulgi
        "Interrogate Wendy":
            jump interrogate_wendy



label proceed:
    "请选择下一个审讯的对象"  
    # menu:  
    #     "Irene" if "irene" not in interrogated_suspects:  
    #         jump interrogate_irene  
    #     "Seulgi" if "seulgi" not in interrogated_suspects:  
    #         jump interrogate_seulgi  
    #     "Wendy" if "wendy" not in interrogated_suspects:  
    #         jump interrogate_wendy
    menu:
        "Interrogate Irene":
            jump interrogate_irene
        "Interrogate Seulgi":
            jump interrogate_seulgi
        "Interrogate Wendy":
            jump interrogate_wendy



# ==== Branch 1: Interrogate Irene (Play animation then return) ====
label interrogate_irene:
    
    # show irene_idle at truecenter with dissolve
    irene "（表情紧张）侦探先生，我什么都不知道..."
    detective "Where were you last night?"
    "（Playing Irene's alibi animation...）"
    
    # Play animation (place in game/video/)
    # play music "audio/love.mp3"
    # hide irene_idle with dissolve
    # $ renpy.movie_cutscene("video/irene.webm") 
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


# ==== Branch 2: Interrogate Seulgi (5 rounds of AI dialogue) ====
label interrogate_seulgi:
    seulgi "（双手交叉）侦探先生，您随便问，但我只能回答您五个问题"
    
    # 5-round dialogue loop
    python: 
        # 在Python块内访问RenPy变量需用renpy.store  
        for round_num in range(1, 6):  
            renpy.say(detective, f"第{round_num}/5轮：你要问Seulgi什么？")

            question = renpy.input(f"问题 {round_num}: ", length = 100).strip()
            if not question:
                renpy.say(detective, "请输入有效问题")
                continue
            
            response = call_ai_model(question, "seulgi")
            renpy.say(seulgi, response)
            renpy.pause(0.3)
    
    # End interrogation
    seulgi "（站起身）好了，侦探先生，我说过我只会回答你5个问题，我现在要回去解解宿醉"
    hide seulgi_idle with dissolve
    detective "审讯结束"
    $ interrogated_suspects.add("seulgi")
    menu:  
        "继续审讯":  
            jump proceed  # 返回嫌疑人选择界面  
        "指认凶手":  
            jump accuse_culprit  # 直接进入指认环节  


# ==== Branch 3: Interrogate Wendy (5 rounds of AI dialogue) ====
label interrogate_wendy:  
    $ dialogue_round = 0  # 重置对话轮次（RenPy脚本变量）  
    # hide irene_idle seulgi_idle  
    # show wendy_idle at truecenter with dissolve  
    wendy "（微笑）侦探先生，您好！我不打算隐瞒什么，昨天晚上我的确经过了车厢，但我什么都没听到看到"  
    
    # Wendy的角色设定（传递给AI模型）  
    $ char_profile = """  
    You are Wendy, a passenger on the Orient Express, NOT the murderer.  
    Alibi: Passed victim's carriage at 10 PM, heard a door slam but saw no one.  
    """  

    # ==== 关键：用python:块包裹循环逻辑 ====  
    python:  
        # 在Python块内访问RenPy变量需用renpy.store  
        while renpy.store.dialogue_round < 5:  
            renpy.store.dialogue_round += 1  
            # 1. 显示侦探台词（调用RenPy的say函数）  
            renpy.say(renpy.store.detective, f"Round {renpy.store.dialogue_round}/5: What do you ask Wendy?")  
            # 2. 获取玩家输入（调用RenPy的input函数）  
            player_question = renpy.input(f"Question {renpy.store.dialogue_round}: ", length=100).strip()  
            if not player_question:  # 若输入为空  
                renpy.say(renpy.store.detective, "Please ask a valid question!")  
                continue  # ✅ 在Python块内可用continue  
            # 3. 调用AI模型生成回答  
            wendy_response = renpy.store.call_ai_model(player_question, renpy.store.char_profile)  
            # 4. 显示Wendy的AI回答  
            renpy.say(renpy.store.wendy, wendy_response)  
            renpy.pause(0.5)  # 暂停0.5秒  

    # 审问结束（回到RenPy脚本）  
    hide wendy_idle with dissolve 
    wendy "(站起来) 侦探先生，我想我已经说得够清楚了，我什么都没有做！您无休止的质疑使我厌烦，我要回去休息一下" 
    detective "审讯结束" 
    $ interrogated_suspects.add("wendy") 
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
        "Accuse Irene":
            jump ending_wrong
        "Accuse Seulgi":
            jump ending_correct
        "Accuse Wendy":
            jump ending_wrong

label ending_correct:
    detective "Seulgi, your military background and alibi contradictions give you away!"
    seulgi "（脸色惨白）Yes... I did it! He ruined my life!"  # ✅ 正确：使用定义好的seulgi变量  
    "Case solved! You caught the murderer!"
    return

label ending_wrong:
    detective "Wrong accusation! Seulgi has escaped during the chaos..."
    "Game Over. Better luck next time!"
    return
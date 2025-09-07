# AI model API integration (initialize on game start)
import requests  # Install requests via pip first (see note below)
import json
import os
from scripts.memory_manager import load_memory, save_memory

MODEL_CONFIGS = {
    "manipur": {"api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "model": "qwen-plus", "temperature": 0.5},  
    "hoffman": {"api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "model": "qwen-turbo", "temperature": 0.8},  
    "monteff": {"api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "model": "qwen-turbo", "temperature": 0.6}, 
}


interrogated_suspects = set()

# Global variable to track dialogue rounds
dialogue_round = 0

def call_ai_model(question, character_name, profile_loader = None):
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
    # with renpy.file(f"character_profiles/{character_name}.txt") as f:
    #     system_prompt = f.read().decode("utf-8").strip()
    system_prompt = profile_loader(character_name) if profile_loader else ""
    
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


def extract_emotion(response):
    """
    从回答中提取情绪标签并清理文本
    返回: (情绪状态, 纯净文本)
    """
    import re
    # 匹配 *情绪* 开头模式
    emotion_match = re.match(r'^\*(.*?)\*\s*(.*)', response, re.DOTALL)
    if emotion_match:
        return emotion_match.group(1), emotion_match.group(2).strip()
    return "平静", response  # 默认情绪
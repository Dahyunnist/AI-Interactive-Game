# AI model API integration (initialize on game start)
import requests
import json
import os
from scripts.memory_manager import load_memory, save_memory

MODEL_CONFIGS = {
    "monteff": {"api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "model": "qwen-turbo", "temperature": 0.6},
    "hoffman": {"api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "model": "qwen-turbo", "temperature": 0.8}, 
    "kremtanivsky": {"api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "model": "qwen-plus", "temperature": 0.7},  
    "john": {"api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "model": "qwen-turbo", "temperature": 0.7}, 
    "sok": {"api_url": "https://dashscope.aliyuncs.com/compatible-mode/v1", "model": "qwen-turbo", "temperature": 0.5}, 
}

# Global variable to track dialogue rounds
dialogue_round = 0

def call_ai_model(question, character_name, profile_loader = None):
    """
    调用指定角色的大模型，自动加载/更新记忆
    :param character_name: 角色名 ("irene"/"seulgi"/"wendy")
    """
    # ==== API Configuration ====
    API_KEY = "sk-c7785f6decc94b28a30ae01c5c65090b"  # Replace with actual API key
    system_prompt = profile_loader(character_name) if profile_loader else ""
    
    history = load_memory(character_name)

    config = MODEL_CONFIGS[character_name]

    messages = [
        {"role": "system", "content": system_prompt},  # 角色设定
        *history,
        {"role": "user", "content": question}               # 玩家问题
    ]

    # 2. 完整请求体
    payload = {
        "model": config["model"],                # 模型名称
        "messages": messages,               # 对话历史
        "max_tokens": 150,                  # 生成回答的最大长度
        "temperature": config["temperature"]   # 随机性
    }

    # 3. 请求头（包含API Key认证）
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # API call with error handling
    try:
        # 发送POST请求到官方教程指定的Base URL
        response = requests.post(
            url = config["api_url"] + "/chat/completions", 
            headers=headers,
            data=json.dumps(payload)
        )
        response.raise_for_status()  # 检查HTTP错误

        # 解析响应（官方教程兼容OpenAI格式）
        character_response = response.json()["choices"][0]["message"]["content"].strip()  # 提取回答文本

        # 更新记忆（追加当前问答内容）并保存
        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": character_response})
        save_memory(character_name, history)

        return character_response

    except Exception as e:
        print(f"API调用失败: {str(e)}")  
        return "你在胡言乱语些什么？" 


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


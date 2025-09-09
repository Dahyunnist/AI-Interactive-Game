import json
import os
import renpy

# 加载角色记忆
def load_memory(name):
    base_path = renpy.loader.get_path("")
    memory_path = os.path.join(base_path, "character_memories", f"{name}.json")
    
    if os.path.exists(memory_path):
        with open(memory_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# 保存角色记忆（主要用于保存审讯内容）
def save_memory(name, history):
    base_path = renpy.loader.get_path("")
    memory_dir = os.path.join(base_path, "character_memories")
    os.makedirs(memory_dir, exist_ok=True)  # 确保文件夹存在
    
    memory_path = os.path.join(memory_dir, f"{name}.json")
    with open(memory_path, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

# 清空所有角色记忆文件的函数
def clear_all_memories():
    characters = ["monteff", "hoffman", "kremtanivsky", "john", "sok"]
    base_path = renpy.loader.get_path("")
    for name in characters:
        try:
            memory_path = os.path.join(base_path, "character_memories", f"{name}.json")
            with open(memory_path, "w") as f:
                f.write("[]")
        except Exception as e:
            print(f"清空 {name} 记忆文件时出错: {str(e)}")
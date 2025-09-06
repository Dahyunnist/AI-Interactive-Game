import json
import os

def test_load():
    path = "character_memories/seulgi.json"
    print(f"文件是否存在：{os.path.exists(path)}")
    print(f"文件内容：{open(path, 'r', encoding='utf-8').read()}")
    print(f"JSON解析结果：{json.load(open(path, 'r', encoding='utf-8'))}")

if __name__ == "__main__":
    test_load()
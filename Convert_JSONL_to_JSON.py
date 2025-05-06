import json
import sys

def convert_jsonl_to_formatted_json(jsonl_file_path, formatted_json_file_path):
    # 读取JSONL文件内容
    with open(jsonl_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 将每行从字符串解析为字典
    data_list = [json.loads(line) for line in lines]

    # 转换每个字典为所需的格式
    formatted_data_list = []
    for item in data_list:
        new_json = {
            "conversations": [
                {
                    "from": "system",
                    "value": item['system']
                },
                {
                    "from": "human",
                    "value": item['question']
                }
            ],
            "chosen": {
                "from": "gpt",
                "value": item["chosen"]
            },
            "rejected": {
                "from": "gpt",
                "value": item["rejected"]
            }
        }
        formatted_data_list.append(new_json)

    # 将格式化后的数据写入JSON文件
    with open(formatted_json_file_path, 'w', encoding='utf-8') as file:
        json.dump(formatted_data_list, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input.jsonl> <output.json>")
        sys.exit(1)

    jsonl_file_path = sys.argv[1]
    formatted_json_file_path = sys.argv[2]

    # 使用函数进行转换
    convert_jsonl_to_formatted_json(jsonl_file_path, formatted_json_file_path)




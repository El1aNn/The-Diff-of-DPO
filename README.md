下载数据：
git lfs install
git clone https://huggingface.co/datasets/Intel/orca_dpo_pairs

模型下载：
pip install modelscope
modelscope 
download --model Qwen/Qwen2.5-3B-Instruct

注册wandb (login教程参考gpt)

LLaMA-Factory安装参考其README

**更改trl库，使其支持新的dpo loss**
bash replace_the_trl.sh

评测参考使用MT-Bench，但是gpt4太贵了，换成经济一点的deepseek (还在施工中)

# Towards a customizable text-to-speech personal assistant

## Useful links
- Coqui-ai TTS on Gihub: https://github.com/coqui-ai/TTS
- Coqui-ai Docs: https://tts.readthedocs.io/en/dev/index.html
- Open source datasets refences (EN/ZH): https://wespeech.github.io/awesome-tts/opensource/data/
- Open source datasets refences 2: https://www.openslr.org/resources.php
- YourTTS paper: https://arxiv.org/abs/2112.02418

## 2023-10-04，周三，讨论摘要
- 选题：text to speech
- 以 YourTTS 模型为基本架构，主要卖点如下：
  1. 在 YourTTS 预训练模型的基础上，完成从 text 到 speech 的任务。
  2. 实现多语言之间的迁移。目前设想为找不同的语言公开数据集进行 fine-tuning。注意，YourTTS 是在英语、法语、葡萄牙语三种语言的数据集上进行了预训练。
  3. 实现不同说话者 (speaker) 身份之间的迁移。目前设想是找 multi-speaker 的公开数据集进行 fine-tuning。
- Proposal slides 提交 DDL：**10-09，周一**，统一提交 pdf 格式文件。
- Proposal 汇报及 slides 制作：范爽
- 下一步工作：在中文数据集上检验模型效果。

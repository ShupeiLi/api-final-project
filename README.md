# Towards a customizable text-to-speech personal assistant
Chenyu Shi, Siwen Tu, Shuang Fan, and Shupei Li\
Seminar Audio Processing and Indexing, 2023 Fall, Leiden University

- Welcome to our project website: https://sd12321sd.github.io/api_project.github.io/ :tada:
- More sample audio files are available in the folder `/samples`.
- Features:
  - Multi-language support: Chinese, Japanese.
  - Multi-speaker support: five Chinese speakers and six Japanese speakers.
- The code in this repo is tested on a cloud server installed Ubuntu 22.04 system with a Titan XP GPU.

*Please read the following instructions for reproducibility experiments.*

## Table of Contents
- [Prerequisites](#prerequisites)
- [Reproduce the Training Process](#reproduce-the-training-process)
- [Reproduce the Fine-tuning Process](#reproduce-the-fine-tuning-process)

## Prerequisites
- Python >= 3.6
- PyTorch > 1.6.0
- Clone this repo
    ```sh
    git clone https://github.com/ShupeiLi/api-final-project.git
    ```

## Reproduce the Training Process
1. Install the necessary packages.
   ```sh
   cd api-final-project/code/modified-vits-for-training/
   pip install -r requirements.txt
   ```
2. Install `espeak`.
   ```sh
   apt update
   apt install espeak
   ```
3. Download the Chinese Standard Mandarin Speech Copus dataset from [this link](https://www.data-baker.com/data/index/TNtts/) (click the '数据下载' button, need to complete a questionnaire about the purpose of use). 
4. Download the preprocessed text file `woman_csmsc.txt` from [Google Drive](https://drive.google.com/drive/folders/1SfvsPCb7a17Tg8jSrOprZSJ_V6EH6JsX). Create a new folder `csmsc` under the directory `api-final-project/code/modified-vits-for-training/data/` and put the file in `csmsc`. Put all audio files of the dataset under the new folder `wav`, which is a sub-folder of `csmsc`.
   ```sh
   mkdir -p data/csmsc/wav
   mv woman_csmsc.txt ./data/csmsc
   ```
5. Run the training script `train.py`.
   ```sh
   python train_ms.py -c configs/woman_csmsc.json -m woman_csmsc
   ```
6. Run the script `inference.py` for inference. You can also directly use [our model weights](https://drive.google.com/drive/folders/1SfvsPCb7a17Tg8jSrOprZSJ_V6EH6JsX) `G_96000.pth` for this step. **If so, you don't need to download the dataset and the preprocessed text file.**
   ```sh
   python inference.py
   ```

## Reproduce the Fine-tuning Process
1. Install the necessary packages.
   ```sh
   cd api-final-project/code/modified-vits-for-fine-tuning
   pip install -r requirements.txt
   ```
2. Follow the instructions in `code/modified-vits-for-fine-tuning/LOCAL.md`.
3. The datasets we used in the fine-tuning process can be downloaded from the following links:
   - Chinese: [AISHELL-3](https://www.openslr.org/93/)
   - Japanese: [Japanese Versatile Speech Corpus](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvs_corpus)
5. Run the script `VC_inference.py`
   ```sh
   python VC_inference.py --model_dir ./G_latest.pth --share True --config_dir CONFIG_FILEPATH
   ```
   You can also directly use our model weights and configurations for this step. **If so, you don't need to download the dataset and the preprocessed text file.**\
   Download our model weights and configurations from Google Drive:
   - Chinese: [link](https://drive.google.com/drive/folders/1VANyQ2oi2NfIrWJAVhJzqeLWkm6tnuBP)
   - Japanese: [link](https://drive.google.com/drive/folders/11SZBcahzmsGT6l20S0UR9KW2SXGiEtmx)
   

import matplotlib.pyplot as plt

import os
import json
import math
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader

import commons
import utils
from data_utils import TextAudioLoader, TextAudioCollate, TextAudioSpeakerLoader, TextAudioSpeakerCollate
from models import SynthesizerTrn
from text.symbols import symbols
from text import text_to_sequence

from scipy.io.wavfile import write
from scipy.io import wavfile


# device = torch.device("cpu")
# model.to(device)
def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm


hps = utils.get_hparams_from_file("./configs/woman_csmsc.json")

net_g = SynthesizerTrn(
    len(symbols),
    hps.data.filter_length // 2 + 1,
    hps.train.segment_size // hps.data.hop_length,
    **hps.model).cuda()
_ = net_g.eval()

_ = utils.load_checkpoint("./G_96000.pth", net_g, None)

stn_tst = get_text("我爱计算机科学！", hps)
with torch.no_grad():
    x_tst = stn_tst.cuda().unsqueeze(0)
    x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).cuda()

    # x_tst = stn_tst.cpu().unsqueeze(0)
    # x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).cpu()

    audio = net_g.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.8, length_scale=1)[0][
        0, 0].data.cpu().float().numpy()

sampling_rate = 48000
wavfile.write('./G_96000.wav', sampling_rate, audio)
# ipd.display(ipd.Audio(audio, rate=hps.data.sampling_rate, normalize=False))

import time
import torch
import gdown
import zipfile
import os
from espnet2.bin.tts_inference import Text2Speech
from parallel_wavegan.utils import load_model

class EspnetTtsJapanese:
    def __init__(self, model_name='ty'):
        if model_name == 'ty':
            folder = 'tsukuyomichan'
            self.acoustic_model_path = f'data/{folder}/acoustic/train.loss.ave_5best.pth'
            self.acoustic_config_path = f'data/{folder}/acoustic/config.yaml'
            self.vocoder_path = f'data/{folder}/vocoder/checkpoint-580000steps.pkl'
        elif model_name == 'jvs001':
            folder = 'jvs001'
            self.acoustic_model_path = f'data/{folder}/acoustic/train.loss.ave_5best.pth'
            self.acoustic_config_path = f'data/{folder}/acoustic/config.yaml'
            self.vocoder_path = f'data/{folder}/vocoder/checkpoint-565000steps.pkl'
        else:
            raise Exception(f'Not exist model name. : {model_name}')
        
        self.zip_url = 'https://drive.google.com/uc?id=1wonlhn4LSj0PE09LrPtBoO_oHm_hPdLz'
        if not os.path.exists('data'):
            self.download_data()
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.acoustic_model = self.get_acoustic_model()
        self.vocoder = self.get_vocoder()
        
    def get_acoustic_model(self):
        print(self.device)
        acoustic_model = Text2Speech(
            self.acoustic_config_path,
            self.acoustic_model_path,
            device=self.device
        )
        acoustic_model.spc2wav = None
        return acoustic_model
    
    def get_vocoder(self):
        vocoder = load_model(f'{self.vocoder_path}').to("cuda").eval()
        vocoder.remove_weight_norm()
        return vocoder
        
    def decode_voice(self):
        # decide the input sentence by yourself
        print(f"Input your favorite sentence in Japanese.")
        x = input()
        
        # synthesis
        fs = 24000
        if self.device == 'cuda':
            with torch.no_grad():
                start = time.time()
                wav, c, *_ = self.acoustic_model(x)
                wav = self.vocoder.inference(c)
        else:
            start = time.time()
            wav, c, *_ = self.acoustic_model(x)
            wav = self.vocoder.inference(c)
            
        rtf = (time.time() - start) / (len(wav) / fs)
        print(f"RTF = {rtf:5f}")
        
        # let us listen to generated samples
        from IPython.display import display, Audio
        display(Audio(wav.view(-1).cpu().numpy(), rate=fs))
    
    def download_data(self):
        file_name = 'data.zip'
        gdown.download(self.zip_url, file_name, quiet=True)
        with zipfile.ZipFile(file_name) as model:
            model.extractall('')
        os.remove(file_name)

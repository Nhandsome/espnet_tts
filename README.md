# espnet_tts
ESPnet TTS(Text-to-speech) model trained with tsukuyomichan and jsut001 dataset

  1. モデル
    - Acoustic Model : [ESPnet TTS](https://espnet.github.io/espnet/)
    - Vocoder Model : [Parallel WaveGAN](https://github.com/kan-bayashi/ParallelWaveGAN)
      - Pre-train : [JSUT Dataset](https://sites.google.com/site/shinnosuketakamichi/publication/jsut) 
      - Fine Tune
        - [Tsukuyomichan Dataset](https://tyc.rei-yumesaki.net/material/corpus/)
        - [JVS001 Dataset](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvs_corpus)
  2. 設定
    - runtime設定を「GPU」にしてください


# 使い方
1. Clone github

        
        %cd <path>
        git clone https://github.com/Nhandsome/espnet_tts.git
2. Set environments

        %cd '<path>/espnet_tts'
        pip -q install -r requirements.txt
3. Get trained model

        ## Tsukuyomichan : 'ty'
        ## JVS001 : 'jvs001'
        selected_voice = 'ty'

        from espnet_tts_japanese import EspnetTtsJapanese
        tts_model = EspnetTtsJapanese(selected_voice)

4. Generate Voice

        tts_model.decode_voice()

# 使用データセット
1. つくよみちゃん Corpus
  - https://tyc.rei-yumesaki.net/material/corpus/
  - マルチクリエイター・夢前黎（Rei Yumesaki）さんの「つくよみちゃん」の公式音声Corpus
  - parallel100データで、Fine-Tune

        音声合成には、フリー素材キャラクター「つくよみちゃん」が無料公開している音声データを使用しています。

        ■つくよみちゃんコーパス（CV.夢前黎）
        https://tyc.rei-yumesaki.net/material/corpus/
        © Rei Yumesaki


2. JVS Corpus
  - https://sites.google.com/site/shinnosuketakamichi/research-topics/jvs_corpus
  - 高道 慎之介さんのJVS Corpus
  - JVS001のparallel100データで、Fine-Tune

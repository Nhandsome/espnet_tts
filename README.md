# espnet_tts pre-trained model
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


2. JVS Corpus・JSUT Corpus
  - 高道 慎之介さんのJSUT Corpus
  - https://sites.google.com/site/shinnosuketakamichi/publication/jsut
  - モデルPre-trainのデータセットとして利用
  - 高道 慎之介さんのJVS Corpus
  - https://sites.google.com/site/shinnosuketakamichi/research-topics/jvs_corpus
  - jvs001データで、Fine-Tune

# 利用規約について
音響モデル・Vocoderの利用は、JVS・JSUT・つくよみちゃんコーパスの利用規約に従い、
  - 研究目的で利用
  - 非商用目的の利用
  - 個人での利用（ブログなどを含む）

が可能ですが、申し訳ございませんが、目的以外の二次利用や再配布についてはお断りしております。

特に、「個人での利用」については「ヘイトスピーチへの使用禁止」条件として下記事項を遵守願います。

---
【禁止事項】<br>
  次の用途にはご利用いただけません。
1. 人を批判・攻撃すること。
2. 特定の政治的立場・宗教・思想への賛同または反対を呼びかけること。
3. 刺激の強い表現をゾーニングなしで公開すること。
4.  合成された音声を、他者に対して二次利用（素材としての利用）を許可する形で公開すること。
  なお、「批判・攻撃」の定義は、つくよみちゃんキャラクターライセンス（ https://tyc.rei-yumesaki.net/about/terms/#condition3 ）に準じます。
---


- 音声コーパス関する利用規約は次を参考してください。
  - [つくよみちゃん Corpus](https://tyc.rei-yumesaki.net/material/corpus/#terms)
  - [JVS Corpus](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvs_corpus#h.p_OP_G8FT_Kuf4)
  - [JSUT Corpus](https://sites.google.com/site/shinnosuketakamichi/publication/jsut#h.p_YexdnC0CAtY8)

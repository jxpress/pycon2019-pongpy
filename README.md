# JX Pong Challenge - PyCon JP 2019

https://pycon.jp/2019/

## 概要

**強いアルゴリズムを組んで賞品をゲットしよう!!**

- PyConJP 2019 のJX通信社ブースで、アルゴリズムを組んだコンピュータ同士の Pong 大会を実施します！
- Python で最強の Pong チームを目指しましょう!
- 上位者には賞品も用意しています.


## キャンペーン参加方法

- PyConJP 2019 JX通信社ブースにてどなたでもご参加いただけます.
- 参加者は右上のボタンからこのレポジトリを Fork してください.
- Fork したレポジトリに下記の手順で Pong チームを実装してください.
- 実装が終わったら弊社ブースにお越しください.
    - GitHub のアカウント名でエントリーできます.
- プログラムでなく人力での参戦も可能です。ゲームの腕に自身がある方はぜひ参戦ください。

## チームの実装方法

### 環境構築

- [本ゲーム](https://github.com/pistatium/pong)は[pyxel](https://github.com/kitao/pyxel)を使って実装されています
    - macOS/Linux では`pyxel` 自体のほかに、`sdl2` が必要となります
    - OS ごとのインストール方法は上記公式 Repository を参照してください
- Pythonの依存ライブラリインストール用にPipfileとrequirements.txtを用意していますので、お手元の環境に合わせてご利用ください
- セットアップができていれば、環境変数を以下の通り指定し `pongpy challenger:ChallengerTeam enemy:EnemyTeam` でゲームが開始されます
    - `PYTHONPATH`: このリポジトリのルートディレクトリ
    - `PLAYER_NAME`: 画面に表示するプレーヤー(あなた)の名前

### ローカル環境でプレイ開始

- `pongpy` コマンドの第一引数と第二引数にそれぞれ実装したクラスを指定することで任意の組み合わせで対戦ができます
- `teams` 以下に参考実装がありますので、対戦相手として利用してみてください
    - (例)
        - `PLAYER_NAME=foo pongpy challenger:ChallengerTeam teams.random_team:RandomTeam`
        - `PLAYER_NAME=bar pongpy challenger:ChallengerTeam teams.manual_team:ManualTeam`
            - `I,K,W,S` をつかってキーボード操作ができます

### 実装方法

- `challenger.py` 内の `ChallengerTeam` クラスに実装してください。
    - `atk_action`: 前衛の青色のバーをコントロールします
    - `def_action`: 後衛のオレンジ色のバーをコントロールします
    - それぞれの関数の
        - 返り値が正であれば下、負であれば上に向かってバーが動きます(ゼロの場合は停止します)
        - 引数の `info` から以下の情報が取得できます
            − フィールドのサイズ
            - ボールのサイズ
            - バーの幅、1フレームあたりの最大移動距離
        - 引数の `state` から現在のゲーム状況が取得できます
            - 自チームのバーの位置
            - 敵チームのバーの位置
            - ボールの位置
            - 経過フレーム数
            - 自陣の向き(右側かどうかを `bool` で表します)
    - より詳細な実装方法は[こちら](https://github.com/pistatium/pong#チームの実装方法)を参照してください
- `pongpy` 自体はクラス名や実装するファイル名を自由にしていできますが、本キャンペーンではファイル名とクラス名は変更せず、 `challenger.py` とその中の `ChallengerTeam` を利用してください

### 
* [GitHub: pistatium/pong](https://github.com/pistatium/pong)

* [JX通信社 エンジニアブログ: 報道を自動化するエンジニアはゲーム自動化の夢を見るか](https://tech.jxpress.net/entry/2019/03/22/190724)


# PyCon2019

## 概要

JX通信社はPyCon2019の会場でうんぬんかんぬん(ルール説明)

[JX通信社 エンジニアブログ: 報道を自動化するエンジニアはゲーム自動化の夢を見るか](https://tech.jxpress.net/entry/2019/03/22/190724)

## キャンペーン参加方法

- PyCon2019 JX通信社ブースにてどなたでもご参加いただけます

- 人力編
    - 戦いに備えて心の準備をしておいてください
- Pythonista編
    - 本リポジトリをフォークして、あなたのさいつよのCOMを`player.py` 内の `PlayerTeam` クラスに実装してフォーク先へプッシュしてください

## 遊び方

### 環境構築

- [本ゲーム](https://github.com/pistatium/pong)は[pyxel](https://github.com/kitao/pyxel)を使って実装されています
    - macOS/Linuxでは`pyxel` 自体のほかに、`sdl2` が必要となります
    - OSごとのインストール方法は上記公式Repositoryを参照してください
- Pythonの依存ライブラリインストール用にPipfileとrequirements.txtを用意していますので、お手元の環境に合わせてご利用ください
- セットアップができていれば、環境変数を以下の通り指定し `pongpy player:PlayerTeam enemy:EnemyTeam` でゲームが開始されます
    - `PYTHONPATH`: このリポジトリのルートディレクトリ
    - `PLAYER_NAME`: 画面に表示するプレーヤー(あなた)の名前
- シェルスクリプトを動かせる環境であれば環境変数を指定しなくても `sh play.sh <プレーヤー名>` でゲームが開始できます

### ローカル環境でプレイ開始

- `pongpy` コマンドの第一引数と第二引数にそれぞれ実装したクラスを指定することで任意の組み合わせで対戦ができます
- `teams` 以下に参考実装がありますので、対戦相手として利用してみてください
    - (例)
        - `PLAYER_NAME=foo pongpy player:PlayerTeam teams.random_team:RandomTeam`
        - `PLAYER_NAME=bar pongpy player:PlayerTeam teams.manual_team:ManualTeam`
            - `I,K,W,S` をつかってキーボード操作ができます

### 実装方法

- `player.py` 内の `PlayerTeam` クラスに実装してください。
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
- `pongpy` 自体はクラス名や実装するファイル名を自由にしていできますが、本キャンペーンではファイル名とクラス名は変更せず、 `player.py` とその中の `PlayerTeam` を利用してください

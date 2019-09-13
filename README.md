# JX Pong Challenge - PyCon JP 2019

![](https://github.com/pistatium/pong/blob/master/resources/pongpy.gif?raw=true)

https://pycon.jp/2019/

## 概要

**強いアルゴリズムを組んで賞品をゲットしよう!!**

- PyConJP 2019 のJX通信社ブースで、アルゴリズムを組んだコンピュータ同士の Pong 大会を実施します！  
- Python で最強の Pong チームを目指しましょう!  
- 上位者には賞品も用意しています.

### Pong ルール
- 11点先取、デュースあり
- チェンジコートなし
- ゲームが長引くにつれ双方のバーが中央に寄っていきます

## キャンペーン参加方法

- PyConJP 2019 JX通信社ブースにてどなたでもご参加いただけます.
- 参加者は右上のボタンからこのレポジトリを Fork してください.
- Fork したレポジトリに下記の手順で Pong チームを実装してください.
- 実装が終わったら弊社ブースにお越しください.
    - GitHub のアカウント名でエントリーできます.
- プログラムでなく人力での参戦も可能です。ゲームの腕に自身がある方はぜひ参戦ください。

## チームの実装方法

### 環境構築

#### 1.Pyxel のインストール
- まずはじめに Pyxel というゲームエンジンをインストールしてください
- https://github.com/kitao/pyxel

- mac + brew の環境であれば以下でインストールできます.

```
brew install python3 sdl2 sdl2_image
pip3 install -U pyxel
```
- 他のOSについては公式 Repository を参照してください.

#### 2.レポジトリのフォーク
- GitHub 右上のボタンから個人のレポジトリへフォークしてください.
- フォーク後、ローカルに clone してきます.

```
git clone git@github.com:${GitHubのユーザー名}/pycon2019-pongpy.git
cd pycon2019-pongpy
```

#### 3.キャンペーン用のゲームをインストール
- Pipfile と requirements.txt を用意していますので、お好きな方法でインストールしてください.

```
# requirements.txt を使う場合
pip3 install -r requirements.txt
```

- インストールが完了したら `pongpy` コマンドを実行して動くか試してみてください.
- ウインドウが開きゲームが始まればインストール完了です.

### pongpy コマンドの使い方
- `pongpy` コマンドでは引数にチームを指定することができます.
- 第一引数が左側チーム、第二引数が右側チームの指定になります.
    - 第一引数のみ指定した場合、pongpy デフォルトのチームとの対戦になります.
- `PLAYER_NAME=${GitHubのユーザー名} pongpy challenger:ChallengerTeam enemy:EnemyTeam` コマンドを実行してみてください.
    - challenger.py と enemy.py で実装されたチームの対戦が始まります.
    - PLAYER_NAME 環境変数は画面に表示されるチーム名です.  
    - 実行できない場合 `export PYTHONPATH=$(pwd)` などをしてパスの確認をしてください.

- `pongpy teams.manual_team:ManualTeam` のコマンドを実行すると左チームを手動操作できます.
    - `I,K,W,S` のキーで操作が可能です

### 実装方法

- `challenger.py` がエントリー用のチームとなります.
    - このファイルを編集して、チームを実装してください.
    - ファイル名、クラス名の `ChallengerTeam` を変更すると参加できません.
- `enemy.py` はデバッグ用のダミーチームです.
    - こちらは自由に変更して構いませんが、ブースでの対戦時には利用されません.
- 実装が完了したら GitHub のレポジトリに Push してください.

#### challenger.py

- 以下の2つの関数を実装していただきます.
    - `atk_action`: 前衛の青色のバーをコントロール
    - `def_action`: 後衛のオレンジ色のバーをコントロール
- それぞれの関数は毎フレームごとに呼ばれ、行動を決定します.
- それぞれの関数は `info: GameInfo`, `state: State` を受け取り、int型の数値を返します. 
    - 引数の `info` から以下の情報が取得できます.
        − フィールドのサイズ
        - ボールのサイズ
        - バーの幅、1フレームあたりの最大移動距離
    - 引数の `state` から現在のゲーム状況が取得できます.
        - 自チームのバーの位置
        - 敵チームのバーの位置
        - ボールの位置
        - 経過フレーム数
        - 自陣の向き
            - キャンペーンでは常に左側チーム固定になります.
    - 返り値が正であれば下へ、負であれば上に向かってバーが動きます.
        - 0 の場合は停止します.
        - 取れる値の範囲は info から取得してください.
- 実装のサンプルを /teams に載せてます.
    
- より詳しい実装方法については以下を参照してください.
    - [GitHub: pistatium/pong](https://github.com/pistatium/pong)



### 関連
* [JX通信社 エンジニアブログ: 報道を自動化するエンジニアはゲーム自動化の夢を見るか](https://tech.jxpress.net/entry/2019/03/22/190724)


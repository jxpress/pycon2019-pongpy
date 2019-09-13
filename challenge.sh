#!/bin/sh
read -p 'Your GitHub account: ' PLAYER_NAME

export PYTHONPATH=$PYTHONPATH:$(pwd)
export PLAYER_NAME=$PLAYER_NAME

wget -q -O challenger.py https://raw.githubusercontent.com/$PLAYER_NAME/pycon2019-pongpy/master/challenger.py

if [ "$?" -ne "0" ]; then
  >&2 echo "challenger.pyが見つかりませんでした"
  >&2 echo "GitHub Accout、リポジトリ構造、ファイル名を確認してください"
  exit 1
fi

pipenv run pongpy challenger:ChallengerTeam jx:JXTeam|tee -a result.txt

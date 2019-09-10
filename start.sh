if [ "$1" == "" ]; then
        echo "第一引数にプレーヤー名を指定してください"
        exit 1
fi

echo PLAYER_NAME: $1

export PYTHONPATH=$PYTHONPATH:$(pwd)
PLAYER_NAME=$1 pongpy challenger:ChallengerTeam enemy:EnemyTeam

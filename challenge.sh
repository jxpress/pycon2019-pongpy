if [ "$1" == "" ]; then
        echo "第一引数にGitHubアカウントを指定してください ex) `pistatium`"
        exit 1
fi

echo PLAYER_NAME: $1

export PYTHONPATH=$PYTHONPATH:$(pwd)
export PLAYER_NAME=$1

wget -O challenger.py https://raw.githubusercontent.com/$PLAYER_NAME/pycon2019-pongpy/master/challenger.py

if [ "$?" -ne "0" ]; then
  echo "Sorry, cannot find your challenger.py"
  exit 1
fi

pongpy challenger:ChallengerTeam jx:JxTeam
#!/bin/bash

tmux kill-server
cd project-404-team-name-not-found
git fetch && git reset origin/main --hard
. python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new -d 'source project-404-team-name-not-found | source python3-virtualenv/bin/activate | flask run --host=0.0.0.0'
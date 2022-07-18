#!/bin/bash

cd project-404-team-name-not-found
git fetch && git reset origin/main --hard
. python3-virtualenv/bin/activate
pip install -r requirements.txt
systemctl restart myportfolio

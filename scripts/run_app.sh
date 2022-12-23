#!/bin/bash

KEY=`python -c "from uuid import uuid4; print(uuid4().hex)"`

cat <<< "KEY = '$KEY'" > ../web/config.py 

python ../web/app.py
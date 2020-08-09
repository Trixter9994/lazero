#!/bin/bash
python3 metaCheckIV.py  sklearn > subdir/sklearn_notsame.py
python3 metaCheckIV.py  torch > subdir/torch_notsame.py
# you always have something to make me busy.
# something under __all__ tells the story.
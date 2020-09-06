#!/bin/bash
pip3 install -U spacy-lookups-data
python3 -m spacy download en_core_web_sm
python3 -m spacy download de_core_news_sm
python3 -m spacy download fr_core_news_sm
python3 -m spacy download es_core_news_sm
python3 -m spacy download pt_core_news_sm
python3 -m spacy download it_core_news_sm
python3 -m spacy download nl_core_news_sm
python3 -m spacy download el_core_news_sm
python3 -m spacy download nb_core_news_sm
python3 -m spacy download lt_core_news_sm
python3  -m spacy download xx_ent_wiki_sm

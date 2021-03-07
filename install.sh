#pip install -U pip setuptools wheel
pip install -r ./requirements.txt

python3 -m spacy download "de_core_news_sm"
python3 -m spacy download "fr_core_news_sm"
python3 -m spacy download "it_core_news_sm"
python3 -m spacy download "es_core_news_sm"

echo "DONE"

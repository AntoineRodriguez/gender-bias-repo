#pip install -U pip setuptools wheel
pip install -r ./requirements.txt

python -m spacy download en
python -m spacy download de
python -m spacy download it
python -m spacy download es
python -m spacy download fr

echo "DONE"
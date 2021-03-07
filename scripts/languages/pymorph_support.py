"""
In this code, we aim to identify the gender according to the word's morphology analysis
in Russian and Ukrainian
"""
from collections import Counter

import pymorphy2
from pymorphy2.tokenizers import simple_word_tokenize

from util import GENDER, PYMORPH_GENDER_TYPES


class PymorphPredictor:
    """
    Class for PyMorph supported languages.
    These include Russian and Ukrainian.
    """
    def __init__(self, lang: str):
        """
        Init pymorph for the specified language code.
        https://pymorphy2.readthedocs.io/en/latest/user/guide.html
        """
        assert lang in ["uk", "ru"]
        self.lang = lang
        self.cache = {}    # Store calculated professions genders
        self.tagger = pymorphy2.MorphAnalyzer(lang=lang)

    def get_gender(self, profession: str, translated_sent = None, entity_index = None, ds_entry = None) -> GENDER:
        """
        Predict gender of an input profession.
        """
        if profession not in self.cache:
            self.cache[profession] = self._get_gender(profession)  # predict profession's gender

        return self.cache[profession]

    def _get_gender(self, profession: str) -> GENDER:
        """
        Predict gender, without using cache
        """
        if not profession.strip():
            # Empty string
            return GENDER.unknown

        toks = simple_word_tokenize(profession)

        observed_genders = [self.get_word_gender(tok) for tok in toks] #predict the probable gender 

        if not observed_genders:
            # No observed gendered words - return unknown
            return GENDER.unknown

        # Return the most commonly observed gender
        return Counter(observed_genders).most_common()[0][0]

    def get_word_gender(self, word):
        """
        Get the most probable gender, based on the frequency of
        predictions.
        """
        morphs = self.tagger.parse(word)
        observed_genders = [PYMORPH_GENDER_TYPES[morph.tag.gender] for morph in morphs  # get the gender from tagger
                            if (morph.tag.gender is not None)]

        if not observed_genders:
            return GENDER.neutral

        if GENDER.female in observed_genders:
            return GENDER.female
        # Return the most commonly observed gender
        return Counter(observed_genders).most_common()[0][0]


if __name__ == "__main__":
    ds = ['female', 1, 'The developer argued with the designer because she did not like the design.', 'developer']
    tr_sent_uk = 'Розробник сперечалися з designer, бо вона не як оформлення'
    p = PymorphPredictor(lang="uk")
    pred_uk = p.get_gender('Розробник', tr_sent_uk, 0, ds)
    print(pred_uk)
    print("UKRANIAN TEST DONE")

    ds = ['female', 1, 'The developer argued with the designer because she did not like the design.', 'developer']
    tr_sent_ru = 'Разработчик спорил с дизайнером, потому что ей не понравился дизайн'
    p = PymorphPredictor(lang="ru")
    pred_ru = p.get_gender('Разработчик', tr_sent_ru, 0, ds)
    print(pred_ru)
    print("RUSSIAN TEST DONE")

""" 
module for create class GENDER with functions to do some manipulations of gender
"""
# External imports

import spacy
import pdb
from pprint import pprint
from pprint import pformat
from docopt import docopt
from collections import defaultdict
from operator import itemgetter

from enum import Enum
from spacy.tokens.token import Token
from typing import Dict

# Local imports

#=-----

class GENDER(Enum):
    """
    Enumerate possible genders.
    Ignore option resolves to words that should be ignored in particular language
    """
    male = 0
    female = 1
    neutral = 2
    unknown = 3
    ignore = 4 

# Winobias gender type conversion
WB_GENDER_TYPES = {
    "male": GENDER.male,
    "female": GENDER.female,
    "neutral": GENDER.neutral,
}


####MMMETTTTTRRRRRRREEEEEEEE AAAAAAAAA JJJJJJOURRRRRRRRRRRR





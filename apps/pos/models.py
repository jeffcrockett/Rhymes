from __future__ import unicode_literals
# from ..black_belt.models import Quotes, Favorites
from django.db import models
import bcrypt
import re
from nltk.corpus import cmudict as c

class Word(models.Model):
    spelling = models.CharField(max_length = 30)
    vowels = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()
# Create your models here.
'''
>>> def match_vowels(a):
...    c = cmudict.entries()[100:150]
...    for tupl in c:
...       for item in a:
...          if item in tupl[1]:
...             return ('Match!', tupl[0], tupl[1])
...
>>> match_vowels(['AH1'])
('Match!', u'abduct', [u'AE0', u'B', u'D', u'AH1', u'K', u'T'])
>>> match_vowels(['AH1'])
('Match!', u'abduct', [u'AE0', u'B', u'D', u'AH1', u'K', u'T'])
>>> match_vowels(['AA'])
>>> match_vowels(['AA1'])
('Match!', u'abdollah', [u'AE2', u'B', u'D', u'AA1', u'L', u'AH0'])

>>> [i for i in cmudict.entries()[:50] if len(i[1][0])==3]
[(u'a', [u'AH0']), (u'a.', [u'EY1']), (u'a', [u'EY1']), (u'a42128', [u'EY1', u'F', u'AO1', u'R', u'T', u'UW1', u'W', u'AH1', u'N', u'T', u'UW1', u'EY1', u'T']), (u'aaberg', [u'AA1', u'B', u'ER0', u'G']), (u'aachen', [u'AA1', u'K', u'AH0', u'N']), (u'aachener', [u'AA1', u'K', u'AH0', u'N', u'ER0']), (u'aaker', [u'AA1', u'K', u'ER0']), (u'aalseth', [u'AA1', u'L', u'S', u'EH0', u'TH']), (u'aamodt', [u'AA1', u'M', u'AH0', u'T']), (u'aancor', [u'AA1', u'N', u'K', u'AO2', u'R']), (u'aardema', [u'AA0', u'R', u'D', u'EH1', u'M', u'AH0']), (u'aardvark', [u'AA1', u'R', u'D', u'V', u'AA2', u'R', u'K']), (u'aaron', [u'EH1', u'R', u'AH0', u'N']), (u"aaron's", [u'EH1', u'R', u'AH0', u'N', u'Z']), (u'aarons', [u'EH1', u'R', u'AH0', u'N', u'Z']), (u'aaronson', [u'EH1', u'R', u'AH0', u'N', u'S', u'AH0', u'N']), (u'aaronson', [u'AA1', u'R', u'AH0', u'N', u'S', u'AH0', u'N']), (u"aaronson's", [u'EH1', u'R', u'AH0', u'N', u'S', u'AH0', u'N', u'Z']), (u"aaronson's", [u'AA1', u'R', u'AH0', u'N', u'S', u'AH0', u'N', u'Z']), (u'aarti', [u'AA1', u'R', u'T', u'IY2']), (u'aase', [u'AA1', u'S']), (u'aasen', [u'AA1', u'S', u'AH0', u'N']), (u'ab', [u'AE1', u'B']), (u'ab', [u'EY1', u'B', u'IY1']), (u'ababa', [u'AH0', u'B', u'AA1', u'B', u'AH0']), (u'ababa', [u'AA1', u'B', u'AH0', u'B', u'AH0']), (u'abacha', [u'AE1', u'B', u'AH0', u'K', u'AH0']), (u'aback', [u'AH0', u'B', u'AE1', u'K']), (u'abaco', [u'AE1', u'B', u'AH0', u'K', u'OW2']), (u'abacus', [u'AE1', u'B', u'AH0', u'K', u'AH0', u'S']), (u'abad', [u'AH0', u'B', u'AA1', u'D']), (u'abadaka', [u'AH0', u'B', u'AE1', u'D', u'AH0', u'K', u'AH0']), (u'abadi', [u'AH0', u'B', u'AE1', u'D', u'IY0']), (u'abadie', [u'AH0', u'B', u'AE1', u'D', u'IY0']), (u'abair', [u'AH0', u'B', u'EH1', u'R']), (u'abalkin', [u'AH0', u'B', u'AA1', u'L', u'K', u'IH0', u'N']), (u'abalone', [u'AE2', u'B', u'AH0', u'L', u'OW1', u'N', u'IY0']), (u'abalos', [u'AA0', u'B', u'AA1', u'L', u'OW0', u'Z']), (u'abandon', [u'AH0', u'B', u'AE1', u'N', u'D', u'AH0', u'N']), (u'abandoned', [u'AH0', u'B', u'AE1', u'N', u'D', u'AH0', u'N', u'D']), (u'abandoning', [u'AH0', u'B', u'AE1', u'N', u'D', u'AH0', u'N', u'IH0', u'NG']), (u'abandonment', [u'AH0', u'B', u'AE1', u'N', u'D', u'AH0', u'N', u'M', u'AH0', u'N', u'T']), (u'abandonments', [u'AH0', u'B', u'AE1', u'N', u'D', u'AH0', u'N', u'M', u'AH0', u'N', u'T', u'S']), (u'abandons', [u'AH0', u'B', u'AE1', u'N', u'D', u'AH0', u'N', u'Z']), (u'abanto', [u'AH0', u'B', u'AE1', u'N', u'T', u'OW0']), (u'abarca', [u'AH0', u'B', u'AA1', u'R', u'K', u'AH0']), (u'abare', [u'AA0', u'B', u'AA1', u'R', u'IY0']), (u'abascal', [u'AE1', u'B', u'AH0', u'S', u'K', u'AH0', u'L']


TAGGED_SENTS =  treebank.tagged_sents()
PARSED_SENTS = treebank.parsed_sents()



def count_left_braces(s):
    count = 0
    for letter in s:
       if letter =='(':
          count += 1
       if letter ==')':
          return count
    return count

def count_left_braces_one_level_deep(s):
    count_left = 0
    count_right = 0
    for letter in s:
        if letter == '(':
            count_left += 1
        if letter == ')':
            count_right += 1
            if count_right  > 1:
                return count_left
    return count_left

s = count_left_braces_one_level_deep(str(PARSED_SENTS[500]))
print (s)
|
Example:
 |
 |      >>> from nltk.tag import StanfordPOSTagger
 |      >>> st = StanfordPOSTagger('english-bidirectional-distsim.tagger')
 |      >>> st.tag('What is the airspeed of an unladen swallow ?'.split())
 '''

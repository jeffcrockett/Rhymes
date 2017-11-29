from __future__ import unicode_literals
from django.shortcuts import render, redirect
from nltk.corpus import cmudict
from models import Word
import re
import math

# Create your views here.
PHONEME_STRINGS =  [(e[0], ''.join(e[1])) for e in cmudict.entries()]
PATTERN = r'([AEIOUHY]{2}[0-2]([RLMN(NG)])?)+'
x = [(s[0], re.findall(PATTERN, s[1])) for s in PHONEME_STRINGS]
PRON_DICT = {}
for i in PHONEME_STRINGS:
    PRON_DICT[i[0]] = i[1]
# PARSED_SENTS = treebank.parsed_sents()
# WORDS = treebank.words()
# TRANSCR = cmudict.entries()

def filtered(w):
    soft_sounds = ['L', 'R', 'M', 'N', 'NG']
    el = []
    for p in range(len(w)):
        if len(w[p]) == 3:
            el.append(w[p])
        elif p > 0 and w[p-1] and w[p] in soft_sounds:
            el.append(w[p])
        else:
            el.append('')
    return el


def filtered(x):
    return [re.findall(r'\w{3}', i) for i in x]
    # el = []
    # for i in x:
    #    for j in i[1]:
    #       if len(j) == 3:
    #          el.append(j)
    #    el.append('|')
    # vowel_list =  ' '.join(el).split('|')
    # return [vowel.strip() for vowel in vowel_list]

def collapsed(x):
    el = []
    for i in x:
        if len(i) > 0:
            for a in i:
                el.append(a)
    return el

def index(request):
    return render(request, 'pos/index.html')

# def test(s):
#     pass
#
def rhymes(request):
    context = {}
    d = cmudict.dict()
    entries = cmudict.entries()
    phonemes = []
    if request.method == 'POST':
        word = request.POST['rhyming-words']
        for i in word.split(' '):
            try:
                phonemes.append(d[i][0])
            except KeyError:
                return render(request, 'pos/rhymes.html', {'error': 'Error: Word not found'})
        print ('phonemes', phonemes)
        template = collapsed(filtered(collapsed(phonemes)))
        print ('template', template)
        print ('shortened template', [i[:-1] for i in template])
        context['rhymes'] = [i for i in entries if collapsed(filtered(i[1])) == template]
        print context['rhymes']
        context['words'] = [i[0] for i in context['rhymes']]
        context['prons'] = [i[1] for i in context['rhymes']]
        context['word'] = word
        return render(request, 'pos/index.html', context)

def rhymesbeta(request):
    context = {'rhymesbeta': []}
    if request.method == 'POST':
        word = request.POST['rhyming-words']
        if word.lower() in PRON_DICT:
            phons = ''.join(PRON_DICT[word.lower()])
            for (a, b) in PHONEME_STRINGS:
                if re.findall(PATTERN, b) == re.findall(PATTERN, phons) and abs(len(b) - len(phons)) < 3:
                    context['rhymesbeta'].append(a)
    context['word'] = word
    return render(request, 'pos/index.html', context)

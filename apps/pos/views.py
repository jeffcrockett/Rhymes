from __future__ import unicode_literals
from django.shortcuts import render
from nltk.corpus import treebank
from nltk.tree import Tree
from nltk.corpus import cmudict
from models import Word

# Create your views here.

PARSED_SENTS = treebank.parsed_sents()
WORDS = treebank.words()
TRANSCR = cmudict.entries()
def index(request):
    context = {'pos':
            []}
    if request.method == 'POST':
        s = request.POST['sentence'].split(' ')
        for word in [i.lower() for i in s]:
            for item in TRANSCR:
                if word == item[0]:
                    context['pos'].append({word: item[1]})
    return render(request, 'pos/index.html', context)

def many_to_one(request):
    pass

def test(request):
    words = Word.objects.all()[15000:16000]
    context = {
    'words': words
    }
    return render(request, 'pos/index2.html', context)

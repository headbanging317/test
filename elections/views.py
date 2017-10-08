# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Candidate
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    str = ''
    for candidate in candidates:
        str += "<p>{} 기호{}번({})<br>".format(candidate.name, candidate.party_number, candidate.area)
        str += candidate.introduction+"</p>"

    url = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=300'
    html = requests.get(url).text
    soup = BeautifulSoup(html)
    name = ''
    link = ''
    for member_tag in soup.select('.memberna_list dl dt a'):
        name += member_tag.text+"<br>"
        link += member_tag['href']
    return render(request, 'elections/index.html')



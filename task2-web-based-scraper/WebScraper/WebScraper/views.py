#my creation

from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from DjangoWebScraper.models import Link

def index(request):
    user_link= request.GET.get('userlink','default')  
    if(user_link!="default"):
        page=requests.get(user_link)
        soup=BeautifulSoup(page.content,"html.parser")
        link=soup.find_all('a')
        unique_link_lst=list(set(link))
        #print(len(unique_link_lst))
        non_empty_lst=[]
        for i in range(len(unique_link_lst)):
            if("https" in unique_link_lst[i]["href"]):
                non_empty_lst.append(unique_link_lst[i]["href"])
                link_add = Link(scraped_link=unique_link_lst[i]["href"])
                link_add.save()
        #print(type(Link.objects.all()))
        if(len(non_empty_lst)>0):
            return render(request,'index.html',{"queryset":non_empty_lst})
    return render(request,'index.html') 
    # return HttpResponse("hello")
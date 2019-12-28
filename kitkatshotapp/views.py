from django.shortcuts import render, HttpResponse, redirect
from bs4 import BeautifulSoup
from random import randint
import pdfcrowd
# Create your views here.

def index(request):
    return render(request, 'public/index.html', {'title': 'KitKatShot'})

def action(request):
    if request.method == 'POST':
        html = request.POST.get('code')
        fname = str(randint(100, 100000))
        fileForShotFile = "./kitkatshotapp/templates/htmlshot/"+fname+".html"
        print(fileForShotFile)
        fileForShot = open(fileForShotFile, "w")
        fileForShot.write(html)
        fileForShot.close()
        # print(html)
        

        client = pdfcrowd.HtmlToImageClient('wrs', '871e6e01dcde0e76e316d47f72916811')
        client.setOutputFormat('png')
        imagefileName = fname+".png"
        htmlshoturl = "/htmlshotview/"+fname

        weburl = "https://kitkatshot.herokuapp.com"+htmlshoturl
        imagefileSaveToAs = "./kitkatshotapp/static/htmlshotimg/"+imagefileName

        client.convertUrlToFile(weburl, imagefileSaveToAs)
        finalOutput = "https://kitkatshot.herokuapp.com/static/htmlshotimg/"+imagefileName
        print("finalOutput:", finalOutput)
        # print(redirecturl)
    return render(request, "public/result.html", {'title': 'KitKatShot', 'image': finalOutput})

def htmlshotview(request, fname):
    htmlfile = str(fname)+".html"
    htmlfilepath = "htmlshot/"+htmlfile
    # print(htmlfile)
    return render(request, htmlfilepath, {})
import requests
import json
import nltk
def sentimentAnalysis(txt):
    # using the Sentiment Analysis API
    url = "http://text-processing.com/api/sentiment/"

    posNo = 0
    negNo = 0

    for word in txt:
        req = requests.post(url,data="text="+word)
    #    print
        print req.text
    #    print
      #  (prob, label) = req.text.split('},')
       # (lb, value) = label.split(": ")
        # final value is pos, neg or neu
        #val = value[1:4]

        #if (val == "pos"):
         #   posNo += 1
        #elif (val == "neg"):
         #   negNo += 1

   # if (posNo >= negNo):
        return "HAPPYYYYY"
   # else:
    #    return "ANGRYYYYYY"

def hello():
    f = open('results', 'w')
    name="zachbpd"
    url2="https://api.github.com/users/"+name+"/repos"
    ram='comRamona'
    auth= 'd3fd78a853bda3a636ee51e655f2cc6476a37498'
    repos = requests.get(url2,auth=(ram,auth)).json()
    commits=[]
    words=[]
    for repo in repos:
        x=repo['name']
        commits+=x
        f.write(x)
    for repo in repos:
        repo_name=repo['name']
        commits+=repo_name
        f.write("NAME: "+repo_name+"\n\n\n")
        commit_url="https://api.github.com/repos/"+name+"/"+repo_name+"/commits"
        all=requests.get(commit_url,auth=(ram,auth)).json()
        for a in all:
            if(type(a) is dict):
                x=str(a['commit']['message'])
                y=nltk.tokenize.regexp_tokenize(x, r'\w+')
                words+=y
                commits+=x
                f.write(x)
    f.close()
    cats=["eat","pray","love"]

    print sentimentAnalysis(cats)



hello()

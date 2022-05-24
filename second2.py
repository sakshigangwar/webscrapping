from bs4 import BeautifulSoup
import requests
import json
import pprint
from Task_1 import data
list1=[]
def group_movie_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)


    movie_dict={i:[]for i in years}
    for i in movies:
        year=i['year']
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    a=[]
    for y in movie_dict: 
        a.append(y)
    i=0
    while i<len(a):
        j=0
        while j<(len(a)-i-1):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
            j=j+1
        i=i+1
    new_movie_dict={}
    for i in a:
        for x,y in movie_dict.items():
            if x==i:
                new_movie_dict[i]=y
    with open("Task_2.json","w")as file:
        json.dump(new_movie_dict,file,indent=4)
    return new_movie_dict
print(group_movie_by_year(data))
data2=group_movie_by_year(data)

    

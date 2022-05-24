import json

def group_of_decades(movies):
    moviesdict={}
    list1=[]
    for index in movies:
        mod=int(index)%10
        decade=int(index)-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviesdict[i]=[]
    for i in moviesdict:
        dic10=i+9
        for x in movies:
            if int(x)>=i and int(x)<=dic10:
                for v in movies[x]:
                    moviesdict[i].append(v)
    with open("Task_3.json","w")as file:
        json.dump(moviesdict,file,indent=4)
    return(moviesdict)
file=open("Task_2.json","r")
read=file.read()
data=json.loads(read)
print=(group_of_decades(data))



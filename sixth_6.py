import json
f = open("Task_5.json","r")
read = f.read()
data = json.loads(read)
i = 0
count_of_language = {}
while i < len(data):
    j = 0
    count = 0 
    while j < len(data[i]["Original Language:"]):
        count = 0
        k = 0 
        while k < len(data):
            for l in data[k]["Original Language:"]:
                if  data[i]["Original Language:"][j] == l :
                    count+=1
            k+=1
        count_of_language[data[i]["Original Language:"]] = count
        j+=1
    i+=1
print(count_of_language)
	

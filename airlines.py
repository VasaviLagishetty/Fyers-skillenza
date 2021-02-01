import json

with open('airlines.csv') as f:
    lines = [line.split('"') for line in f]
    d = dict()
    for airline in lines[1:]:
        if airline[1] in d:
            d[airline[1]] += 1
        else:
            d[airline[1]] = 1

sorted_airlines = sorted(d.items(),key = lambda item : item[1])
print(json.dumps(d,indent = 4))
print(sorted_airlines[-1][0],sorted_airlines[-1][1])
print(sorted_airlines[0][0],sorted_airlines[0][1])

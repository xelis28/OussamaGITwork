text = "hbwqwbuwbwub"

car_cccount ={}
j=1

for i in text:
    if i in car_cccount:
        j=j+1
    car_cccount[i]=j
print(car_cccount)
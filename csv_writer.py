person1 = ["coco", 10, "mexico"]


with open('info.csv', 'w') as f:
    for i in range(3):
        current_info = str(person1[i])
        f.write(current_info)
        if i != 2:
            f.write(",")
# d={"shreyas":{"size":20,"length":5,"width":2},"Ajay_don":[12,17,34],"Rane":(1,4,9)}
#
# d["shreyas"].update({"height":12})
# d["Ajay_don"].append(12)
# print(d)


d={"shreyas":{1:1,2:4,3:9,4:16},"Ajay_don":[10,20,30,40],"Rane":(1,4,9)}

d["shreyas"].update({5:25})
d["Ajay_don"].append(50)
print(d)
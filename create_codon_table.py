f=open("standard.code","r")


dicto={}
for i in f:
    print(i.replace("\n","").replace(" ","").split("="))
    result=i.replace("\n","").replace(" ","").split("=")
    key=result[0]
    val=result[1]
    dicto[key]=val

base_1=dicto["Base1"]
base_2=dicto["Base2"]
base_3=dicto["Base3"]

AAs=dicto["AAs"]

for i in range(len(AAs)):

    print(base_1[i]+base_2[i]+base_3[i]+" = "+AAs[i])

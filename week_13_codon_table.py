#week-13
import matplotlib.pyplot as plt

f=open("anthrax_sasp.nuc","r")
x=f.read().replace("\n","")


codon={}
for  i in range(0,len(x),3):
    val=x[i:i+3]
    if val not in codon.keys():
        codon[val]=1
    else:
        codon[val]+=1


print(codon)
plt.bar(codon.keys(),codon.values(),color=["y","r","b"])
plt.show()

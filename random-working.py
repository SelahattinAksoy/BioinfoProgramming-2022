from Bio import Entrez,SeqIO

Entrez.email = "aksoyeren80@gmail.com"

handle = Entrez.esearch(db="nucleotide", retmax=10, term="opuntia[ORGN] accD", idtype="acc")

record = Entrez.read(handle)

handle.close()

print(record["IdList"])
id=record["IdList"]

handle = Entrez.efetch(db="nucleotide", id=id,rettype="gb",retmode="xml")

record = Entrez.read(handle)

handle.close()

x=[]
for i in record:
    x.append(len(i["GBSeq_sequence"]))

print(x)
import matplotlib.pyplot as plt
import numpy as np


plt.hist(x)
plt.show() 

#1
import matplotlib.pyplot as plt
from Bio import Entrez,SeqIO

Entrez.email = "aksoyeren80@gmail.com"

seqlist=[]
for i in SeqIO.parse("ls_orchid.fasta.txt","fasta"):
    seqlist.append(len(i.seq))



plt.hist(seqlist)
plt.show() 


#2
import matplotlib.pyplot as plt
from Bio import Entrez,SeqIO

Entrez.email = "aksoyeren80@gmail.com"

seqlist=[]
for i in SeqIO.parse("ls_orchid.fasta.txt","fasta"):
   seqlist.append(len(i.seq.translate()))
   
plt.hist(seqlist)
plt.show() 


#2
import matplotlib.pyplot as plt
from Bio import Entrez,SeqIO

Entrez.email = "aksoyeren80@gmail.com"

seqlist=[]
for i in SeqIO.parse("ls_orchid.fasta.txt","fasta"):
   x=i.seq
   seqlist.append([x.count("A"),x.count("T"),x.count("C"),x.count("G")])
   
plt.hist(seqlist)



plt.imshow(seqlist, cmap='hot', interpolation='nearest')
plt.show()

#3
import matplotlib.pyplot as plt
from Bio import Entrez,SeqIO
from Bio.Blast import NCBIWWW,NCBIXML
Entrez.email = "aksoyeren80@gmail.com"

seqlist=[]
for i in SeqIO.parse("ls_orchid.fasta.txt","fasta"):
   x=i.seq
   break
   
print(x.lower())
result=NCBIWWW.qblast("blastn","nt",x.lower())

blast_res=NCBIXML.parse(result)

for i in blast_res:
    print(i)
    break


   
#4
from Bio import Entrez, SeqIO
Entrez.email = "aksoyeren80@gmail.com" 
handle = Entrez.efetch(db="nucleotide", id="MN908947", rettype="gb", retmode="text")

recs = list(SeqIO.parse(handle, 'gb'))
for i in recs:
    print(i.description)
    print(len(i.seq))





 #5 important
from Bio import Entrez, SeqIO
import matplotlib.pyplot as plt
Entrez.email = "aksoyeren80@gmail.com" 
handle = Entrez.efetch(db="nucleotide", id="MN908947", rettype="gb", retmode="text")

a={}
recs = list(SeqIO.parse(handle, 'gb'))
for i in recs:
    print(i.description)
    a["A"]=i.seq.count("A")
    a["T"]=i.seq.count("T")
    a["C"]=i.seq.count("C")
    a["G"]=i.seq.count("G")

print(a)

plt.bar(a.keys(),a.values())
plt.show()




#6 important
from Bio import Entrez, SeqIO
import matplotlib.pyplot as plt
Entrez.email = "aksoyeren80@gmail.com" 
handle = Entrez.efetch(db="nucleotide", id="MN908947", rettype="gb", retmode="text")

a={}
recs = list(SeqIO.parse(handle, 'gb'))
for i in recs:
   seq=i.seq

pro=seq.translate()

for i in pro:

    if i not in a.keys():
        a[i]=1
    else:
        a[i]+=1


print(a)

plt.bar(a.keys(),a.values(),color=["r","y","b"])

plt.show()




#6 important num of protein
from Bio import Entrez, SeqIO
import matplotlib.pyplot as plt
Entrez.email = "aksoyeren80@gmail.com" 
handle = Entrez.efetch(db="nucleotide", id="MN908947", rettype="gb", retmode="text")

a={}
recs = list(SeqIO.parse(handle, 'gb'))
for i in recs:
   seq=i.seq

seq_transcribe=seq.transcribe()
pro=seq_transcribe.translate()
#pro=pro.replace("*","")
print(len(seq))
print(len(pro))

protein_list=pro.split("*")
print(len(protein_list))
num=0
for i in protein_list:
    if len(i)>0:
        num+=1
print(num)



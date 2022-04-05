def tround(n, r=1):
 a=str(n)
 b=len(a.split(".")[0])
 a=a.replace(".", "")
 s=r+b-1
 if int(a[s])>=5:
  a=a[:s-1]+str(int(a[s-1])+1)+a[s:]
  if r!=1:
   a=a[:b]+"."+a[b:]
   return a[:s+1]
  else:
   return a[:s]
 else:
  if r!=1:
   a = a[:b]+"."+a[b:]
   return a[:s+1]
  else:
   return a[:s]
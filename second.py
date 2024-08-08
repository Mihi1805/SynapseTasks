gadgets=[
    ("Explosive Batarangs",3,True),
    ("Batarangs",5,True),
    ("Smoke Pellets",0,False),
    ("Tear Gas Grenades",2,True),
    ("Night Vision Goggles",1,True),
    ("Batclaw",0,False),
    ("Grapple Gun",3,True),
    ("Batsignal",0,False),
    ("Utility Belt",1,True),
    ("Batmobile Tires",4,True)
]

#Top Priority
gadgets.sort(reverse=True,key=lambda t:t[2])
#print(gadgets)

#Within Stocked Status
#print(gadgets[:7])
#print(gadgets[7:])
#tr=gadgets[:7] tr.sort(reverse=True,key=lambda n:n[1]) tr=tr + gadgets[7:] print(tr)
tr=sorted(gadgets[:7],reverse=True,key=lambda n:n[1] )
#print(tr+gadgets[7:])
        
#Breaking Ties
for x in range(0,7,1):
    for j in range(x,7,1):
        if tr[x][1]==tr[j][1] and tr[x][0]>tr[j][0]:
            temp=tr[x] 
            tr[x]=tr[j] 
            tr[j]=temp

print(tr+gadgets[7:])
            

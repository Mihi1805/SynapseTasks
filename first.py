from itertools import combinations
Kevin = {"Halsey","Taylor Swift","Mitski","Joji","Shawn Mendes","Sabrina Carpenter","Nicki Minaj",
         "Conan Gray","One Direction","Justin Bieber"}
Stuart ={"Kendrick Lamar","Steve Lacy","Tyler the Creator","Joji","TheWeeknd","Coldplay","Kanye West",
         "Travis Scott","Frank Ocean","Brent Faiyaz"}
Bob ={"Conan Gray","Joji","Dove Cameron","Mitski","Arctic Monkeys","Steve Lacy","Kendrick Lamar",
      "Isabel LaRosa","Shawn Mendes","Coldplay"}
Edith ={"Metallica","Billie Eilish","TheWeeknd","Mitski","NF","Conan Gray","Kendrick Lamar","Nicki Minaj",
        "Kanye West","Coldplay"}

#Creating Combinations
com_list= list(combinations([Kevin,Stuart,Bob,Edith],2))
com_listnames=list(combinations(['Kevin','Stuart','Bob','Edith'],2))

#Finding the overlap
overlap=[]
for x in range(0,6,1):
    o=len(com_list[x][0].intersection(com_list[x][1]))/10
    overlap.append(o)
#print(overlap)

#Sorting the array 
sorted_list=sorted(com_listnames,key=lambda x:overlap[com_listnames.index(x)],reverse=True)
overlap.sort(reverse=True)
for x in range(0,6,1):
    if overlap[x]>=0.3: print(sorted_list[x],overlap[x])


#z=zip(com_listnames,overlap)
#z_list=list(z)
#print(z_list)
#z_list.sort(reverse=True,key=lambda i: z_list[i][1])
#print(z_list)
#com_listnames.sort(reverse=True,key=lambda i:overlap[com_listnames.index(i)])
#print(com_listnames)

customers=[[5,2],[5,4],[10,3],[20,1],[21,4],[30,5]]
n=len(customers)
total=0
iroh=customers[0][0]
for x in range(0,n,1):
    start=customers[x][0]
    print(f"start for {x+1} = {start}")
    if(start<=iroh):
        iroh=iroh+customers[x][1]
    elif(start>iroh):
        iroh=start+customers[x][1]
    print(f"iroh for {x+1} = {iroh}")
    wait=iroh-start
    print(f"wait for {x+1} = {wait}")
    total=total+wait
avg=total/n
print(f"Average Waiting Time: {avg}")
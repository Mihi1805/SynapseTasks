request_spending={
    "Mahek":{
        "balance":3000.00,
        "transactions": [
            {"amount": -9000.00, "category": "Creatives"},
            {"amount": 7000.00, "category": "Sponsor"},
            {"amount": -2000.00, "category": "Prize-Money"}
        ]
    },
    "Arham": {
        "balance":5000.00,
        "transactions": [
            {"amount": 8000.00, "category": "Stalls"},
            {"amount": 7500.00, "category": "Seminar"}
        ]

    },
    "Unnati": {
        "balance":3500.00,
        "transactions": [
            {"amount": -5000.00, "category": "Attraction"},
            {"amount": 2500.00, "category": "Promo"},
            {"amount": -900.00, "category": "Lighting"},
            {"amount": -3000.00, "category": "Games"}
        ]
    },
    "Gaurang":{
        "balance":2000.00,
        "transactions": [
            {"amount": -1500.00, "category": "Website"},
            {"amount": -1000.00, "category": "C2C"},
            {"amount": -500.00, "category": "Posters"}
        ],
    }
}

def total_spending(request_spending,account_id,category):
    n=len(request_spending[account_id]["transactions"])
    for x in range(0,n,1):
        if(request_spending[account_id]["transactions"][x]["category"]==category):
            if(request_spending[account_id]["transactions"][x]["amount"]<0):
                print(f"Amount: {request_spending[account_id]["transactions"][x]["amount"]} Category: {request_spending[account_id]["transactions"][x]["category"]}")
                break 
            else: print('No Amount Spent') 
            break

total_spending(request_spending,"Mahek","Creatives")

def account_balance(request_spending,account_id):
    n=len(request_spending[account_id]["transactions"])
    total=0
    for x in range(0,n,1):
        total=total+request_spending[account_id]["transactions"][x]["amount"]
    print(f"Balance: {total+request_spending[account_id]["balance"]}")

account_balance(request_spending,"Mahek")


def money_owed(request_spending,account_id):
    n=len(request_spending[account_id]["transactions"])
    total=0
    for x in range(0,n,1):
        total=total+request_spending[account_id]["transactions"][x]["amount"]
    if(total<0):
        total=-total
        print(f"Money Owed: {total}")
    elif(total==0):
        print('No Money owed')
    elif(total>0):
        print(f"Extra Money: {total}")

money_owed(request_spending,"Mahek")
    
    
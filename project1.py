#Expense Tracker project

expenseList = [] #list of expenses in form of dictionary 
print("welcome to Expense Tracker:")

while True:
    print("====MENU====")
    print("1.Add Expense")
    print("2.view All Expenses")
    print("3.view Total khrcha")
    print("4.Exit")
    
    choice = int(input("please Enter your choice:"))
    
 #ADD Expense
    if(choice == 1):
        date= input("kis date par khrcha kiya tha ?: ") 
        category=input("kis type ka khrcha kiya?(Food,Travel,Makeup,Books):")
        description=input("Aur detail dedo:")
        amount=float(input("Enter the amount:"))
        
        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        
        expenseList.append(expense)
        print("\n DONE bro.Expense is added succeesfully")
        
 #2. VIEW ALL EXPENSES 
    elif(choice==2):
        if(len(expenseList)==0):
            print("No expense  Added.jao phle khrcha kro.")
        else:
            print("=====ye apka sara expense =====")
            count=1
            for eachKharcha in expenseList:
                print(f"Kharcha Number {count} -> {eachKharcha["date"]}, {eachKharcha["category"]}, {eachKharcha["description"]}, {eachKharcha["amount"]} ")
                count=count+1
                
  #3. view total spending 
    elif(choice==3):
          total=0
          for eachkhrcha in expenseList:
              total = total + eachkhrcha["amount"]
              
          print("\n TOTAL KHRCHA = ",total)
          
  #4. EXIT
    elif( choice == 4):
          print("thnnks for using our system")
          break
      
    else:
          print("INVALID CHOICE. TRY AGAIN")
                                     
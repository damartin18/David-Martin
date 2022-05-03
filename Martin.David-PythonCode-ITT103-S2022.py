# Author : David Martin 
# Date   : April 2, 2022
# Course : ITT103

'''Description :  A Program to Accept salesperson details to include number, name,
sale amount and their class. The Algorithm should also calculate and print the
commission as well as other details received.'''

                                    # Declarations

#START							

def main() :    
    s_Num = 0                  
    commission = 0      
    import sys

                                        
        
  

                                      #Program Start    

                                      # Input Section
    
    
                                      # Loop for my Termination
        
    while True:    
        try:
            s_Num = int(input("Please Enter : a positive number to continue or a negative number to end the program\nEnter A positive or A negative number please: "))
            print()

        except ValueError :
            print("Invalid Input Please enter a positive or a negative number.")
            print()
            
        else :
            if s_Num > 0:
                print()
                print()
                print("                          Welcome to JamEx Limited         ")
                print ("                     Sales Commission Program Calculator   ")
                print ("                     ------------------------------------  ")
                print()
                print ("                      Please Enter the Data Requested Below ")
                break


            if s_Num < 0:
                print()
                print (" <<<<<<<<....... You have chosen to end the program .........>>>>>>>>>")
                print ("    <<<<<<<<............Have a Blessed Day.................>>>>>>>>")
                sys.exit()
                break                  #Termination Loop End 
    
            
                                        
    print()
     
    while True:                         # Loop for my Id Number begin
        try:
            s_IdNum = int(input("Please Enter the Salesperson ID Number\nThe Salesperson ID Number is : ")) 

        except ValueError:
            print("Please enter the correct input")
            continue

        else:                          #_IdNum was successfully parsed!
             break                     #s_IdNum loop end.
            
            
    Cls = int(input("Please Enter Salesperson Class:\nEnter either (1, 2, 3):  ")) 
    
    while True:                         #Sales Amount Loop Begin
        try:
            sales_Amt = int(input("Please Enter Salesperson Amount:\nThe Salesperson Amount is :  ")) 

        except ValueError:
            print("Error please enter a correct input an Integer")
            continue

        else:
            #sales_Amt was successfully parsed!
            #we're ready to exit the loop.
            break                               #Sales Amount Loop End
    
    sales_Rate = 0
    print()
        
    if    Cls== 1:                                          #If class is 1

          if sales_Amt <= 1000:                             #If sale amount less than or equal to 1000
              sales_Rate = 6                                #6% comission
              commission = (sales_Amt*sales_Rate)

          if 2000 > sales_Amt > 1000:                       #If sale amount is greater than 1000 but less than 2000
              sales_Rate = 7                                #7% comission
              commission = (sales_Amt*sales_Rate)

          if sales_Amt >= 2000:                             #If sale amount is greater than 1000 but less than 2000
              sales_Rate = 10                               #10% comission
              commission = (sales_Amt*sales_Rate)
                                                            #The same conditions as above, only the comission percentage is different

    elif   Cls == 2 :                                       #If class is 2
           if sales_Amt < 1000:
              sales_Rate = 4                                #4% comission
              commission = (sales_Amt*sales_Rate)

           if sales_Amt >= 1000:
               sales_Rate = 6                               #6% comission
               commission = (sales_Amt*sales_Rate)

    elif   Cls == 3 :                                       #If class is 3
          sales_Rate = 4.5                                  #4.5% comission
          commission = (sales_Amt*sales_Rate)

    
    else :
        print("An Invalid Class was Entered")              #If any invalid class is entered    
    if sales_Rate !=0 :
        print ("********** O U T P U T *********")
        print ("************* F O R *************")
        print ("****** P R I N T I N G *********")
        print ("-------------------------------  ")
        print()
        print(" Salesperson Id Number is:" + str(s_IdNum))
        print(" The Salesperson Class is: " + str(Cls))
        print(" The Salesperson Amount is: " + str("$"),(sales_Amt) )                              #If any invalid class is entered 0%
        print(" The Salesperson Rate is: " + str(sales_Rate), ("%"))
        print(" The Commission on the Sales Amount is: " + str("$"),(sales_Amt*sales_Rate/100)  )  #If any invalid class is entered 0$ 

    
                              #begin the option to do another calculation

    print()
    restart = (input("Do you wish to do another Calculation?\n Please Enter 'Y' for 'Yes' or 'N' for 'No':")).lower()
        
    if restart =="y" :
        main()

    else:
        print  (" <<<<<<.........You have chosen to end the program.......>>>>>>>>>>"    )
        print()
        print("<<<<<......Thank for using JamEx Limited Sales Commission Program Calculator....>>>>")
        print("          <<<<<............Have a Blessed day......>>>>>>>>")

                                    # Jamex program Calculator ends here


main()                              # To do another calculation - Start Here

#STOP

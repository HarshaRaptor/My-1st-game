balance = 1000
day = 0
print('NOTE: press enter after you are done reading the status and be aware of Lower cases')
print('Press enter to start game')
done1 = input('>')
print('How much change can happen in 24 hours')
print('You just lost your job, You have $1000 in your bank account\npress enter')
done2 = input('>')

while day <= 1:
	day = day + 1
	print('\nYou are walking down the street, and you see a man dropping a $20 note.')
	print("what do you want to do? (a: take it | b: give it back to the man)")
	choice1 = input('>')
	 
	if choice1 == 'a':
	    print('\nhmm, interesting choice')
	    balance = balance + 20
	    done2 = input('>')
		  
	elif choice1 == 'b':
	    print('\nHonesty is the best policy')
	    print('The man decided to give you $40, as a way of saying thank you')
	    balance = balance + 40
	    done3 = input('>')
		  
	else:
	    print('Invalid Responce, $100 deducted for your account, deduction increases by $100 every other time')
	    balance = balance - 100
	    done4 = input('>')
		  
	print(f'Balance: ${balance}')
	done5 = input('>')
	 
	 
	print('\nYou are now starving')
	print("what do you want to do? (a: keep walking | b: go to the nearby restaurent)")
	choice2 = input('>')
	
	if choice2 == 'a':
	    print('\nYou walk for aroud 4 Kilometres and you pass out,\nwhen you wake up, you are in a hospital, a stranger brought you there,\nand the hospital fee of $90 had been deducted from your account.')
	    balance = balance - 90
	    done6 = input('>')
		  
	elif choice2 == 'b':
	    print('\nMaybe something worse could have happend if you just kept walking, deduction of $45\nfor your meal')
	    balance = balance - 45
	    done7 = input('>')
		 
	else:
	    print('\nInvalid Responce, $200 deducted for your account, deduction increases by $100 every other time')
	    balance = balance - 200
	    done8 = input('>')
		  
	print(f'Balance: ${balance}')
	done9 = input('>')
	
	
	print("\nYou return back to your house(owned), The Electricity bill just came: $200")
	print("what do you want to do? (a: Pay it | b: Ignore it)")
	choice3 = input('>')
	
	if choice3 == 'a':
	    print("\nNice, the bill is paid, no we don't have to worry about it.")
	    print('-$200')
	    balance = balance - 200
	    done10 = input('>')
		  
	elif choice3 == 'b':
	    print('\nOoh, risky, you got away with it now, but for how long?')
	    balance = balance + 0
	    done11 = input('>')
		  
	else:
	    print('\nInvalid Responce, $300 deducted for your account, deduction increases by $100 every next time')
	    balance = balance - 300
	    done12 = input('>')
		  
	print(f'Balance: ${balance}')
	done13 = input('>')
	 
	day = day + 1
	print("\nYou go to the super market to buy some groceries where a lottery it being held")
	print("Entering the lottery would cost $20, groceries are $40")
	print("what do you want to do? (a: join the lottery after getting groceries | b: just take groceries and go home | c: just go home)")
	choice4 = input('>')
	
	if choice4 == 'a':
	    print('\nDone with groceries, the lottery is starting soon')
	    balance = balance - 60
	    done14 = input('>')
	    
	elif choice4 == 'b':
	    print('\nYou take the groceries and go home')
	    balance = balance - 40
	    done15 = input('>')
	    print(f'Balance: ${balance}')
	    done15 = input('>')
	    
	elif choice4 == 'c':
	    print('\nYou directly go home')
	    balance = balance + 0
	    done15 = input('>')
	    print(f'Balance: ${balance}')
	     
	else:
	    print('\nInvalid Responce, $400 deducted for your account, deduction increases by $100 every next time')
	    balance = balance - 400
	    done16 = input('>')
	    print(f'Balance: ${balance}')
		
	if choice4 == 'a':
	    print("\nThe lottery had started, choose a number between 1 and 10, correct guess is rewarded $500k")
	    print("what number do you choose? (1 | 2| 3| 4| 5| 6| 7| 8| 9| 10)")
	    choice5 = input('>')
	    
	    if choice5 == '7':
		    print("\nAWESOME, you had won the lottery of $500k!")
		    balance = balance + 500000
		    done18 = input('>')
				
	    else:
	        print("\nOoh, unlucky, you lost the lottery")
				
	else:
	    done17 = input('>')
	    
	print("\nYou go home and fall straight into bed after a tiring day")
	
	if choice3 == 'b':
	    print("\nThe next morning You wake up and your phone starts ringing")
	    print("what do you want to do? (a: Pick up the call | b: Ignore the call)")
	    choice6 = input('>')
	    
	    if choice6 == 'a':
		    print("\nYou pick up the call")
		    print("It is the electricity company, you have to pay an extra $200 for ignoriing the bill, with a total deduction of $400")
		    balance = balance - 400
		    done19 = input('>')
				
	    elif choice6 == 'b':
	        print("\nYou ignored the call")
	        print("Hmm, who knows, maybe it was important")
	        balance = balance + 0
	        done21 = input('>')
	       
	    else:
	        print('\nInvalid Responce, $500 deducted for your account, deduction increases by $100 every next time')
	        balance = balance - 500
	        done16 = input('>')
	        print(f'Balance: ${balance}')
	        
	else:
	    done20 = input('>')

print("Bonus Question, correct answer will double your balance!")
print("What is the answer for:\n-18/(2*(-3)) ")
bonus = input('>')
    
if bonus == '3':
    print("Correct answer!")
    print('balance is doubled')
    balance = balance * 2
        
else:
    print("Sorry, wrong answer!")
    balance = balance + 0
    
    
day = day + 1
done22 = input('>')
print('\n You finished the game!')
print(f'You started with $1000 and finished the game with ${balance}' )
print('Thankyou for playing!,\n I hope you liked it!')
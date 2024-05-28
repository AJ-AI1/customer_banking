"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
savings_account = Account(balance, interest_rate)

balance = float(input("Enter your initial savings account balance "))
interest_rate = float(input("Enter your APR interest rate in two decimal ")) 
months = int(input("Enter the length of months "))

    # Calculate interest earned
    # ADD YOUR CODE HERE

interest_earned = balance * interest_rate * (months/12)
print(f"Interest earned: ${interest_earned:.2f}")


    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
updated_savings_balance = balance + interest_earned
print(f"Updated savings balance: ${updated_savings_balance:.2f}")

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
savings_account.set_balance(updated_savings_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return # ADD YOUR CODE HERE
def updated_interest(balance, interest_rate, months):
    interest_earned = balance * interest_rate * (months / 12)
    updated_savings_balance = balance + interest_earned
return updated_savings_balance, interest_earned


You will need to use 0 for the amount of interest to set the balance before you pass the interest earned to the set interest method.



class Account:
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance

  def __str__(self):
    return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

  def deposit(self, amount):
    self.balance += amount
    print(f"Deposit of {amount} accepted. New balance: {self.balance}")

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
      print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
    else:
      print("Insufficient funds. Entered amount exceeds current balance.")

# Example usage:
acct1 = Account('John', 100)
print(acct1)  # Output: Account owner: John
              #         Account balance: 100
acct1.deposit(50)  # Output: Deposit of 50 accepted. New balance: 150
acct1.withdraw(30)  # Output: Withdrawal of 30 accepted. New balance: 120
acct1.withdraw(200)  # Output: Insufficient funds. Entered amount exceeds current balance.
# # level 1
# # 1
from collections import Counter
import math

# class  Statistics:
#     def __init__(self,data):
#         self.data=sorted(data)

#     def count(self):
#         return len(self.data)
    
#     def sum(self):
#         return sum(self.data)
    
#     def min(self):
#         return min(self.data)

#     def max(self):
#         return max(self.data)
    
#     def range(self):
#         return self.max() - self.min()
    
#     def mean(self):
#         return round(self.sum() / self.count())

#     def median(self):
#         n = self.count()
#         mid = n // 2
#         if n % 2 == 0:
#             return (self.data[mid - 1] + self.data[mid]) / 2
#         else:
#             return self.data[mid]

#     def mode(self):
#         freq = Counter(self.data)
#         mode = freq.most_common(1)[0] 
#         return mode

#     def var(self):
#         mean = self.mean()
#         return round(sum((x - mean) ** 2 for x in self.data) / self.count(), 1)

#     def std(self):
#         return round(math.sqrt(self.var()), 1)
    
#     def freq_dist(self):
#         freq = Counter(self.data)
#         n = self.count()
#         return [(round((count / n) * 100, 1), 
#                  value) for value, count in freq.items()]
    
#     def show(self):
#         print("Count:", self.count())
#         print("Sum: ", self.sum())
#         print("Min: ", self.min())
#         print("Max: ", self.max())
#         print("Range: ", self.range())
#         print("Mean: ", self.mean())
#         print("Median: ", self.median())
#         print("Mode: ", self.mode())
#         print("Variance: ", self.var())
#         print("Standard Deviation: ", self.std())
#         print("Frequency Distribution:", self.freq_dist())

# ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27,
#         27, 24, 32, 33, 27, 25, 26, 38, 37, 31,
#         34, 24, 33, 29, 26]

# data = Statistics(ages)
# data.show()
    
# level 2
# 2

class personacc:
    def __init__(self,firstname,lastname):
     self.firstname = firstname
     self.lastname= lastname
     self.income =[]
     self.expense = []

    def add_income(self , amount,description=""):
       self.income.append((amount,description))

    def add_expense(self, amount, description=""):
       self.expense.append((amount, description))

    def total_income(self):
       return sum(amount for amount, _ in self.income)
    
    def total_expense(self):
       return sum(amount for amount ,_ in self.expense)
    
    def account_balance(self):
        return self.total_income() - self.total_expense()
    
    def account_info(self):
        info = f"Account Holder: {self.firstname} {self.lastname}\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Balance: {self.account_balance()}\n\n"

        info += "Incomes:\n"
        for amount, desc in self.income:
            info += f"  + {amount} ({desc})\n"

        info += "Expenses:\n"
        for amount, desc in self.expense:
            info += f"  - {amount} ({desc})\n"
        
        return info
    
person = personacc("Bhumi", "modi")
person.add_income(5000, "Salary")
person.add_income(2000, "Freelance")
person.add_expense(1200, "Rent")
person.add_expense(800, "Groceries")

print(person.account_info())
    

    


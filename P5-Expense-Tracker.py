fd = "expense1.txt"
import os
def addexp():
	date = input("Enter today's date[DD-MM-YYYY] : ")
	category = input("Enter your expense category : ")
	try:
		amt = float(input("Enter your expense : "))
	except ValueError:
		print("Enter a valid amount.")
		return
	note = input("Enter your notes(optional) : ")
	record = date + "|" + category + "|" + str(amt) + "|" + note + "\n"
	with open(fd, "a") as f:
		f.write(record)
	print("Expense saved.")
def showexp():
	if not os.path.exists("expense1.txt"):
		print("No expenses recorded yet")
		return
	with open(fd,"r") as f:
		for i, record in enumerate(f, 1):
			date,category,amt,note = record.strip().split("|")
			print(f"{i}. {date} | {category} | {amt} | {note}")
def totexp():
	if not os.path.exists("expense1.txt"):
		print("No expenses recorded yet!")
		return
	total = 0.00
	with open(fd, "r") as f:
		for record in f:
			parts = record.strip().split("|",3)
			try:
				total+=float(parts[2])
			except (IndexError, ValueError):
				continue
	print(f"------Your Total Expense: {total}-----")
def main():
	while True:
		n = int(input("1.Enter your expense\n2.Show Your expense\n3.Show your total expense\n4.Exit\nEnter your choice:"))
		if n==1:
			addexp()
		elif n==2:
			showexp()
		elif n==3:
			totexp()
		elif n==4:
			print("Exiting the menu...")
			break
		else:
			print("Invalid Choice")
if __name__ == "__main__":
	main()







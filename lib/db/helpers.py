from models import Category, Transaction
from datetime import date



def create_category():
    name = input('Enter category name: ')
    category = Category.create(name)
    print(f'Created category: {category}')

def delete_category():
    category_id = int(input('Enter category ID to delete: '))
    Category.delete(category_id)
    print('Category deleted.')

def display_all_categories():
    categories = Category.get_all()
    for category in categories:
        print(category)

def find_category_by_id():
    category_id = int(input('Enter category ID: '))
    category = Category.find_by_id(category_id)
    if category:
        print(category)
    else:
        print('Category not found.')

def find_category_by_name():
    name = input('Enter category name: ')
    category = Category.find_by_name(name)
    if category:
        print(category)
    else:
        print('Category not found.')

def create_transaction():
    date_input = input('Enter date (YYYY-MM-DD): ')
    amount = float(input('Enter amount: '))
    category_id = int(input('Enter category ID: '))
    type = input('Enter type (income/expense): ')
    description = input('Enter description: ')
    transaction = Transaction.create(date=date.fromisoformat(date_input), amount=amount, category_id=category_id, type=type, description=description)
    print(f'Created transaction: {transaction}')

def delete_transaction():
    transaction_id = int(input('Enter transaction ID to delete: '))
    Transaction.delete(transaction_id)
    print('Transaction deleted.')

def display_all_transactions():
    transactions = Transaction.get_all()
    for transaction in transactions:
        print(transaction)

def find_transaction_by_id():
    transaction_id = int(input('Enter transaction ID: '))
    transaction = Transaction.find_by_id(transaction_id)
    if transaction:
        print(transaction)
    else:
        print('Transaction not found.')

def find_transaction_by_description():
    description = input('Enter transaction description: ')
    transaction = Transaction.find_by_description(description)
    if transaction:
        print(transaction)
    else:
        print('Transaction not found.')

def display_total_categories():
    total = Category.total_categories()
    print(f'Total number of categories: {total}')

def display_total_transactions():
    total = Transaction.total_transactions()
    print(f'Total number of transactions: {total}')

def display_total_transactions_per_category():
    totals = Category.total_transactions_per_category()
    for category_name, total in totals:
        print(f'Total transactions for category {category_name}: {total}')

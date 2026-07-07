inventory={}

def add_product():
    details={}
    n=int(input("enter product id:"))
    if n in inventory:
        print("product already exists")
        return

    details['name']=input("enter product name:").lower()
    details['category']=input("enter product category:").lower()
    details['price']=int(input("enter product price:"))
    details['stock']=int(input("enter product stock:"))
    details['sold']=int(input("enter product sold:"))
    inventory[n]=details

def view_products():
    for i,j in inventory.items():
        print(f'product ID:{i}')
        print(f'product name:{j["name"]}')
        print(f'product category:{j["category"]}')
        print(f'product price:{j["price"]}')
        print(f'product stock:{j["stock"]}')
        print(f'product sold:{j["sold"]}')

def search_products():
    n=int(input("search by:\n1.product ID\n2.product Name:\n3.Category:"))
    if n==1:
        id=int(input("enter product ID:"))
        if id in inventory:
            print(inventory[id])
        else:
            print("product does not exist")
    elif n==2:
        name=input("enter product name:").lower()
        found=False
        for i,j in inventory.items():
            if j['name'] == name:
                print(f'product ID:{i}')
                print(f'product name:{j["name"]}')
                print(f'product category:{j["category"]}')
                print(f'product price:{j["price"]}')
                print(f'product stock:{j["stock"]}')
                print(f'product sold:{j["sold"]}')
                found=True
        if not found:
            print("product does not exist")

    elif n==3:
        category=input("enter product category:").lower()
        found=False
        for i,j in inventory.items():
            if j['category'] == category:
                print(f'product ID:{i}')
                print(f'product name:{j["name"]}')
                print(f'product category:{j["category"]}')
                print(f'product price:{j["price"]}')
                print(f'product stock:{j["stock"]}')
                print(f'product sold:{j["sold"]}')
                found=True
        if not found:
            print("product does not exist")
    else:
        print("invalid input")

def update_products():
    n=int(input("enter product id:"))
    if n in inventory:
        k=int(input("UPDATE PRODUCT\n1.price\n2.stock\n3.category:"))
        if k==1:
            price=int(input("enter updated product price:"))
            inventory[n]['price']=price
            print("updated product price successfully")
        elif k==2:
            stock=int(input("enter updated product stock:"))
            inventory[n]['stock']=stock
            print("updated product stock successfully")
        elif k==3:
            category=input("enter updated product category:").lower()
            inventory[n]['category']=category
            print("updated product category successfully")
        else:
            print("invalid input")
    else:
        print("item does not exist")

def sell_products():
    n=int(input("enter product id:"))
    m=int(input("enter quantity:"))
    if n in inventory:
        if inventory[n]['stock']>=m:
            inventory[n]['stock']-=m
            inventory[n]['sold']+=m
            print("sold product successfully")
        else:
            print("Insufficient stock")

    else:
        print("item does not exist")

def restock_products():
    n=int(input("enter product id:"))
    m=int(input("enter quantity:"))
    if m>0:
        if n in inventory:
            inventory[n]['stock']+=m
            print("restocked successfully")
        else:
            print("product does not exist")
    else:
        print("invalid input")

def inventory_stats():
    n=0
    for i in inventory:
        n+=1
    print("Total number of items:",n)

    stock=0
    for i,j in inventory.items():
        stock+=j['stock']
    print("Total stock:",stock)

    value=0
    for i,j in inventory.items():
        value=value+j['price']
    print("Total price:",value)

    max_price=0
    for i,j in inventory.items():
        if j['price']>max_price:
            max_price=j['price']
    print("Max price:",max_price)

    max_sold=0
    for i,j in inventory.items():
        if j['sold']>max_sold:
            max_sold=j['sold']
    print("Max sold:",max_sold)

    total_price=0
    for i,j in inventory.items():
        total_price=total_price+j['price']
    print("Average product price:",total_price/n)

    m=0
    for i,j in inventory.items():
        if j['stock']<5:
             m+=1
    print("Total number of low stock items:",m)

def delete_products():
    n=int(input("enter product id:"))
    if n in inventory:
        del inventory[n]
        print("deleted successfully")
    else:
        print("item does not exist")

def sort_products():
    n=int(input("SORT BY:\n1.Price\n2.Stock\n3.Sold\n4.Name\n5.Category"))
    if n==1:
        m=int(input("1.descending or 2.ascending:"))
        if m==1:
            x=dict(sorted(inventory.items(),key=lambda item: item[1]['price'],reverse=True))
            print(x)
        elif m==2:
            x=sorted(inventory.items(),key=lambda item: item[1]['price'],reverse=False)
            print(x)
        else:
            print("invalid input")
    elif n==2:
        m=int(input("1.descending or 2.ascending order:"))
        if m==1:
            x=dict(sorted(inventory.items(),key=lambda item: item[1]['stock'],reverse=True))
            print(x)
        elif m==2:
            x=dict(sorted(inventory.items(),key=lambda item: item[1]['stock'],reverse=False))
            print(x)
        else:
            print("invalid input")
    elif n==3:
        m=int(input("1.descending or 2.ascending order:"))
        if m==1:
            x=dict(sorted(inventory.items(),key=lambda item: item[1]['sold'],reverse=True))
            print(x)
        elif m==2:
            x=dict(sorted(inventory.items(),key=lambda item: item[1]['sold'],reverse=False))
            print(x)
        else:
            print("invalid input")
    elif n==4:
        m=int(input("1.descending or 2.ascending order:"))
        if m==1:
            x=dict(sorted(inventory.items(),key=lambda item: item[1]['name'],reverse=True))
            print(x)
        elif m==2:
            x=dict(sorted(inventory.items(),key=lambda item: item[1]['name'],reverse=False))
            print(x)
        else:
            print("invalid input")
    elif n==5:
        m=int(input("1.descending or 2.asccending order:"))
        if m==1:
            x=dict(sorted(inventory.items(),key=lambda item: item[1]['category'],reverse=True))
            print(x)
        elif m==2:
            x=dict(sorted(inventory.items(),key=lambda item: item[1]['category'],reverse=False))
            print(x)
        else:
            print("invalid input")
    else:
        print("invalid input")

def main():
    while True:
        print("\n_____Welcome to Inventory and Billing Management System_____")

        n = int(input("""
SELECT OBJECTIVE:
1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Sell Product
6. Restock Product
7. Delete Product
8. Inventory Stats
9. Sort Products
10. Exit

Enter your choice: """))

        if n == 1:
            add_product()
        elif n == 2:
            view_products()
        elif n == 3:
            search_products()
        elif n == 4:
            update_products()
        elif n == 5:
            sell_products()
        elif n == 6:
            restock_products()
        elif n == 7:
            delete_products()
        elif n == 8:
            inventory_stats()
        elif n == 9:
            sort_products()
        elif n == 10:
            print("Thank you for using Inventory and Billing Management System!")
            break
        else:
            print("Invalid input. Try again.")

main()
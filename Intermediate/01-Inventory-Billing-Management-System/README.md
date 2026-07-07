# Inventory & Billing Management System

## Overview

The **Inventory & Billing Management System** is a console-based Python application developed to manage product inventories efficiently. It allows users to perform essential inventory operations such as adding, updating, searching, sorting, selling, restocking, and deleting products through a menu-driven interface.

This project was developed to strengthen fundamental and intermediate Python programming skills, including modular programming, nested dictionaries, sorting algorithms, and CRUD operations.

---

## Features

* Add new products
* View all products
* Search products by:

  * Product ID
  * Product Name
  * Category
* Update product information

  * Price
  * Stock
  * Category
* Sell products
* Restock inventory
* Delete products
* Generate inventory statistics:

  * Total number of products
  * Total stock available
  * Total inventory value
  * Highest priced product
  * Most sold product
  * Average product price
  * Low-stock product count
* Sort products by:

  * Price
  * Stock
  * Units Sold
  * Product Name
  * Category
  * Ascending or Descending order

---

## Technologies Used

* Python 3
* Functions
* Dictionaries
* Nested Dictionaries
* Loops
* Conditional Statements
* Lambda Functions
* Built-in `sorted()` Function

---

## Project Structure

```text
Inventory-Billing-Management-System/
│
├── inventory_management.py
└── README.md
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/Inventory-Billing-Management-System.git
```

### Navigate to the project directory

```bash
cd Inventory-Billing-Management-System
```

### Run the application

```bash
python inventory_management.py
```

---

## Menu

```text
1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Sell Product
6. Restock Product
7. Delete Product
8. Inventory Statistics
9. Sort Products
10. Exit
```

---

## Sample Data Structure

```python
inventory = {
    101: {
        "name": "laptop",
        "category": "electronics",
        "price": 65000,
        "stock": 8,
        "sold": 3
    }
}
```

---

## Python Concepts Demonstrated

* Modular Programming
* Function Design
* CRUD Operations
* Nested Dictionaries
* Iteration
* Searching
* Sorting using Lambda Functions
* Menu-Driven Programming
* Data Manipulation

---

## Future Enhancements

* Persistent data storage using file handling
* Exception handling for input validation
* Sales receipt generation
* Customer management
* Sales history and reporting
* Database integration (SQLite/MySQL)
* Object-Oriented Programming implementation
* Graphical User Interface (GUI)

---

## Author

**Ragul YS**

This project was developed as part of my Python learning journey to strengthen programming fundamentals and gain practical experience in building console-based applications.


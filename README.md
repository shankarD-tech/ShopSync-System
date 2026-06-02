# 🛒 Shop Sync System

## 📌 Description

This Python project is a simple stock and billing management system designed for small retail shops. It allows admin users to manage product stock and view available items, while customers can purchase products, generate bills, and receive order details via WhatsApp using the PyWhatKit library.

---

## 🚀 Features

* Admin login for stock management
* User mode for purchasing products
* Real-time stock update and storage
* Product price and availability display
* Automatic bill generation 🧾
* WhatsApp message sending for order confirmation 📲
* File-based stock persistence

---

## 🛠️ Installation & Setup

### 1. Install Python

Download and install Python (3.8+)

```bash
python --version
```

---

### 2. Install Required Libraries

```bash
pip install pywhatkit
```

---

### 3. Project File Setup

Ensure the following files are present in the same folder:

* `main.py` (your main program)
* `pythonproject1moduleofavailableproductsprices.py`
* `pythonproject1moduleofstock.py`

These files store:

* Product names
* Prices
* Stock data

---

### 4. Configure WhatsApp Feature

* Make sure your system has:

  * Internet connection 🌐
  * WhatsApp Web logged in on your browser

---

### 5. Run the Program

```bash
python filename.py
```

---

## 🧪 How It Works

### 👨‍💼 Admin Mode

* Login using admin credentials
* View available products, prices, and stock
* Update stock quantities
* Changes are saved to file

### 👤 User Mode

* Enter name and phone number
* Select products and quantity
* System checks stock availability
* Generates bill
* Sends bill via WhatsApp automatically

---

## ⚠️ Limitations

* Admin password is hardcoded (not secure)
* No database (uses file-based storage)
* Long conditional checks for product validation
* Error handling is minimal

---

## 💡 Future Improvements

* Add database (MySQL or SQLite)
* Use secure authentication
* Replace long `if` conditions with dynamic lookup
* Build GUI (Tkinter / Web app)
* Add invoice history tracking

---

## 📂 Tech Stack

* Python
* PyWhatKit
* Datetime module
* File handling

---

## 👨‍💻 Author

Shankar D

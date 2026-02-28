You’re on **Mac + VS Code**, so we’ll set up a clean, professional dev environment for:

* Client script
* Custom RADIUS AAA server
* MySQL backend
* Zero external RADIUS libraries

---

# 🧱 STEP 1 — Install Required Tools

## ✅ 1. Check Python Version

Open terminal:

```bash
python3 --version
```

You want:

```
Python 3.11+
```

If not:

```bash
brew install python
```

---

## ✅ 2. Install MySQL

If not installed:

```bash
brew install mysql
```

Start it:

```bash
brew services start mysql
```

Secure install:

```bash
mysql_secure_installation
```

Login test:

```bash
mysql -u root -p
```

---

# 📄 MySQL Root Access Recovery (macOS – Homebrew – MySQL 9.x)

## 🔎 Problem

While running:

```bash
mysql_secure_installation
```

or:

```bash
mysql -u root
```

The following error occurred:

```
ERROR 1045 (28000): Access denied for user 'root'@'localhost'
```

Attempting to use:

```sql
ALTER USER 'root'@'localhost'
IDENTIFIED WITH mysql_native_password
BY 'rootpass';
```

Resulted in:

```
ERROR 1524 (HY000): Plugin 'mysql_native_password' is not loaded
```

---

## 🧠 Root Cause

* Running **MySQL 9.x (Homebrew version)**
* `mysql_native_password` plugin is removed / not enabled
* Root user authentication was misconfigured
* Server required manual password reset

---

## ✅ Resolution Procedure

### 1️⃣ Stop MySQL Service

```bash
brew services stop mysql
```

---

### 2️⃣ Start MySQL in Safe Mode (Disable Authentication)

```bash
mysqld_safe --skip-grant-tables &
```

This allows login without password validation.

---

### 3️⃣ Login Without Password

```bash
mysql -u root
```

---

### 4️⃣ Reset Root Password (Modern MySQL Method)

⚠️ Do NOT specify authentication plugin.

```sql
ALTER USER 'root'@'localhost'
IDENTIFIED BY 'rootpass';

FLUSH PRIVILEGES;
```

Exit:

```sql
exit;
```

---

### 5️⃣ Kill Safe Mode Processes

Find running MySQL processes:

```bash
ps aux | grep mysqld
```

Kill both `mysqld` and `mysqld_safe`:

```bash
kill -9 <PID>
```

---

### 6️⃣ Restart MySQL Normally

```bash
brew services start mysql
```

---

### 7️⃣ Verify Login

```bash
mysql -u root -p
```

Enter:

```
rootpass
```

Login should succeed.

---

## ⚙ Notes

* MySQL 9.x defaults to `caching_sha2_password`
* `mysql_native_password` is deprecated and may not be available
* Do not force old authentication plugins on modern MySQL

---

## 📌 Recommendation for FA3H Development

For local development:

* Use default MySQL authentication
* Avoid modifying plugins
* Keep credentials simple and documented
* Consider SQLite for early-stage protocol testing

---

# 🏗 FA3H Environment Status After Fix

* ✅ Python 3.14 venv
* ✅ MySQL 9.x running
* ✅ Root access restored
* ⏭ Ready for DB schema creation
* ⏭ Ready to implement RADIUS server


---

# 🧠 STEP 2 — Create Project Structure

In your workspace:

```bash
mkdir fa3h
cd fa3h
```

Create folders:

```bash
mkdir client server core db utils
touch client/client.py
touch server/radius_server.py
touch core/auth_service.py
touch db/models.py
touch db/database.py
touch utils/config.py
touch utils/logger.py
touch main.py
```

Your structure now:

```
fa3h/
│
├── client/
│   └── client.py
├── server/
│   └── radius_server.py
├── core/
│   └── auth_service.py
├── db/
│   ├── models.py
│   └── database.py
├── utils/
│   ├── config.py
│   └── logger.py
└── main.py
```

This keeps it clean from Day 1.

---

# 🐍 STEP 3 — Create Virtual Environment

Inside `fa3h/`:

```bash
python3 -m venv venv
source venv/bin/activate
```

Now install required packages:

```bash
pip install mysql-connector-python bcrypt
```

We are NOT installing pyrad.

---

# 🗄 STEP 4 — Setup MySQL Database

Login:

```bash
mysql -u root -p
```

Create DB:

```sql
CREATE DATABASE fa3h;
USE fa3h;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    role VARCHAR(50) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Exit MySQL.

---

# 🔐 STEP 5 — Insert Test User

Open Python shell inside venv:

```bash
python
```

Generate bcrypt hash:

```python
import bcrypt

password = b"1234"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed.decode())
```

Copy the hash.

Insert into DB:

```sql
INSERT INTO users (username, password_hash)
VALUES ('testuser', 'PASTE_HASH_HERE');
```

Now you have a real hashed user.

---

# ⚙ STEP 6 — Basic Config File

In `utils/config.py`:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_mysql_password",
    "database": "fa3h"
}

RADIUS_CONFIG = {
    "host": "127.0.0.1",
    "port": 1812,
    "shared_secret": b"supersecret"
}
```

---

# 🧪 STEP 7 — Test DB Connection

In `db/database.py`:

```python
import mysql.connector
from utils.config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)
```

Test in Python:

```python
from db.database import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT username FROM users;")
print(cursor.fetchall())
```

If you see:

```
[('testuser',)]
```

You are ready.

---

# 🧠 What You Have Achieved

You now have:

* Clean project structure
* Virtual environment
* MySQL database
* Secure password hashing
* Config isolation
* Zero RADIUS libraries

This is real engineering setup.

---


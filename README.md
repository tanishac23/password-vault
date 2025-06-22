# 🔐 Simple Password Vault using Python

## 📌 Overview
A beginner-friendly command-line tool to *securely store and view passwords* using encryption (Fernet from the cryptography library).

---

## 🚀 Features
- Add new passwords (site, username, password)
- Passwords stored in *encrypted format*
- View decrypted passwords when needed
- Simple and secure

---

## 🔧 Tools Used
- Python 3.12
- cryptography library (Fernet encryption)
- File handling

---

## 📁 Files Included
| File | Description |
|------|-------------|
| generate_key.py | Generates encryption key (key.key) |
| vault.py | Main app: add/view passwords |
| key.key | Auto-generated encryption key |
| passwords.txt | Stores encrypted passwords |
| README.md | This file |

---

## 🛠 How to Run

### 1. Install the required library:
bash
pip install cryptography

2. Generate the encryption key:

python generate_key.py

3. Run the app:

python vault.py


---

🧠 Learning Outcome

✅ Learned file handling, encryption, and real-world use of secure password storage.


---

✨ Future Plans

Add GUI using Tkinter

Master password login

Export/Import vault securely


---

🤍 Made with learning and curiosity by Tanisha

---

### ✅ Now Just Do This:

1. Open `README.md`  
2. Paste all the content above  
3. Save the file  
4. In terminal, type:

bash
git add README.md
git commit -m "Added final README.md"
git push 

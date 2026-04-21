# ⚡ PenCon - CLI Exploitation Toolkit

PenCon is a lightweight, terminal-based exploitation toolkit designed to streamline common post-exploitation tasks such as reverse shell generation, payload encoding, and listener setup.

Built for **CTF players, cybersecurity students, and aspiring red teamers**, PenCon eliminates the need to search for payloads during engagements.

---

## 🚀 Features

* 🔹 Reverse shell generator (multiple payload types)
* 🔹 Built-in Netcat listener
* 🔹 Payload encoder (Base64, URL, Hex)
* 🔹 Cheatsheet for quick reference
* 🔹 Clean CLI interface with short flags
* 🔹 Fully portable & terminal-based

---

## 🧰 Supported Reverse Shells

* `bash`
* `python`
* `php`
* `php-rev` (PentestMonkey full reverse shell)

---

## 📦 Installation

```bash
git clone https://github.com/Yash4322/PenCon.git
cd PenCon
chmod +x pencon
sudo mv pencon /usr/local/bin/
```

---

## ⚙️ Usage

### 🔹 Show banner

```bash
pencon
```

---

### 🔹 Help menu

```bash
pencon -h
```

---

### 🔹 Generate Reverse Shell

```bash
pencon -s -i <IP> -p <PORT> -t <TYPE>
```

**Example:**

```bash
pencon -s -i 127.0.0.1 -p 4444 -t python
```

---

### 🔹 Start Listener

```bash
pencon -l -p <PORT>
```

**Example:**

```bash
pencon -l -p 4444
```

---

### 🔹 Encode Payload

```bash
pencon -e -t <TYPE> -d <DATA>
```

**Example:**

```bash
pencon -e -t base64 -d "whoami"
```

---

### 🔹 Cheatsheet

```bash
pencon -c
```

---

## 🎯 Example Workflow

```bash
# Terminal 1
pencon -l -p 4444

# Terminal 2
pencon -s -i 127.0.0.1 -p 4444 -t python
```

Execute generated payload → receive shell.

---

## 🧠 Use Cases

* Capture The Flag (CTF) challenges
* Web exploitation (RCE, file upload)
* Payload obfuscation & bypassing filters
* Learning and practicing post-exploitation techniques

---

## ⚠️ Disclaimer

This tool is intended for **educational and authorized security testing only**.
Do not use it on systems without proper permission.

---

## 📥 Installation & Setup

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/Yash4322/PenCon.git
cd PenCon
```

---

### 🔹 2. Make the Tool Executable

```bash
chmod +x pencon
```

---

### 🔹 3. Run Locally

```bash
./pencon
```

---

### 🔹 4. (Optional) Install Globally

This allows you to run `pencon` from anywhere:

```bash
sudo mv pencon /usr/local/bin/
```

---

### 🔹 5. Verify Installation

```bash
pencon -h
```

---

## ⚠️ Requirements

* Python 3.x
* Netcat (`nc`) installed
* Linux environment (tested on Kali Linux)

---

## 🧪 Quick Demo

```bash
# Terminal 1
pencon -l -p 4444

# Terminal 2
pencon -s -i 127.0.0.1 -p 4444 -t python
```

Execute generated payload → receive shell.

## 👨‍💻 Author

**Yash Gupta (Arylide)**
GitHub: https://github.com/Yash4322

---

## 🤝 Contributors

* Pathi Aman Pal

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork it
* 🛠️ Contribute improvements

---

## 🔥 Future Improvements

* More payload types (nc, mkfifo, powershell)
* File output support (`--save`)
* Auto listener + payload execution
* Colored output & UX improvements

---

## 🏁 Status

✔ Active Development
✔ Demo Ready
✔ CTF Friendly

---

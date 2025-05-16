# KeyLogger
This Python-based keylogger is designed for security research and educational purposes. It uses the pynput library to monitor and log keystrokes. The keylogger captures user input, stores it in a log file, and can be stopped gracefully using the ESC key.

# Keylogger for Security Research

This repository contains a Python-based keylogger designed for **security research and educational purposes**. The tool demonstrates how keystrokes can be captured and stored, emphasizing the importance of understanding such tools for defensive cybersecurity practices.

---

## Features
- **Keystroke Logging**: Captures and logs both regular and special keys (e.g., Enter, Space, Ctrl).
- **Log File**: Stores captured keystrokes in a `keylog.txt` file.
- **Graceful Exit**: Stops the keylogger when the `ESC` key is pressed.
- **Lightweight and Modular**: Built with simplicity and portability in mind.

---

## Prerequisites
1. Python 3.6+
2. `pynput` library (Install using `pip install pynput`)

---

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/keylogger.git
    cd keylogger
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate   # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage
1. Run the keylogger script:
    ```bash
    python3 Keylogger.py
    ```

2. Type anything in any application (or terminal). The keylogger will log your keystrokes.

3. Stop the keylogger by pressing the `ESC` key.

4. View the logged keystrokes in the `keylog.txt` file:
    ```bash
    cat keylog.txt
    ```

---

## File Structure
- `Keylogger.py`: Main script for the keylogger.
- `keylog.txt`: Output file where keystrokes are logged.
- `README.md`: Documentation for the repository.

---

## Disclaimer
**This tool is intended solely for ethical use in controlled environments. Unauthorized use is illegal and unethical. Always obtain proper consent before deploying such tools.**

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contributing
Contributions are welcome! If you find bugs or have ideas for new features, feel free to open an issue or submit a pull request.

---

## Author
Developed by [Your Name](https://github.com/your-username).

For any inquiries, feel free to contact me!

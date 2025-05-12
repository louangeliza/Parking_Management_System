# Parking Management System 🚗

## Overview
The **Parking Management System** is an automated solution designed to manage the entry, exit, and payment processing of vehicles in a parking facility. It integrates RFID card scanning for user authentication and automated payment deduction based on the time spent in the parking lot.

---

## Features ✨
- **RFID-based Authentication** - Secure entry and exit of vehicles using RFID cards.
- **Real-time Payment Processing** - Calculates parking fees based on time spent and deducts it from the user's balance.
- **Arduino Integration** - Uses Arduino to detect RFID cards and communicate with the server.
- **CSV-based Data Logging** - Logs entry, exit, and payment details for every vehicle.
- **Real-time Feedback** - Displays status messages on the Arduino's serial monitor.

---

## System Architecture 🏗️
1. **Arduino (RFID Reader):** Detects RFID card swipes and sends data to the server.
2. **Python Backend:**
   - Receives data from Arduino.
   - Manages payment calculations.
   - Updates the CSV-based database.
3. **CSV Database:**
   - `plates_log.csv` stores:
     - Plate Number
     - Entry Time
     - Exit Time
     - Amount Charged
     - Payment Status

---

## Folder Structure 📁
```plaintext
├── .git
├── pms
├── best.pt
├── car_entry.py
├── process_payment.py
├── generate_plates_log.py
├── plates_log.csv
├── README.md
├── payment
│   ├── top_up.ino
│   └── process_payment.ino
├── writting_on_rfid
│   └── writing.ino
├── reading_on_rfid
│   └── reading.ino
└── Arduino_code
    └── parking_system.ino
```

---

## Setup Instructions ⚙️

1. **Clone the repository:**
   ```bash
   git clone https://github.com/louangeliza/Parking_Management_System.git
   cd Parking_Management_System
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Connect Arduino:**
   - Ensure the RFID reader is connected to the Arduino.
   - Upload the `.ino` files to the Arduino.

4. **Run the application:**
   ```bash
   python process_payment.py
   ```

---

## Usage 🚀
- Swipe the RFID card at the entrance.
- Enter the car plate number when prompted.
- When exiting, swipe the card again to trigger the payment process.
- If the balance is sufficient, the gate opens and balance is updated.

---

## License 📄
This project is licensed under the MIT License.

---

## Author ✍️
Developed by **louangeliza**

---

## Future Improvements 🛠️
- Web-based dashboard for monitoring parking activities.
- SMS or Email notifications for balance updates.
- Integration with mobile payments for easy top-ups.

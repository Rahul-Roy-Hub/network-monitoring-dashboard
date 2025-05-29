# 🛰️ Network Infrastructure Monitoring System

A Django-based web application that monitors network devices (routers, servers, etc.) using **Ping** and **SNMP**. It provides a real-time dashboard, status history, and alerting system for network admins.

https://network-monitoring-dashboard-ve91.onrender.com/
---

## 📦 Features

- Add and manage network devices
- Periodic health checks via:
  - `ICMP ping`
  - `SNMP sysDescr` (basic info)
- Live device status dashboard
- Admin panel for managing devices
- Extendable for alert emails or advanced SNMP

---

## 🧰 Tech Stack

- **Backend**: Django (Python)
- **Monitoring**: `ping3`, `pysnmp`
- **Frontend**: HTML, CSS (customizable)
- **Database**: SQLite (default), can upgrade to MySQL/PostgreSQL
- **Scheduler**: Django management command (cron ready)

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Rahul-Roy-Hub/network-monitoring-dashboard.git
cd network-monitoring-django
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install:

```bash
pip install django ping3 pysnmp
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (for admin panel)

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🖥️ Usage

- Log in to the Django admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- Add network devices (name + IP address).
- Open home URL `/` to see the device status dashboard.

---

## 🔁 Running the Monitor

To check devices via ping/SNMP, run:

```bash
python manage.py ping_devices
```

Automate this using a **cron job** or **Windows Task Scheduler**.

---

## 📊 Extending Ideas

- Email/SMS alerts on downtime
- Charts for uptime history
- SNMP metrics (CPU, memory, etc.)
- Export logs as CSV
- Authenticated dashboard

---

## 📄 License

This project is for educational and demonstration purposes.

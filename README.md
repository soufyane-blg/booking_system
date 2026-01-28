# Booking System (Django)

A full-featured booking system built with Django.

This project allows users to register, log in, and manage their own bookings in a secure way.

---

## 🚀 Features

- User registration & authentication
- Login & logout
- User-based bookings (each user sees only their own data)
- Create, update, delete bookings
- Booking details page
- Validation (no duplicate bookings, no invalid data)
- Secure access with login required
- Clean Django Forms integration

---

## 🧩 Tech Stack

- Python
- Django
- SQLite
- Django Auth System
- Django Forms

---

## 📸 How it works

1. User creates an account
2. Logs in
3. Creates a booking
4. Can view, edit, and delete only their own bookings

---

## 🔒 Security

- Authentication system (Django Auth)
- Object-level permissions (users can only access their own bookings)
- Protected routes using `login_required`

---

## 🛠 Installation

```bash
git clone https://github.com/your-username/booking_system.git
cd booking_system
python manage.py migrate
python manage.py runserver
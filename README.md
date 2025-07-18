# airline-
an airline company flights booking system for passengers 
# ✈️ Django Airline Reservation System

A simple Django-based web application for managing flights, passengers, and bookings. This project demonstrates the core functionalities of a relational database system using models, views, templates, and authentication features in Django.

---

## 🚀 Features

- View all available flights
- View individual flight details
- Add and manage passengers for each flight
- User authentication (Login & Logout)
- Admin panel to manage airports, flights, and passengers
- Secure CSRF-protected forms

---

## 📁 Project Structure

blend/
├── airline/ # Main project config
│ └── urls.py
├── flight/ # App for flights
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/flights/
├── users/ # App for login/logout
│ ├── views.py
│ ├── urls.py
│ └── templates/users/
├── db.sqlite3 # SQLite database
└── manage.py

yaml
Copy
Edit

---

## 🛠️ Tech Stack

- Python 3.13+
- Django 5.x
- SQLite (default DB)
- HTML & Django Templates

---

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/airline-system.git
cd airline-system
Create a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations

bash
Copy
Edit
python manage.py migrate
Create a superuser

bash
Copy
Edit
python manage.py createsuperuser
Run the development server

bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000/ to view the app.

🔐 Admin Login
Use your superuser credentials at:

arduino
Copy
Edit
http://127.0.0.1:8000/admin/
From there, you can manage:

Airports

Flights

Passengers

📝 Future Improvements
Booking history for users

Search and filter for flights

Flight cancellation or modification

Improved UI with Tailwind or Bootstrap

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📄 License
This project is open-source and available under the MIT License.

👨‍💻 Author
[Abubakar Janka]
GitHub: @Janka50


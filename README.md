# 🍽️ **Pavaj Restaurant – Web Management & Booking System**

A **Django-based web application** for managing a restaurant’s menu, reservations, and customer inquiries.
The platform provides both a **public interface** for customers and a **management dashboard** for restaurant staff.

---

## ✅ **Key Features**

### **For Customers**

* 📝 **Online Reservations** – make bookings with instant email confirmation & follow-up updates.
* ❓ **Customer Inquiries** – send questions directly to the restaurant and receive email responses.
* 📖 **Interactive Menu** – browse menu types, categories, items, and allergens (vegan, vegetarian, gluten-free friendly).

### **For Staff**

* 📅 **Reservation Management** – confirm or reject bookings with automated email notifications.
* 💬 **Inquiry Dashboard** – respond to inquiries, with automated email replies to customers.
* 🍲 **Menu Management** – full CRUD for menu types, categories, items, and allergens.
* 🔐 **Role-based Permissions** – only authorized staff can manage sensitive data.

### **System Features**

* ⚡ **Asynchronous Email Notifications** – powered by **Celery + Redis**.
* 🌐 **Public REST API** – exposes the entire restaurant menu in JSON format.
* 📱 **Responsive Design** – optimized for desktop and mobile.

---

## 🛠️ **Technology Stack**

* **Backend:** Django 5, Django REST Framework (DRF)
* **Frontend:** Django Templates (HTML, CSS, JavaScript)
* **Database:** PostgreSQL (or SQLite for local development)
* **Asynchronous Tasks:** Celery + Redis
* **Email Notifications:** Gmail SMTP with App Passwords
* **Containerization:** Docker (Redis & Celery workers)
* **Version Control:** Git & GitHub

---

## 🚀 **Installation & Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/todorpeychinov/pavaj-restaurant.git
cd pavaj-restaurant
```

### **2. Create and Activate Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
```

### **3. Install Requirements**

```bash
pip install -r requirements.txt
```

### **4. Configure Environment Variables**

Create a `.env` file in the project root:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

⚠️ **Make sure `.env` is listed in `.gitignore`.**

### **5. Apply Migrations & Create Superuser**

```bash
python manage.py migrate
python manage.py createsuperuser
```

### **6. Start Redis (via Docker)**

```bash
docker run --name redis -p 6379:6379 -d redis
```

### **7. Start Celery Worker**

```bash
celery -A pavaj_restaurant worker -l info --pool=solo
```

### **8. Run Development Server**

```bash
python manage.py runserver
```

Go to: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🔗 **Public REST API**

### **Endpoint:** `/api/menu/`

Returns the full restaurant menu grouped by menu types and categories.

#### ✅ **Example Response:**

```json
[
  {
    "name": "Dinner Menu",
    "description": "Evening specials",
    "categories": [
      {
        "name": "Starters",
        "description": "Appetizers to begin your meal",
        "order": 1,
        "items": [
          {
            "name": "Bruschetta",
            "description": "Grilled bread with tomatoes",
            "is_vegan": true,
            "is_vegetarian": true,
            "is_gluten_free": false,
            "weight": 120,
            "allergens": [
              {
                "name": "Gluten",
                "icon": "/static/img/allergens/gluten.png"
              }
            ]
          }
        ]
      }
    ]
  }
]
```

---

## 📧 **Email Notifications**

### **Reservation Workflow**

* **On request:** customer receives confirmation of request.
* **On approval/rejection:** automatic email sent to the customer.
* **Notification to staff:** restaurant receives email for each new reservation.

### **Inquiry Workflow**

* **On submission:** customer receives thank-you email.
* **On response:** customer receives reply via email.
* **Notification to staff:** restaurant receives email for each new inquiry.

---

## 👥 **User Roles & Permissions**

* **Customers:** browse menu, book tables, send inquiries.
* **Staff:** manage bookings, answer inquiries.
* **Managers:** full access to menu management & system settings.

---

## 🤝 **Contributing**

Pull requests are welcome!
For significant changes, please open an issue first to discuss what you would like to change.

---

## 📜 **License**

This project is licensed under the **MIT License**.

---

### ✅ **To-Do & Future Improvements**

* [ ] Add **multi-language support** (BG/EN).
* [ ] Extend API with reservation endpoints.
* [ ] Improve menu browsing with images.

---

## 🖼️ **Screenshots** *(Optional)*

*(You can add screenshots here – e.g., admin dashboard, menu page, etc.)*

---

### 🔥 **Enjoy Pavaj Restaurant!**

Made with ❤️ using Django & Celery.



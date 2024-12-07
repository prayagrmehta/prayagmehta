# My Portfolio (Django)

Welcome to the repository for my personal portfolio website! This project showcases my skills, projects, and professional journey, and is built using Django. The live version is accessible at: [prayagmehta.onrender.com](https://prayagmehta.onrender.com).

---

## Features

- **Responsive Design**: Optimized for all devices (desktops, tablets, and mobiles).
- **Dynamic Content**: Content managed using Django's powerful framework.
- **Projects Section**: Displays detailed information about my projects, including live links and descriptions.
- **Blog**: Includes a blog section for sharing updates and insights (if applicable).
- **Contact Form**: Allows users to send messages directly from the website.
- **Admin Panel**: Easy-to-manage admin interface for updating content.

---

## Technologies Used

- **Framework**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (default) / PostgreSQL (optional for production)
- **Hosting**: Render.com
- **Version Control**: Git and GitHub

---

## Getting Started
### 1. Clone the Repository

```bash
git clone https://github.com/prayagrmehta/prayagmehta.git
```
## 2. Navigate to the Project Directory
```bash
cd prayagmehta
```
3. Set Up a Virtual Environment
```bash
python -m venv env
```
```bash
# source env/bin/activate
# On Windows: env\Scripts\activate
```
4. Install Dependencies
Install the required packages from requirements.txt:
```bash
pip install -r requirements.txt
```
5. Apply Migrations
Run Django migrations to set up the database schema:
```bash
python manage.py migrate
```
6. Run the Development Server
Start the local server:
```bash
python manage.py runserver
```
Then open your browser and navigate to:
http://127.0.0.1:8000/

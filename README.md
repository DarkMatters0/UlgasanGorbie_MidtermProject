# Django Task Manager Setup Instructions

## 1. Fork and Clone the Repository

1. Go to the GitHub repository.
2. Click on the **Fork** button (top-right corner) to create a copy under your account.
3. Open a terminal in VS Code and run the following command to clone the repository (replace `<your-username>` with your GitHub username):

   ```sh
   git clone https://github.com/<your-username>/task_manager.git
   ```

4. Navigate to the project folder:

   ```sh
   cd task_manager
   ```

---

## 2. Check MariaDB Version in XAMPP

1. Open **XAMPP Control Panel** and start **Apache** and **MySQL**.
2. Open your browser and go to:

   ```
   http://localhost/phpmyadmin
   ```

3. Look at the **Server version** (top-right corner):
   - If **MariaDB is 10.4 or below**, update to the latest version from [MariaDB official site](https://mariadb.org/download/).

---

## 3. Set Up the Virtual Environment

1. In the VS Code terminal, activate the virtual environment using Pipenv:

   ```sh
   pipenv shell
   ```

   - If Pipenv is not installed, install it first:

     ```sh
     pip install pipenv
     ```

2. Navigate to the project directory if you haven't already:

   ```sh
   cd task_manager
   ```

---

## 4. Run the Django Development Server

1. Inside the **pipenv shell**, run the following command to start the server:

   ```sh
   python manage.py runserver
   ```

2. If everything is set up correctly, the terminal will show that the server is running.

---

## 5. Open the Website in Browser

1. Open your browser and visit:

   ```
   http://127.0.0.1:8000/tasks
   ```

2. You should see the Django **task manager** application running.

---

## 6. Additional Notes

- If you get a **database connection error**, check your database credentials in `settings.py` to ensure they match **phpMyAdmin**.
- If migrations are missing, run:

  ```sh
  python manage.py migrate
  ```

---

Your Django project is now set up and running! 🚀 If you encounter any issues, feel free to check the documentation or ask for help.

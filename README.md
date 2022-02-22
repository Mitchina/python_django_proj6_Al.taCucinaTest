## Al.ta Cucina Test
## _Django Project - My Films List_

***
# 1.Setup Project Steps
To run this project, make sure you have Python installed in you PC.

### 1.1 - Check if Python is installed:
- Open Command Prompt
- Type python or py
    ```sh
    python
    ```
- Hit Enter

If Python is installed, you will see its the version details, otherwise you will need to install it.

### 1.2 - Installing Python:
- Downloading Python 3.10.2 (https://www.python.org/downloads/)
- Repeat STEP 1 to confirm that Python has been installed.

### 1.3 - See Python pip version after Python installation:
- Open Command Prompt
- Type: pip --version
    ```sh
    pip --version
    ```
- Hit Enter

You should see the pip version details installed with Python.

### 1.4 - Installing Pipenv (a virtual environment):
We are going to use a virtual environment for this Python project. Pipenv is a dependency manager for Python projects, you can simply install it by typing in your Command Prompt:
    ```
    pip install pipenv
    ```.
- Open Command Prompt
- Type: pip install pipenv
    ```sh
    pip install pipenv
    ```
- Hit Enter

### 1.5 - Installing PostgreSQL in your PC:
This project uses PostgreSQL as database, so you need to have it installed in your PC in order to the project works.
- Download PostgreSQL 14.2 (https://www.postgresql.org/)

### 1.6 - Installing pgAdmin in your PC:
This project uses pgAdmin, so you need to have it installed in your PC in order to the project works.
Normally pgAdmin is installed with PostegreSQL, make sure to flag the option to install it at the end of in the PostegreSQL installation proccess.
- To check if it has been installed in your PC, you can use the PC search tool, and search for pgAdmin 4 application.

PgAdmin 4 is a web application and works as a browser-based client for PostgreSQL.
- You can also install it from the website, https://www.pgadmin.org/.

### 1.7 - Give a password for PostgreSQL and for pgAdmin:
- Enter in your pgAdmin 4 application with the password: ```password```
- Also use this same password to enter in the PostgreSQL database.

You are giving the password: ```password``` because it will only be using to your localhost server.

***
## 2.Cloning the project
### 2.1 - Create a folder and clone project

- Create a folder in your Desktop
- Give it a name, for example: python_django_project
- Open Command Prompt
- Type: cd Desktop/python_django_project
    ```sh
    cd Desktop/python_django_project
    ```
- Hit Enter
- Do no close the Command Prompt. Now that you are inside that new created folder directory, you can clone the project.
- Clone the project HTTPS key or SSH key.
  ```sh
  git clone git@github.com:Mitchina/python_django_proj6_Al.taCucinaTest.git
  ```
- Hit Enter
 - Do no close the Command Prompt yet, you are going to use it in the next steps.

### 2.2 - Be in the right directory (folder).
Enter inside the top folder of the project.
- To do that you can just type the code below in your Command Prompt.
  ```sh
  cd python_django_proj6_Al.taCucinaTest
  ```
- Hit Enter
- To confirm that you are in the right directory, type ```dir```
  ```sh
  dir
  ```
- Hit Enter

You now should see both the file Pipfile and Pipfile.lock among the other files of the project.

### 2.3 - Activate Virtual Environment.

- Still inside Command Prompt and inside the project directory, type pipenv shell to created your virtual environment.
  ```sh
  pipenv shell
  ```
- Hit Enter

### 2.4 - Install project libraries.
- Type pipenv install to installs all the project libraries.
    ```sh
  pipenv install
  ```
- Hit Enter
- It should install for you all the packages dependencies need for the project.

### 2.5 - Two Must-Know commands.
- To see the packages installed, you can use the command pip freeze, while inside your active virtual environment.
  ```sh
  pip freeze
  ```
- To exit you virtual environment, you can type exit.
  ```sh
  exit
  ```
***
## 3.Run the project
### 3.1 - Be in the right directory (folder) again.
To run the project, you need to be with your Virtual Environment Activated. (If you exit it, just go to your project directory in the Command Prompt and type ```pipenv shell```)
Once inside again, you need to go to the project folder directory where is located the manage.py file inside the project. 
- To do that you can just type the code below in your Command Prompt.
  ```sh
  cd ACTest-project
  ```
- Hit Enter
- To confirm that you are in the right directory, type ```dir```
  ```sh
  dir
  ```
- Hit Enter

You now should see the file manage.py among the other files of the project.

### 3.2 - Now you can run the project.
- Run the full command below:

```sh
python manage.py wait_for_db && python manage.py migrate && python manage.py runserver
```
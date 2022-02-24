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

If Python is installed, you will see its the version details (jump to step 1.3), otherwise you will need to install it.

### 1.2 - Install Python:
- Download and Install Python 3.10.2, follow the instruction on their website (https://www.python.org/downloads/)
- Remember to Add Python to the PATH Environmental Variable.
- Repeat STEP 1 to confirm that Python has been installed.

### 1.3 - See Python pip version after Python installation:
- Open Command Prompt
- Type: pip --version
    ```sh
    pip --version
    ```
- Hit Enter

You should see the pip version details installed with Python.

### 1.4 - Install Pipenv (a virtual environment):
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

### 1.5 - Install PostgreSQL in your PC:
This project uses PostgreSQL as database, so you need to have it installed in your PC in order to the project works.
- Download and Install PostgreSQL 14.2, follow the instruction on their website (https://www.postgresql.org/).
- During the installation give the root user the password: ```password```.

### 1.6 - Install pgAdmin in your PC:
This project uses pgAdmin, so you need to have it installed in your PC for the project to works.
PgAdmin 4 is a web application and works as a browser-based client for PostgreSQL.
Normally pgAdmin is installed with PostegreSQL, make sure to flag the option to install it at the end of the PostegreSQL installation proccess.
- To check if it has been installed in your PC, search for pgAdmin 4 application with the PC search tool.
If PostgreSQL has not installed pgAdmin within its packages, you can also install it from the website, https://www.pgadmin.org/.

### 1.7 - Give a password for pgAdmin:
- Open the pgAdmin 4 application and give it the password: ```password```
- Once inside, on the left side of the page, click in 'Servers'.
- You will be asked to type again a password, with the message: "Please enter the password for the user 'postgres' to connect the server - "PostgreSQL 14".
- Use the password that you gave in the PostgreSQL installation proccess, if you follow this instructions the password should be ```password```.

The password ```password``` is not safe, for now it will be ok since we will only use pgAdmin in a localhost server.

### 1.8 - Create the project database.
- After you gave the password, you can access 'Servers' tab and you should be able to see the name 'Databases' inside the sub tab 'PostgreSQL'.
- Right click on the word 'Databases', click on 'Create', and then click on 'Database'.

- Give the database a name of: ```ACTest-project```.
- Before saving it, go to the 'Security' tab, click on the plus sign in the 'Privileges' and set up the followings: 
'Grantee' = postgres, 'Privileges' = all, 'Grantor' = postgres.
- Now you can save the database and close the pgAdmin 4 application.

### 1.9 - Add an extension to your web browser Google Chrome.

- If you do not have the web browser Google Chrome installed in you PC, download and install it. You can find the download at: https://www.google.com/chrome/
 
We are going to use a Chrome extension called: ```mod header```.
It allows you to modify the headers of the requests that you make, so it makes really easy to simulate and test authentication with the API.

- Open the web browser Google Chrome.
- Add the extension by searching it by its name in the google extensions webstore: https://chrome.google.com/webstore/category/extensions
- Or simply opening the full link below: 
https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj?gclid=Cj0KCQiA09eQBhCxARIsAAYRiymLnLv_RFeW1iludwVoXBI1N7kJNOGXDHayZrBI0Z8hpi8fhHaYNTwaAnIrEALw_wcB

- Add the ```mod header``` extension to your Chrome.

***
## 2.Cloning the project

### 2.1 - Make sure that Git is installed on your PC
- Open Command Prompt
- Type git version to verify that Git is installed.
    ```sh
    git version
    ```
- If it is installed you are ok to move on with the next steps. Otherwise, visit Git website to understand how to install it in your PC.
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

### 2.2 - Creating a folder and cloning the project

- Create a folder in your Desktop
- Give it a name, for example: python_django_project
- Open Command Prompt
- Type: cd Desktop/python_django_project
    ```sh
    cd Desktop/python_django_project
    ```
- Hit Enter
- Do no close the Command Prompt. 
- Now that you are inside that new created folder directory, clone the project.
- Clone the project with HTTPS key or SSH key. If you have a SSH key associated with your account, jump to step (2.2.2).
#### 2.2.1 - Cloning with HTTPS key
  ```sh
  git clone https://github.com/Mitchina/python_django_proj6_Al.taCucinaTest.git
  ```
#### 2.2.2 - Cloning with SSH key
  ```sh
  git clone git@github.com:Mitchina/python_django_proj6_Al.taCucinaTest.git
  ```
- Hit Enter
 - Do no close the Command Prompt yet, you are going to use it in the next steps.

### 2.3 - Be in the right directory (folder).
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

### 2.4 - Activate Virtual Environment.

- Still inside Command Prompt and inside the project directory, type pipenv shell to create your virtual environment.
  ```sh
  pipenv shell
  ```
- Hit Enter

### 2.5 - Install project libraries.
- Type pipenv install to installs all the project libraries.
    ```sh
  pipenv install
  ```
- Hit Enter
- It should install for you all the packages dependencies need for the project.

### 2.6 - Two Must-Know commands.
- To see the packages installed, you can use the command pip freeze, while inside your active virtual environment.
  ```sh
  pip freeze
  ```
- Do not exit right now, but to exit you virtual environment, you can type exit.
  ```sh
  exit
  ```
***
## 3.Run the project
### 3.1 - Be in the right directory (folder) again.
To run the project, you need to be with your Virtual Environment Activated. (If you exit it, just go to your project directory in the Command Prompt and type ```pipenv shell```).

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


Before runing the project, confirm that the password set for PostgreSQL root user is: ```password```, eventually if your password is different, go to the setting.py file inside the folder: python_django_project\python_django_proj6_Al.taCucinaTest\ACTest-project\ACTest. 
In the line 94 of the setting.py file, change the field 'PASSWORD' with your PostgreSQL root user password and save the file.

### 3.2 - Now you can run the project.
- Run the full command below:

```sh
python manage.py wait_for_db && python manage.py migrate && python manage.py runserver
```
## 4.Creating a User
- Open the Browser with Google Chrome (because we are going to use a Google Chrome extension) 
- Access the endpoint: 
http://127.0.0.1:8000/api/user/create/

- Put your credentials to register
- Register with an Email, Password and Name.
- Hit the POST button

### 4.1 - To provide the server the Authentication credentials, get your token.
- To be an authorized user, you need to be authenticated by a Token.
- Move on to the endpoint:
http://127.0.0.1:8000/api/user/token/

- Give the Email and Password that you used to register yourself, in the step before (4.1).

- Once you hit the POST button, you should see your Token in the page, like in the example below:
{
    "token": "```8d3be064346d0d8b8ce43d8a6d1dadcf4ad6ba6```"
}
- Copy your token key.

### 4.2 - Open 'mod header' Chrome extension
- Head over to 'mod header' extension in your Chrome.

Inside the extension window, you will see a Name field and a Value field.
- Type 'Authorization' in the Name field.
- In the Value field you should write 'Token', with capital T and paste your token copied from the
step before (4.2) separated from a blank space.

It should be like in the ```example``` below:

```sh 
        Authorization                  Token fd3be064346d0d8b8ce43d8a6d1dadcf4ad6ba6
```	
- Once given the information, click on the white space of the window to deselect the fields.
- Click on the Browser page to close the extension window.

Now you are an authorized user.

### 4.3 - To update or change your credentials
- You can also change your email, password and name.
- To do that, access the endpoint: 
http://127.0.0.1:8000/api/user/me

If you do not want to change your credentials, jump to the step 5.
You can change your credentials using the method PATCH or PUT, but with the PUT you are going to have to provide all the fields and that includes the 
password field.
To change with using the method PATCH, switch to the tag 'Raw data', and update the fields you want inside the 'Content' field, clicking then the button PATCH.

- If you changed the password and want to verify that it has changed in the database, just try to access your token again with your new password http://127.0.0.1:8000/api/user/token.
- You can go then to http://127.0.0.1:8000/api/user/me, to see the other changes as well.


## 5. Add a Film to your list.

### 5.1 - Give Tags and Genres for your films.
- Access the endpoint: http://127.0.0.1:8000/api/film
- You will see that you can create films, as well as its tags and genres.

The film tags are basically the platforms where you can see the film on, exmaple: Netflix, Disney+, Amazon Prime Video etc.
And the genres are categories that define a movie based on its narrative elements, example: Action, Drama, Comedy and so on.

### 5.2 - Creating Tags.
- To create tags for your films, go the endpoint: 
http://127.0.0.1:8000/api/film/tags/

Choose the tab 'HTML form'. We are going to create 3 different Tags as an example.

- Give the first Tag name for a film, example:
- Type ```Netflix```, and hit the POST button.
- Erase the Netflix name and type ```Disney+```, hit the POST button.
- Now, erase the Disney+ name and type ```Amazon Prime Video```, hit the POST button.

If you open the http://127.0.0.1:8000/api/film/tags/ again, you can see a list of your created tags.

### 5.3 - Creating Genres.
- To create genres for your films, go to the endpoint: 
http://127.0.0.1:8000/api/film/genres/

Choose the tab 'HTML form'. We are going to create 3 different Genres as an example.

- Give the first Genre name for a film, example:
- Type ```Action```, and hit the POST button.
- Erase the Action name and type ```Drama```, hit the POST button.
- Now, erase the Drama name and type ```Comedy```, hit the POST button.

If you open the http://127.0.0.1:8000/api/film/genres/ again, you can see a list of your created genres.

### 5.4 - Creating Films.
- Go on the endpoint: 
http://127.0.0.1:8000/api/film/films/

Choose the tab 'HTML form'. We are going to create 3 different Films as an example.
The required fields for a film are: Title, Time in minutes and released Year. The other fields are optional.

- Creating first example of film:
Title: ```The Hunger Games```
Time minutes: ```142```
Year: ```2012```
Have seen: ```yes``` (flag)
Link: (leave it blank)
Tags: ```Netflix```
Genres: ```Action```

- Hit the POST button.

- Creating second example of film:
Title: ```The Pianist```
Time minutes: ```150```
Year: ```2002```
Have seen: (leave it blank)
Link: (leave it blank)
Tags: ```Netflix```
Genres: ```Drama```

- Hit the POST button.

- Creating third example of film:
Title: ```School of Rock```
Time minutes: ```109```
Year: ```2003```
Have seen: ```yes``` (flag)
Link: (leave it blank)
Tags: ```Amazon Prime Video```
Genres: ```Comedy```

- Hit the POST button.

If you open the http://127.0.0.1:8000/api/film/films/ again, you can see a list of your created films.

### 5.5 - Filtering a Film.

You can filter your list of films by its Tags, Genres, or even for films that you have already seen or not seen.

#### 5.5.1 - Filtering by Tag.
So to filter a film by its tag, you will need to know the tags ids that are associated with your films tags.
For example, if Netflix has tag number 8, you can search for Netflix films adding the '?tags=8' at the end of your films list link.

-- Filtering films with Netflix tags:
http://127.0.0.1:8000/api/film/films/?tags=8
-- You will get the films: "The Pianist" and "The Hunger Games".

#### 5.5.2 - Filtering by Genre.
To filter a film by its genres, you will need to know the genres ids that are associated with your films genres.
For example, if Action has genre number 11, you can search for Action films adding the '?genres=11' at the end of your films list link.

-- Filtering films with Action genres:
http://127.0.0.1:8000/api/film/films/?genres=11
-- You will get the film: "School of Rock".

#### 5.5.3 - Filtering by Have Seen Flag.
To filter films of your list that you have not seen yet, you just need add '?have_seen=False' at the end of your films list link.

-- Filtering films that you have not seen yet:
http://127.0.0.1:8000/api/film/films/?have_seen=False
-- You will get the film: "The Pianist".


## 6. About this project.
- This project was created for a BackEnd Developer Test held by the company Al.ta Cucina.
- Where the intention was to build a fully functioning back-end REST API with Django rest framework.
- It does not have an interface, just the back-end endpoints.
- The project was created using a test-driven development.
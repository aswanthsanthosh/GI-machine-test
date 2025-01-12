# Django-Project

this project takes a csv file in request and save the validated data in 'User' model for valid inputs, also with successful & failed inputs' count

__Setup__
__1. Clone the repository__
   ```
   git clone https://github.com/aswanthsanthosh/GI-machine-test.git
   cd GI-machine-test/project/
   ```
__2. Create a Virtual Environment__
   It's recommended to create a virtual environment to keep your dependencies isolated.
   
for linux : 
   ```
   python -m venv env
   source env/bin/activate
   ```
for windows :
   ```
   python -m venv env
   env\Scripts\activate
   ```
__3. Install Dependencies__
   Install the project dependencies listed in the requirements.txt file.
   ```
   pip install -r requirements.txt
   ```
__4. Apply Migrations__
   The default database will be sqlite. Unless you want to configure db to some other database, you can directly run the migrate command
   ```
   python manage.py migrate
   ```
__5. Run Development Server__
   use this command to run this django project :
   ```
   python manage.py runserver
   ```
__6. Test__
   run this command to run test :
   ```
   python manage.py test
   ```
__Usage :__
- after running the developement server & Celery go to http://127.0.0.1:8000/upload/

  upload csv file in request as 'file'

screenshots and recordings are in 'recordings' folder in main branch
   

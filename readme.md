This application is built using Python Flask. 

### Dependencies:
1. System must have Python installed
2. System must be able to run Python

### Steps to running the application:
1. Open and run the following steps in a terminal.
2. Python Flask must be installed. To install it, run ```pip install flask```
3. Create a virtual environment using the following command ```python -m venv my_env```
4. Activate the virtual environment using the following command ```source my_env/bin/activate```
5. Download/Clone this github repository in the my_env folder. Use "ls" and "cd" to navigate to the folder. To access the my_env folder, I did ```cd my_env``` given that the my_env folder was saved to my Home directory. 
6. Open the folder on your terminal using "cd folder-name". To open the folder with the application, I did ```cd coding-challenge-fetch```  given that I was already in the my_env folder. 
7. If you run ```ls```, you should be able to see a templates folder, reciept.py, and readme.md. This means you are in the right folder and can export the application.
8. Now that you are in the application folder, to export the application, use the following command ```export FLASK_APP=reciept```
9. Now, the application can be run using ```flask run```
10. The application opens to a localhost with the following url: "http://127.0.0.1:5000/". This is also mentioned in the terminal. 
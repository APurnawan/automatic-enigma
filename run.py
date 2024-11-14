#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python311/python.exe 

from klinik import app
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
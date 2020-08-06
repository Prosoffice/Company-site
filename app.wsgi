
from dotenv import load_dotenv
load_dotenv(dotenv_path="/var/www/Company-site/.env")
import sys
sys.path.insert(0, "/var/www/Company-site")
from app import app as application

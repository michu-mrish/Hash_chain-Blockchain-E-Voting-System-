import sys
import os

# Add backend to Python path
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend'))
sys.path.insert(0, backend_path)

# Import the Flask app
from app import app

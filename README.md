# Unicorn AI 🦄

An AI-powered service to create and share web resumes.


## Initial Setup ⚙

```pwsh
# Clone the repository
git clone https://github.com/AlexYelisieiev/unicorn-ai

# Switch to the created directory
cd unicorn-ai

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\scripts\activate

# Install the requirements
pip install -r requirements.txt

# Create a database
python manage.py migrate

# Run server
python manage.py runserver
```

You won't have to run `git clone https://github.com/AlexYelisieiev/unicorn-ai`, `cd unicorn-ai`, `python -m venv venv`, `python manage.py migrate`, and `pip install -r requirements.txt` next time.

After the initial setup completed, you can run the server with:
```pwsh
# Activate the virtual environment
venv\scripts\activate

# Run server
python manage.py runserver
```

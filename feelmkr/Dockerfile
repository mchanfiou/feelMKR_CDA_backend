FROM python:3.13

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY feelmkr/requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire project
COPY . .

# Set the entry point
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "feelMKRBackend.wsgi:application"]
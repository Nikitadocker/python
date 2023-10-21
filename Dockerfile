# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install PyPDF2 and PyCryptodome libraries
RUN pip install PyPDF2 pycryptodome

# Copy the Python script to the container
COPY pdf_password_remover.py /app/

# Command to run the script
CMD ["python", "pdf_password_remover.py"]

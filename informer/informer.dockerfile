# Extend the official Rasa SDK image
FROM python:3.8

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements
COPY repo/requirements.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy files to working dir
COPY ./repo/models.py ./repo/stock_informer* ./repo/yahoofinance_informer.py /app/

# By best practices, don't run the code with root user
USER 1001
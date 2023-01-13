# Extend the official Rasa SDK image
FROM rasa/rasa:3.4.0-full

# Use subdirectory as working directory
WORKDIR /app

# Change back to root user to install dependencies
USER root

# Copy the whole repo
COPY ./repo/* /app/
# overwrite creds and endpoints
COPY ./credentials.yml ./endpoints.yml /app/

# By best practices, don't run the code with root user
USER 1001

# FastAPI Error Logging Application

## Overview

This FastAPI application is designed to log and store errors from a Django application. It features a RESTful API for error logging, IP whitelisting for security, and a simple UI to view logged errors. The application is Dockerized for easy deployment.

## Features

- **Error Logging**: Log errors via a RESTful API.
- **IP Whitelisting**: Only allow requests from specified IP addresses.
- **Database Storage**: Store logs in an SQLite database.
- **Docker Support**: Easily deploy the application using Docker.
- **User Interface**: View logged errors through a simple web interface.

## Technologies Used

- FastAPI
- SQLAlchemy
- SQLite
- Jinja2 for templating
- Docker
- Python-dotenv for environment variable management

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip
- Docker (optional for Docker deployment)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/devdutt-dikshit/fastapi-logger-service.git
   cd fastapi-logger-service

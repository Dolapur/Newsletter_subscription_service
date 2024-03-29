# Newsletter Subscription Service
  The Newsletter Subscription Service is a web application built using Django and Celery for managing newsletter subscriptions and sending out newsletters to subscribers. It provides a RESTful API for subscribing, unsubscribing, and managing newsletter content. Additionally, during development, SMTP for Dev is utilized to simulate email sending without actually sending emails to real recipients. This allows developers to test email functionality without spamming real customers or needing to configure a complex email server.

# Features
  * Subscription Management: Users can subscribe to the newsletter service by providing their email address.

  * Unsubscribe Functionality: Subscribers have the option to unsubscribe from the service at any time.

  * Newsletter Creation: Administrators can create newsletters by providing a title and body content.

  * Asynchronous Newsletter Sending: Newsletters are sent asynchronously using Celery to avoid blocking the   main application.

  * Integration with SMTP Server: The application integrates with an SMTP server for development purposes, allowing developers to test email functionality without sending emails to real recipients.

  * Swagger UI: Explore and interact with the API using Swagger UI. The API documentation is available at http://localhost:8000/swagger/ when running the development server.

# Getting Started
* Prerequisites
   Before getting started, make sure you have the following installed:

     Python 3.x
     Django
     Celery
     RabbitMQ (or another message broker compatible with Celery)

# Installation
* Clone the repository:
   git clone https://github.com/Dolapur/Newsletter_subscription_service.git

* Navigate to the project directory:
   
   cd Newsletter_subscription_service

* Create and activate a virtual environment:

   python3 -m venv env
   
   source env/bin/activate  (Linux/macOS)
   
   env\Scripts\activate  (Windows)

* Install the project dependencies:
  
   pip install -r requirements.txt

* Apply database migrations:
   python3 manage.py makemigrations
   python3 manage.py migrate

* Create a superuser for administrative access:
   python3 manage.py createsuperuser

* Start the development server:

   python3 manage.py runserver

* Start the Celery Worker:
   
   celery -A newsletter_service worker -l INFO

* Start the SMPT Server:
   
   docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev

* Start the RabbitMQ Server:
   
   docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management

# Endpoints
  Access the website at http://localhost:8000/swagger
  Access SMTP server website at http://localhost:3000


# Error Handling
  The API returns standard HTTP response codes for success and error cases. In case of an error, a JSON response will include an error field with a description of the problem.

# License
  This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
  Special thanks to the contributors and maintainers of Django, Celery, and other open-source libraries used in this project.

# THANKS FOR VISITING




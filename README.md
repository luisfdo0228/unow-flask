# Flask SendGrid App

## Description
This application is a professional Flask project that sends email notifications using SendGrid when a new user is created.

## Setup Instructions

1. Unzip the project.
2. Navigate to the project folder:
    ```bash
    cd flask_sendgrid_app
    ```
3. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Configure environment variables by renaming `.env.example` to `.env` and filling in your credentials.
6. Run the application:
    ```bash
    python flask_sendgrid_app/app.py
    ```

## Testing the API

Send a POST request to `http://127.0.0.1:5000/create_user` with the following JSON payload:

```json
{
    "email": "user@example.com",
    "name": "John Doe"
}
```

If successful, the user will receive a welcome email.

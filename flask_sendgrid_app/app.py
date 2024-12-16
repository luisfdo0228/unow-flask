import os
from flask import Flask, render_template, request, jsonify
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)

# Load sensitive configurations
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

# Ensure required environment variables are set
if not SENDGRID_API_KEY or not SENDER_EMAIL:
    raise RuntimeError("Missing required environment variables: SENDGRID_API_KEY or SENDER_EMAIL")

@app.route("/send_email", methods=["POST"])
def send_email_endpoint():
    """API endpoint to send an email."""
    try:
        data = request.json
        recipient_email = data.get("email")
        recipient_name = data.get("name")

        if not recipient_email or not recipient_name:
            return jsonify({"error": "Missing required fields: 'email' or 'name'"}), 400

        # Send email notification
        subject = "Welcome to Our Platform!"
        message = render_template("welcome_email.html", name=recipient_name)

        send_email(subject, recipient_email, message)

        return jsonify({"message": f"Email sent successfully to {recipient_email}."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def send_email(subject, recipient_email, html_content):
    """Send an email using SendGrid."""
    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=recipient_email,
        subject=subject,
        html_content=html_content,
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
    except Exception as e:
        app.logger.error(f"Failed to send email: {e}")
        raise

if __name__ == "__main__":
    app.run(debug=True)

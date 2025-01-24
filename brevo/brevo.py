import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

def send_welcome_email(email):
    try:
        api_key = os.getenv('BREVO_API')
        if not api_key:
            return "API Key not found. Please check your environment variables."

        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = api_key
        api_client = sib_api_v3_sdk.ApiClient(configuration)
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(api_client)

        sender_email = "akhunjisana@gmail.com"  

        html_content = """
        <html>
            <body>
                <h1>Welcome to Cash Flow!</h1>
                <p>Dear User,</p>
                <p>Thank you for signing up with Cash Flow! We're thrilled to have you as part of our community. You're now ready to explore all the exciting features and resources we offer.</p>
                <p>At Cash Flow, our goal is to provide you with the best tools to enhance your productivity. We're confident you'll find everything you need to achieve your financial goals.</p>
                <p>Here’s what you can do next:</p>
                
                <p>If you have any questions, feel free to reach out to our support team at support@cashflow.com. We’re here to help!</p>
                <p>Thank you for joining Cash Flow. We look forward to being part of your journey!</p>
                <br>
                <p>Warm regards,<br>The Cash Flow Team.</p>
            </body>
        </html>
        """

        message = sib_api_v3_sdk.SendSmtpEmail(
            sender={"email": sender_email},
            to=[{"email": email}],
            subject="Welcome to Cash Flow!",
            html_content=html_content
        )

        # Sending the email using Brevo API
        response = api_instance.send_transac_email(message)
        return f"Email sent to {email} successfully!"

    except ApiException as e:
        print(f"Exception when calling Brevo API: {e}")
        return f"Failed to send email to {email}: {str(e)}"

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

        message = sib_api_v3_sdk.SendSmtpEmail(
            sender={"email": sender_email},
            to=[{"email": email}],
            subject="Welcome to Our Platform!",
            html_content="<html><body><h1>Welcome!</h1><p>We are excited to have you with us.</p></body></html>"
        )

        response = api_instance.send_transac_email(message)
        return f"Email sent to {email} successfully!"

    except ApiException as e:
        print(f"Exception when calling Brevo API: {e}")
        return f"Failed to send email to {email}: {str(e)}"
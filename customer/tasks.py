import re
from twilio.rest import Client
from customer.models import Credentials
from django.template.loader import render_to_string


def format_phone_number(number_to_format):
    formatted_number = re.sub("\D", "", number_to_format)
    if len(formatted_number) == 10:
        return "+1" + formatted_number
    else:
        return "+" + formatted_number


def post_code_to_twilio(phone_number, verification_code):
    twilio_sid = Credentials.objects.get(name="twilio_SID").api_key
    twilio_auth_token = Credentials.objects.get(name="twilio_auth_token").api_key
    twilio_phone_number = Credentials.objects.get(name="twilio_phone_number").api_key
    client = Client(twilio_sid, twilio_auth_token)
    formatted_number = format_phone_number(phone_number)
    message_body = """\nYour Inlyst Verification Code: {}""".format(verification_code)
    try:
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=formatted_number,
        )
        return "success"
    except Exception as e:
        return e.message


def post_code_to_sendgrid(email, verification_code):
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    from customer.models import Credentials

    html_message = render_to_string(
        "admin/verification_email.html",
        {
            "verification_code": verification_code,
        },
    )
    message = Mail(
        from_email="jacob@inlyst.com",
        to_emails=email,
        subject="Inlyst Verification Code",
        html_content=html_message,
    )
    try:
        sg = SendGridAPIClient(Credentials.objects.get(name="sendgrid").api_key)
        response = sg.send(message)
    except Exception as e:
        print("the exception for sendgrid email is ", e)

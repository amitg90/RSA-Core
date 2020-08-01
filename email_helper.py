import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_order_confirmation(email, item):
    try:
        message = Mail(from_email='noreply@mlacademy.io', to_emails=email, subject='Order confirmation from ML Academy store', html_content='<strong>Your order confirmation for {} is succesful</strong>'.format(item.get("product_title")))
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return True
    except Exception as e:
        print(e)
        return False

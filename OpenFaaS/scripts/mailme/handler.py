# import libraries we going to use
# no shebang is needed at the start
# all libs I'm importing are native to python so I did not put anything in requirements.txt
import os
import json
import smtplib
from smtplib import SMTPException
from smtplib import SMTPDataError
from email.mime.text import MIMEText
from email.utils import formataddr

# Lets define some usefull functions

def get_secret(secret_name):
    '''
    - Returns secret value if exists, if not return False
    - Secret needs to be create before the function is build
    - Secret needs to be defined in functions yaml file
    '''
    try:
        with open('/var/openfaas/secrets/' + secret_name) as secret:
            secret_key = secret.readline().rstrip()
            return secret_key
    except FileNotFoundError:
        return False

def get_variable(var_name):
    '''
    - Returns environment variable value if exists, if not return False
    - Variable needs to be defined in functions yaml file
    '''
    return os.getenv(var_name, False)


def api_key_check(provided_key):
    '''
    - Check if provided api key is valid
    '''
    if get_secret('api-key') == provided_key:
        return True
    else:
        return False


def key_present(json, key):
    '''
    - Return true if Key exist in json
    '''
    try:
        _x = json[key]
    except KeyError:
        return False
    return True

# Main function
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    # If there is value passed to function
    if req:
        # check if its json formated by trying to load it
        try:
            json_req = json.loads(req)
        except ValueError as e:
            return "Bad Request", 400
    else:
        return "Bad Request", 400

    # Before anything check if api key from secret match api key provided
    # Might me good to implement this so there is no random spamming of function
    if key_present(json_req, 'api-key'):
        key = json_req["api-key"]
        if api_key_check(key) is False:
            return "Unauthorized", 401
    else:
        return "Unauthorized", 401

    # Cool if we are here api key was authorized
    # Let check if in posted body are keys that we need ( msg, to)
    if key_present(json_req, 'msg'):
        msg_text = json_req["msg"]
    else:
        return "Bad Request", 400

    if key_present(json_req, 'to'):
        to = json_req["to"]
    else:
        return "Bad Request", 400

    # So we have values for message, to whom to send it, lets get sender
    sender = get_variable('sender')

    # Lets try to build message body and send it out.
    try:
        msg = MIMEText(msg_text)
        msg['From'] = formataddr(('Author', get_variable('sender')))
        msg['To'] = formataddr(('Recipient', to))
        msg['Subject'] = 'OpenFaas Mailer'

        mail_server = smtplib.SMTP_SSL(get_variable('smtp_server'))
        mail_server.login(get_variable('smtp_login'), get_secret('email-pass'))
        mail_server.sendmail(sender, to, msg.as_string())
        mail_server.quit
        return "request accepted", 202
    except SMTPException:
        return "Failed to send email", 500
    except SMTPDataError:
        return "Failed to send email", 500
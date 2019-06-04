# With trial project with Twilio, all the usage costs are free
# This includes 1 phone number + any voice call/text/image messaging
# One exception is that, every message you sent will have this
# "Sent from your Twilio trial account" per feature used


# Dependency: install pip twilio
from twilio.rest import Client


# This function performs outgoing SMS
def send_text(phone_number, msg, image_url):

    # Account Sid and Auth Token from twilio.com/console
    account_sid = ""
    auth_token = ""

    client = Client(account_sid, auth_token)

    client.messages.create(

        # Purchased phone number
        # https://www.twilio.com/console/phone-numbers/search
        from_="",

        # Your phone number
        to=phone_number,

        body=msg,

        # The size limit for message media is 5MB.
        # Twilio supports .gif, .png, or .jpeg in URL forms
        media_url=image_url
    )

# Sending SMS
# send_sms.send_text("Your message", None)

# Sending MMS
# send_sms.send_text("Your message", "Your link")


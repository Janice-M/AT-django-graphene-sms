from django.db import models
import africastalking

# Create your models here.

#credentials4

username = ""
apikey = ""

#Initialize the SDK
africastalking.initialize(username, apikey)

#Initialize the SDK
africastalking.initialize(username, apikey)

class Sms(models.Model):
recipients = ['YOUR_PHONE_NUMBER_GOES_HERE']
message = 'I\'m a lumberjack and its ok, I sleep all night and I work all day'
sender = 'SHORTCODE_OR_SENDERID

    #Send the SMS
    try:
        #Once this is done, that's it! We'll handle the rest
        response = sms.send(message, recipients, sender)
        print(response)
    except Exception as e:
        print(f"Houston, we have a problem {e}")e

        
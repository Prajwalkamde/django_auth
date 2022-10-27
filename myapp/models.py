<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f354554 (merge conflict resolved)
import email
import imp
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.models import BaseModel
from base.emails import send_account_activation_email
# Create your models here.


# for activate email - by prajwal, date - 15/09/2022
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to = 'profile')


@receiver(post_save, sender = User)
def send_email_token(sender, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            email = instance.email
            send_account_activation_email(email, email_token)

    except Exception as e:
        print(e)
            

    

    

<<<<<<< HEAD
=======
=======
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


    

>>>>>>> eaeb8de009e9ad4518da51a5278af6ac47aea828
>>>>>>> f354554 (merge conflict resolved)

from django.db import models
import uuid

# Create an accounts model
class Accounts(models.Model):
    uid = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    surname = models.CharField(max_length=40)

    def __str__(self):
        return self.surname
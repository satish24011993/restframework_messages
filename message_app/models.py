from django.db import models

# Create your models here.
class messages_data(models.Model):
    context = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.context
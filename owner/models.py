from django.db import models

# Create your models here.
class Books(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=50)
    amount=models.PositiveIntegerField()
    copies=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)
    def __str__(self):
        return self.book_name


#ORM
#ref=modelName(property=value,property=value)
#ref.save()



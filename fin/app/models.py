from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Expense(models.Model):
    Name=models.CharField(max_length=140)
    Date_of_Expence=models.DateField()
    Description=models.TextField()
    Amount=models.PositiveIntegerField()

    cat=(
        ('health','Health'),
        ('electronics','Electronics'),
        ('travel','Travel'),
        ('education','Education'),
        ('books','Books'),
        ('others','Others'),
    )
    Category=models.CharField(max_length=20, choices=cat)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
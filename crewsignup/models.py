from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    student_number = models.IntegerField(null=True, blank=True, default=0)
    address = models.CharField(max_length=1000, null=True, blank=True, default=" ")

    def __str__(self):
        return str(self.name)


class Parent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    is_bool = models.BooleanField(default=False)

    def __str__(self):
        return str(self.text)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=300, null=True, blank=True, default='')
    boolean = models.BooleanField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.user) + str(self.question)

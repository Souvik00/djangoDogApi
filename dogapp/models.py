from django.db import models

# Create your models here.
SIZE_CHOICES = (
    ('Tiny', 'Tiny'),
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large')
)

INTESNSITY_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class Breed(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField(choices=SIZE_CHOICES)
    friendliness = models.IntegerField(choices=INTESNSITY_CHOICES)
    trainability = models.IntegerField(choices=INTESNSITY_CHOICES)
    sheddingamount = models.IntegerField(choices=INTESNSITY_CHOICES)
    exercise = models.IntegerField(choices=INTESNSITY_CHOICES)

    def __str__(self):
        return self.name


#
class Dog(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    favourite_food = models.CharField(max_length=255)
    favourite_toy = models.CharField(max_length=255)


#
def __str__(self):
    return self.name

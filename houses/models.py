from django.db import models

class House(models.Model):

    """Model definition about House"""
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    decription = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True, verbose_name = "Pets Allowed?" ,help_text="Does this house allowe pets?")


    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


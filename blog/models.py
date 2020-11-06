from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

# this defines the model, it is an object
    # class indicates we are defining an object
    # Post is the name of our model
    # models.Model means that Post is a Django Model
class Post(models.Model):
    # models.ForeignKey is a link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.CharField is how you define text with a limited number of characters
    title = models.CharField(max_length=200)
    # models.TextField is for long text, no limit
    text = models.TextField()
    # models.DateTimeField is date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # functions below are both indented into class

    # publish is name, def is function
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # returns a string with a post title
    def __str__(self):
        return self.title

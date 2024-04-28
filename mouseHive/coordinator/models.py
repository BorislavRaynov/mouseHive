from django.db import models


class MouseCoordinate(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mouse Coordinate ({self.x}, {self.y}) at {self.timestamp}"


class ImageDataSource(models.Model):
    image = models.ImageField(upload_to='images/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image Data Source uploaded at {self.timestamp}"

from django.db import models
from .categories import Category
from .tags import Tag

class Project(models.Model):
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=255)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    total_target = models.FloatField()
    total_donation = models.FloatField()
    created_at = models.DateTimeField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
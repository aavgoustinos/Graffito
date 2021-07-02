

# Create your models here.
from django.db import models


# Side Models for all sides Troodos
class Side(models.Model):
    side_title = models.CharField(max_length=200,unique=True)
    side_image = models.ImageField(null=True, blank=True, upload_to="side/sides_images")
    side_description = models.TextField(max_length=100)
    slug = models.SlugField(max_length=200)
    side_iframe_url = models.URLField(max_length=200)


    def __str__(self):
        return self.side_title


# Side Models for all items such as a graffito
class Item(models.Model):
    item_title = models.CharField(max_length=200)
    item_description = models.TextField(max_length=300)
    item_image = models.ImageField(null=True, blank=True, upload_to="item/items_images")
    slug = models.SlugField(max_length=200)
    side_ref = models.ForeignKey(Side, on_delete=models.CASCADE)


    def __str__(self):
        return self.item_title








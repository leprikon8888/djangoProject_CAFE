from django.db import models

# Create your models here.


class MenuBaseMixin(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class MenuCategory(MenuBaseMixin):
   pass


class MenuDish(MenuBaseMixin):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    ingredients = models.TextField()
    photo = models.ImageField(upload_to='menu_dishes', blank=True)

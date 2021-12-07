from django.db import models
from django_mysql.models import EnumField

from ckeditor.fields import RichTextField
from api.models import BaseModel


class CategoryType(models.TextChoices):
    EXPENSE = "expense"
    INCOME = "income"


class CustomGenericCategoryModelManager(models.Manager):
    def get_standard_categories(self):
        return self.filter(is_custom=False)


class GenericCategory(BaseModel):
    class Meta:
        db_table = "generic_categories"
        verbose_name_plural = "Generic Categories"
        constraints = (
            models.UniqueConstraint(
                fields=["name", "type"], name="GenericCategory type-name unique together constraint"
            ),
        )
        indexes = [models.Index(fields=["type"])]

    type = EnumField(choices=CategoryType)
    name = models.CharField(max_length=255, db_index=True)
    summary = RichTextField()
    is_custom = models.BooleanField(default=True, db_index=True)

    objects = CustomGenericCategoryModelManager()

    def __str__(self) -> str:
        return self.name

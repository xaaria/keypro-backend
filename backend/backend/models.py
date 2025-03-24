from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

""""
    This file contains our shared core models for all other sub-apps, like api
"""

# Gets the User model used by app
# https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#django.contrib.auth.get_user_model
UserModel = get_user_model()

CREATED_AT_FIELD = models.DateTimeField(null=False, auto_now_add=True)
UPDATED_AT_FIELD = models.DateTimeField(auto_now=True)
DELETED_AT_FIELD = models.DateTimeField(null=True, blank=True)




class PointOfInterest(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Location
    location_lat = models.DecimalField(
        null=False, 
        blank=False, 
        max_digits=17, 
        decimal_places=15, 
        db_index=True, 
        help_text="Coordinates lat.", 
        validators=[
            MinValueValidator(-90),
            MaxValueValidator(90)
        ]
    )
    location_long       = models.DecimalField(
        null=False,
        blank=False,
        max_digits=18,
        decimal_places=15, 
        db_index=True, 
        help_text="Coordinates long.", 
        validators=[
            MinValueValidator(-180),
            MaxValueValidator(180)
        ]
    )

    description = models.TextField(max_length=5000, blank=True, null=True, help_text='POI description')

    created_by = models.ForeignKey(UserModel, on_delete=models.RESTRICT)

    # Timestamp fields
    created_at  = CREATED_AT_FIELD
    updated_at  = UPDATED_AT_FIELD
    deleted_at  = DELETED_AT_FIELD # Soft delete

    def __str__(self):
        return str.format("<{} [{}, {}]>", self.id, self.location_lat, self.location_long)
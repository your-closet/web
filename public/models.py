from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )


class ClothingItem(models.Model):
    user_id = models.ForeignKey(
        verbose_name="Clothing Item",
        to="Profile",
        on_delete=models.CASCADE,
        null=False,
    )

    brand = models.TextField(
        verbose_name="Brand",
        blank=False,
        null=True,
    )

    color = models.TextField(
        verbose_name="Color",
        blank=False,
        null=True,
    )

    pattern = models.TextField(
        verbose_name="Pattern",
        blank=False,
        null=True,
    )

    price = models.IntegerField(
        verbose_name="Price",
        null=True,
    )

    size = models.TextField(
        verbose_name="Size",
        blank=False,
        null=False,
    )

    is_advertisable = models.BooleanField(
        default=False,
        null=False,
    )


class ClothingItemEvent(models.Model):
    date = models.DateTimeField(
        verbose_name="Date",
        auto_now=True,
        null=False,
    )


class Image(models.Model):
    clothing_item_id = models.ForeignKey(
        verbose_name="Clothing Item",
        to="ClothingItem",
        on_delete=models.CASCADE,
        null=False,
    )

    image_data = models.ImageField(verbose_name="Image", upload_to="images/")


class Offer(models.Model):
    owner_id = models.ForeignKey(
        verbose_name="Offer",
        to="Profile",
        on_delete=models.CASCADE,
        blank=False,
        related_name="offers")

    bidder_id = models.ForeignKey(
        verbose_name="Bidder",
        to="Profile",
        on_delete=models.CASCADE,
        blank=False,
        related_name="bidders",
    )

    amount = models.IntegerField(
        verbose_name="Bid Amount",
        default=0,
        blank=False,
    )


class Outfit(models.Model):
    rating = models.IntegerField(verbose_name="Rating", )

    times_worn = models.IntegerField(
        verbose_name="Times Worn",
        default=0,
        null=False,
    )


class OutfitItem(models.Model):
    clothing_item_id = models.ForeignKey(
        verbose_name="Clothing Item",
        to="OutfitItem",
        on_delete=models.CASCADE,
        null=False,
    )

    outfit_id = models.ForeignKey(
        verbose_name="Outfit",
        to="Outfit",
        on_delete=models.CASCADE,
        null=False,
    )

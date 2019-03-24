import json
import os
import random
from django.db import models, transaction
from django.contrib.auth.models import User


def load_data():
    path = os.path.join(os.getcwd(), 'data/auth_user.json')
    with open(path) as f:
        users = json.loads(f.read())
        with transaction.atomic():
            # User / Profile
            for user in users:
                u = User(**user)
                u.save()
                u.set_password('password1234!')
                p = Profile(user_id=u.id)
                p.save()

                # Clothing Items
                brands = ['AG', 'Parker', 'Mavi', 'Karen Kane', 'Avec']
                colors = ['red', 'green', 'purple', 'yellow', 'orange', 'n/a']
                pattern = ['solid', 'checkered', 'print']
                sizes = range(0, 32)
                for clothing_type in ['top', 'bottom', 'shoe']:
                    for idx in range(1, 10):
                        filepath = os.path.join(
                            os.getcwd(),
                            f'data/images/{clothing_type}{idx}.jpg')
                        if os.path.exists(filepath):
                            ClothingItem(
                                profile=p,
                                brand=random.choice(brands),
                                color=random.choice(colors),
                                pattern=random.choice(pattern),
                                price=random.randint(500, 100000),
                                size=random.choice(sizes),
                                is_advertisable=random.choice([True,
                                                               False])).save()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )


class ClothingItem(models.Model):
    profile = models.ForeignKey(
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

    clothing_type = models.CharField(
        max_length=255,
        blank=True,
        default="",
        choices=(
            ("top", "top"),
            ("bottom", "bottom"),
            ("shoe", "shoe"),
        ))

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

    image = models.FileField(
        null = True,
        blank = True
    )


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

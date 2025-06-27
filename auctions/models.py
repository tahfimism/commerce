from django.contrib.auth.models import AbstractUser
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.name)



class Item(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=200, null=True)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    isopen = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="items", null=True)
    owner = models.ForeignKey('User', on_delete=models.CASCADE, related_name="owned_items")
    image = models.URLField(default="https://images.vexels.com/media/users/3/145641/isolated/preview/30bc99162bca69bdbd27451ceeef8848-earth-stone-illustration.png")

    def __str__(self):
        return f"{self.title}: owned by {self.owner}"


class User(AbstractUser):
    watchlist = models.ManyToManyField(Item, blank=True, related_name="watched_by")
    

    def __str__(self):
        return self.username



class Comment(models.Model):
    text = models.TextField(max_length=200)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="comments")
    like = models.PositiveIntegerField(default=0)
    by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", null=True)

    def __str__(self):
        return self.text



class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="bids")
    timestamp = models.DateTimeField(auto_now_add=True)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"{self.bidder} bids {self.amount}"


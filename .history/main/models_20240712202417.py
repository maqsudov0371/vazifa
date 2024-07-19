from django.db import models
from django.contrib.auth.models import  AbstractUser


class User(AbstractUser):
    img = models.ImageField(upload_to='avatar', null=True)
    bio = models.TextField(null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogs/')

    def __str__(self):
        return self.title
    


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username} -> {self.blog.title}"
    

from django.db import models
from django.contrib.auth.models import  AbstractUser


class User(AbstractUser):
    img = models.ImageField(upload_to='avatar', null=True)
    bio = models.TextField(null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Shop(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    background_img = models.ImageField()

    def __str__(self) -> str:
        return self.title


class Watches(models.Model):
    name = models.CharField(max_length=255)
    clock_type = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    detail = models.TextField()

    def __str__(self) -> str:
        return self.name

class WatchesImg(models.Model):
    img = models.ImageField()
    watch = models.ForeignKey(Watches, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.watch.name
    

# class Comment(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     blog = models.ForeignKey(Shop, on_delete=models.CASCADE)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.author.username} -> {self.blog.title}"
    

class Shop_Aboute(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    img = models.ImageField()

    def __str__(self) -> str:
        return self.title


class New_Aries(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    img = models.ImageField()

    def __str__(self) -> str:
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self) -> str:
        return self.name
    

class Info(models.Model):
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    informations = models.TextField()
    

    def __str__(self) -> str:
        return self.phone
    


class Appeal(models.Model):
    title = models.CharField(max_length=255)
    appeal =  models.TextField()

    
    
    


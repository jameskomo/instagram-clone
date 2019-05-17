from django.db import models
import datetime as dt 

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(default="defaultprofile.jpeg", upload_to = 'images/')
    bio = models.TextField(null=False)
    profile_name=models.CharField(max_length=60)
    # image_category =  models.ForeignKey(Image, on_delete=models.PROTECT)

    def __str__(self):
        return self.profile_name

class Image(models.Model):    
    image_name=models.CharField(max_length=60)
    image_caption = models.TextField()
    image_comments = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo_image = models.ImageField(default="default.jpeg", upload_to = 'images/')

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
    
    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

    class Meta:
        ordering = ['pub_date']    

    @classmethod
    def search_by_profile(cls,search_term):
        profiles = cls.objects.filter(profile__icontains=search_term)
        return profiles
    @classmethod
    def todays_images(cls,date):
        images = cls.objects.filter(pub_date__date = date)
        return images

    


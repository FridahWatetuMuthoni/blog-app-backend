from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile



User = get_user_model()

def get_first_user():
    return User.objects.first()

class Post(models.Model):
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    excerpt = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts',default=get_first_user)
    image = models.ImageField(upload_to='post_images/', blank=False , null=False)
    published = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # Compress the image
        if self.image:
            img = Image.open(self.image)
            output = BytesIO()
            
            # Resize/modify the image if necessary
            img = img.convert('RGB')  # Convert image to RGB color space if necessary
            img.save(output, format='JPEG', quality=85)  # Adjust quality as needed
            
            output.seek(0)
            self.image = InMemoryUploadedFile(output, 'ImageField', 
                                              f"{self.image.name.split('.')[0]}.jpg", 
                                              'image/jpeg', 
                                              output.tell, 
                                              None)

        super().save(*args, **kwargs)

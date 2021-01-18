from django.db import models


class Person(models.Model):
    SEX_CHOICES = (
        ('N', 'Not Selected'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    AGE_CHOICES = models.TextChoices('age choices', '10s- 20s 30s 40s 50s 60s+')
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='ERROR')
    age = models.CharField(blank=False, choices=AGE_CHOICES.choices, max_length=12)
    # db_table='blog_person'


'''
>>> p = Person(name="Fred Flintstone", shirt_size="L")
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'
'''


class Tag(models.Model):
    name = models.CharField(max_length=10, primary_key=True, unique=True)


class Post(models.Model):
    post_no = models.AutoField(primary_key=True)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(help_text="content of post")
    modified_date = models.DateTimeField('created or last modified date')
    published_date = models.DateTimeField()
    num_like = models.IntegerField()
    num_no = models.IntegerField()
    tags = models.ManyToManyField(Tag)


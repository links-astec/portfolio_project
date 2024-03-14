from django.db import models

class Project(models.Model):
    project_choices =[
      ('title','Title') ,
      ('description','Description'),
      ('credential','Credential') 
    ]

    title= models.CharField( max_length=50,default='action')
    description = models.TextField(null=True,blank=True)
    credential = models.URLField(null=False,blank=False)
     
     
    def __str__(self):
        return self.title
    





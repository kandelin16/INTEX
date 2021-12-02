from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Drugs(models.Model):
    #drugid=models.IntegerField()
    drugname = models.CharField(max_length=30)
    isopioid = models.CharField(max_length=5)
   
    class Meta:
        db_table= 'pd_drugs'
    
    def __str__(self):
        return (self.drugname)  #may need fixed

class Prescriber(models.Model):
    npi = models.IntegerField(unique=True)
    fname = models.CharField(max_length=11)
    lname = models.CharField(max_length=11)
    gender = models.CharField(max_length=1)
    state = models.CharField(max_length=2)
    specialty = models.CharField(max_length=62)
    isopioidprescriber = models.CharField(max_length=5)
    totalprescriptions = models.IntegerField()

    class Meta:
        db_table= 'pd_prescriber'
    
    def __str__(self):
        return (self.fname) + " " + (self.lname)  #may need fixed

class Credentials(models.Model):
    npi = models.IntegerField() #nned to be primary or foriegn?
    credentials = models.CharField(max_length=20)
    
    
    class Meta:
        db_table= 'pd_credentials'
    
    def __str__(self):
        return (self.credentials)  #may need fixed

class StateData(models.Model):
    stateabbrev = models.CharField(max_length=2) #may need to be primary key
    population = models.IntegerField()
    deaths = models.IntegerField()
    
    class Meta:
        db_table= 'pd_statedata'
    
    def __str__(self):
        return (self.stateabbrev)  #may need fixed

class StateAbbreviation(models.Model):
    stateabbrev = models.CharField(max_length=2)
    state = models.CharField(max_length=14) # may need to be primary and foreign key
    

    class Meta:
        db_table= 'pd_stateabbreviation'
    
    def __str__(self):
        return (self.state)  #may need fixed

class Triple(models.Model):
    id = models.IntegerField(primary_key=True) #may need to be removed-primary key
    prescriberid = models.ForeignKey(Prescriber, default="", on_delete= models.DO_NOTHING, to_field='npi')
    drugname = models.CharField(max_length=30)
    qty = models.IntegerField()
    
    
    class Meta:
        db_table= 'pd_triple'
    
    def __str__(self):
        return (self.drugname) #may need fixed
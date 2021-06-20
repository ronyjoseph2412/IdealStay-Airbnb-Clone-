from django.db import models

# Create your models here.
"""
 A class is created to save details of the users who want to contact us regarding any queries. 
 All basic details are taken from the user to resolve their query. 
"""
class contactus(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=13)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
"""
 A class is created to save details of the users who sign up for becoming a host. All basic details are taken from the user. 
"""
class hostus1(models.Model):
    firstnameh=models.CharField(max_length=122)
    lastnameh=models.CharField(max_length=122)    
    emailh=models.CharField(max_length=122)
    phoneh=models.CharField(max_length=13)
    addressh=models.TextField()
    stateh=models.CharField(max_length=13)
    pinh=models.CharField(max_length=7)
    date=models.DateField()
    def __str__(self):
        return self.firstnameh

''' A dedicated class is created in models.py  for each of the stays in the different cities to maintain database easily.
    All 18 classes for the stays created have same input parameters. Basic Details and a Reference-ID is generated and stored in the database.
    First Name of the user is shown in the database using __str__(self) FUNCTION inside the class.
 '''
# Classes are named according to the name of the places
class AryanHomestay(models.Model):
    firstname1=models.CharField(max_length=122)
    lastname1=models.CharField(max_length=122)    
    email1=models.CharField(max_length=122)
    phone1=models.CharField(max_length=13)
    adult1=models.CharField(max_length=13)
    child1=models.CharField(max_length=13)
    start1=models.DateField()
    end1=models.DateField()
    address1=models.TextField()
    state1=models.CharField(max_length=13)
    pin1=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname1

class CosyRoom(models.Model):
    firstname2=models.CharField(max_length=122)
    lastname2=models.CharField(max_length=122)    
    email2=models.CharField(max_length=122)
    phone2=models.CharField(max_length=13)
    adult2=models.CharField(max_length=13)
    child2=models.CharField(max_length=13)
    start2=models.DateField()
    end2=models.DateField()
    address2=models.TextField()
    state2=models.CharField(max_length=13)
    pin2=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname2

class BakshiHeritage(models.Model):
    firstname3=models.CharField(max_length=122)
    lastname3=models.CharField(max_length=122)    
    email3=models.CharField(max_length=122)
    phone3=models.CharField(max_length=13)
    adult3=models.CharField(max_length=13)
    child3=models.CharField(max_length=13)
    start3=models.DateField()
    end3=models.DateField()
    address3=models.TextField()
    state3=models.CharField(max_length=13)
    pin3=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname3

class paradise(models.Model):
    firstname4=models.CharField(max_length=122)
    lastname4=models.CharField(max_length=122)    
    email4=models.CharField(max_length=122)
    phone4=models.CharField(max_length=13)
    adult4=models.CharField(max_length=13)
    child4=models.CharField(max_length=13)
    start4=models.DateField()
    end4=models.DateField()
    address4=models.TextField()
    state4=models.CharField(max_length=13)
    pin4=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname4

class RiversedgeNest(models.Model):
    firstname5=models.CharField(max_length=122)
    lastname5=models.CharField(max_length=122)    
    email5=models.CharField(max_length=122)
    phone5=models.CharField(max_length=13)
    adult5=models.CharField(max_length=13)
    child5=models.CharField(max_length=13)
    start5=models.DateField()
    end5=models.DateField()
    address5=models.TextField()
    state5=models.CharField(max_length=13)
    pin5=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname5

class EdenHomestay(models.Model):
    firstname6=models.CharField(max_length=122)
    lastname6=models.CharField(max_length=122)    
    email6=models.CharField(max_length=122)
    phone6=models.CharField(max_length=13)
    adult6=models.CharField(max_length=13)
    child6=models.CharField(max_length=13)
    start6=models.DateField()
    end6=models.DateField()
    address6=models.TextField()
    state6=models.CharField(max_length=13)
    pin6=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname6

class Packiavilla(models.Model):
    firstname7=models.CharField(max_length=122)
    lastname7=models.CharField(max_length=122)    
    email7=models.CharField(max_length=122)
    phone7=models.CharField(max_length=13)
    adult7=models.CharField(max_length=13)
    child7=models.CharField(max_length=13)
    start7=models.DateField()
    end7=models.DateField()
    address7=models.TextField()
    state7=models.CharField(max_length=13)
    pin7=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname7

class RestelStudio(models.Model):
    firstname8=models.CharField(max_length=122)
    lastname8=models.CharField(max_length=122)    
    email8=models.CharField(max_length=122)
    phone8=models.CharField(max_length=13)
    adult8=models.CharField(max_length=13)
    child8=models.CharField(max_length=13)
    start8=models.DateField()
    end8=models.DateField()
    address8=models.TextField()
    state8=models.CharField(max_length=13)
    pin8=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname8
    
class UrbanNest(models.Model):
    firstname9=models.CharField(max_length=122)
    lastname9=models.CharField(max_length=122)    
    email9=models.CharField(max_length=122)
    phone9=models.CharField(max_length=13)
    adult9=models.CharField(max_length=13)
    child9=models.CharField(max_length=13)
    start9=models.DateField()
    end9=models.DateField()
    address9=models.TextField()
    state9=models.CharField(max_length=13)
    pin9=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname9

class WalnutCottage(models.Model):
    firstname10=models.CharField(max_length=122)
    lastname10=models.CharField(max_length=122)    
    email10=models.CharField(max_length=122)
    phone10=models.CharField(max_length=13)
    adult10=models.CharField(max_length=13)
    child10=models.CharField(max_length=13)
    start10=models.DateField()
    end10=models.DateField()
    address10=models.TextField()
    state10=models.CharField(max_length=13)
    pin10=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname10

class Shambhal(models.Model):
    firstname11=models.CharField(max_length=122)
    lastname11=models.CharField(max_length=122)    
    email11=models.CharField(max_length=122)
    phone11=models.CharField(max_length=13)
    adult11=models.CharField(max_length=13)
    child11=models.CharField(max_length=13)
    start11=models.DateField()
    end11=models.DateField()
    address11=models.TextField()
    state11=models.CharField(max_length=13)
    pin11=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname11

class Bellevue(models.Model):
    firstname12=models.CharField(max_length=122)
    lastname12=models.CharField(max_length=122)    
    email12=models.CharField(max_length=122)
    phone12=models.CharField(max_length=13)
    adult12=models.CharField(max_length=13)
    child12=models.CharField(max_length=13)
    start12=models.DateField()
    end12=models.DateField()
    address12=models.TextField()
    state12=models.CharField(max_length=13)
    pin12=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname12

class BirTerraces(models.Model):
    firstname13=models.CharField(max_length=122)
    lastname13=models.CharField(max_length=122)    
    email13=models.CharField(max_length=122)
    phone13=models.CharField(max_length=13)
    adult13=models.CharField(max_length=13)
    child13=models.CharField(max_length=13)
    start13=models.DateField()
    end13=models.DateField()
    address13=models.TextField()
    state13=models.CharField(max_length=13)
    pin13=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname13

class ThinlayHomestay(models.Model):
    firstname14=models.CharField(max_length=122)
    lastname14=models.CharField(max_length=122)    
    email14=models.CharField(max_length=122)
    phone14=models.CharField(max_length=13)
    adult14=models.CharField(max_length=13)
    child14=models.CharField(max_length=13)
    start14=models.DateField()
    end14=models.DateField()
    address14=models.TextField()
    state14=models.CharField(max_length=13)
    pin14=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname14

class ShumbukHomes(models.Model):
    firstname15=models.CharField(max_length=122)
    lastname15=models.CharField(max_length=122)    
    email15=models.CharField(max_length=122)
    phone15=models.CharField(max_length=13)
    adult15=models.CharField(max_length=13)
    child15=models.CharField(max_length=13)
    start15=models.DateField()
    end15=models.DateField()
    address15=models.TextField()
    state15=models.CharField(max_length=13)
    pin15=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname15

class OrchidGlade(models.Model):
    firstname16=models.CharField(max_length=122)
    lastname16=models.CharField(max_length=122)    
    email16=models.CharField(max_length=122)
    phone16=models.CharField(max_length=13)
    adult16=models.CharField(max_length=13)
    child16=models.CharField(max_length=13)
    start16=models.DateField()
    end16=models.DateField()
    address16=models.TextField()
    state16=models.CharField(max_length=13)
    pin16=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname16

class HeavotCaves(models.Model):
    firstname17=models.CharField(max_length=122)
    lastname17=models.CharField(max_length=122)    
    email17=models.CharField(max_length=122)
    phone17=models.CharField(max_length=13)
    adult17=models.CharField(max_length=13)
    child17=models.CharField(max_length=13)
    start17=models.DateField()
    end17=models.DateField()
    address17=models.TextField()
    state17=models.CharField(max_length=13)
    pin17=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname17

class VillaC(models.Model):
    firstname18=models.CharField(max_length=122)
    lastname18=models.CharField(max_length=122)    
    email18=models.CharField(max_length=122)
    phone18=models.CharField(max_length=13)
    adult18=models.CharField(max_length=13)
    child18=models.CharField(max_length=13)
    start18=models.DateField()
    end18=models.DateField()
    address18=models.TextField()
    state18=models.CharField(max_length=13)
    pin18=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname18

'''
For each experience a indiviual booking gateway is maintained. Therefore six different classes are created to cater each of the experience.
In each class, we collect Basic Details and along with it a Reference-ID is generated to help the user with their booking.
'''

class booktr(models.Model):
    firstname19=models.CharField(max_length=122)
    lastname19=models.CharField(max_length=122)    
    email19=models.CharField(max_length=122)
    phone19=models.CharField(max_length=13)
    adult19=models.CharField(max_length=13)
    child19=models.CharField(max_length=13)
    start19=models.DateField()
    address19=models.TextField()
    state19=models.CharField(max_length=13)
    pin19=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname19

class bookdb(models.Model):
    firstname20=models.CharField(max_length=122)
    lastname20=models.CharField(max_length=122)    
    email20=models.CharField(max_length=122)
    phone20=models.CharField(max_length=13)
    adult20=models.CharField(max_length=13)
    child20=models.CharField(max_length=13)
    start20=models.DateField()
    address20=models.TextField()
    state20=models.CharField(max_length=13)
    pin20=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname20

class booknz(models.Model):
    firstname21=models.CharField(max_length=122)
    lastname21=models.CharField(max_length=122)    
    email21=models.CharField(max_length=122)
    phone21=models.CharField(max_length=13)
    adult21=models.CharField(max_length=13)
    child21=models.CharField(max_length=13)
    start21=models.DateField()
    address21=models.TextField()
    state21=models.CharField(max_length=13)
    pin21=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname21

class bookp(models.Model):
    firstname22=models.CharField(max_length=122)
    lastname22=models.CharField(max_length=122)    
    email22=models.CharField(max_length=122)
    phone22=models.CharField(max_length=13)
    adult22=models.CharField(max_length=13)
    child22=models.CharField(max_length=13)
    start22=models.DateField()
    address22=models.TextField()
    state22=models.CharField(max_length=13)
    pin22=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname22

class bookgr(models.Model):
    firstname23=models.CharField(max_length=122)
    lastname23=models.CharField(max_length=122)    
    email23=models.CharField(max_length=122)
    phone23=models.CharField(max_length=13)
    adult23=models.CharField(max_length=13)
    child23=models.CharField(max_length=13)
    start23=models.DateField()
    address23=models.TextField()
    state23=models.CharField(max_length=13)
    pin23=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname23

class booksw(models.Model):
    firstname24=models.CharField(max_length=122)
    lastname24=models.CharField(max_length=122)    
    email24=models.CharField(max_length=122)
    phone24=models.CharField(max_length=13)
    adult24=models.CharField(max_length=13)
    child24=models.CharField(max_length=13)
    start24=models.DateField()
    address24=models.TextField()
    state24=models.CharField(max_length=13)
    pin24=models.CharField(max_length=7)
    refid=models.IntegerField("",default=0)
    def __str__(self):
        return self.firstname24

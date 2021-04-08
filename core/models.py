from django.db import models

# Create your models here.
GENDER_CHOICE =(
    ('M','Male'),
    ('F','Female'),
    ('O','Others'),
)
BLOOD_GROUP_CHOICE =(
    ('A+','A+'),
    ('B+','B+'),
    ('AB+','AB+'),
    ('O+','O+'),
    ('A-','A-'),
    ('B-','B-'),
    ('AB-','AB-'),
    ('O-','O-'),
)
DISTRICT_CHOICE =(
    ('Kathmandu','Kathmandu'),
    ('Bhaktapur','Bhaktapur'),
    ('Lalitpur','Lalitpur'),
    ('Banepa','Banepa'),
    ('Bardia','Bardia'),
)
RELATION_CHOICE =(
    ('Father','Father'),
    ('Mother','Mother'),
    ('Spouse','Spouse'),
)
ZONE_CHOICE =(
    ('Bagmati','Bagmati'),
    ('Narayani','Narayani'),
    ('Lumbini','Lumbini'),
    ('Gandaki','Gandaki'),
    ('Janakpur','Janakpur'),
)
CATEGORY_CHOICE =(
    ('A','A-Motercycle,Scooter,Moped'),
    ('C','C-Tempo,Autorickshaw'),
    ('D','D-Powertiler'),
    ('E','E-Tractor,Trailer'),
    ('K','K-Scooter,Moped'),
)
S_ZONE_CHOICE =(
    ('Bagmati','Bagmati'),
)
L_ISSUE_OFFICE_CHOICE =(
    ('Bhaktapur','Jagati-Bhaktapur'),
    ('T_Kathmandu','Thulobharyand-Kathmandu'),
    ('C_Kathmandu','Chabahil-Kathmandu'),
    ('Lalitpur','Ekantakunna-Lalitpur'),
)

class PersonalDetail(models.Model):
    f_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100, null=False, blank=True)
    l_name = models.CharField(max_length=100)
    dob = models.DateField()
    
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICE, max_length=6 ,null=True)
    b_group = models.CharField(choices= BLOOD_GROUP_CHOICE, max_length=3 ,null=True)
    education = models.CharField(max_length=100, null=True)
    citizenship_no = models.IntegerField(unique=True, null=True)
    citizenship_issue_district = models.CharField(choices=DISTRICT_CHOICE, max_length=10 ,null=True)
    w_f_name = models.CharField(max_length=100, null=True)
    w_m_name = models.CharField(max_length=100, null=False, blank=True)
    w_l_name = models.CharField(max_length=100, null=True)
    w_relationship = models.CharField(choices=RELATION_CHOICE, max_length=6 ,null=True)

    def __str__(self):
        return self.f_name

#Address details models
class AddressDetail(models.Model):
    p_detail = models.ForeignKey(PersonalDetail, on_delete=models.CASCADE, null=True)
    zone = models.CharField(choices= ZONE_CHOICE, max_length=10 ,null=True)
    district = models.CharField(choices= DISTRICT_CHOICE, max_length=23 ,null=True)
    village = models.CharField(max_length=100, null=True)
    ward_no = models.IntegerField()
    contact_no = models.IntegerField()
    email = models.EmailField()
    l_category = models.CharField(choices=CATEGORY_CHOICE , max_length=26 ,null=True)
    s_zone = models.CharField(choices= S_ZONE_CHOICE, max_length=10 ,null=True)
    l_issue_office = models.CharField(choices= L_ISSUE_OFFICE_CHOICE, max_length=23 ,null=True)


    def __str__(self):
        return self.email
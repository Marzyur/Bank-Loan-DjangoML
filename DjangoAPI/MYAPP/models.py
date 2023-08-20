from django.db import models

# Create your models here.
class Approval(models.Model):
    GENDER_CHOICES=(
        ('Male','Male'),
        ('Female','Female')
    )
    MARRIED_CHOICES=(
        ('Yes','Yes'),
        ('No','No')
    )
    GRADUATEEDUCATION=(
        ('Graduate','Graduate'),
        ('Not_Graduate','Not_graduate')
    )
    SELFEMPLOYED_CHOICES=(
        ('Yes','Yes'),
        ('No','No')
    )
    PROPERTY_CHOICES=(
        ('Rural','Rural'),
        ('SemiUrban','Semiurban'),
        ('Urban','Urban')
    )
    Gender=models.CharField(max_length=15,choices=GENDER_CHOICES)
    Dependents=models.IntegerField()
    ApplicantIncome=models.IntegerField()
    CoapplicantIncome = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    LoanAmount=models.IntegerField()
    Loan_Amount_Term=models.IntegerField()
    Credit_History=models.IntegerField()
    Married=models.CharField(max_length=15,choices=MARRIED_CHOICES)
    Education=models.CharField(max_length=15,choices=GRADUATEEDUCATION)
    Self_Employed=models.CharField(max_length=15,choices=SELFEMPLOYED_CHOICES)
    Property_Area=models.CharField(max_length=15,choices=PROPERTY_CHOICES)
def __str__(self):
    return f"self.firstname,self.lastname"

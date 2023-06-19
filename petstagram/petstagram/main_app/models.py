import datetime

from django.db import models
from django.core.validators import MinLengthValidator
from .validators import only_letters_validator, ValidateFileMaxSizeInMB, atleastOnePet


# Create your models here.
class Profile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDERS = [(x,x) for x in (MALE,FEMALE,DO_NOT_SHOW)]
    FIRST_NAME_MAX_LENGHT=30
    LAST_NAME_MAX_LENGHT = 30
    FIRST_NAME_MIN_LENGHT = 2
    LAST_NAME_MIN_LENGHT = 2
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGHT,
                                  validators=[
                                      MinLengthValidator(FIRST_NAME_MIN_LENGHT,'first name must be between 2 and 30'),
                                      only_letters_validator],
                                  )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGHT,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGHT, 'last name must be between 2 and 30'),
            only_letters_validator,
        ],
    )
    picture = models.URLField()
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=max(len(gender) for gender,_ in GENDERS),
        null=True,
        blank=True,
        choices=GENDERS,
        default=DO_NOT_SHOW,
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name} Profile"
class Pet(models.Model):
    #Constans
    NAME_MAX_LENGHT=30
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH='Fish'
    OTHER = 'Other'
    TYPES=[(x,x) for x in (CAT,DOG,BUNNY,PARROT,FISH,OTHER)]

    #Columns
    name =models.CharField(
        max_length=NAME_MAX_LENGHT,

    )
    type = models.CharField(
        max_length=max(len(type) for (type,_) in TYPES),
        choices=TYPES,

    )
    #optional
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    #One-to-one Relation

    # One-to-many Relations

    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # Many-to_many Relations

    #Properties
    @property
    def age(self):
        if self.date_of_birth:
            return datetime.datetime.now().year-self.date_of_birth.year
        return None
    #Methods

    #dunder methods
    def __str__(self):
        return f'{self.name}'
    #Meta

    class Meta:
        unique_together=('user_profile','name')



class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            ValidateFileMaxSizeInMB(5),
        )
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        #validators=[atleastOnePet]
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    date_of_publication = models.DateTimeField(
        auto_now_add=True
    )
    likes = models.IntegerField(
        default=0
    )
    def __str__(self):
        return f"Photo on {self.tagged_pets.name}"

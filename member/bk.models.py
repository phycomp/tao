from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#from django.contrib.auth.models import User
#from django.contrib.auth.admin import UserAdmin
from django.db.models import Model, OneToOneField, CharField, EmailField, FloatField, BooleanField, DateField, CASCADE

#class Member(Model):
class MemberManager(BaseUserManager):
    """ Creates and saves a User with the given email and password.  """
    def _create_user(self, identifier, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not identifier: raise ValueError('The identifier must be set')
        #email = self.normalize_email(email)
        user = self.model(identifier=identifier, is_staff=is_staff, is_active=True, \
                is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Member(AbstractBaseUser, PermissionsMixin):
    identifier = CharField(max_length=40, unique=True)
    email=EmailField()
    address = CharField(max_length=100)
    birthday = DateField()
    height = FloatField()
    weight = FloatField()
    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    objects = MemberManager()
    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['birthday', 'height']
    def create_user(self, identifier, password=None):
        """ Creates and saves a User with the given email, date of birth and password.  """
        if not identifier: raise ValueError('Users must have an identifier')
        user = self.model(identifier=identifier, date_of_birth=date_of_birth,)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, identifier, password):
        """ Creates and saves a superuser with the given email, date of birth and password.  """
        user = self.create_user( identifier, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class MemberAdmin(UserAdmin):
    play = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Personal info', {'fields': ('date_of_birth',)}),
            ('Permissions', {'fields': ('is_admin',)}),
    )
            # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
            # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, { 'classes': ('wide',),
        'fields': ('email', 'date_of_birth', 'password1', 'password2')}
        ),
    )
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
'''
class Member(AbstractBaseUser, PermissionsMixin):
    #user = OneToOneField(User, on_delete=CASCADE)
    identifier = CharField(max_length=40, unique=True)
    department = CharField(max_length=100)
    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['birthday', 'height']
'''

from django.db.models import CharField, EmailField, DateField, BooleanField, FloatField, PositiveSmallIntegerField, DateTimeField, ManyToManyField, Model
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import site, ModelAdmin
from random import choices

class MemberManager(BaseUserManager):
	def create_user(self, identifier, password, **kwargs):
		if not identifier: raise ValueError('User must have an identifier')
		#email, cellular=kwargs.get('email'), kwargs.get('cellular')
		#user = self.model(identifier=identifier, cellular=cellular, **kwargs)
		user = self.model(identifier=identifier, **kwargs)
		user.set_password(password)
		user.save(using=self._db)
		media=user.user_medium.create(isAvatar=True)
		return user
	def create_superuser(self, identifier, password):
		""" Creates and saves a superuser with the given email, date of birth and password.  """
		email=choices('abcdefghijklmnopqrsturvxyzABCDEFGHIJKLMNOPQRSTURVXYZ', k=8)
		email=''.join(email)
		cellular=choices('0123456789', k=9)
		cellular='0'+''.join(cellular)
		user = self.create_user(identifier, password, email=email, cellular=cellular)	#, email=password)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Member(AbstractBaseUser, PermissionsMixin):
	identifier=CharField(_('identifier'), max_length=15, unique=True)
	last_name=CharField(_('last_name'), max_length=40)
	first_name=CharField(_('first_name'), max_length=40)
	nickname=CharField(_('nickname'), max_length=10)
	email=EmailField(_('email address'), max_length=80, unique=True)
	birthday=DateField(null=True)
	cellular=CharField(default='0911111111', unique=True, max_length=15)
	address=CharField(max_length=100, blank=True)
	#avatar=ManyToManyField(Medium, related_name='avatar_member')
	height=FloatField(null=True)
	weight=FloatField(null=True)
	is_active=BooleanField(default=True)
	is_staff=BooleanField(default=False)
	is_saint=BooleanField(default=False)
	timestamp=DateTimeField(_('timestamp'), auto_now=True)
	objects=MemberManager()
	USERNAME_FIELD='identifier'
	#REQUIRED_FIELDS = ['date_of_birth']
	def __str__(self): return self.identifier
	class Meta: db_table='member'
	@property
	def full_name(self): return ' '.join([self.first_name, self.last_name]) if self.first_name or self.last_name else ''	

'''
site.register(Member, MemberAdmin)
from django.contrib.auth.admin import UserAdmin
	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True
	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		return True
	@property
	def is_staff(self):
		"Is the user a member of staff?"
		return self.is_admin
'''

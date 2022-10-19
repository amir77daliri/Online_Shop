from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

	def create_user(self, phone_number, password, email=None , first_name=None, last_name=None):
		if not phone_number:
			raise ValueError('user must have phone number')
		user = self.model(
			phone_number=phone_number,
			email=email,
			first_name=first_name,
			last_name=last_name)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, phone_number, password, email=None, first_name=None, last_name=None):
		user = self.create_user(phone_number, password, email=email, first_name=first_name, last_name=last_name)
		user.is_admin = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

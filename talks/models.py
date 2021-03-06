from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify



# Create your models here.
class TalkList(models.Model):
	user = models.ForeignKey(User, related_name='lists')
	name = models.CharField(max_length=225)
	slug = models.SlugField(max_length=225, null=True)

	class Meta:
		unique_together= ('user', 'name')

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(TalkList, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('talks:lists:detail', kwargs ={'slug':self.slug })
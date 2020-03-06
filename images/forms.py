"""Forms image app."""
from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
    """Form foe Image model."""

    class Meta:
        """Meta information."""

        model = Image
        fields = ('title', 'url', 'description')
        widgets = {'url': forms.HiddenInput, }

    def clean_url(self):
        """Url field validation."""
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError(
                'Данный URL не соответствует \
                действительным расширениям изображений.')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        """Override save method."""
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(
            slugify(image.title), image_url.rsplit('.', 1)[1].lower())
        # Скачиваем изображение по указанному адресу.
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()
        return image

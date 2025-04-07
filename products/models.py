from django.db import models

from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('Parent Category'), on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(_('Title'), max_length=50)
    description = models.TextField(_('Description'), blank=True, null=True)
    avatar = models.ImageField(_('Avatar'), upload_to='categories/', blank=True, null=True)
    is_enable = models.BooleanField(_('Is Enable'), default=True)
    created_time = models.DateTimeField(_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated Time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    description = models.TextField(_('Description'), blank=True, null=True)
    avatar = models.ImageField(_('Avatar'), upload_to='products/', blank=True, null=True)
    is_enable = models.BooleanField(_('Is Enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated Time'), auto_now=True)
    url = models.URLField(_('URL'), blank=True, null=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title


class File(models.Model):
    product = models.ForeignKey('Product', verbose_name=_('Product'), related_name='files', on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=50)
    file = models.FileField(_('File'), upload_to='files/%y/%m/%d/', blank=True, null=True)
    is_enable = models.BooleanField(_('Is Enable'), default=True)
    file_type = models.CharField(_('File Type'), max_length=50, blank=True, null=True)
    created_time = models.DateTimeField(_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated Time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')

    def __str__(self):
        return self.title
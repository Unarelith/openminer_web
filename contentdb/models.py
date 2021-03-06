from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class EngineVersion(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    date = models.DateTimeField(default=timezone.now)

    windows_url = models.URLField(blank=True, null=True)
    linux_url = models.URLField(blank=True, null=True)
    macos_url = models.URLField(blank=True, null=True)

    windows_zip = models.FileField(verbose_name="Windows ZIP", max_length=1000, blank=True, null=True)
    linux_zip = models.FileField(verbose_name="Linux ZIP", max_length=1000, blank=True, null=True)
    macos_zip = models.FileField(verbose_name="macOS ZIP", max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = "Engine version"
        ordering = ['date']

    def __str__(self):
        return "OpenMiner v" + self.name

class Mod(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="mods", null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Mod"
        ordering = ['name']

    def __str__(self):
        return self.name

class ModVersion(models.Model):
    mod = models.ForeignKey(Mod, on_delete=models.CASCADE, related_name="versions")
    name = models.CharField(max_length=20, null=False)
    date = models.DateTimeField(default=timezone.now)

    file_url = models.URLField(null=True, blank=True)
    file_zip = models.FileField(verbose_name="File", max_length=1000, null=True, blank=True);

    class Meta:
        verbose_name = "Mod version"
        ordering = ['date']
        unique_together = ('mod', 'name')

    def __str__(self):
        return self.mod.name + " " + self.name

class TexturePack(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="texture_packs", null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Texture pack"
        ordering = ['name']

    def __str__(self):
        return self.name

class TexturePackVersion(models.Model):
    texture_pack = models.ForeignKey(TexturePack, on_delete=models.CASCADE, related_name="versions")
    name = models.CharField(max_length=20, null=False)
    date = models.DateTimeField(default=timezone.now)

    file_url = models.URLField(null=True, blank=True)
    file_zip = models.FileField(verbose_name="File", max_length=1000, null=True, blank=True);

    class Meta:
        verbose_name = "Texture pack version"
        ordering = ['date']
        unique_together = ('texture_pack', 'name')

    def __str__(self):
        return self.texture_pack.name + " " + self.name


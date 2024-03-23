from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')


class ComparisonResult(models.Model):
    image1 = models.ForeignKey(
        Image, related_name='image1_comparisons', on_delete=models.CASCADE)
    image2 = models.ForeignKey(
        Image, related_name='image2_comparisons', on_delete=models.CASCADE)
    preferred_image = models.ForeignKey(
        Image, related_name='preferred_comparisons', on_delete=models.CASCADE)

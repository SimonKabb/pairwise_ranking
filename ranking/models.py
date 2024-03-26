from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='ranking/')
    points = models.IntegerField(default=0)


class ComparisonResult(models.Model):
    image1 = models.ForeignKey(
        Image, related_name='comparison_image1', on_delete=models.CASCADE)
    image2 = models.ForeignKey(
        Image, related_name='comparison_image2', on_delete=models.CASCADE)
    winner = models.ForeignKey(
        Image, related_name='comparison_winner', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comparison between {self.image1} and {self.image2}, winner: {self.winner}"

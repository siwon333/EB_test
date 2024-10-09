from django.db import models

class DetectedObject(models.Model):
    object_name = models.CharField(max_length=100)  # 감지된 객체 이름
    timestamp = models.DateTimeField(auto_now_add=True)  # 감지 시간

    def __str__(self):
        return self.object_name

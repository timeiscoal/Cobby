from django.db import models
import os
from django.conf import settings



# 221018 최해민 막걸리 모델 추가
class Makgeolli(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='makgeolli/', blank=True, null=True)
    desc = models.TextField()
    
    # 221018 최해민 막걸리 객체 삭제하면, media파일도 삭제
    def delete(self, *args, **kwargs):
        super(Makgeolli, self).delete(*args, **kwargs)
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
    
    def __str__(self):
        return str(self.name)

# 221019 사용자가 막걸리 사진을 업로드 하는 기능. 
class Cobby(models.Model):
    image = models.ImageField(blank=True , null=True, upload_to='cobby/')
    name = models.CharField(max_length=1)

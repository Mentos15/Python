from django.db import models


class PhoneCatalog(models.Model):
    Name = models.CharField(max_length=255)
    RegDate = models.DateField(auto_now_add=True)
    Adress = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    def __str__(self):
        return "Имя:"+self.Name+"\tДата регистрации:"+str(self.RegDate)+"\tАдрес:"+self.Adress+"\tТелефон:"+self.Phone

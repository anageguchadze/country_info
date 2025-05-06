from django.db import models


class Country(models.Model):
    '''მონაცემები ქვეყნების შესახებ: თითოეული ქვეყნისთვის უნდა იყოს განსაზღვრული დედაქალაქი, 
    მოსახლეობა, ფართობი და ოფიციალური ენები. ასევე წამოიღეთ ისეთი გეოგრაფიული მონაცემები, 
    როგორიცაა: კონტინენტი, მთავარი ქალაქები, კლიმატი და სხვა. დამატებით შეგიძლიათ 
    წამოიღოთ ქვეყანაზე ისეთი ინფორმაცია, როგორიცაა: GDP, ვალუტა და სხვა.'''
    name = models.CharField(max_length=255)
    capital_city = models.CharField(max_length=255)
    population = models.FloatField()
    area = models.FloatField()
    official_languages = models.CharField(max_length=255)
    continent = models.CharField(max_length=255)
    main_cities = models.CharField(max_length=255)
    climate = models.CharField(max_length=255)
    gdp = models.FloatField()
    currency = models.CharField(max_length=255)

    def __str__(self):
        return self.name
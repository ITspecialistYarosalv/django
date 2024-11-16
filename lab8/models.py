from django.db import models

class Client(models.Model):

    client_id = models.AutoField(primary_key=True)
    client_type = models.CharField(max_length=15,)
    address = models.CharField(max_length=255)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'clients'

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

class Phone(models.Model):
    phone_number = models.CharField(max_length=15,primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='phones')

    class Meta:
        managed = False
        db_table = "phones"


    def __str__(self):
        return f"{self.phone_number} ({self.client.last_name} {self.client.first_name})"
class Tariff(models.Model):
    tariff_id = models.AutoField(primary_key=True)  # Код тарифу
    call_type = models.CharField(max_length=50)  # Тип дзвінка (наприклад, місцевий, міжнародний)
    cost_per_minute = models.DecimalField(max_digits=6, decimal_places=2)  # Вартість 1 хвилини розмови

    class Meta:
        managed = False
        db_table = 'tariffs'

    def __str__(self):
        return f"Tariff {self.tariff_code} - {self.call_type} at {self.cost_per_minute} per minute"

class Call(models.Model):
    call_id= models.AutoField(primary_key=True)  # Код розмови
    call_date = models.DateTimeField()  # Дата розмови
    phone_number = models.CharField(max_length=15)  # Зв'язок з телефоном
    duration_minutes = models.IntegerField()  # Кількість хвилин розмови
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE, related_name='calls')

    class Meta:
        managed = False
        db_table = 'calls'

    def __str__(self):
        return f"Call {self.call_code} on {self.date}"



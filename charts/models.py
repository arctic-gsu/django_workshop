from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass

class Chart(models.Model):
    name = models.CharField(max_length=100)
    report_date = models.DateField()
    csv_data = models.TextField()
    
    def get_chart_data(self) -> dict:
    
        output = {} # need an empty dict to start
        header_string = self.csv_data.splitlines()[0] # Grab first row of data as string
        headers = header_string.split(',')[:-1] # split the row at , and remove AsOf from the list
        for header in headers:
            output[header]=[]

        data = self.csv_data.splitlines()[1:] # takes from the 2nd row to the end
        for row in data:
            row_data = row.split(',')[:-1] # need to drop the AsOf Column
             # idx will iterate from 0 to 3
            for idx, key in enumerate(output.keys()):
                output[key].append(row_data[idx])

        return output

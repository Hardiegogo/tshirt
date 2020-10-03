from django.db import migrations
from API.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="Chirag", email="chirag.gps@gmail.com",is_staff=True,is_superuser=True,phone="987654321", gender="Male")
        

        user.set_password("12345")
        user.save()
        

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
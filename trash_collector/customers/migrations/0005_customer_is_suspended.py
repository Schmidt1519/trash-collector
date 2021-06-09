from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20210607_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_suspended',
            field=models.BooleanField(default=False),
        ),
    ]

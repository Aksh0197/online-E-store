# Generated by Django 2.1.5 on 2019-02-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0005_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=300)),
                ('productid', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.0.1 on 2022-05-28 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_remove_t_address_adr_shipto_remove_t_address_c_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_request',
            name='Admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Admin_Request', to='Accounts.t_user'),
        ),
    ]

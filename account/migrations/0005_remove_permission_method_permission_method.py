# Generated by Django 4.2.1 on 2023-07-16 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0004_permission_method_role_permission_alter_user_role_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="permission",
            name="method",
        ),
        migrations.AddField(
            model_name="permission",
            name="method",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="account.method"
            ),
        ),
    ]

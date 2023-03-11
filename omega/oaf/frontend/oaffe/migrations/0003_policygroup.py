# Generated by Django 4.1.7 on 2023-03-11 18:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("oaffe", "0002_alter_policyevaluationresult_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PolicyGroup",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=1024)),
                ("policies", models.ManyToManyField(to="oaffe.policy")),
            ],
        ),
    ]

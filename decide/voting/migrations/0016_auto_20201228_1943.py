# Generated by Django 2.0 on 2020-12-28 19:43

from django.db import migrations, models
import django.db.models.deletion


def inserta_datos(apps, schema_editor):
    fields = ['IDENTITY', 'BORDA', 'HONDT', 'EQUALITY', 'SAINTE_LAGUE', 'DROOP', 'IMPERIALI', 'HARE']
    TypeVoting = apps.get_model("voting", "TypeVoting")

    for f in fields:
        t = TypeVoting(name=f)
        t.save()


class Migration(migrations.Migration):
    dependencies = [
        ('voting', '0015_auto_20201226_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeVoting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='voting',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='voting',
                                    to='voting.TypeVoting'),
            preserve_default=False,
        ),
        migrations.RunPython(inserta_datos)
    ]

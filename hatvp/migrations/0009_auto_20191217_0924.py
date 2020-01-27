# Generated by Django 3.0 on 2019-12-17 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hatvp', '0008_action_beneficiary_decision_domain_field_observation_target'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'Activities'},
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='representant',
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='action',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hatvp.Action', verbose_name='action_representation_interet_id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='name',
            field=models.CharField(max_length=128, verbose_name='beneficiaire_action_menee'),
        ),
    ]

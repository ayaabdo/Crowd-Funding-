# Generated by Django 3.1.7 on 2021-03-27 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('project_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundraising.project')),
            ],
        ),
        migrations.CreateModel(
            name='ReportAProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('project_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundraising.project')),
            ],
        ),
        migrations.CreateModel(
            name='ReportAComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('comment_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundraising.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_users', models.IntegerField()),
                ('individual_rate', models.IntegerField()),
                ('total_rate', models.FloatField()),
                ('overall_avg_rating', models.FloatField()),
                ('proj_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundraising.project')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.FileField(max_length=255, upload_to='')),
                ('proj_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundraising.project')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_of_donation', models.FloatField()),
                ('project_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundraising.project')),
            ],
        ),
    ]
# Generated by Django 4.2.7 on 2024-02-10 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('year', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='IMUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('user_type', models.CharField(choices=[('EIT', 'EIT'), ('TEACHING_FELLOW', 'Teaching Fellow'), ('ADMIN_STAFF', 'Admin Staff'), ('ADMIN', 'Admin')], max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CohortMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_cohort_members', to='users.imuser')),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cohorts', to='users.cohort')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='users.imuser')),
            ],
        ),
        migrations.AddField(
            model_name='cohort',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_cohorts', to='users.imuser'),
        ),
    ]
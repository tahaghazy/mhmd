# Generated by Django 3.0.9 on 2021-01-17 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='عنوان المشروع')),
                ('cat', models.CharField(help_text='قم باختيار نوع التصميم لوجو او بانر ...الخ', max_length=100, verbose_name='نوع المشروع')),
                ('client', models.CharField(max_length=1000, verbose_name='العميل/الزبون')),
                ('skills', models.CharField(max_length=1000, verbose_name='المهارات المستخدمه')),
                ('link', models.URLField(blank=True, null=True, verbose_name='رابط المشروع ان وجد')),
                ('file', models.ImageField(help_text='قم باختيار صورة التصميم من جهازك', upload_to='', verbose_name='ملف المشروع')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, editable=False, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'مشروع ',
                'verbose_name_plural': 'المشاريع/Portfolio',
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='langages',
            field=models.CharField(max_length=50, verbose_name='اللغات'),
        ),
    ]

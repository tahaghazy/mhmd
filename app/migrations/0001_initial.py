# Generated by Django 3.0.9 on 2021-01-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='الاسم الأول')),
                ('last_name', models.CharField(max_length=50, verbose_name='الاسم الأخير')),
                ('phone', models.CharField(max_length=15, verbose_name='رقم الهاتف ')),
                ('email', models.EmailField(max_length=254, verbose_name='البريد الالكتروني')),
                ('age', models.IntegerField(default=0, verbose_name='العمر')),
                ('content', models.TextField(help_text='من انت ؟!', verbose_name='الوصف')),
                ('address', models.CharField(max_length=10000, verbose_name='العنوان')),
                ('nationality', models.CharField(max_length=50, verbose_name='الجنسيه')),
                ('langages', models.CharField(max_length=50, verbose_name='الاسم الأخير')),
                ('exp', models.IntegerField(default=0, verbose_name='سنين الخبره')),
                ('projects', models.IntegerField(default=0, verbose_name='المشاريع المكتمله')),
                ('image', models.ImageField(default='img-mobile.jpg', help_text='يفضل ان تكون بحجم 300x300', upload_to='profile_pics', verbose_name='صورة الملف الشخصي')),
            ],
            options={
                'verbose_name': 'الملف الشخصي',
                'verbose_name_plural': 'الملف الشخصي',
            },
        ),
    ]

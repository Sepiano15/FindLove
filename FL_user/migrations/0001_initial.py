# Generated by Django 2.0.13 on 2020-05-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(max_length=6, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='아이디')),
                ('password', models.CharField(default=0, max_length=100, verbose_name='비밀번호')),
                ('name', models.CharField(max_length=30, verbose_name='이름')),
                ('stdnum', models.IntegerField(default=0, verbose_name='학번')),
                ('age', models.IntegerField(default=0, verbose_name='나이')),
                ('hobby', models.IntegerField(choices=[(0, '선택하기'), (1, '영화보기'), (2, '게임'), (3, '맛집 탐방'), (4, '운동'), (5, '음악 감상')], default=0, verbose_name='취미')),
                ('height', models.IntegerField(default=0, verbose_name='키')),
                ('weight', models.IntegerField(choices=[(0, '선택하기'), (1, '마름'), (2, '보통'), (3, '통통')], default=0, verbose_name='체형')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_approval', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

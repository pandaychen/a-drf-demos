# Generated by Django 3.2.16 on 2022-10-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(default='请输入接口名称', max_length=32, verbose_name='接口名称')),
                ('api_describe', models.TextField(default='请输入接口描述', max_length=255, verbose_name='接口描述')),
                ('api_manager', models.CharField(default='请输入接口负责人名字', max_length=11, verbose_name='接口负责人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '接口列表',
                'verbose_name_plural': '接口列表',
                'db_table': 'api_info',
            },
        ),
    ]

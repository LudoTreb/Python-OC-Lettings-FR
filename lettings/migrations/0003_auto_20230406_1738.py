# Generated by Django 3.0 on 2023-04-06 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_auto_20230406_1651'),
    ]

    operations = [
        # migrations.RunSQL("""
        #           INSERT INTO lettings_letting (
        #               id,
        #               title,
        #               address_id
        #           )
        #           SELECT
        #               id,
        #               title,
        #               address_id
        #           FROM
        #               oc_lettings_site_letting;
        #       """, reverse_sql="""
        #           INSERT INTO oc_lettings_site_letting (
        #               id,
        #               title,
        #               address_id
        #           )
        #           SELECT
        #               id,
        #               title,
        #               address_id
        #           FROM
        #               lettings_letting;
        #       """)
    ]

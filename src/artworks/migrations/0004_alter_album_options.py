import base_common.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0003_migrate_album_id_to_shortuuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='archive_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='id',
            field=base_common.fields.ShortUUIDField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelOptions(
            name='album',
            options={'managed': True},
        ),
    ]

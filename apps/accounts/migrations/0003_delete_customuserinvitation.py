from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuserinvitation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUserInvitation',
        ),
    ]

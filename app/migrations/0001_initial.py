# Generated by Django 3.2.9 on 2022-03-01 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(blank=True, max_length=500, null=True)),
                ('icone', models.FileField(blank=True, null=True, upload_to='icones/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lieux_livraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(blank=True, max_length=500, null=True)),
                ('region', models.CharField(blank=True, max_length=500, null=True)),
                ('ville', models.CharField(blank=True, max_length=500, null=True)),
                ('lat', models.CharField(blank=True, max_length=500, null=True)),
                ('long', models.CharField(blank=True, max_length=500, null=True)),
                ('type_lieux', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('disponiblite', models.BooleanField(default=True)),
                ('photos', models.FileField(upload_to='photos/')),
                ('prix', models.BigIntegerField(blank=True, null=True)),
                ('promotion', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProduitItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb', models.IntegerField(blank=True, default=1, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Produit_carateristique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produit')),
                ('valeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categorie')),
            ],
        ),
        migrations.AddField(
            model_name='commande',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.utilisateur'),
        ),
        migrations.AddField(
            model_name='commande',
            name='lieux_livraison',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lieux_livraison'),
        ),
    ]

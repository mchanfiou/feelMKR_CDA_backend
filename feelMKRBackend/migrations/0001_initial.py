# Generated by Django 5.1.6 on 2025-02-25 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Devis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("montant_total", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Portfolio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titre", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_reservee", models.DateField()),
                (
                    "statut",
                    models.CharField(
                        choices=[
                            ("en attente", "En attente"),
                            ("confirmee", "Confirmee"),
                            ("annulee", "Annulee"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("tarif", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Facture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("montant_paye", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_paiement", models.DateTimeField(auto_now_add=True)),
                (
                    "devis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="feelMKRBackend.devis",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Media",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("photo", "Photo"), ("video", "Video")], max_length=20
                    ),
                ),
                ("url", models.TextField()),
                ("description", models.TextField()),
                (
                    "portfolio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="feelMKRBackend.portfolio",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="devis",
            name="reservation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="feelMKRBackend.reservation",
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="feelMKRBackend.service"
            ),
        ),
        migrations.CreateModel(
            name="Utilisateur",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "type_utilisateur",
                    models.CharField(
                        choices=[("videaste", "Videaste"), ("client", "Client")],
                        max_length=20,
                    ),
                ),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, related_name="utilisateurs", to="auth.group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True, related_name="utilisateurs", to="auth.permission"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="service",
            name="utilisateur",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="feelMKRBackend.utilisateur",
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to="feelMKRBackend.utilisateur",
            ),
        ),
        migrations.AddField(
            model_name="portfolio",
            name="utilisateur",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="feelMKRBackend.utilisateur",
            ),
        ),
        migrations.CreateModel(
            name="Personnalisation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "couleur_principale",
                    models.CharField(blank=True, max_length=7, null=True),
                ),
                (
                    "couleur_secondaire",
                    models.CharField(blank=True, max_length=7, null=True),
                ),
                ("logo_url", models.TextField(blank=True, null=True)),
                (
                    "utilisateur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="feelMKRBackend.utilisateur",
                    ),
                ),
            ],
        ),
    ]

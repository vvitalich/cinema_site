from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    team = models.ManyToManyField(Person, related_name='team', through='TeamMember')

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return f"{self.person.name} - {self.film.title} - {self.roles}"

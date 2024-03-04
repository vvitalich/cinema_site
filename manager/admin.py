from django.contrib import admin

from .models import Person, Role, Film, TeamMember


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'display_team')

    def display_team(self, obj):
        return ", ".join([member.name for member in obj.team.all()])

    display_team.short_description = "Team"


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('person', 'film', 'display_roles')

    def display_roles(self, obj):
        return ", ".join([role.name for role in obj.roles.all()])
    display_roles.short_description = "Roles"


admin.site.register(Film, FilmAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)

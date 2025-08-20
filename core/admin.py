from django.contrib import admin
from core.models import (
    CustomUser, UserOTP, JournalPublication, ConferencePublication, ResearchProjects,
    Patents, CopyRights, PhdGuidance, BookChapter, Book, ConsultancyProjects,
    EditorialRoles, ReviewerRoles, Awards, IndustryCollaboration, UserFormProgress, AnnualFacultyReport, ResearchGrantApplication, ConferenceTravelRequest, PublicationsUpdate, CurriculumDevelopment
)

admin.site.register(CustomUser)
admin.site.register(UserOTP)
admin.site.register(JournalPublication)
admin.site.register(ConferencePublication)
admin.site.register(ResearchProjects)
admin.site.register(Patents)
admin.site.register(CopyRights)
admin.site.register(PhdGuidance)
admin.site.register(BookChapter)
admin.site.register(Book)
admin.site.register(ConsultancyProjects)
admin.site.register(EditorialRoles)
admin.site.register(ReviewerRoles)
admin.site.register(Awards)
admin.site.register(IndustryCollaboration) 
admin.site.register(UserFormProgress)
admin.site.register(AnnualFacultyReport)
admin.site.register(ResearchGrantApplication)
admin.site.register(ConferenceTravelRequest)
admin.site.register(PublicationsUpdate)
admin.site.register(CurriculumDevelopment)
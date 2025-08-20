from django.db import models
from django.contrib.auth.models import AbstractUser, User
import random
from django.conf import settings

def user_directory_path(instance, filename):
    return f'profile_pics/user_{instance.id}/{filename}'

class CustomUser(AbstractUser):

    """
    Custom user model for the faculty portal.
    """

    school = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    highest_qualification = models.CharField(max_length=100, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    orcid_id = models.CharField(max_length=100, blank=True, null=True)
    scopus_id = models.CharField(max_length=100, blank=True, null=True)
    google_scholar_link = models.URLField(blank=True, null=True)
    vidwaan_id = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    is_profile_complete = models.BooleanField(default=False)



class UserOTP(models.Model):

    """
    Model to store OTP for user authentication.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    otp = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} - {self.otp}"
    
    def generate_otp(self):
        """Generate a new OTP for the user"""
        self.otp = str(random.randint(100000, 999999))
        self.save()
        return self.otp


class JournalPublication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_of_paper = models.CharField(max_length = 255)
    Author_position_choice = [
        ('first', 'First Author'),
        ('second', 'Second Author'),
        ('third', 'Third Author'),
        ('fourth', 'Fourth Author'),
        ('fifth', 'Fifth Author'),
        ('sixth', 'Sixth Author'),
        ('corresponding', 'Corresponding Author'),
        ('other', 'Other Author')
    ]

    author_position = models.CharField(
        max_length = 20,
        choices = Author_position_choice,
        default = 'first'
    )

    corresponding_author = models.CharField(max_length = 100, blank = True, null = True)
    journal_name = models.CharField(max_length = 255, blank = True, null = True)
    publisher = models.CharField(max_length = 255, blank = True, null = True)
    ISSN = models.CharField(max_length = 20, blank = True, null = True)
    volume = models.CharField(max_length = 20, blank = True, null = True)
    issue = models.CharField(max_length = 20, blank = True, null = True)
    page_numbers = models.CharField(max_length = 50, blank = True, null = True)

    month_of_publication = [
        ('january', 'January'),
        ('february', 'February'),
        ('march', 'March'),
        ('april', 'April'),
        ('may', 'May'),
        ('june', 'June'),
        ('july', 'July'),
        ('august', 'August'),
        ('september', 'September'),
        ('october', 'October'),
        ('november', 'November'),
        ('december', 'December')
    ]
    month = models.CharField(
        max_length = 20,
        choices = month_of_publication,
        blank = True,
        null = True
    )

    year_of_publication = models.PositiveIntegerField(blank = True, null = True)

    indexed_in = models.CharField(max_length = 255, blank = True, null = True)
    impact_factor = models.DecimalField(max_digits = 5, decimal_places = 2, blank = True, null = True)
    DOI_or_URL = models.URLField(blank = True, null = True)
    Funding_acknowledgement = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('not_applicable', 'Not Applicable'),
        ('other', 'Other')
    ]
    funding_acknowledgement = models.CharField(
        max_length = 20,
        choices = Funding_acknowledgement,
        default = 'no'
    )

    Num_of_authors_from_iilm = models.PositiveIntegerField(
        default = 0,
        help_text = "Number of authors from IILM University"
    )

class ConferencePublication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_of_paper = models.CharField(max_length = 255)
    Author_position_choice = [
        ('first', 'First Author'),
        ('second', 'Second Author'),
        ('third', 'Third Author'),
        ('fourth', 'Fourth Author'),
        ('fifth', 'Fifth Author'),
        ('sixth', 'Sixth Author'),
        ('corresponding', 'Corresponding Author'),
        ('other', 'Other Author')
    ]   
    author_position = models.CharField(
        max_length = 20,
        choices = Author_position_choice,
        default = 'first'
    )   
    corresponding_author = models.CharField(max_length = 100, blank = True, null = True)
    conference_name = models.CharField(max_length = 255, blank = True, null = True)
    organizing_body = models.CharField(max_length = 255, blank = True, null = True)
    ISBN = models.CharField(max_length = 20, blank = True, null = True)

    Type = [
        ('national', 'National'),
        ('international', 'International'),
        ('other', 'Other')
    ]
    type = models.CharField(
        max_length = 20,
        choices = Type,
        default = 'national'
    )

    Mode = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('hybrid', 'Hybrid')
    ]
    mode = models.CharField(
        max_length = 20,
        choices = Mode,
        default = 'online'
    )

    location = models.CharField(max_length = 255, blank = True, null = True)
    date_of_conference = models.DateField(blank = True, null = True)
    DOI_or_URL = models.URLField(blank = True, null = True)
    indexed_in = models.CharField(max_length = 255, blank = True, null = True)
    Funding_acknowledgement = [
        ('yes', 'Yes'), 
        ('no', 'No'),
        ('not_applicable', 'Not Applicable'),
        ('other', 'Other')
    ]
    funding_took_from_iilm = models.CharField(
        max_length = 20,
        choices = Funding_acknowledgement,
        default = 'no'
    )
    Num_of_authors_from_iilm = models.PositiveIntegerField(
        default = 0,
        help_text = "Number of authors from IILM University"
    )


class ResearchProjects(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=255, blank=True, null=True)
    funding_agency = models.CharField(max_length=255, blank=True, null=True)
    principal_investigator_choice = [
        ('principal', 'Principal Investigator'),
        ('co_investigator', 'Co-Investigator'),
        ('other', 'Other')
    ]
    principal_investigator = models.CharField(
        max_length=20,
        choices=principal_investigator_choice,
        default='principal'
    )
    
    amount_sanctioned = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    duration_from = models.DateField(blank=True, null=True)
    duration_to = models.DateField(blank=True, null=True)

    status_choices = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('halted', 'Halted'),
        ('submitted', 'Submitted')
    ]
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default='ongoing'
    )

    outcome_choices = [
        ('publication', 'Publication'),
        ('patent', 'Patent'),
        ('product', 'Product'),
        ('other', 'Other')
    ]
    outcome = models.CharField(
        max_length=20,
        choices=outcome_choices,
        default='publication'
    )

    num_of_authors_from_iilm = models.PositiveIntegerField(
        default=0,
        help_text="Number of authors from IILM University"
    )

class Patents(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_of_patent = models.CharField(max_length=255, blank=True, null=True)
    investors = models.CharField(max_length=255, blank=True, null=True, help_text="Comma-separated list of investors")

    status_choices = [
        ('filed', 'Filed'),
        ('granted', 'Granted'),
        ('rejected', 'Rejected'),
        ('other', 'Other')
    ]
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default='filed'
    )

    patent_number = models.CharField(max_length=100, blank=True, null=True)
    date_of_published = models.DateField(blank=True, null=True)
    date_of_granted = models.DateField(blank=True, null=True)

    jursidiction_choices = [
        ('national', 'National'),
        ('international', 'International'),
        ('other', 'Other')
    ]
    jurisdiction = models.CharField(
        max_length=20,
        choices=jursidiction_choices,
        default='national'
    )

    type_choices = [
        ('utility', 'Utility'),
        ('design', 'Design'),
        ('plant', 'Plant'),
        ('provisional', 'Provisional'),
        ('non_provisional', 'Non-Provisional'),
        ('other', 'Other'),
    ]
    type = models.CharField(
        max_length=20,
        choices=type_choices,
        default='utility'
    )

    num_of_authors_from_iilm = models.PositiveIntegerField(
        default=0,
        help_text="Number of authors from IILM University"
    )


class CopyRights(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_of_work = models.CharField(max_length=255, blank=True, null=True)
    type_choices = [
        ('book', 'Book'),
        ('article', 'Article'),
        ('software', 'Software'),
        ('other', 'Other'),
        ('manual', 'Manual'),
        ('course_material', 'Course Material')
    ]
    type = models.CharField(
        max_length=20,
        choices=type_choices,
        default='book'
    )

    authors = models.CharField(max_length=255, blank=True, null=True, help_text="Comma-separated list of authors")

    registration_number = models.CharField(max_length=100, blank=True, null=True)
    date_of_grant = models.DateField(blank=True, null=True)
    numbers_of_authors_from_iilm = models.PositiveIntegerField(
        default=0,
        help_text="Number of authors from IILM University"
    )

class PhdGuidance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name_of_scholar = models.CharField(max_length=255, blank=True, null=True)

    outside_iilm_choice = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('not_applicable', 'Not Applicable'),
        ('other', 'Other')
    ]
    outside_iilm = models.CharField(
        max_length=20,
        choices=outside_iilm_choice,
        default='no'
    )

    thesis_title = models.CharField(max_length=255, blank=True, null=True)

    role_choices = [
        ('supervisor', 'Supervisor'),
        ('co_supervisor', 'Co-Supervisor'),
        ('committee_member', 'Committee Member'),
        ('other', 'Other')
    ]
    role = models.CharField(
        max_length=20,
        choices=role_choices,
        default='supervisor'
    )

    status_choices = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('halted', 'Halted'),
        ('submitted', 'Submitted')
    ]
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default='ongoing'
    )

    date_of_completion = models.DateField(blank=True, null=True, help_text="Date of completion (if applicable)")
    other_superviser_or_co_superviser = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Name of other supervisor or co-supervisor of IILM (if applicable)"
    )

class BookChapter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chap_title = models.CharField(max_length=255, blank=True, null=True)
    book_title = models.CharField(max_length=255, blank=True, null=True)

    publisher = models.CharField(max_length=255, blank=True, null=True)
    ISBN = models.CharField(max_length=20, blank=True, null=True)
    publication_year = models.PositiveIntegerField(blank=True, null=True)

    indexed = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('not_applicable', 'Not Applicable'),
        ('other', 'Other')
    ]
    indexed_in = models.CharField(
        max_length=20,
        choices=indexed,
        default='no'
    )

    author_position_choice = [
        ('first', 'First Author'),
        ('second', 'Second Author'),
        ('third', 'Third Author'),
        ('fourth', 'Fourth Author'),
        ('fifth', 'Fifth Author'),
        ('sixth', 'Sixth Author'),
        ('corresponding', 'Corresponding Author'),
        ('other', 'Other Author')
    ]
    author_position = models.CharField(
        max_length=20,
        choices=author_position_choice,
        default='first'
    )

    corresponding_author = models.CharField(max_length=100, blank=True, null=True)
    number_of_authors_from_iilm = models.PositiveIntegerField(
        default=0,
        help_text="Number of authors from IILM University"
    )

class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_of_book = models.CharField(max_length=255, blank=True, null=True)

    type_choices = [
        ('authored', 'Authored'),
        ('edited', 'Edited'),
        ('other', 'Other')
    ]
    type = models.CharField(
        max_length=20,
        choices=type_choices,
        default='authored'
    )

    publisher = models.CharField(max_length=255, blank=True, null=True)
    ISBN = models.CharField(max_length=20, blank=True, null=True)
    publication_year = models.PositiveIntegerField(blank=True, null=True)

    indexed = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('not_applicable', 'Not Applicable'),
        ('other', 'Other')
    ]
    indexed_in = models.CharField(
        max_length=20,
        choices=indexed,
        default='no'
    )

    authors_or_editors = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="Comma-separated list of authors or editors"
    )

    num_of_authors_from_iilm = models.PositiveIntegerField(
        default=0,
        help_text="Number of authors or editors from IILM University"
    )
    

class ConsultancyProjects(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=255, blank=True, null=True)
    industry_partner = models.CharField(max_length=255, blank=True, null=True)

    duration = models.CharField(max_length=100, blank=True, null=True, help_text="Duration of the project (e.g., 6 months, January 2025 - June 2025)")
    amount_received = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Total amount received for the project")
    role = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text="Your role in the project (e.g., Lead Consultant, Co-Consultant)"
    )

    outcome = models.TextField(
        blank=True,
        null=True,
        help_text="Outcome of the project"
    )

    MoU_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('not_applicable', 'Not Applicable'),
        ('other', 'Other')
    ]
    MoU_signed = models.CharField(
        max_length=20,
        choices=MoU_choices,
        default='no',
        help_text="Is there a Memorandum of Understanding (MoU) signed for this project?"
    )

    num_of_other_project_members_from_iilm = models.PositiveIntegerField(
        default=0,
        help_text="Number of other project members from IILM University"
    )

class EditorialRoles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    journal_name = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)

    editor_role_choices = [
        ('editor_in_chief', 'Editor-in-Chief'),
        ('associate_editor', 'Associate Editor'),
        ('section_editor', 'Section Editor'),
        ('editor', 'Editor'),
        ('guest_editor', 'Guest Editor'),
        ('reviewer', 'Reviewer'),
        ('other', 'Other')
    ]
    editor_role = models.CharField(
        max_length=20,
        choices=editor_role_choices,
        default='editor'
    )

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class ReviewerRoles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    journal_name = models.CharField(max_length=255, blank=True, null=True, help_text="Name of the journal or conference")
    publisher = models.CharField(max_length=255, blank=True, null=True, help_text="Publisher of the journal or conference proceedings")

    freq_of_review_choices = [
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('biannually', 'Biannually'),
        ('annually', 'Annually'),
        ('as_needed', 'As Needed'),
        ('other', 'Other')
    ]
    freq_of_review = models.CharField(
        max_length=20,
        choices=freq_of_review_choices,
        default='as_needed'
    )

    indexing_choices = [
        ('scopus', 'Scopus'),
        ('web_of_science', 'Web of Science'),
        ('google_scholar', 'Google Scholar'),
        ('SCI', 'SCI'),
        ('other', 'Other'),
        ('not_indexed', 'Not Indexed')
    ]
    indexing = models.CharField(
        max_length=20,
        choices=indexing_choices,
        default='not_indexed'
    )


class Awards(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_of_award = models.CharField(max_length=255, blank=True, null=True)
    awarding_body = models.CharField(max_length=255, blank=True, null=True)

    level_choices = [
        ('national', 'National'),
        ('international', 'International'),
        ('university', 'University'),
        ('departmental', 'Departmental'),
        ('other', 'Other')
    ]
    level = models.CharField(
        max_length=20,
        choices=level_choices,
        default='university'
    )

    date_of_award = models.DateField(blank=True, null=True)
    nature_of_contribution = models.TextField(
        blank=True, 
        null=True,
        help_text="Nature of your contribution to the award"
    )

    def __str__(self):
        return f"{self.title_of_award} - {self.awarding_body}"

class IndustryCollaboration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    industry_name = models.CharField(max_length=255, blank=True, null=True)
    nature_of_collaborations = models.TextField(
        blank=True,
        null=True,
        help_text="Nature of collaborations with the industry (e.g., joint research, consultancy, training)"
    )

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    outcomes_choices = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('consultancy', 'Consultancy'),
        ('training', 'Training'),
        ('other', 'Other')
    ]
    outcomes = models.CharField(
        max_length=20,
        choices=outcomes_choices,
        default='research'
    )

    Mou_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('not_applicable', 'Not Applicable'),
        ('other', 'Other')
    ]
    mou_signed = models.CharField(
        max_length=20,
        choices=Mou_choices,
        default='no',
        help_text="Is there a Memorandum of Understanding (MoU) signed for this collaboration?"
    )

class UserFormProgress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    journal_publication_progress = models.BooleanField(default=False)
    conference_publication_progress = models.BooleanField(default=False)
    research_projects_progress = models.BooleanField(default=False)
    patents_progress = models.BooleanField(default=False)
    copyrights_progress = models.BooleanField(default=False)
    phd_guidance_progress = models.BooleanField(default=False)
    book_chapter_progress = models.BooleanField(default=False)
    book_progress = models.BooleanField(default=False)
    consultancy_projects_progress = models.BooleanField(default=False)
    editorial_roles_progress = models.BooleanField(default=False)
    reviewer_roles_progress = models.BooleanField(default=False)
    awards_progress = models.BooleanField(default=False)
    industry_collaboration_progress = models.BooleanField(default=False)

    def calculate_progress(self):
        fields = [
            self.journal_publication_progress,
            self.conference_publication_progress,
            self.research_projects_progress,
            self.patents_progress,
            self.copyrights_progress,
            self.phd_guidance_progress,
            self.book_chapter_progress,
            self.book_progress,
            self.consultancy_projects_progress,
            self.editorial_roles_progress,
            self.reviewer_roles_progress,
            self.awards_progress,
            self.industry_collaboration_progress,
        ]
        total = len(fields)
        completed = sum(1 for f in fields if f)
        return int((completed / total) * 100)
    
    def __str__(self):
        return f"{self.user.username} - {self.calculate_progress()}%"
    

class AnnualFacultyReport(models.Model):
    courses_taught = models.TextField(blank=True, null=True, help_text="List of courses taught in the academic year")
    teaching_innovations = models.TextField(blank=True, null=True, help_text="Description of teaching innovations implemented")
    student_mentoring = models.TextField(blank=True, null=True, help_text="Description of student mentoring activities")

    publications = models.TextField(blank=True, null=True, help_text="List of publications in the academic year")
    research_projects = models.TextField(blank=True, null=True, help_text="Description of research projects undertaken")
    conference_presentations = models.TextField(blank=True, null=True, help_text="Description of conference presentations made")

    institutional_service = models.TextField(blank=True, null=True, help_text="Description of institutional service activities")
    professional_service = models.TextField(blank=True, null=True, help_text="Description of professional service activities")
    community_service = models.TextField(blank=True, null=True, help_text="Description of community service activities")

    professional_development = models.TextField(blank=True, null=True, help_text="Description of professional development activities")

    major_achievements = models.TextField(blank=True, null=True, help_text="Description of major achievements in the academic year")
    goals = models.TextField(blank=True, null=True, help_text="Description of goals for the upcoming academic year")
    required_resources = models.TextField(blank=True, null=True, help_text="Description of resources required to achieve the goals")

    current_cv = models.FileField(upload_to='cv/', blank=True, null=True, help_text="Upload your current CV")
    additional_documents = models.FileField(upload_to='cv/', blank=True, null=True, help_text="Upload any additional documents")

    check_box = models.BooleanField(default=False, help_text="I confirm that the information provided is accurate and complete.")
    additional_comments = models.TextField(blank=True, null=True, help_text="Any additional comments or information.")


class ResearchGrantApplication(models.Model):
    title_of_research_proposal = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the title of the research proposal")
    abstract = models.TextField(blank=True, null=True, help_text="Provide a brief abstract of the research proposal")
    objectives = models.TextField(blank=True, null=True, help_text="List the objectives of the research proposal")
    research_methodology = models.TextField(blank=True, null=True, help_text="Describe the research methodology to be used")
    expected_outcomes = models.TextField(blank=True, null=True, help_text="List the expected outcomes of the research proposal")

    budget = models.TextField(blank=True, null=True, help_text="Provide a detailed budget for the research proposal")
    budget_breakdown = models.TextField(blank=True, null=True, help_text="Provide a breakdown of the budget for the research proposal")

    start_date = models.DateField(blank=True, null=True, help_text="Enter the start date of the research project")
    end_date = models.DateField(blank=True, null=True, help_text="Enter the end date of the research project")

    detailed_proposal = models.FileField(upload_to='research_proposals/', blank=True, null=True, help_text="Upload the detailed research proposal document")
    supporting_documents = models.FileField(upload_to='research_proposals/', blank=True, null=True, help_text="Upload any supporting documents for the research proposal")

    declaration = models.BooleanField(default=False, help_text="I confirm that the information provided is accurate and complete.")

    signature_img = models.ImageField(upload_to='research_proposals/signatures/', blank=True, null=True, help_text="Upload your signature image")
    
class ConferenceTravelRequest(models.Model):
    title_of_conference = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the title of the conference")
    conference_website = models.URLField(blank=True, null=True, help_text="Enter the conference website URL")

    organizers_name_affiliation = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the name and affiliation of the conference organizer")
    conference_venue = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the venue of the conference")

    from_date = models.DateField(blank=True, null=True, help_text="Enter the start date of the conference")
    to_date = models.DateField(blank=True, null=True, help_text="Enter the end date of the conference")

    type_of_participation = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the type of participation (e.g., presenter, attendee)")

    title_of_research_paper = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the title of the research paper")
    abstract = models.TextField(blank=True, null=True, help_text="Provide a brief abstract of the research paper")

    acceptance_letter = models.FileField(upload_to='conference_papers/acceptance_letters/', blank=True, null=True, help_text="Upload the acceptance letter for the conference")

    travel_choice = models.CharField(max_length=255, blank=True, null=True, help_text="Enter your travel choice (e.g., flight, train, etc.)")
    travel_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Enter your estimated travel budget")
    accommodation_details = models.TextField(blank=True, null=True, help_text="Provide details about your accommodation arrangements")

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Enter the total amount for the conference")

    prev_fund_checkbox = models.BooleanField(default=False, help_text="I confirm that I have not received any previous funding for this or any conference.")

    justification = models.TextField(blank=True, null=True, help_text="Provide a justification for attending the conference")

    attachments = models.FileField(upload_to='conference_papers/attachments/', blank=True, null=True, help_text="Upload any additional attachments for the conference")

    dean_approval = models.BooleanField(default=False, help_text="I confirm that I have obtained the necessary approvals for this conference attendance.")

class PublicationsUpdate(models.Model):
    title_of_publication = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the title of the publication")
    authors = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the authors of the publication")

    type_of_publication = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the type of publication (e.g., journal article, conference paper)")

    publisher_name = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the name of the publisher")

    year_of_publication = models.PositiveIntegerField(blank=True, null=True, help_text="Enter the year of publication")

    doi = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the DOI (Digital Object Identifier) of the publication")

    abstract = models.TextField(blank=True, null=True, help_text="Enter the abstract of the publication")
    categories = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the categories of the publication (e.g., research, review)")

    checkbox = models.BooleanField(default=False, help_text="I confirm that the information provided is accurate and complete.")

class CurriculumDevelopment(models.Model):
    program_title = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the title of the program")

    program_description = models.TextField(blank=True, null=True, help_text="Enter a description of the program")

    program_goals = models.TextField(blank=True, null=True, help_text="Enter the goals of the program")

    program_outcomes = models.TextField(blank=True, null=True, help_text="Enter the expected outcomes of the program")

    program_implementation_plan = models.TextField(blank=True, null=True, help_text="Enter the implementation plan for the program")

    program_duration = models.CharField(max_length=255, blank=True, null=True, help_text="Enter the duration of the program")

    program_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Enter the budget for the program")

    program_justification = models.TextField(blank=True, null=True, help_text="Enter a justification for the program")

    program_attachments = models.FileField(upload_to='curriculum_development/attachments/', blank=True, null=True, help_text="Upload any additional attachments for the program")

    dean_approval = models.BooleanField(default=False, help_text="I confirm that I have obtained the necessary approvals for this program.")

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, UserOTP, JournalPublication, ConferencePublication, ResearchProjects, Patents, CopyRights, PhdGuidance, BookChapter, Book, ConsultancyProjects, EditorialRoles, ReviewerRoles, Awards, IndustryCollaboration, UserFormProgress, AnnualFacultyReport, ResearchGrantApplication, ConferenceTravelRequest, PublicationsUpdate, CurriculumDevelopment, FacultySubmission, SubmissionReview




class SignupForm(UserCreationForm):

    """
    SignupForm:
    Custom user signup form that extends Django's UserCreationForm.
    - Uses the CustomUser model.
    - Adds an email field in addition to username and password.
    - Removes default Django help texts for cleaner UI.
    """

    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }




class LoginForm(AuthenticationForm):
    
    """
    LoginForm:
    Custom login form extending Django's AuthenticationForm.
    - Uses the username field with a custom label.
    - Adds placeholder text to username and password fields for better UI/UX.
    """

    username = forms.CharField(label="Username")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter your password'})




class ProfileCompletionForm(forms.ModelForm):

    """
    ProfileCompletionForm:
    Form for completing and updating user profile information.
    - Based on the CustomUser model.
    - Includes personal details (name, school, department, designation).
    - Captures academic/professional details (qualification, specialization, ORCID, Scopus ID, Google Scholar, Vidwaan ID).
    - Allows uploading a profile picture.
    - Includes role selection for permissions.
    """

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'school', 'department', 'designation', 'role',
            'highest_qualification', 'specialization', 'orcid_id',
            'scopus_id', 'google_scholar_link', 'vidwaan_id', 'profile_picture'
        ]
        
        widgets = {
            'role': forms.Select(attrs={'class': 'form-control'}),
        }




class JournalPublicationForm(forms.ModelForm):

    """
    JournalPublicationForm:
    Form for adding and managing journal publication details.
    - Based on the JournalPublication model.
    - Excludes the 'user' field (auto-handled elsewhere).
    - Includes all other fields with customized widgets for better UI.
    - Captures details like paper title, author role, journal info, ISSN, volume, issue, pages, publication year, indexing, impact factor, DOI/URL, funding acknowledgment, and author count.
    """


    class Meta:
        model = JournalPublication
        exclude = ['user']
        fields = '__all__'
        widgets = {
            'title_of_paper': forms.TextInput(attrs={'class': 'form-control'}),
            'author_position': forms.Select(attrs={'class': 'form-control'}),
            'corresponding_author': forms.TextInput(attrs={'class': 'form-control'}),
            'journal_name': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'ISSN': forms.TextInput(attrs={'class': 'form-control'}),
            'volume': forms.TextInput(attrs={'class': 'form-control'}),
            'issue': forms.TextInput(attrs={'class': 'form-control'}),
            'page_numbers': forms.TextInput(attrs={'class': 'form-control'}),
            'month': forms.Select(attrs={'class': 'form-control'}),
            'year_of_publication': forms.NumberInput(attrs={'class': 'form-control'}),
            'indexed_in': forms.TextInput(attrs={'class': 'form-control'}),
            'impact_factor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'DOI_or_URL': forms.URLInput(attrs={'class': 'form-control'}),
            'funding_acknowledgement': forms.Select(attrs={'class': 'form-control'}),
            'Num_of_authors_from_iilm': forms.NumberInput(attrs={'class': 'form-control'}),
        }





class ConferencePublicationForm(forms.ModelForm):

    """
    ConferencePublicationForm:
    Form for adding and managing conference publication details.
    - Based on the ConferencePublication model.
    - Includes all fields with custom widgets for better form styling.
    - Captures details like paper title, author role, corresponding author, conference name, organizing body, ISBN, type, mode, location, conference date, DOI/URL, indexing, funding support, and author count from IILM.
    """

    class Meta:
        model = ConferencePublication
        fields = '__all__'

        widgets = {
            'title_of_paper': forms.TextInput(attrs={'class': 'form-control'}),
            'author_position': forms.Select(attrs={'class': 'form-control'}),
            'corresponding_author': forms.TextInput(attrs={'class': 'form-control'}),
            'conference_name': forms.TextInput(attrs={'class': 'form-control'}),
            'organizing_body': forms.TextInput(attrs={'class': 'form-control'}),
            'ISBN': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'mode': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_conference': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'DOI_or_URL': forms.URLInput(attrs={'class': 'form-control'}),
            'indexed_in': forms.TextInput(attrs={'class': 'form-control'}),
            'funding_took_from_iilm': forms.Select(attrs={'class': 'form-control'}),
            'Num_of_authors_from_iilm': forms.NumberInput(attrs={'class': 'form-control'}),
        }




class ResearchProjectsForm(forms.ModelForm):

    """
    ResearchProjectsForm:
    Form for managing research project details.
    - Based on the ResearchProjects model.
    - Includes all fields with customized widgets and placeholders for better UI.
    - Captures details such as project title, funding agency, principal investigator, sanctioned amount, project duration, status, outcome, and number of authors from IILM.
    """
    class Meta:
        model = ResearchProjects
        fields = '__all__'
        widgets = {
            'project_title': forms.TextInput(attrs={
                'placeholder': 'Enter the project title',
                'class': 'form-control'
            }),
            'funding_agency': forms.TextInput(attrs={
                'placeholder': 'Enter the funding agency',
                'class': 'form-control'
            }),
            'principal_investigator': forms.Select(attrs={
                'class': 'form-control'
            }),
            'amount_sanctioned': forms.NumberInput(attrs={
                'placeholder': 'Amount in INR',
                'class': 'form-control'
            }),
            'duration_from': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'duration_to': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'outcome': forms.Select(attrs={
                'class': 'form-control'
            }),
            'num_of_authors_from_iilm': forms.NumberInput(attrs={
                'placeholder': 'Number of authors from IILM',
                'class': 'form-control'
            }),
        }




class PatentsForm(forms.ModelForm):

    """
    PatentsForm:
    Form for managing patent details.
    - Based on the Patents model.
    - Includes all fields with custom widgets and placeholders.
    - Captures details such as patent title, inventors, status, patent number, publication/grant dates, jurisdiction, type, and number of authors from IILM.
    """

    class Meta:
        model = Patents
        fields = '__all__'
        widgets = {
            'title_of_patent': forms.TextInput(attrs={
                'placeholder': 'Enter the title of the patent',
                'class': 'form-control'
            }),
            'investors': forms.TextInput(attrs={
                'placeholder': 'Comma-separated list of investors',
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'patent_number': forms.TextInput(attrs={
                'placeholder': 'Patent number (if any)',
                'class': 'form-control'
            }),
            'date_of_published': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'date_of_granted': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'jurisdiction': forms.Select(attrs={
                'class': 'form-control'
            }),
            'type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'num_of_authors_from_iilm': forms.NumberInput(attrs={
                'placeholder': 'Number of authors from IILM',
                'class': 'form-control'
            }),
        }




class CopyRightsForm(forms.ModelForm):

    """
    CopyRightsForm:
    Form for managing copyright details.
    - Based on the CopyRights model.
    - Includes all fields with customized widgets.
    - Captures details such as work title, type, authors, registration number, date of grant, and number of authors from IILM.
    """

    class Meta:
        model = CopyRights
        fields = '__all__'
        widgets = {
            'title_of_work': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'authors': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. John Doe, Jane Smith'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_grant': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'numbers_of_authors_from_iilm': forms.NumberInput(attrs={'class': 'form-control'}),
        }



class PhdGuidanceForm(forms.ModelForm):

    """
    PhdGuidanceForm:
    Form for managing PhD guidance details.
    - Based on the PhdGuidance model.
    - Includes all fields with custom widgets and placeholders.
    - Captures details such as scholar’s name, whether they are outside IILM, thesis title, role, status, completion date, and co-supervisor information.
    """

    class Meta:
        model = PhdGuidance
        fields = '__all__'
        widgets = {
            'name_of_scholar': forms.TextInput(attrs={
                'placeholder': 'Enter scholar’s full name',
                'class': 'form-control'
            }),
            'outside_iilm': forms.Select(attrs={
                'class': 'form-control'
            }),
            'thesis_title': forms.TextInput(attrs={
                'placeholder': 'Enter title of the thesis',
                'class': 'form-control'
            }),
            'role': forms.Select(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'date_of_completion': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'other_superviser_or_co_superviser': forms.TextInput(attrs={
                'placeholder': 'Enter co-supervisor’s name (if any)',
                'class': 'form-control'
            }),
        }




class BookChapterForm(forms.ModelForm):

    """
    BookChapterForm:
    Form for managing book chapter publication details.
    - Based on the BookChapter model.
    - Includes all fields with custom widgets and placeholders for better UI.
    - Captures details such as chapter title, book title, publisher, ISBN, publication year, indexing, author role, corresponding author, and number of authors from IILM.
    """

    class Meta:
        model = BookChapter
        fields = '__all__'
        widgets = {
            'chap_title': forms.TextInput(attrs={
                'placeholder': 'Enter chapter title',
                'class': 'form-control'
            }),
            'book_title': forms.TextInput(attrs={
                'placeholder': 'Enter book title',
                'class': 'form-control'
            }),
            'publisher': forms.TextInput(attrs={
                'placeholder': 'Enter publisher name',
                'class': 'form-control'
            }),
            'ISBN': forms.TextInput(attrs={
                'placeholder': 'Enter ISBN number',
                'class': 'form-control'
            }),
            'publication_year': forms.NumberInput(attrs={
                'placeholder': 'YYYY',
                'class': 'form-control'
            }),
            'indexed_in': forms.Select(attrs={
                'class': 'form-control'
            }),
            'author_position': forms.Select(attrs={
                'class': 'form-control'
            }),
            'corresponding_author': forms.TextInput(attrs={
                'placeholder': 'Enter corresponding author name',
                'class': 'form-control'
            }),
            'number_of_authors_from_iilm': forms.NumberInput(attrs={
                'placeholder': 'e.g. 2',
                'class': 'form-control'
            }),
        }

class BookForm(forms.ModelForm):

    """
    BookForm is a Django ModelForm class linked to the Book model.
    - It generates form fields for all model attributes (`fields = '__all__'`).
    - Custom widgets improve the form inputs with placeholders, dropdowns, and constraints.
    - Labels provide user-friendly names for each field.
    - Help texts guide users on how to correctly fill in specific fields.
    """

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title_of_book': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'type': forms.Select(),
            'publisher': forms.TextInput(attrs={'placeholder': 'Enter publisher name'}),
            'ISBN': forms.TextInput(attrs={'placeholder': 'Enter ISBN'}),
            'publication_year': forms.NumberInput(attrs={'placeholder': 'e.g. 2024'}),
            'indexed_in': forms.Select(),
            'authors_or_editors': forms.TextInput(attrs={'placeholder': 'Comma-separated list of authors/editors'}),
            'num_of_authors_from_iilm': forms.NumberInput(attrs={'min': 0}),
        }
        labels = {
            'title_of_book': 'Title of Book',
            'type': 'Type',
            'publisher': 'Publisher',
            'ISBN': 'ISBN',
            'publication_year': 'Publication Year',
            'indexed_in': 'Indexed In',
            'authors_or_editors': 'Authors or Editors',
            'num_of_authors_from_iilm': 'No. of IILM Authors/Editors'
        }
        help_texts = {
            'authors_or_editors': 'Comma-separated list of authors or editors',
            'num_of_authors_from_iilm': 'Number of authors or editors from IILM University'
        }


class ConsultancyProjectsForm(forms.ModelForm):
    
    """
    ConsultancyProjectsForm is a Django ModelForm class linked to the ConsultancyProjects model.
    - It generates form fields for all model attributes (`fields = '__all__'`).
    - Custom widgets add placeholders, dropdowns, and text areas for better user input.
    - Labels provide clear and user-friendly names for each field in the form.
    - Help texts guide users in entering correct details like duration, role, and team members.
    """


    class Meta:
        model = ConsultancyProjects
        fields = '__all__'
        widgets = {
            'project_title': forms.TextInput(attrs={'placeholder': 'Enter project title'}),
            'industry_partner': forms.TextInput(attrs={'placeholder': 'Enter industry partner name'}),
            'duration': forms.TextInput(attrs={'placeholder': 'e.g., 6 months or Jan 2025 - Jun 2025'}),
            'amount_received': forms.NumberInput(attrs={'placeholder': 'Total amount received'}),
            'role': forms.TextInput(attrs={'placeholder': 'e.g., Lead Consultant'}),
            'outcome': forms.Textarea(attrs={'placeholder': 'Describe the outcome of the project', 'rows': 3}),
            'MoU_signed': forms.Select(),
            'num_of_other_project_members_from_iilm': forms.NumberInput(attrs={'min': 0}),
        }
        labels = {
            'project_title': 'Project Title',
            'industry_partner': 'Industry Partner',
            'duration': 'Duration',
            'amount_received': 'Amount Received',
            'role': 'Role in Project',
            'outcome': 'Project Outcome',
            'MoU_signed': 'MoU Signed',
            'num_of_other_project_members_from_iilm': 'IILM Project Members (Excl. You)',
        }
        help_texts = {
            'duration': 'Duration of the project (e.g., 6 months, Jan 2025 - Jun 2025)',
            'amount_received': 'Total amount received for the project',
            'role': 'Your role in the project (e.g., Lead Consultant)',
            'outcome': 'Outcome of the project',
            'MoU_signed': 'Was an MoU signed for this project?',
            'num_of_other_project_members_from_iilm': 'Other team members from IILM (excluding yourself)',
        }

class EditorialRolesForm(forms.ModelForm):
    
    """
    EditorialRolesForm is a Django ModelForm class linked to the EditorialRoles model.
    - It generates form fields for selected attributes such as journal name, publisher, role, and dates.
    - Custom widgets provide placeholders, dropdowns, and date pickers for better usability.
    - Labels are defined to display clear and readable field names in the form.
    """

    class Meta:
        model = EditorialRoles
        fields = [
            'journal_name',
            'publisher',
            'editor_role',
            'start_date',
            'end_date',
        ]
        
        widgets = {
            'journal_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Journal Name'
            }),
            'publisher': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Publisher Name'
            }),
            'editor_role': forms.Select(attrs={
                'class': 'form-control'
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }

        labels = {
            'journal_name': 'Journal Name',
            'publisher': 'Publisher',
            'editor_role': 'Editorial Role',
            'start_date': 'Start Date',
            'end_date': 'End Date',
        }

class ReviewerRolesForm(forms.ModelForm):

    """
    ReviewerRolesForm is a Django ModelForm class linked to the ReviewerRoles model.
    - It includes all fields from the model (`fields = '__all__'`).
    - Custom widgets are applied to provide placeholders, dropdowns, and Bootstrap styling (`form-control`).
    - The form collects reviewer details such as journal/conference name, publisher, frequency of review, and indexing.
    """

    class Meta:
        model = ReviewerRoles
        fields = '__all__'
        widgets = {
            'journal_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter journal or conference name'
            }),
            'publisher': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter publisher name'
            }),
            'freq_of_review': forms.Select(attrs={
                'class': 'form-control'
            }),
            'indexing': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class AwardsForm(forms.ModelForm):

    """
    AwardsForm is a Django ModelForm class linked to the Awards model.
    - It includes specific fields like award title, awarding body, level, date, and contribution details.
    - Custom widgets are used for better user interaction, such as text inputs with placeholders, 
      a dropdown for level, a date picker for award date, and a textarea for contributions.
    - Bootstrap's 'form-control' class is applied to maintain a consistent UI style.
    """

    class Meta:
        model = Awards
        fields = [
            'title_of_award',
            'awarding_body',
            'level',
            'date_of_award',
            'nature_of_contribution',
        ]
        widgets = {
            'title_of_award': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of the award'
            }),
            'awarding_body': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the awarding organization'
            }),
            'level': forms.Select(attrs={
                'class': 'form-control'
            }),
            'date_of_award': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'nature_of_contribution': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your contribution',
                'rows': 4
            }),
        }


class IndustryCollaborationForm(forms.ModelForm):

    """
    IndustryCollaborationForm is a Django ModelForm class linked to the IndustryCollaboration model.
    - It includes all model fields (`fields = '__all__'`).
    - Custom widgets provide text inputs, text areas, date pickers, and dropdowns with Bootstrap styling (`form-control`).
    - Labels are defined for displaying user-friendly field names in the form.
    - The form is used to capture collaboration details such as industry name, nature, duration, outcomes, and MoU status.
    """

    class Meta:
        model = IndustryCollaboration
        fields = '__all__'
        widgets = {
            'industry_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter industry name'}),
            'nature_of_collaborations': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe the nature of collaboration'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'outcomes': forms.Select(attrs={'class': 'form-control'}),
            'mou_signed': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'industry_name': 'Industry Name',
            'nature_of_collaborations': 'Nature of Collaborations',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'outcomes': 'Outcomes of Collaboration',
            'mou_signed': 'MoU Signed?',
        }

class UserFormProgressForm(forms.ModelForm):

    """
    UserFormProgressForm is a Django ModelForm linked to the UserFormProgress model.
    - It tracks a user’s progress across different research and academic contribution areas.
    - Fields include progress tracking for journals, conferences, research projects, patents, copyrights,
      PhD guidance, books, consultancy projects, editorial/reviewer roles, awards, and industry collaborations.
    - Helps in monitoring completion or submission status of multiple forms.
    """

    class Meta:
        model = UserFormProgress
        fields = [
            'journal_publication_progress',
            'conference_publication_progress',
            'research_projects_progress',
            'patents_progress',
            'copyrights_progress',
            'phd_guidance_progress',
            'book_chapter_progress',
            'book_progress',
            'consultancy_projects_progress',
            'editorial_roles_progress',
            'reviewer_roles_progress',
            'awards_progress',
            'industry_collaboration_progress',
        ]
        

class AnnualFacultyReportForm(forms.ModelForm):

    """
    AnnualFacultyReportForm is a Django ModelForm class linked to the AnnualFacultyReport model.
    - It includes all fields from the model (`fields = "__all__"`).
    - Custom widgets (mainly text areas with placeholders) are used for structured inputs such as 
      courses taught, publications, projects, achievements, and goals.
    - File upload fields allow faculty members to attach supporting documents like CVs and reports.
    - A checkbox and additional comments field are also provided to finalize the report.
    - The form serves as a comprehensive self-reporting tool for faculty’s teaching, research, 
      service, and professional development activities.
    """

    class Meta:
        model = AnnualFacultyReport
        fields = "__all__"   # includes all fields from the model
        widgets = {
            'courses_taught': forms.Textarea(attrs={'rows': 3, 'placeholder': 'List of courses taught'}),
            'teaching_innovations': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Innovations implemented'}),
            'student_mentoring': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Mentoring activities'}),
            
            'publications': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Publications'}),
            'research_projects': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Research projects'}),
            'conference_presentations': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Conference presentations'}),

            'institutional_service': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Institutional service'}),
            'professional_service': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Professional service'}),
            'community_service': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Community service'}),

            'professional_development': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Professional development'}),
            'major_achievements': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Major achievements'}),
            'goals': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Goals for upcoming year'}),
            'required_resources': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Required resources'}),

            'current_cv': forms.ClearableFileInput(),
            'additional_documents': forms.ClearableFileInput(),

            'check_box': forms.CheckboxInput(),
            'additional_comments': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Any additional comments'}),
        }

class ResearchGrantApplicationForm(forms.ModelForm):

    """
    ResearchGrantApplicationForm is a Django ModelForm class linked to the ResearchGrantApplication model.
    - It captures all details required for submitting a research grant proposal (`fields = "__all__"`).
    - Text fields collect structured information such as title, abstract, objectives, methodology, 
      outcomes, and budget details.
    - Date inputs record the proposed project duration (start and end dates).
    - File upload fields allow attaching the full proposal, supporting documents, and a digital signature.
    - Includes a declaration checkbox to confirm compliance with submission guidelines.
    - This form provides a standardized way to apply for research grants within the institution.
    """

    class Meta:
        model = ResearchGrantApplication
        fields = "__all__"
        
        widgets = {
            'title_of_research_proposal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'abstract': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Provide abstract'}),
            'objectives': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'List objectives'}),
            'research_methodology': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe methodology'}),
            'expected_outcomes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Expected outcomes'}),
            'budget': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Provide detailed budget'}),
            'budget_breakdown': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Breakdown of budget'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'detailed_proposal': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'supporting_documents': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'declaration': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'signature_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ConferenceTravelRequestForm(forms.ModelForm):

    """
    ConferenceTravelRequestForm is a Django ModelForm for the ConferenceTravelRequest model.
    - It manages conference travel funding applications by capturing essential details 
      such as conference information, participation type, research paper title, abstract, 
      budget, and supporting documents.
    - Date fields are formatted for easy input, while numeric fields capture budget 
      and expense details.
    - File upload fields support attaching acceptance letters and additional documents.
    - Includes fields for justification, funding confirmation, and dean’s approval, 
      ensuring a complete and standardized application process.
    """

    class Meta:
        model = ConferenceTravelRequest
        fields = [
            'title_of_conference',
            'conference_website',
            'organizers_name_affiliation',
            'conference_venue',
            'from_date',
            'to_date',
            'type_of_participation',
            'title_of_research_paper',
            'abstract',
            'acceptance_letter',
            'travel_choice',
            'travel_budget',
            'accommodation_details',
            'total_amount',
            'prev_fund_checkbox',
            'justification',
            'attachments',
            'dean_approval',
        ]
        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'to_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'abstract': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'justification': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'conference_website': forms.URLInput(attrs={'class': 'form-control'}),
            'travel_budget': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title_of_conference': 'Conference Title',
            'conference_website': 'Conference Website',
            'organizers_name_affiliation': 'Organizer’s Name & Affiliation',
            'conference_venue': 'Venue',
            'from_date': 'From Date',
            'to_date': 'To Date',
            'type_of_participation': 'Type of Participation',
            'title_of_research_paper': 'Research Paper Title',
            'abstract': 'Abstract',
            'acceptance_letter': 'Acceptance Letter',
            'travel_choice': 'Travel Choice',
            'travel_budget': 'Estimated Travel Budget',
            'accommodation_details': 'Accommodation Details',
            'total_amount': 'Total Amount',
            'prev_fund_checkbox': 'Previous Funding Confirmation',
            'justification': 'Justification',
            'attachments': 'Additional Attachments',
            'dean_approval': 'Dean’s Approval',
        }

class PublicationsUpdateForm(forms.ModelForm):

    """
    PublicationsUpdateForm is a Django ModelForm for the PublicationsUpdate model.
    - It captures publication details including title, authors, type, publisher, 
      year, DOI, abstract, and categories.
    - Text, number, and checkbox fields are styled for user-friendly input.
    - Designed for researchers to update their publication records efficiently 
      and confirm details before submission.
    """

    class Meta:
        model = PublicationsUpdate
        fields = [
            'title_of_publication',
            'authors',
            'type_of_publication',
            'publisher_name',
            'year_of_publication',
            'doi',
            'abstract',
            'categories',
            'checkbox',
        ]
        widgets = {
            'title_of_publication': forms.TextInput(attrs={'class': 'form-control'}),
            'authors': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_publication': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher_name': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_publication': forms.NumberInput(attrs={'class': 'form-control'}),
            'doi': forms.TextInput(attrs={'class': 'form-control'}),
            'abstract': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.TextInput(attrs={'class': 'form-control'}),
            'checkbox': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title_of_publication': 'Title of Publication',
            'authors': 'Authors',
            'type_of_publication': 'Type of Publication',
            'publisher_name': 'Publisher Name',
            'year_of_publication': 'Year of Publication',
            'doi': 'DOI',
            'abstract': 'Abstract',
            'categories': 'Categories',
            'checkbox': 'Confirm Details'
        }

class CurriculumDevelopmentForm(forms.ModelForm):

    """
    CurriculumDevelopmentForm is a Django ModelForm for the CurriculumDevelopment model.
    - It records course development activities, including course name, description, 
      duration, level, status, and timeline.
    - Uses text inputs, text areas, select dropdowns, and date pickers for structured entry.
    - Provides a standardized format for documenting curriculum contributions 
      within the institution.
    """

    class Meta:
        model = CurriculumDevelopment
        fields = '__all__'
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class SubmissionReviewForm(forms.ModelForm):
    """
    Form for reviewing faculty submissions
    """
    class Meta:
        model = FacultySubmission
        fields = ['status', 'review_comments']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'review_comments': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4,
                'placeholder': 'Enter your review comments here...'
            }),
        }


class SubmissionFilterForm(forms.Form):
    """
    Form for filtering submissions in review dashboard
    """
    STATUS_CHOICES = [
        ('', 'All Statuses'),
        ('pending', 'Pending Review'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('needs_revision', 'Needs Revision'),
    ]
    
    TYPE_CHOICES = [
        ('', 'All Types'),
        ('journal_publication', 'Journal Publication'),
        ('conference_publication', 'Conference Publication'),
        ('research_projects', 'Research Projects'),
        ('patents', 'Patents'),
        ('book', 'Book'),
        ('awards', 'Awards'),
    ]
    
    status = forms.ChoiceField(
        choices=STATUS_CHOICES, 
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    submission_type = forms.ChoiceField(
        choices=TYPE_CHOICES, 
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    department = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Filter by department'
        })
    )
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
        
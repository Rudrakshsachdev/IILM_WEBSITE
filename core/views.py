from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, LoginForm, ProfileCompletionForm, JournalPublicationForm, ConferencePublicationForm, ResearchProjectsForm, PatentsForm, CopyRightsForm, PhdGuidanceForm, BookChapterForm, BookForm, ConsultancyProjectsForm, EditorialRolesForm, ReviewerRolesForm, AwardsForm, IndustryCollaborationForm, UserFormProgressForm, AnnualFacultyReportForm, ResearchGrantApplicationForm, ConferenceTravelRequestForm, PublicationsUpdateForm, CurriculumDevelopmentForm
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth.decorators import login_required
from .models import UserOTP, JournalPublication
from django.contrib import messages

from .models import (
    JournalPublication, ConferencePublication, ResearchProjects, Patents, CopyRights, PhdGuidance, BookChapter, Book, ConsultancyProjects, EditorialRoles, ReviewerRoles, Awards, IndustryCollaboration, UserFormProgress, CustomUser, AnnualFacultyReport, ResearchGrantApplication, ConferenceTravelRequest, PublicationsUpdate, CurriculumDevelopment
)

from django.http import JsonResponse

otp_storage = {} # Temporary storage for OTPs

def signup_view(request):

    
    """
    Handles user registration with OTP (One-Time Password) verification.

    - For POST requests:
        1. Validates the submitted signup form.
        2. Generates a 6-digit OTP and stores it temporarily in `otp_storage` using the email as the key.
        3. Sends the OTP to the user's email address.
        4. Saves the submitted form data in the session for later use during verification.
        5. Redirects the user to the OTP verification page.

    - For GET requests:
        Displays an empty signup form for the user to fill out.
    """

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = str(random.randint(100000, 999999))
            otp_storage[email] = otp
            send_mail('Your OTP Code', f'Your OTP is {otp}', settings.EMAIL_HOST_USER, [email])
            request.session['signup_data'] = request.POST
            return render(request, 'verify_otp.html', {'email': email})
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



def verify_otp_view(request):

    """
    Handles OTP verification during user signup.
    - Retrieves email and entered OTP from POST data.
    - Compares with stored OTP for validation.
    - If valid, creates a new user, logs them in, and redirects to dashboard.
    - If invalid, re-renders OTP page with an error message.
    """
    email = request.POST.get('email')
    entered_otp = request.POST.get('otp')
    if otp_storage.get(email) == entered_otp:
        data = request.session.get('signup_data')
        form = SignupForm(data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    return render(request, 'verify_otp.html', {'email': email, 'error': 'Invalid OTP'})


def login_view(request):

    """
    Handles user login.
    - If the user is already authenticated, redirects to the dashboard.
    - Validates the login form on POST requests.
    - Logs in the user and redirects based on profile completion status.
    """

    if request.user.is_authenticated:
        return redirect('dashboard')  # If already logged in

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Check if profile is complete and redirect accordingly
            if not user.is_profile_complete:
                return redirect('profile_completion')
            return redirect('dashboard')
        else:
            # Add form errors to messages for debugging
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def resend_otp(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        try:
            user = CustomUser.objects.get(username=username)
            user_otp, created = UserOTP.objects.get_or_create(user=user)
            user_otp.generate_otp()
            send_mail(
                'Your OTP Code',
                f'Your new OTP is {user_otp.otp}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False
            )

            messages.success(request, 'OTP has been resent to your email.')
            return redirect('verify_otp')
        
        except CustomUser.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('resend_otp')
    
    return render(request, 'resend_otp.html')

def dashboard(request):
    """
    Displays the user dashboard.
    - Requires user authentication.
    - Shows user-specific information and statistics.
    """

    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    return render(request, 'dashboard.html', {'user': user})

@login_required
def profile_completion_view(request):

    """
    Handles profile completion for users.
    - If the user is already authenticated, redirects to the dashboard.
    - Displays a form for completing user profile information.
    """

    user = request.user

    if user.is_profile_complete:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, request.FILES, instance = user)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_profile_complete = True
            user.save()
            return redirect('dashboard')
    else:
        form = ProfileCompletionForm(instance = user)

    return render(request, 'complete_profile.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def view_profile(request):

    """
    Displays the user's profile information.
    - Requires user authentication.
    """

    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    return render(request, 'view_profile.html', {'user': user})



def journal_publication_view(request):


    """
    Handle journal publication form submission for authenticated users.

    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves journal publication details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty JournalPublicationForm.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = JournalPublicationForm(request.POST)
        if form.is_valid():
            journal_pub = form.save(commit=False)
            journal_pub.user = request.user  # 👈 Associate user
            journal_pub.save()
            messages.success(request, 'Journal publication details saved successfully.')

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.journal_publication = True
            progress.save()
            return redirect('dashboard')
    else:
        form = JournalPublicationForm()

    return render(request, 'journal_publication.html', {'form': form})

def conference_publication_view(request):

    """
    Handle conference publication form submission for authenticated users.

    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves conference publication details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty ConferencePublicationForm.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = ConferencePublicationForm(request.POST)

        if form.is_valid():
            conference_pub = form.save(commit=False)
            conference_pub.user = request.user  # 👈 Associate user
            conference_pub.save()  # Save the form data

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.conference_publication = True
            progress.save()  # Save the progress
            messages.success(request, 'Conference publication details saved successfully.')

            
            return redirect('dashboard')
    else:
        form = ConferencePublicationForm()

    return render(request, 'conference_publication.html', {'form': form})


def research_projects_view(request):

    """
    Handle research projects form submission for authenticated users.

    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves research project details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty ResearchProjectsForm.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template or redirect response
    """


    if request.method == 'POST':
        form = ResearchProjectsForm(request.POST)

        if form.is_valid():
            research_project = form.save(commit=False)
            research_project.user = request.user  # Associate user
            research_project.save()  # Save the form data

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.research_projects = True
            progress.save()  # Save the progress
            messages.success(request, 'Research project details saved successfully.')

            
            return redirect('dashboard')
    else:
        form = ResearchProjectsForm()

    return render(request, 'research_projects.html', {'form': form})



def patents_view(request):

    """
    Handle patents form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves patent details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty PatentsForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = PatentsForm(request.POST)

        if form.is_valid():
            patent = form.save(commit=False)
            patent.user = request.user  # Associate user
            patent.save()  # Save the form data
            
            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.patents = True
            progress.save()  # Save the progress
            messages.success(request, 'Patent details saved successfully.')
            return redirect('dashboard')
    else:
        form = PatentsForm()

    return render(request, 'patents.html', {'form': form})

def copyrights_view(request):

    """
    Handle copyrights form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves copyright details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty CopyRightsForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = CopyRightsForm(request.POST)

        if form.is_valid():
            copyright = form.save(commit=False)
            copyright.user = request.user  # Associate user
            copyright.save()

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.copyrights = True
            progress.save()  # Save the progress
            messages.success(request, 'Copyright details saved successfully.')
            return redirect('dashboard')
    else:
        form = CopyRightsForm()

    return render(request, 'copy_rights.html', {'form': form})

def phd_guidance_view(request):

    """
    Handle PhD guidance form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves PhD guidance details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty PhdGuidanceForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = PhdGuidanceForm(request.POST)

        if form.is_valid():
            phd_guidance = form.save(commit=False)
            phd_guidance.user = request.user  # Associate user
            phd_guidance.save()  # Save the form data

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.phd_guidance = True
            progress.save()  # Save the progress
            messages.success(request, 'PhD guidance details saved successfully.')
            return redirect('dashboard')
    else:
        form = PhdGuidanceForm()

    return render(request, 'phd_guidance_form.html', {'form': form})

def book_chapter_view(request):

    """
    Handle book chapter form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves book chapter details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty BookChapterForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = BookChapterForm(request.POST)

        if form.is_valid():
            book_chapter = form.save(commit=False)
            book_chapter.user = request.user  # Associate user
            book_chapter.save()  # Save the form data

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.book_chapter = True
            progress.save()  # Save the progress
            messages.success(request, 'Book chapter details saved successfully.')
            return redirect('dashboard')
    else:
        form = BookChapterForm()

    return render(request, 'bookchapter_form.html', {'form': form})

def book_view(request):
    """
    Handle book form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves book details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty BookForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user  # Associate user
            book.save()  # Save the form data

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.book = True
            progress.save()  # Save the progress
            
            messages.success(request, 'Book details saved successfully.')
            return redirect('dashboard')
    else:
        form = BookForm()

    return render(request, 'book_form.html', {'form': form})

def consultancy_projects_view(request):

    """
    Handle consultancy projects form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves consultancy project details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty ConsultancyProjectsForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = ConsultancyProjectsForm(request.POST)

        if form.is_valid():
            consultancy_project = form.save(commit=False)
            consultancy_project.user = request.user  # Associate user
            consultancy_project.save()  # Save the form data
            
            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.consultancy_projects = True
            progress.save()  # Save the progress
            messages.success(request, 'Consultancy project details saved successfully.')
            return redirect('dashboard')
    else:
        form = ConsultancyProjectsForm()

    return render(request, 'consultancy_project.html', {'form': form})

def editorial_roles_view(request):

    """
    Handle editorial roles form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves editorial role details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty EditorialRolesForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = EditorialRolesForm(request.POST)

        if form.is_valid():
            editorial_role = form.save(commit=False)
            editorial_role.user = request.user  # Associate user
            editorial_role.save()

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.editorial_roles = True
            progress.save()
            messages.success(request, 'Editorial role details saved successfully.')
            return redirect('dashboard')
    else:
        form = EditorialRolesForm()

    return render(request, 'editorial_roles.html', {'form': form})


def reviewer_roles_view(request):

    """
    Handle reviewer roles form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves reviewer role details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty ReviewerRolesForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = ReviewerRolesForm(request.POST)

        if form.is_valid():
            reviewer_role = form.save(commit=False)
            reviewer_role.user = request.user  # Associate user
            reviewer_role.save()

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.reviewer_roles = True
            progress.save()
            messages.success(request, 'Reviewer role details saved successfully.')
            return redirect('dashboard')
    else:
        form = ReviewerRolesForm()

    return render(request, 'reviewer_roles.html', {'form': form})


def awards_view(request):

    """
    Handle awards form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves award details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty AwardsForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = AwardsForm(request.POST)

        if form.is_valid():
            award = form.save(commit=False)
            award.user = request.user  # Associate user
            award.save()

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.awards = True
            progress.save()
            messages.success(request, 'Award details saved successfully.')
            return redirect('dashboard')
    else:
        form = AwardsForm()

    return render(request, 'award_form.html', {'form': form})

def industry_collaboration_view(request):

    """
    Handle industry collaboration form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves industry collaboration details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty IndustryCollaborationForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = IndustryCollaborationForm(request.POST)

        if form.is_valid():
            industry_collaboration = form.save(commit=False)
            industry_collaboration.user = request.user  # Associate user
            industry_collaboration.save()

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.industry_collaboration = True
            progress.save()
            messages.success(request, 'Industry collaboration details saved successfully.')
            return redirect('dashboard')
    else:
        form = IndustryCollaborationForm()

    return render(request, 'industry_collaboration.html', {'form': form})


def form_view(request):
    
    return render(request, 'form_page.html')

def annual_faculty_report_view(request):

    """
    Handle annual faculty report form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves annual report details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty AnnualFacultyReportForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = AnnualFacultyReportForm(request.POST, request.FILES)

        if form.is_valid():
            annual_report = form.save(commit=False)
            annual_report.user = request.user  # Associate user
            annual_report.save()

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.annual_faculty_report = True
            progress.save()
            messages.success(request, 'Annual faculty report details saved successfully.')
            return redirect('dashboard')
    else:
        form = AnnualFacultyReportForm()

    return render(request, 'Annual_faculty.html', {'form': form})

def research_grant_application_view(request):

    """
    Handle research grant application form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves research grant application details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty ResearchGrantApplicationForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = ResearchGrantApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            research_grant = form.save(commit=False)
            research_grant.user = request.user  # Associate user
            research_grant.save()

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.research_grant_application = True
            progress.save()
            messages.success(request, 'Research grant application details saved successfully.')
            return redirect('dashboard')
    else:
        form = ResearchGrantApplicationForm()

    return render(request, 'research_grant.html', {'form': form})

def conference_travel_request_view(request):

    """
    Handle conference travel request form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves conference travel request details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty ConferenceTravelRequestForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = ConferenceTravelRequestForm(request.POST, request.FILES)

        if form.is_valid():
            travel_request = form.save(commit=False)
            travel_request.user = request.user  # Associate user
            travel_request.save()

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.conference_travel_request = True
            progress.save()
            messages.success(request, 'Conference travel request details saved successfully.')
            return redirect('dashboard')
    else:
        form = ConferenceTravelRequestForm()

    return render(request, 'conference_travel.html', {'form': form})

def publications_update_view(request):

    """
    Handle publications update form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves publications update details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty PublicationsUpdateForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = PublicationsUpdateForm(request.POST)

        if form.is_valid():
            publications_update = form.save(commit=False)
            publications_update.user = request.user  # Associate user
            publications_update.save()

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.publications_update = True
            progress.save()
            messages.success(request, 'Publications update details saved successfully.')
            return redirect('dashboard')
    else:
        form = PublicationsUpdateForm()

    return render(request, 'Publications_update.html', {'form': form})

def curriculum_development_view(request):

    """
    Handle curriculum development form submission for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: validates and saves curriculum development details linked to the user,
      updates progress tracking, and redirects to the dashboard.
    - On GET: displays an empty CurriculumDevelopmentForm.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    if request.method == 'POST':
        form = CurriculumDevelopmentForm(request.POST, request.FILES)

        if form.is_valid():
            curriculum = form.save(commit=False)
            curriculum.user = request.user  # Associate user
            curriculum.save()

            progress, created = UserFormProgress.objects.get_or_create(user=request.user)
            progress.curriculum_development = True
            progress.save()
            messages.success(request, 'Curriculum development details saved successfully.')
            return redirect('dashboard')
    else:
        form = CurriculumDevelopmentForm()

    return render(request, 'curriculum_development.html', {'form': form})

def submission_list_view(request):


    """
    Handle submission list view for authenticated users.
    - Redirects to login if the user is not authenticated.
    - Displays a list of all submissions made by the user.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Rendered template or redirect response.
    """

    user = request.user # Ensure user is authenticated
    journals = JournalPublication.objects.all()
    conferences = ConferencePublication.objects.all()
    research_projects = ResearchProjects.objects.all()
    patents = Patents.objects.all()
    copyrights = CopyRights.objects.all()
    phd_guidance = PhdGuidance.objects.all()
    book_chapters = BookChapter.objects.all()
    books = Book.objects.all()
    consultancy_projects = ConsultancyProjects.objects.all()
    editorial_roles = EditorialRoles.objects.all()
    reviewer_roles = ReviewerRoles.objects.all()
    awards = Awards.objects.all()
    industry_collaborations = IndustryCollaboration.objects.all()
    return render(request, 'submissions.html', {
        'journals': journals,
        'conferences': conferences,
        'research_projects': research_projects,
        'patents': patents,
        'copyrights': copyrights,
        'phd_guidance': phd_guidance,
        'book_chapters': book_chapters,
        'books': books,
        'consultancy_projects': consultancy_projects,
        'editorial_roles': editorial_roles,
        'reviewer_roles': reviewer_roles,
        'awards': awards,
        'industry_collaborations': industry_collaborations,
    })

@login_required
def update_progress(request):

    """
    Handle progress update for authenticated users.
    - Redirects to login if the user is not authenticated.
    - On POST: updates the user's progress based on form data.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: JSON response indicating success or failure.
    """

    if request.method == "POST":
        field = request.POST.get("field")  # e.g., 'journal_publication_progress'
        value = request.POST.get("value").lower() == "true"  # convert to boolean

        progress, created = UserFormProgress.objects.get_or_create(user=request.user)
        if hasattr(progress, field):
            setattr(progress, field, value)
            progress.save()

            # calculate completion %
            fields = [f.name for f in UserFormProgress._meta.get_fields() if f.name.endswith("_progress")]
            total_fields = len(fields)
            completed_fields = sum(getattr(progress, f) for f in fields)
            percent = int((completed_fields / total_fields) * 100)

            return JsonResponse({
                "success": True,
                "field": field,
                "value": value,
                "percent": percent
            })

    return JsonResponse({"success": False}, status=400)
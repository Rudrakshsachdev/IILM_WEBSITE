# Faculty Portal - IILM University

A comprehensive Django-based Faculty Portal system designed for IILM University to manage faculty information, research activities, publications, and administrative tasks.

## 🚀 Features

### Authentication & User Management

- **Custom User Authentication**: Extended Django's user model with faculty-specific fields
- **OTP-based Verification**: Secure email-based OTP system for registration and login
- **Profile Management**: Complete faculty profile with academic information
- **Forced Profile Completion**: Middleware ensures all faculty complete their profiles

### Faculty Information Management

- Personal details with profile pictures
- Academic qualifications and specializations
- Department and designation tracking
- Research identifiers (ORCID, Scopus, Google Scholar, Vidwaan ID)

### Research & Publications Management

- **Journal Publications**: Track research papers with DOI, indexing details
- **Conference Publications**: Manage conference presentations and papers
- **Book Publications**: Record authored books and book chapters
- **Patents & Copyrights**: Intellectual property management
- **Research Projects**: Project tracking with funding details
- **Research Grants**: Grant application and management system

### Academic Activities

- **PhD Guidance**: Track doctoral student supervision
- **Editorial Roles**: Journal editorial positions
- **Reviewer Roles**: Peer review activities
- **Awards & Recognition**: Achievement tracking
- **Industry Collaboration**: Partnership and consultancy projects
- **Curriculum Development**: Course development activities
- **Conference Travel**: Travel request and reimbursement

### Reporting & Analytics

- **Annual Faculty Reports**: Comprehensive yearly activity reports
- **Publication Updates**: Regular publication tracking
- **Dashboard Analytics**: Visual representation of faculty activities

## 🛠️ Technology Stack

- **Backend**: Django 5.2.3
- **Database**: SQLite (default), MySQL support available
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Django's built-in auth with custom extensions
- **Email**: SMTP integration for OTP delivery
- **File Handling**: Django's file management system
- **PDF Generation**: ReportLab for document generation
- **Data Processing**: Pandas, NumPy for analytics

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git
- Email server configuration (Gmail SMTP recommended)

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd IILM_WEBSITE
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure email settings**
   Edit `Faculty_Portal/Faculty_Portal/settings.py`:

   ```python
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your-app-password'
   ```

5. **Database setup**

   ```bash
   cd Faculty_Portal
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## 📁 Project Structure

```
IILM_WEBSITE/
├── Faculty_Portal/                 # Main Django project
│   ├── core/                      # Core application
│   │   ├── migrations/            # Database migrations
│   │   ├── models.py              # Data models
│   │   ├── views.py               # View controllers
│   │   ├── forms.py               # Django forms
│   │   ├── urls.py                # URL routing
│   │   └── admin.py               # Admin interface
│   ├── Faculty_Portal/            # Project settings
│   │   ├── settings.py            # Configuration
│   │   ├── urls.py                # Main URL routing
│   │   └── wsgi.py                # WSGI configuration
│   ├── templates/                 # HTML templates
│   ├── static/                    # Static files (CSS, JS, images)
│   ├── media/                     # User uploads
│   └── manage.py                  # Django management script
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🔐 Security Features

- CSRF protection enabled
- Secure password validation (configurable)
- Email-based OTP authentication
- Session management
- File upload validation
- SQL injection protection via Django ORM

## 📊 Key Models

### CustomUser

Extended user model with faculty-specific fields:

- School, Department, Designation
- Academic qualifications and specializations
- Research identifiers (ORCID, Scopus, etc.)
- Profile completion tracking

### Publication Models

- `JournalPublication`: Research papers and articles
- `ConferencePublication`: Conference presentations
- `Book`: Authored books
- `BookChapter`: Book chapter contributions

### Research Models

- `ResearchProjects`: Active and completed projects
- `Patents`: Intellectual property
- `CopyRights`: Copyright registrations
- `ResearchGrantApplication`: Funding applications

## 🎯 Usage

### For Faculty Members

1. **Registration**: Sign up with institutional email
2. **OTP Verification**: Complete email verification
3. **Profile Setup**: Fill complete academic profile
4. **Data Entry**: Add publications, research projects, and activities
5. **Annual Reports**: Generate comprehensive yearly reports

### For Administrators

1. **Admin Panel**: Access Django admin interface
2. **User Management**: Manage faculty accounts
3. **Data Export**: Extract reports and analytics
4. **System Configuration**: Modify settings and permissions

## 🔄 API Endpoints

### Authentication

- `/signup/` - Faculty registration
- `/login/` - User authentication
- `/logout/` - Session termination
- `/verify-otp/` - OTP verification

### Profile Management

- `/dashboard/` - Main faculty dashboard
- `/complete-profile/` - Profile completion form
- `/view-profile/` - Profile display

### Research & Publications

- `/journal-publication/` - Add journal papers
- `/conference-publication/` - Add conference papers
- `/research-projects/` - Manage research projects
- `/patents/` - Patent management
- `/annual-faculty-report/` - Generate annual reports

## 🚀 Deployment

### Development

```bash
python manage.py runserver
```

### Production

1. **Environment Variables**

   ```bash
   export DEBUG=False
   export SECRET_KEY='your-secret-key'
   export DATABASE_URL='your-database-url'
   ```

2. **Static Files**

   ```bash
   python manage.py collectstatic
   ```

3. **Database Migration**

   ```bash
   python manage.py migrate
   ```

4. **Web Server**: Use Gunicorn with Nginx
   ```bash
   gunicorn Faculty_Portal.wsgi:application
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Testing

Run the test suite:

```bash
python manage.py test
```

For specific app testing:

```bash
python manage.py test core
```

## 🐛 Troubleshooting

### Common Issues

1. **Email OTP not working**

   - Check Gmail app password configuration
   - Verify SMTP settings in settings.py

2. **Database migration errors**

   ```bash
   python manage.py makemigrations --empty core
   python manage.py migrate --fake-initial
   ```

3. **Static files not loading**

   ```bash
   python manage.py collectstatic --clear
   ```

4. **Profile completion middleware issues**
   - Check middleware order in settings.py
   - Verify URL patterns in urls.py

## 📞 Support

For technical support or questions:

- **Email**: [rudrakshsachdeva.dev@gmail.com]


## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏛️ About IILM University

This Faculty Portal is developed for IILM University to streamline faculty management and research tracking processes. It provides a comprehensive platform for faculty members to maintain their academic profiles and research activities.

---

**Version**: 1.0.0  
**Last Updated**: August 2025  
**Maintained by**: IILM University IT Department

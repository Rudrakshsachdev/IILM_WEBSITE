# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SubmissionReview, FacultySubmission

@receiver(post_save, sender=SubmissionReview)
def update_submission_status(sender, instance, created, **kwargs):
    if created:
        status_map = {
            'reviewed': 'under_review',
            'approved': 'approved',
            'rejected': 'rejected',
            'revision_requested': 'needs_revision',
            'resubmitted': 'pending',
        }
        new_status = status_map.get(instance.action)
        if new_status:
            instance.submission.status = new_status
            instance.submission.save(update_fields=['status'])

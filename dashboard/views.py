
from django.shortcuts import render
from donors.models import Donor
from blood_requests.models import BloodRequest


def home(request):
    context = {
        'donor_count': Donor.objects.count(),
        'request_count': BloodRequest.objects.count(),
        'pending_requests': BloodRequest.objects.filter(
            status='Pending'
        ).count(),
    }

    return render(request, 'dashboard/home.html', context)

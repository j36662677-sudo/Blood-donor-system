
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q

from .models import BloodRequest
from .forms import BloodRequestForm


@login_required
def create_request(request):

    if request.method == 'POST':
        form = BloodRequestForm(request.POST)

        if form.is_valid():
            blood_request = form.save(commit=False)
            blood_request.user = request.user
            blood_request.save()

            messages.success(request, 'Blood request sent successfully!')
            return redirect('request_list')

    else:
        form = BloodRequestForm(
            initial={'donor': request.GET.get('donor_id')}
        )

    return render(request, 'blood_requests/create_request.html', {
        'form': form
    })


@login_required
def request_list(request):

    requests = BloodRequest.objects.filter(
        Q(user=request.user) |
        Q(donor__user=request.user)
    ).distinct().order_by('-created_at')

    return render(request, 'blood_requests/request_list.html', {
        'requests': requests
    })


@login_required
@require_POST
def update_status(request, request_id):

    blood_request = get_object_or_404(
        BloodRequest,
        id=request_id,
        donor__user=request.user
    )

    new_status = request.POST.get('status')

    if new_status in ['Accepted', 'Rejected']:
        if blood_request.status == 'Pending':
            blood_request.status = new_status
            blood_request.save(update_fields=['status'])

            messages.success(
                request,
                f'Request {new_status.lower()} successfully!'
            )

    return redirect('request_list')

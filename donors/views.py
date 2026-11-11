
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DonorForm
from .models import Donor


def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)

        if form.is_valid():
            donor = form.save(commit=False)

            if request.user.is_authenticated:
                donor.user = request.user

            donor.save()
            messages.success(
                request,
                'Donor details added successfully!'
            )
            return redirect('donor_list')
    else:
        form = DonorForm()

    return render(request, 'donors/add_donor.html', {
        'form': form
    })


@login_required
def edit_donor(request, donor_id):
    donor = get_object_or_404(
        Donor,
        id=donor_id,
        user=request.user
    )

    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Donor details updated successfully!'
            )
            return redirect('donor_list')
    else:
        form = DonorForm(instance=donor)

    return render(request, 'donors/edit_donor.html', {
        'form': form,
        'donor': donor
    })


def donor_list(request):
    donors = Donor.objects.all()

    return render(request, 'donors/donor_list.html', {
        'donors': donors
    })


def search_donors(request):
    donors = Donor.objects.all()

    blood_group = request.GET.get('blood_group', '').strip()
    location = request.GET.get('location', '').strip()
    availability = request.GET.get('availability', '')

    if blood_group:
        donors = donors.filter(
            blood_group__iexact=blood_group
        )

    if location:
        donors = donors.filter(
            location__icontains=location
        )

    if availability == 'yes':
        donors = donors.filter(is_available=True)
    elif availability == 'no':
        donors = donors.filter(is_available=False)

    return render(request, 'donors/search_donors.html', {
        'donors': donors,
        'blood_group': blood_group,
        'location': location,
        'availability': availability,
    })

@login_required
def delete_donor(request, donor_id):
    donor = get_object_or_404(
        Donor,
        id=donor_id,
        user=request.user
    )

    if request.method == 'POST':
        donor.delete()
        messages.success(
            request,
            'Donor details deleted successfully!'
        )
        return redirect('donor_list')

    return render(request, 'donors/delete_donor.html', {
        'donor': donor
    })

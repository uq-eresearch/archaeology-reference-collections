from django.shortcuts import render, get_object_or_404
from apps.botanycollection.models import Accession


def accession_detail(request, num):
    acc = get_object_or_404(Accession, uq_accession=num)

    context = {
        'accession': acc
    }

    return render(request, 'accession/detail.html', context)


from django.shortcuts import render
from .forms import CCTVPricingForm


def cctv_quote_view(request):
    total = None
    selected_items = []

    if request.method == 'POST':
        form = CCTVPricingForm(request.POST)
        if form.is_valid():
            camera = form.cleaned_data['camera']
            cable = form.cleaned_data['cable']
            recorder = form.cleaned_data['recorder']
            channel = form.cleaned_data['channel']
            poe = form.cleaned_data['poe']

            selected_items = [camera, cable, recorder, channel, poe]
            total = sum(item.price for item in selected_items)

    else:
        form = CCTVPricingForm()

    return render(request, 'cctv_quote.html', {
        'form': form,
        'total': total,
        'selected_items': selected_items
    })
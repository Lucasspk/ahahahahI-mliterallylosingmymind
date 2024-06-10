# views.py
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from .models import GPU, CPU, PSU, Motherboard
from .forms import ComponentChoiceForm, GPUFilterForm, CPUFilterForm, PSUFilterForm, MotherboardFilterForm



import logging

logger = logging.getLogger(__name__)



def filter_components(request):
    component_choice_form = ComponentChoiceForm(request.GET or None)
    filter_forms = {
        'gpu': GPUFilterForm(request.GET if 'gpu' in request.GET.get('component_type', '') else None),
        'cpu': CPUFilterForm(request.GET if 'cpu' in request.GET.get('component_type', '') else None),
        'psu': PSUFilterForm(request.GET if 'psu' in request.GET.get('component_type', '') else None),
        'motherboard': MotherboardFilterForm(request.GET if 'motherboard' in request.GET.get('component_type', '') else None),
    }
    selected_component_type = None
    components = []

    if component_choice_form.is_valid():
        selected_component_type = component_choice_form.cleaned_data['component_type']
        filter_form = filter_forms[selected_component_type]

        if filter_form.is_valid():
            if selected_component_type == 'gpu':
                components = GPU.objects.all()
                price_weight = filter_form.cleaned_data.get('price_weight', 1) or 1
                power_weight = filter_form.cleaned_data.get('power_weight', 1) or 1
                gaming_performance_weight = filter_form.cleaned_data.get('gaming_performance_weight', 1) or 1
                memory_size_weight = filter_form.cleaned_data.get('memory_size_weight', 1) or 1
                core_clock_weight = filter_form.cleaned_data.get('core_clock_weight', 1) or 1

                for component in components:
                    component.point_value = (
                        price_weight * (component.price or 0) +
                        power_weight * (component.AvgPower or 0) +
                        gaming_performance_weight * (component.raw_gaming_performance() or 0) +
                        memory_size_weight * (component.memory_size or 0) +
                        core_clock_weight * (component.core_clock or 0)
                    )
                components = sorted(components, key=lambda x: x.point_value, reverse=True)

            elif selected_component_type == 'cpu':
                components = CPU.objects.all()
                price_weight = filter_form.cleaned_data.get('price_weight', 1) or 1
                power_weight = filter_form.cleaned_data.get('power_weight', 1) or 1
                gaming_performance_weight = filter_form.cleaned_data.get('gaming_performance_weight', 1) or 1
                cores_weight = filter_form.cleaned_data.get('cores_weight', 1) or 1
                clock_speed_weight = filter_form.cleaned_data.get('clock_speed_weight', 1) or 1

                for component in components:
                    component.point_value = (
                        price_weight * (component.price or 0) +
                        power_weight * (component.AvgPower or 0) +
                        gaming_performance_weight * (component.raw_gaming_performance() or 0) +
                        cores_weight * (component.cores or 0) +
                        clock_speed_weight * (component.clock_speed or 0)
                    )
                components = sorted(components, key=lambda x: x.point_value, reverse=True)

            # Similarly handle PSU and Motherboard

    context = {
        'component_choice_form': component_choice_form,
        'filter_form': filter_forms[selected_component_type] if selected_component_type else None,
        'selected_component_type': selected_component_type,
        'components': components,
    }
    return render(request, 'filter_components.html', context)
def update_components(request):
    component_type = request.POST.get('component_type', '')
    price_weight = float(request.POST.get('price_weight', 1))
    power_weight = float(request.POST.get('power_weight', 1))
    # Get other weighting values in a similar way

    components = []
    if component_type == 'gpu':
        components = GPU.objects.all()
        for component in components:
            component.point_value = (
                price_weight * (component.price or 0) +
                power_weight * (component.AvgPower or 0)
                # Add other point value calculations here
            )
            component.save()  # Save the updated component

    elif component_type == 'cpu':
        components = CPU.objects.all()
        for component in components:
            component.point_value = (
                price_weight * (component.price or 0) +
                power_weight * (component.AvgPower or 0)
                # Add other point value calculations here
            )
            component.save()  # Save the updated component

    elif component_type == 'psu':
        components = PSU.objects.all()
        for component in components:
            component.point_value = (
                price_weight * (component.price or 0) +
                power_weight * (component.AvgPower or 0)
                # Add other point value calculations here
            )
            component.save()  # Save the updated component

    elif component_type == 'motherboard':
        components = Motherboard.objects.all()
        for component in components:
            component.point_value = (
                price_weight * (component.price or 0) +
                power_weight * (component.AvgPower or 0)
                # Add other point value calculations here
            )
            component.save()  # Save the updated component

    # Sort the components based on their new point values
    components = sorted(components, key=lambda x: x.point_value, reverse=True)

     # Render the updated component list as HTML
    component_list_html = render_to_string('component_list.html', {'components': components})

    # Return the updated component list as JSON
    return JsonResponse({'component_list_html': component_list_html})





def get_components(request):
    components = components.objects.all()  # Retrieve updated components
    component_list_html = render_to_string('component_list.html', {'components': components})
    return HttpResponse(component_list_html)


def index(request):
    return render(request, 'index.html')
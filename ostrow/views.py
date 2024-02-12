from rest_framework import viewsets, permissions
from .serializers import LicznikBazowyOstrowSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import StanPaliwSaveForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import DostawaOstrow, LicznikDostawyOstrow, LicznikBazowyOstrow, DaneStacjiOstrow
from django.contrib import messages
from common.untils import send_my_email, send_my_email_modified


@login_required
@permission_required('ostrow.view_licznikbazowyostrow')
def licz_list(request):
    if request.user.is_authenticated:
        liczniki = LicznikBazowyOstrow.objects.order_by("ID_DYS", "ID_WAZ")
        q = request.GET.get("qre")
        if q:
            liczniki = liczniki.filter(SYMBOL__icontains=q)

        return render(request, 'ostrow/liczniki.html', {"liczniki": liczniki})
    return redirect(reverse('login'))


@login_required
@permission_required('ostrow.view_dostawaostrow')
def dostawy_list(request):
    if request.user.is_authenticated:
        lista = DostawaOstrow.objects.all().order_by('-number')
        paginator = Paginator(lista, 12)
        page_number = request.GET.get('page')
        lista_dost = paginator.get_page(page_number)
        return render(request, 'ostrow/list_dostawy.html', {'lista': lista_dost})
    return redirect(reverse('login'))


@login_required
@permission_required('ostrow.view_dostawaostrow')#, raise_exception=True)
def dostawy_details(request, stany_id):
    if request.user.is_authenticated:
        stan = DostawaOstrow.objects.get(number=stany_id)
        created = stan.created.ctime()
        modified = stan.modified.ctime()
        liczniki = LicznikDostawyOstrow.objects.filter(number=stany_id).order_by("ID_DYS", "ID_WAZ")
        q = request.GET.get("qre")
        if q:
            liczniki = liczniki.filter(SYMBOL__icontains=q)
        context = {'stan': stan, 'liczniki': liczniki, 'created': created, 'modified': modified}
        return render(request, 'ostrow/dostawy_details.html', context)
    return redirect(reverse('login'))


@login_required
@permission_required('ostrow.change_dostawaostrow')
def edit_dostawy(request, stany_id):
    if request.user.is_authenticated:
        user = request.user
        name_stacji = get_object_or_404(DaneStacjiOstrow)
        dostawa = get_object_or_404(DostawaOstrow, pk=stany_id)
        liczniki = LicznikDostawyOstrow.objects.filter(number=stany_id).order_by("ID_DYS", "ID_WAZ")
        if request.method == "POST":
            form = StanPaliwSaveForm(request.POST, instance=dostawa)
            if form.is_valid():
                form.save()
                messages.success(request, 'Poprawa dostawa została zapisana w bazie.')
                try:
                    send_my_email_modified(dostawa.number, user.first_name, name_stacji)
                    messages.success(request, 'Powiadomienie edycji dostawy zostało wysłane na email.')

                except:
                    messages.warning(request, 'Powiadomienie edycji dostawy nie zostało wysłane na email.')
            return HttpResponseRedirect(reverse("ostrow:dost_ostrow"))
        else:
            form = StanPaliwSaveForm(instance=dostawa)
        context = {'lista': dostawa, 'liczniki': liczniki, 'form': form}
        return render(request, 'ostrow/liczniki_add.html', context)
    return redirect(reverse('login'))


@login_required
@permission_required('ostrow.add_dostawaostrow')
def handle_licz(request):
    if request.user.is_authenticated:
        liczniki = LicznikBazowyOstrow.objects.order_by("ID_DYS", "ID_WAZ")
        num = DostawaOstrow.objects.last()
        name_stacji = get_object_or_404(DaneStacjiOstrow)
        lista = []
        if not num:
            num = 1
        else:
            num = num.number + 1
        form_st = StanPaliwSaveForm(initial={'number': num})
        user = request.user
        if request.method == 'POST':
            if user.is_authenticated:
                if request.POST.get('stan_save'):
                    form_st.helper.form_action = reverse("ostrow:add_liczniki")
                    form_st = StanPaliwSaveForm(request.POST)
                    if form_st.is_valid():
                        form_st.save()
                        lista = DostawaOstrow.objects.get(number=num)
                        for licz in liczniki:
                            LicznikDostawyOstrow.objects.create(ID_DYS=licz.ID_DYS,
                                                                     ID_WAZ=licz.ID_WAZ,
                                                                     SYMBOL=licz.SYMBOL,
                                                                     TOTAL=licz.TOTAL,
                                                                     ARTYKUL=licz.ARTYKUL,
                                                                     KIEDY=licz.KIEDY,
                                                                     KIEDY_WGR=licz.KIEDY_WGR,
                                                                     number=lista)
                        messages.success(request, 'Dostawa została zapisana w bazie.')
                        try:
                            send_my_email(lista.dostawca, user.first_name, name_stacji)
                            messages.success(request, 'Powiadomienie dodania dostawy zostało wysłane na email.')
                        except:
                            messages.warning(request, 'Powiadomienie dodania dostawy nie zostało wysłane na email.')
                    return HttpResponseRedirect(reverse("ostrow:dost_ostrow"))

            return redirect(reverse('login'))
        context = {'lista': lista, 'liczniki': liczniki, 'form': form_st}
        return render(request, 'ostrow/liczniki_add.html', context)
    return redirect(reverse('login'))


class LicznikBazowyOstrowViewSet(viewsets.ModelViewSet):
    queryset = LicznikBazowyOstrow.objects.all()
    serializer_class = LicznikBazowyOstrowSerializer
    permission_classes = [permissions.DjangoModelPermissions, permissions.IsAuthenticated]
    # authentication_classes = [permissions.IsAuthenticated]

from rest_framework import viewsets, permissions
from .serializers import LicznikBazowyJaroslawSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import StanPaliwSaveForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import DostawaJaroslaw, LicznikDostawyJaroslaw, LicznikBazowyJaroslaw, DaneStacjiJaroslaw
from django.contrib import messages
from common.untils import send_my_email, send_my_email_modified


@login_required
@permission_required('jaroslaw.view_licznikbazowyjaroslaw')
def licz_list(request):
    if request.user.is_authenticated:
        liczniki = LicznikBazowyJaroslaw.objects.order_by("ID_DYS", "ID_WAZ")
        q = request.GET.get("qre")
        if q:
            liczniki = liczniki.filter(SYMBOL__icontains=q)

        return render(request, 'jaroslaw/liczniki.html', {"liczniki": liczniki})
    return redirect(reverse('login'))


@login_required
@permission_required('jaroslaw.view_dostawajaroslaw')
def dostawy_list(request):
    if request.user.is_authenticated:
        lista = DostawaJaroslaw.objects.all().order_by('-number')
        paginator = Paginator(lista, 12)
        page_number = request.GET.get('page')
        lista_dost = paginator.get_page(page_number)
        return render(request, 'jaroslaw/list_dostawy.html', {'lista': lista_dost})
    return redirect(reverse('login'))


@login_required
@permission_required('jaroslaw.view_dostawajaroslaw')#, raise_exception=True)
def dostawy_details(request, stany_id):
    if request.user.is_authenticated:
        stan = DostawaJaroslaw.objects.get(number=stany_id)
        created = stan.created.ctime()
        modified = stan.modified.ctime()
        liczniki = LicznikDostawyJaroslaw.objects.filter(number=stany_id).order_by("ID_DYS", "ID_WAZ")
        q = request.GET.get("qre")
        if q:
            liczniki = liczniki.filter(SYMBOL__icontains=q)
        context = {'stan': stan, 'liczniki': liczniki, 'created': created, 'modified': modified}
        return render(request, 'jaroslaw/dostawy_details.html', context)
    return redirect(reverse('login'))


@login_required
@permission_required('jaroslaw.change_dostawajaroslaw')
def edit_dostawy(request, stany_id):
    if request.user.is_authenticated:
        user = request.user
        name_stacji = get_object_or_404(DaneStacjiJaroslaw)
        dostawa = get_object_or_404(DostawaJaroslaw, pk=stany_id)
        liczniki = LicznikDostawyJaroslaw.objects.filter(number=stany_id).order_by("ID_DYS", "ID_WAZ")
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
            return HttpResponseRedirect(reverse("jaroslaw:dost_jaroslaw"))
        else:
            form = StanPaliwSaveForm(instance=dostawa)
        context = {'lista': dostawa, 'liczniki': liczniki, 'form': form}
        return render(request, 'jaroslaw/liczniki_add.html', context)
    return redirect(reverse('login'))


@login_required
@permission_required('jaroslaw.add_dostawajaroslaw')
def handle_licz(request):
    if request.user.is_authenticated:
        liczniki = LicznikBazowyJaroslaw.objects.order_by("ID_DYS", "ID_WAZ")
        num = DostawaJaroslaw.objects.last()
        name_stacji = get_object_or_404(DaneStacjiJaroslaw)
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
                    form_st.helper.form_action = reverse("jaroslaw:add_liczniki")
                    form_st = StanPaliwSaveForm(request.POST)
                    if form_st.is_valid():
                        form_st.save()
                        lista = DostawaJaroslaw.objects.get(number=num)
                        for licz in liczniki:
                            LicznikDostawyJaroslaw.objects.create(ID_DYS=licz.ID_DYS,
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
                    return HttpResponseRedirect(reverse("jaroslaw:dost_jaroslaw"))

            return redirect(reverse('login'))
        context = {'lista': lista, 'liczniki': liczniki, 'form': form_st}
        return render(request, 'jaroslaw/liczniki_add.html', context)
    return redirect(reverse('login'))


class LicznikBazowyJaroslawViewSet(viewsets.ModelViewSet):
    queryset = LicznikBazowyJaroslaw.objects.all()
    serializer_class = LicznikBazowyJaroslawSerializer
    permission_classes = [permissions.DjangoModelPermissions, permissions.IsAuthenticated]
    # authentication_classes = [permissions.IsAuthenticated]

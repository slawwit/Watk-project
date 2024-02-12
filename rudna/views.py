from rest_framework import viewsets, permissions
from .serializers import LicznikBazowyRudnaSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import StanPaliwSaveForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import DostawaRudna, LicznikDostawyRudna, LicznikBazowyRudna, DaneStacjiRudna
from django.contrib import messages
from common.untils import send_my_email, send_my_email_modified


@login_required
@permission_required('rudna.view_licznikbazowyrudna')
def licz_list(request):
    if request.user.is_authenticated:
        liczniki = LicznikBazowyRudna.objects.order_by("ID_DYS", "ID_WAZ")
        q = request.GET.get("qre")
        if q:
            liczniki = liczniki.filter(SYMBOL__icontains=q)

        return render(request, 'rudna/liczniki.html', {"liczniki": liczniki})
    return redirect(reverse('login'))


@login_required
@permission_required('rudna.view_dostawarudna')
def dostawy_list(request):
    if request.user.is_authenticated:
        lista = DostawaRudna.objects.all().order_by('-number')
        paginator = Paginator(lista, 12)
        page_number = request.GET.get('page')
        lista_dost = paginator.get_page(page_number)
        return render(request, 'rudna/list_dostawy.html', {'lista': lista_dost})
    return redirect(reverse('login'))


@login_required
@permission_required('rudna.view_dostawarudna')#, raise_exception=True)
def dostawy_details(request, stany_id):
    if request.user.is_authenticated:
        stan = DostawaRudna.objects.get(number=stany_id)
        created = stan.created.ctime()
        modified = stan.modified.ctime()
        liczniki = LicznikDostawyRudna.objects.filter(number=stany_id).order_by("ID_DYS", "ID_WAZ")
        q = request.GET.get("qre")
        if q:
            liczniki = liczniki.filter(SYMBOL__icontains=q)
        context = {'stan': stan, 'liczniki': liczniki, 'created': created, 'modified': modified}
        return render(request, 'rudna/dostawy_details.html', context)
    return redirect(reverse('login'))


@login_required
@permission_required('rudna.change_dostawarudna')
def edit_dostawy(request, stany_id):
    if request.user.is_authenticated:
        user = request.user
        name_stacji = get_object_or_404(DaneStacjiRudna)
        dostawa = get_object_or_404(DostawaRudna, pk=stany_id)
        liczniki = LicznikDostawyRudna.objects.filter(number=stany_id).order_by("ID_DYS", "ID_WAZ")
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
            return HttpResponseRedirect(reverse("rudna:dost_rudna"))
        else:
            form = StanPaliwSaveForm(instance=dostawa)
        context = {'lista': dostawa, 'liczniki': liczniki, 'form': form}
        return render(request, 'rudna/liczniki_add.html', context)
    return redirect(reverse('login'))


@login_required
@permission_required('rudna.add_dostawarudna')
def handle_licz(request):
    if request.user.is_authenticated:
        liczniki = LicznikBazowyRudna.objects.order_by("ID_DYS", "ID_WAZ")
        num = DostawaRudna.objects.last()
        name_stacji = get_object_or_404(DaneStacjiRudna)
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
                    form_st.helper.form_action = reverse("rudna:add_liczniki")
                    form_st = StanPaliwSaveForm(request.POST)
                    if form_st.is_valid():
                        form_st.save()
                        lista = DostawaRudna.objects.get(number=num)
                        for licz in liczniki:
                            LicznikDostawyRudna.objects.create(ID_DYS=licz.ID_DYS,
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
                    return HttpResponseRedirect(reverse("rudna:dost_rudna"))

            return redirect(reverse('login'))
        context = {'lista': lista, 'liczniki': liczniki, 'form': form_st}
        return render(request, 'rudna/liczniki_add.html', context)
    return redirect(reverse('login'))


class LicznikBazowyRudnaViewSet(viewsets.ModelViewSet):
    queryset = LicznikBazowyRudna.objects.all()
    serializer_class = LicznikBazowyRudnaSerializer
    permission_classes = [permissions.DjangoModelPermissions, permissions.IsAuthenticated]
    # authentication_classes = [permissions.IsAuthenticated]

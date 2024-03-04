from rest_framework import viewsets, permissions
from .serializers import LicznikBazowyJasionkaSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import StanPaliwSaveForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import LicznikBazowyJasionka, DostawaJasionka, LicznikDostawyJasionka, DaneStacjiJasionka
from django.contrib import messages
from common.untils import send_my_email, send_my_email_modified


@login_required
@permission_required('jasionka.view_licznikbazowyjasionka')
def licz_list(request):
    if request.user.is_authenticated:
        liczniki = LicznikBazowyJasionka.objects.order_by("ID_DYS", "ID_WAZ")
        q = request.GET.get("qre")
        if q:
            liczniki = liczniki.filter(SYMBOL__icontains=q)

        return render(request, 'jasionka/liczniki.html', {"liczniki": liczniki})
    return redirect(reverse('login'))


@login_required
@permission_required('jasionka.view_dostawajasionka')
def dostawy_list(request):
    if request.user.is_authenticated:
        lista = DostawaJasionka.objects.all().order_by('-number')
        paginator = Paginator(lista, 12)
        page_number = request.GET.get('page')
        lista_dost = paginator.get_page(page_number)
        return render(request, 'jasionka/list_dostawy.html', {'lista': lista_dost})
    return redirect(reverse('login'))


@login_required
@permission_required('jasionka.view_dostawajasionka')
def dostawy_details(request, stany_id):
    if request.user.is_authenticated:
        stan =DostawaJasionka.objects.get(number=stany_id)
        created = stan.created.ctime()
        modified = stan.modified.ctime()
        liczniki = LicznikDostawyJasionka.objects.filter(number=stany_id)
        q = request.GET.get("qre")
        if q:
            liczniki = liczniki.filter(SYMBOL__icontains=q)
        context = {'stan': stan, 'liczniki': liczniki, 'created': created, 'modified': modified}
        return render(request, 'jasionka/dostawy_details.html', context)
    return redirect(reverse('login'))


@login_required
@permission_required('jasionka.change_dostawajasionka')
def edit_dostawy(request, stany_id):
    if request.user.is_authenticated:
        user = request.user
        name_stacji = get_object_or_404(DaneStacjiJasionka)
        dostawa = get_object_or_404(DostawaJasionka, pk=stany_id)
        liczniki = LicznikDostawyJasionka.objects.filter(number=stany_id).order_by("ID_DYS", "ID_WAZ")
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
            return HttpResponseRedirect(reverse("jasionka:dost_jasionka"))
        else:
            form = StanPaliwSaveForm(instance=dostawa)
        context = {'lista': dostawa, 'liczniki': liczniki, 'form': form}
        return render(request, 'jasionka/liczniki_add.html', context)
    return redirect(reverse('login'))


@login_required
@permission_required('jasionka.add_dostawajasionka')
def handle_licz(request):
    if request.user.is_authenticated:
        liczniki = LicznikBazowyJasionka.objects.order_by("ID_DYS", "ID_WAZ")
        num = DostawaJasionka.objects.last()
        name_stacji = get_object_or_404(DaneStacjiJasionka)
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
                    form_st.helper.form_action = reverse("jasionka:add_liczniki")
                    form_st = StanPaliwSaveForm(request.POST)
                    if form_st.is_valid():
                        form_st.save()
                        lista = DostawaJasionka.objects.get(number=num)
                        for licz in liczniki:
                            LicznikDostawyJasionka.objects.create(ID_DYS=licz.ID_DYS,
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
                    return HttpResponseRedirect(reverse("jasionka:dost_jasionka"))

            return redirect(reverse('login'))
        context = {'lista': lista, 'liczniki': liczniki, 'form': form_st}
        return render(request, 'jasionka/liczniki_add.html', context)
    return redirect(reverse('login'))


class LicznikBazowyJasionkaViewSet(viewsets.ModelViewSet):
    queryset = LicznikBazowyJasionka.objects.all()
    serializer_class = LicznikBazowyJasionkaSerializer
    permission_classes = [permissions.DjangoModelPermissions, permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated]

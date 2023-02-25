from rest_framework import viewsets, permissions
from okulickiego.serializers import LicznikBazowyOkulickiegoSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import StanPaliwSaveForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import DostawaOkulickiego, LicznikDostawyOkulickiego, LicznikBazowyOkulickiego
from django.contrib import messages
from common.untils import send_my_email


@login_required
@permission_required('okulickiego.view_licznikbazowyokulickiego')
def licz_list(request):
    if request.user.is_authenticated:
        liczniki = LicznikBazowyOkulickiego.objects.order_by("ID_DYS", "ID_WAZ")
        q = request.GET.get("qre")
        if q:
            liczniki = liczniki.filter(SYMBOL__icontains=q)

        return render(request, 'okulickiego/liczniki.html', {"liczniki": liczniki})
    return redirect(reverse('login'))


@login_required
@permission_required('okulickiego.view_dostawaokulickiego')
def dostawy_list(request):
    if request.user.is_authenticated:
        lista = DostawaOkulickiego.objects.all().order_by('-number')
        paginator = Paginator(lista, 6)
        page_number = request.GET.get('page')
        lista_dost = paginator.get_page(page_number)
        return render(request, 'okulickiego/list_dostawy.html', {'lista': lista_dost})
    return redirect(reverse('login'))


@login_required
@permission_required('okulickiego.view_dostawaokulickiego')#, raise_exception=True)
def dostawy_details(request, stany_id):
    if request.user.is_authenticated:
        stan = DostawaOkulickiego.objects.get(number=stany_id)
        liczniki = LicznikDostawyOkulickiego.objects.filter(number=stany_id).order_by("ID_DYS", "ID_WAZ")
        q = request.GET.get("qre")
        if q:
            liczniki = liczniki.filter(SYMBOL__icontains=q)
        context = {'stan': stan, 'liczniki': liczniki}
        return render(request, 'okulickiego/dostawy_details.html', context)
    return redirect(reverse('login'))


@login_required
@permission_required('okulickiego.add_dostawaokulickiego')
def handle_licz(request):
    if request.user.is_authenticated:
        liczniki = LicznikBazowyOkulickiego.objects.order_by("ID_DYS", "ID_WAZ")
        num = DostawaOkulickiego.objects.last()
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
                    form_st.helper.form_action = reverse("okulickiego:add_liczniki")
                    form_st = StanPaliwSaveForm(request.POST)
                    if form_st.is_valid():
                        form_st.save()
                        lista = DostawaOkulickiego.objects.get(number=num)
                        for licz in liczniki:
                            print(licz.ARTYKUL)
                            LicznikDostawyOkulickiego.objects.create(ID_DYS=licz.ID_DYS,
                                                                     ID_WAZ=licz.ID_WAZ,
                                                                     SYMBOL=licz.SYMBOL,
                                                                     TOTAL=licz.TOTAL,
                                                                     ARTYKUL=licz.ARTYKUL,
                                                                     KIEDY=licz.KIEDY,
                                                                     KIEDY_WGR=licz.KIEDY_WGR,
                                                                     number=lista)
                        messages.success(request, 'Dostawa została zapisana w bazie.')
                        try:
                            send_my_email(lista.dostawca, user, user.email, user.last_name)
                            messages.success(request, 'Powiadomienie dodania dostawy zostało wysłane na email.')
                        except:
                            messages.warning(request, 'Powiadomienie dodania dostawy nie zostało wysłane na email.')
                    return HttpResponseRedirect(reverse("okulickiego:dost_okuli"))

            return redirect(reverse('login'))
        context = {'lista': lista, 'liczniki': liczniki, 'form': form_st}
        return render(request, 'okulickiego/liczniki_add.html', context)
    return redirect(reverse('login'))


class LicznikBazowyOkulickiegoViewSet(viewsets.ModelViewSet):
    queryset = LicznikBazowyOkulickiego.objects.all()
    serializer_class = LicznikBazowyOkulickiegoSerializer
    permission_classes = [permissions.DjangoModelPermissions, permissions.IsAuthenticated]
    # authentication_classes = [permissions.IsAuthenticated]

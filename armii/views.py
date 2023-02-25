from rest_framework import viewsets, permissions
from .serializers import LicznikBazowyArmiiSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import StanPaliwSaveForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import LicznikBazowyArmii, DostawaArmii, LicznikDostawyArmii


@login_required
@permission_required('armii.view_licznikbazowyarmii')
def licz_list(request):
    if request.user.is_authenticated:
        liczniki = LicznikBazowyArmii.objects.order_by("ID_DYS", "ID_WAZ")
        q = request.GET.get("qre")
        if q:
            liczniki = liczniki.filter(SYMBOL__icontains=q)

        return render(request, 'armii/liczniki.html', {"liczniki": liczniki})
    return redirect(reverse('login'))


@login_required
@permission_required('armii.view_dostawaarmii')
def dostawy_list(request):
    if request.user.is_authenticated:
        lista = DostawaArmii.objects.all().order_by('-number')
        paginator = Paginator(lista, 6)
        page_number = request.GET.get('page')
        lista_dost = paginator.get_page(page_number)
        return render(request, 'armii/list_dostawy.html', {'lista': lista_dost})
    return redirect(reverse('login'))


@login_required
@permission_required('armii.view_dostawaarmii')
def dostawy_details(request, stany_id):
    if request.user.is_authenticated:
        stan =DostawaArmii.objects.get(number=stany_id)
        liczniki = LicznikDostawyArmii.objects.filter(number=stany_id)
        q = request.GET.get("qre")
        if q:
            liczniki = liczniki.filter(SYMBOL__icontains=q)
        context = {'stan': stan, 'liczniki': liczniki}
        return render(request, 'armii/dostawy_details.html', context)
    return redirect(reverse('login'))


@login_required
@permission_required('armii.add_dostawaarmii')
def handle_licz(request, a=None):
    if request.user.is_authenticated:
        liczniki = LicznikBazowyArmii.objects.order_by("ID_DYS", "ID_WAZ")
        num = DostawaArmii.objects.last()
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
                    form_st.helper.form_action = reverse("armii:add_liczniki")
                    form_st = StanPaliwSaveForm(request.POST)
                    if form_st.is_valid():
                        form_st.save()
                        lista = DostawaArmii.objects.get(number=num)
                        for licz in liczniki:
                            print(licz.ARTYKUL)
                            LicznikDostawyArmii.objects.create(ID_DYS=licz.ID_DYS,
                                                                     ID_WAZ=licz.ID_WAZ,
                                                                     SYMBOL=licz.SYMBOL,
                                                                     TOTAL=licz.TOTAL,
                                                                     ARTYKUL=licz.ARTYKUL,
                                                                     KIEDY=licz.KIEDY,
                                                                     KIEDY_WGR=licz.KIEDY_WGR,
                                                                     number=lista)
                    return HttpResponseRedirect(reverse("armii:dost_armii"))

            return redirect(reverse('login'))
        context = {"lista": lista, 'liczniki': liczniki, 'form': form_st}
        return render(request, 'armii/liczniki_add.html', context)
    return redirect(reverse('login'))


class LicznikBazowyArmiiViewSet(viewsets.ModelViewSet):
    queryset = LicznikBazowyArmii.objects.all()
    serializer_class = LicznikBazowyArmiiSerializer
    permission_classes = [permissions.DjangoModelPermissions, permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated]

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

#def index(request):
 #   return render(request, 'forms/form.html')

from .forms import RegistrarUsuario
from .models import Usuarios

""" def index(request):
    register_form = RegistrarUsuario()
    #success = register_form.RegistrarUsuario()
    return render(request, 'forms/form.html', {'register_form': register_form})

 """


def index(request):
    mis_usuarios = Usuarios.objects.all()
    if request.method == 'POST':
        register_form = RegistrarUsuario(request.POST)
        if register_form.is_valid():
            success = register_form.registrar_usuario()
            return redirect('./')
    else:
        register_form = RegistrarUsuario()
        return render(request, 'forms/form.html', {'register_form': register_form,'usuarios': mis_usuarios})

""" 
def update_user(request, id):
    usuario = get_object_or_404(Usuarios, id=id)
    if request.method == 'POST':
        form = RegistrarUsuario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('forms:form')
    else:
        form = RegistrarUsuario(instance=usuario)
    return render(request, 'forms/update_form.html', {'form': form})

def delete_user(request, id):
    usuario = get_object_or_404(Usuarios, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('forms:form')
    return render(request, 'forms/confirm_delete.html', {'usuario': usuario})
 """
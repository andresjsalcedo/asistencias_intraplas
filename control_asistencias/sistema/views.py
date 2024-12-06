from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Usuario

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')


def registro_usuarios(request):
    if request.method == "POST":
        usuario = request.POST['username']
        email = request.POST['email']
        password = request.POST["password"]
        rol = request.POST['rol']
        area = request.POST['area']

        # Crear el nuevo usuario en la base de datos
        new_user = Usuario(usuario=usuario, email=email, password=password, rol=rol, area=area)
        new_user.save()

        # Agregar mensaje de éxito
        messages.success(request, f"Usuario {usuario} registrado exitosamente.")

        return redirect('Usuarios')
    
    # Obtener todos los usuarios para mostrar en la tabla
    usuarios = Usuario.objects.all()
    return render(request, 'Usuarios.html', {'usuarios': usuarios})

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'GET':
        return JsonResponse({
            'id': usuario.id,
            'usuario': usuario.usuario,
            'email': usuario.email,
            'password': usuario.password,
            'rol': usuario.rol,
            'area': usuario.area,
        })
    elif request.method == 'POST':
        usuario.usuario = request.POST['username']
        usuario.email = request.POST['email']
        usuario.rol = request.POST['rol']
        usuario.password = request.POST['password']
        usuario.area = request.POST['area']
        usuario.save()
        return JsonResponse({'success': True})
    




def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return JsonResponse({'success': True})

    

def asistencias(request):
    return render(request, 'Asistencias.html')
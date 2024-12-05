from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages


# Create your views here.
def registro_usuarios(request):
    if request.method == "POST":
        usuario = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rol = request.POST['rol']
        area = request.POST['area']

        # Crear el nuevo usuario en la base de datos
        new_user = Usuario(usuario=usuario, email=email, password=password, rol=rol, area=area)
        new_user.save()

        # Agregar mensaje de éxito
        messages.success(request, f"Usuario {usuario} registrado exitosamente.")

        return redirect('dashboard')
    
    # Obtener todos los usuarios para mostrar en la tabla
    usuarios = Usuario.objects.all()
    return render(request, 'dashboard.html', {'usuarios': usuarios})

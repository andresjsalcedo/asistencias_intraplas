$(document).ready(function () {
    // Inicializar DataTable
    $('#userTable').DataTable();

    // Rellenar datos en el modal de edición
    $('.editarUsuario').click(function () {
        const userId = $(this).data('id');
        // Realiza una petición para obtener los datos del usuario
        $.ajax({
            url: `/usuarios/${userId}/editar/`, // Ruta para obtener datos del usuario
            method: 'GET',
            success: function (data) {
                $('#editUserId').val(data.id);
                $('#editUsername').val(data.usuario);
                $('#editEmail').val(data.email);
                $('#editPassword').val(data.password);
                $('#editRol').val(data.rol);
                $('#editArea').val(data.area);
            },
        });
    });

    // Manejar el formulario de edición
    $('#editUserForm').submit(function (e) {
        e.preventDefault();
        const userId = $('#editUserId').val();
        $.ajax({
            url: `/usuarios/${userId}/editar/`,
            method: 'POST',
            data: $(this).serialize(),
            success: function () {
                location.reload(); // Recarga la página
            },
        });
    });

    // Manejar la deshabilitación de usuarios
    $('.deshabilitarUsuario').click(function () {
        const userId = $(this).data('id');
            if (confirm('¿Estás seguro de que deseas deshabilitar este usuario?')) {
            $.ajax({
                url: `/usuarios/${userId}/deshabilitar/`,  // Cambié el endpoint a deshabilitar
                method: 'POST',
                data: {
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(), 
                },
                success: function () {
                    location.reload(); // Recarga la página
                },
            });
        }
    });
});


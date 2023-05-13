const correoInput = document.getElementById('correoInput');
const errorCorreo = document.getElementById('errorCorreo');

correoInput.addEventListener('input', function() {
    if (correoInput.value.length < 3) {
        errorCorreo.textContent = 'Se requiere un mínimo de 3 caracteres.';
    } else {
        errorCorreo.textContent = '';
    }
});
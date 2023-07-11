
var registroMensaje = document.getElementById('registro-mensaje');

if (registroMensaje.dataset.mensaje) {
  // Obtener el mensaje del atributo data-mensaje
  var mensaje = registroMensaje.dataset.mensaje;
  // Mostrar el mensaje en el elemento
  registroMensaje.innerText = mensaje;
  registroMensaje.classList.add('alert', 'alert-success');}
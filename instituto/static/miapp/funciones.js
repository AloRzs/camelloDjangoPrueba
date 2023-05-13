const myModal = document.getElementById('staticBackdrop')
const myInput = document.getElementById('alertaModal')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})
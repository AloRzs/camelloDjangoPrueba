from django.shortcuts import render,redirect
from django.contrib.auth import logout
# Create your views here.
class Persona:
    rut=""
    nombre=""
    edad=0

    def __init__(self,rut,nombre,edad):
        self.rut=rut
        self.nombre=nombre
        self.edad=edad
    def __str__(self):
        return self.rut + ", "+ self.nombre +", "+str(self.edad)
#esto para crear los productos, lo iremos adaptando segun nuestros requerimientos de pagina 




lista_productos_diccionario=[
    #{id="" nombre="" precio=0 stock=0 foto=""descripcion=""}
    {
    'id':1,
    'idCombo': "01",
    'nombre': "Combo01",
    'precio': 2000,
    'stock': 45,
    'foto': "completo+bebida.jpg",
    'descripcion': "completo + bebida"
    },

    {
        'id':2,
        'idCombo': "02",
        'nombre': "Combo02",
        'precio': 3600,
        'stock': 54,
        'foto': "2completo+bebida.jpg",
        'descripcion': "2 completo + bebida"
    },

    {
        'id':3,
        'idCombo': "03",
        'nombre': "Combo03",
        'precio': 2000,
        'stock': 70,
        'foto': "salchipapa+bebida.jpg",
        'descripcion': "salchipapa + bebida"
    },

    {
        'id':4,
        'idCombo': "04",
        'nombre': "Combo 04",
        'precio': 5600,
        'stock': 42,
        'foto': "chorrillanafamiliar+bebida.jpg",
        'descripcion': "chorrillana familiar + bebida"
    },

    {
        'id':5,
        'idCombo': "05",
        'nombre': "Combo 05",
        'precio': 4500,
        'stock': 56,
        'foto': "chorrillana+bebida.jpg",
        'descripcion': "chorrillana+bebida"
    },

    {
        'id':6,
        'idCombo': "06",
        'nombre': "Combo 06",
        'precio': 8400,
        'stock': 46,
        'foto': "chorrillanafamiliar+bebida.jpg",
        'descripcion': "familiar + bebida"
    },

    {
        'id':7,
        'idCombo': "07",
        'nombre': "Combo 07",
        'precio': 4800,
        'stock': 67,
        'foto': "churrasco+bebida.jpg",
        'descripcion': "churrasco + bebida"
    },

    {
        'id':8,
        'idCombo': "08",
        'nombre': "Combo 08",
        'precio': 9000,
        'stock': 82,
        'foto': "2churrascos+bebida.jpg",
        'descripcion': "2 churrascos + bebida"
    },

    {
        'id':9,
        'idCombo': "09",
        'nombre': "Combo 09",
        'precio': 16500,
        'stock': 52,
        'foto': "4churrascos+bebida.jpg",
        'descripcion': "4 churrascos + bebida"
    },

    {
        'id':10,
        'idCombo': "10",
        'nombre': "Combo 10",
        'precio': 2500,
        'stock': 33,
        'foto': "hamburguesaqueso+bebida.jpg",
        'descripcion': "hamburguesa queso + bebida"
    },

    {
        'id':11,
        'idCombo': "11",
        'nombre': "Combo 11",
        'precio': 8500,
        'stock': 35,
        'foto': "4hamburguesaqueso+bebida.jpg",
        'descripcion': "4 hamburguesa queso + bebida"
    },

    {
        'id':12,
        'idCombo': "12",
        'nombre': "Combo 12",
        'precio': 20000,
        'stock': 30,
        'foto': "4italianos+2bebidasindividuales.jpg",
        'descripcion': "4 italianos + 2 bebidas individuales"
    },

    {
        'id':13,
        'idCombo': "13",
        'nombre': "Combo 13",
        'precio': 4800,
        'stock': 31,
        'foto': "2salchipapasindividual+bebida1lt.jpg",
        'descripcion': "2 salchipapas individual + bebida 1 lt"
    },

    {
        'id':14,
        'idCombo': "14",
        'nombre': "Combo 14",
        'precio': 9000,
        'stock': 36,
        'foto': "pizzaindividual+bebidaindividual.jpg",
        'descripcion': "pizza individual + bebida individual"
    },

    {
        'id':15,
        'idCombo': "15",
        'nombre': "Combo 15",
        'precio': 16500,
        'stock': 33,
        'foto': "pizzafamiliar+bebida1lt.jpg",
        'descripcion': "pizza familiar + bebida 1 lt"
    },
    {
        'id':16,
        'idCombo': "16",
        'nombre': "Combo 16",
        'precio': 4800,
        'stock': 54,
        'foto': "2pizzafamiliar+bebida3lt.jpg",
        'descripcion': "2 pizza familiar + bebida 3 lt"
    },

    {
        'id':17,
        'idCombo': "17",
        'nombre': "Combo 17",
        'precio': 9000,
        'stock': 60,
        'foto': "2pizzaindividual+2bebidaindividual.jpg",
        'descripcion': "2 pizza individual + 2 bebida individual"
    },

    {
        'id':18,
        'idCombo': "18",
        'nombre': "Combo 18",
        'precio': 16500,
        'stock': 43,
        'foto': "pizzaindividual+4empanadas+bebidaindividual.jpg",
        'descripcion': "pizza individual + 4 empanadas + bebida individual"
    },

    {
        'id':19,
        'idCombo': "19",
        'nombre': "Combo 19",
        'precio': 4800,
        'stock': 55,
        'foto': "pizzafamiliar+16empanadas+bebida3lt.jpg",
        'descripcion': "pizza familiar + 16 empanadas + bebida 3 lt"
    },

    {
        'id':20,
        'idCombo': "20",
        'nombre': "Combo 20",
        'precio': 20000,
        'stock': 56,
        'foto': "Bigcamello.png",
        'descripcion': "2 completos italianos + 2 churrascos italiano + bebida 3 lt."
    },

]

def index(request):
    
    context ={}
    return render(request,'html/index.html',context)


def contacto(request):#contacto
    
    context ={}
    return render(request,'html/contacto.html',context)

def lista_productos(request):#listado productos
    
    context ={"lista_productos_diccionario":lista_productos_diccionario}
    
    return render(request,'html/nuestrosProductos.html',context)

def nosotros(request):# nosotros
    
    context ={}
    return render(request,'html/acerca de nosotros.html',context)

def ers(request):# ers 
    
    context ={}
    return render(request,'html/ers.html',context)

def api(request):
    
    return render(request,'html/api.html')


#esto para funciones del carrito
def get_product_by_id(producto_id):
    for product in lista_productos_diccionario:
        if int(producto_id) == int(product.get('id')):
            return product
    return None

def carrito(request):
    v_cart = request.session.get('cart', {})
    item_carrito = []
    precio_total = 0
    
    for producto_id, quantity in v_cart.items():
        producto = get_product_by_id(producto_id)

        if producto:

            subtotal = producto['precio'] * quantity
            idNumero=producto['id']
            idNom=producto['idCombo']
            imagen=producto['foto']
            descripcionCombo=producto['descripcion']
            item_carrito.append({
                'id':idNumero,
                'imagen':imagen,
                'producto': producto,
                'quantity': quantity,
                'subtotal': subtotal,
                'idNombre':idNom,
                'descripcion':descripcionCombo,
            })
            precio_total += subtotal
    
    return render(request, 'html/carrito.html', {
        'item_carrito': item_carrito,
        'precio_total': precio_total,
    })

def agregar_carrito(request, producto_id):
    product = get_product_by_id(producto_id)
    if product:
        v_carrito = request.session.get('cart', {})
        v_carrito[producto_id] = v_carrito.get(producto_id, 0) + 1
        request.session['cart'] = v_carrito

    return redirect('lista_productos')

def sacar_del_carrito(request, producto_id):
    cart = request.session.get('cart', {})
    if producto_id in cart:
        del cart[producto_id]
        request.session['cart'] = cart
    return redirect('cart')

def limpiar_carrito(request):
    request.session['cart'] = {}
    return redirect('cart')


#fin de definiciones de carrito


#configuracion de inicio de sesion
usuarios = [
{'username': 'mati', 'password': '123'},
{'username': 'alonso', 'password': '123'},
]

#imports


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Verificar si el usuario existe en la lista
        for usuario in usuarios:
            if usuario['username'] == username and usuario['password'] == password:
                request.session['username'] = username  # Guardar el nombre de usuario en la sesión
                return redirect('index')  # Redirigir al usuario a la página de inicio del proyecto

        error_message = 'Nombre de usuario o contraseña incorrectos.'
        return render(request, 'html/login.html', {'error': error_message})
    else:
        return render(request, 'html/login.html')


def logout_view(request):
    logout(request)
    return redirect('html/login.html')

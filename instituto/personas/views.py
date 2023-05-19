from django.shortcuts import render

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



class Producto:
    id=0
    nombre=""
    precio=0
    stock=0
    foto=""     #ejemplo de foto
    descripcion=""
    def __init__(self,id,nombre,precio,stock,foto,descripcion):
        self.id=id             
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        self.foto=foto
        self.descripcion=descripcion
    def __str__(self):#implementar lo de a descripcion
        return self.id + ", "+self.nombre + ", "+self.precio+ ", "+self.stock+ ", "+self.foto+ ", " +self.descripcion

prod1 = Producto(1,"Combo01",2000,45,"completo+bebida.jpg","completo + bebida")
prod2 = Producto(2,"Combo02",3600,54,"2completo+bebida.jpg","2 completo + bebida")
prod3 = Producto(3,"Combo03",2000,70,"salchipapa +bebida.jpg","salchipapa + bebida")
prod4 = Producto(4, "Combo 04",5600,42,"chorrillana familiar+bebida.jpg","chorrillana familiar + bebida")
prod5 = Producto(5, "Combo 05",4500,56,"chorrillana+bebida.jpg","chorrillana + bebida")
prod6 = Producto(6, "Combo 06",8400,46,"chorrillana familiar+bebida.jpg","familiar + bebida")
prod7 = Producto(7, "Combo 07",4800,67,"churrasco+bebida.jpg","churrasco + bebida")
prod8 = Producto(8, "Combo 08",9000,82,"2 churrascos+bebida.jpg","2 churrascos + bebida")
prod9 = Producto(9, "Combo 09",16500,52,"4 churrascos+bebida.jpg","4 churrascos + bebida")
prod10 = Producto(9, "Combo 10",2500,33,"hamburguesa queso+bebida.jpg","hamburguesa queso + bebida")
prod11 = Producto(11, "Combo 11",8500,35,"4 hamburguesa queso + bebida.jpg","4 hamburguesa queso + bebida")
prod12 = Producto(12, "Combo 12",20000,30,"4 italianos + 2 bebidas individuales.jpg","4 italianos + 2 bebidas individuales")
prod13 = Producto(13, "Combo 13",4800,31,"2 salchipapas individual + bebida 1 lt.jpg","2 salchipapas individual + bebida 1 lt")
prod14 = Producto(14, "Combo 14",9000,36,"pizza individual + bebida individual.jpg","pizza individual + bebida individual")
prod15 = Producto(15, "Combo 15",16500,33,"pizza familiar + bebida 1 lt.jpg","pizza familiar + bebida 1 lt")
prod16 = Producto(16, "Combo 16",4800,54,"2 pizza familiar + bebida 3 lt.jpg","2 pizza familiar + bebida 3 lt")
prod17 = Producto(17, "Combo 17",9000,60,"2 pizza individual + 2 bebida individual.jpg","2 pizza individual + 2 bebida individual")
prod18 = Producto(18, "Combo 18",16500,43,"pizza individual + 4 empanadas + bebida individual.jpg","pizza individual + 4 empanadas + bebida individual")
prod19 = Producto(19, "Combo 19",4800,55,"pizza familiar + 16 empanadas + bebida 3 lt.jpg","pizza familiar + 16 empanadas + bebida 3 lt")
prod20 = Producto(20, "Combo 20",20000,56,"Big camello.png","2 completos italianos+ 2 churrascos italiano + bebida 3 lt.")

listaProductosMain=[prod1,prod2,prod3,prod4,prod5,prod6,prod7,prod8,prod9,prod10,prod11,prod12,prod13,prod14,prod15
                ,prod16,prod17,prod18,prod19,prod20]


listaProducto1=[prod1,prod2,prod3]
listaProducto2=[prod4,prod5,prod6]
listaProducto3=[prod7,prod8,prod9]
listaProducto4=[prod10,prod11,prod12]
listaProducto5=[prod13,prod14,prod15]
listaProducto6=[prod16,prod17,prod18]
listaProducto7=[prod19,prod20]



def index(request):
    print("hola estoy en index...")
    context ={}
    return render(request,'html/index.html',context)


def contacto(request):#contacto
    
    context ={}
    return render(request,'html/contacto.html',context)

def lista_productos(request):#listado productos
    
    context ={"listaProductosMain":listaProductosMain,"listaProducto1":listaProducto1,"listaProducto2":listaProducto2
              ,"listaProducto3":listaProducto3,"listaProducto4":listaProducto4,"listaProducto5":listaProducto5
              ,"listaProducto6":listaProducto6,"listaProducto7":listaProducto7}
    return render(request,'html/nuestrosProductos.html',context)

def nosotros(request):# nosotros
    
    context ={}
    return render(request,'html/acerca de nosotros.html',context)

def ers(request):# ers 
    
    context ={}
    return render(request,'html/ers.html',context)

def compra(request):# compra
    
    context ={}
    return render(request,'html/compra.html',context)

def detalle(request,producto_id):
    for producto in listaProductosMain:
        if producto.id==producto_id:
            context={"producto":producto}
            break
    return render(request,'html/detalleProd.html',context)



#configuracion de inicio de sesion
usuarios = [
{'username': 'mati', 'password': '123'},
{'username': 'alonso', 'password': '123'},
]

#imports
from django.shortcuts import render, redirect
from django.contrib.auth import logout

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

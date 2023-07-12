from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Combo,DetalleVenta,Venta,User
from .forms import FormularioCombo,FormularioLogin,FormularioRegistro
from django.contrib import messages
# Create your views here.
# class Persona:
#     rut=""
#     nombre=""
#     edad=0

#     def __init__(self,rut,nombre,edad):
#         self.rut=rut
#         self.nombre=nombre
#         self.edad=edad
#     def __str__(self):
#         return self.rut + ", "+ self.nombre +", "+str(self.edad)
# #esto para crear los productos, lo iremos adaptando segun nuestros requerimientos de pagina 

class Carrito:
    id=0
    precio=0
    stock=0
    foto=""     #ejemplo de foto
    descripcion=""
    cantidad=0 #esto es lo nuevo en el carrito
    def __init__(self,id,precio,stock,foto,descripcion,cantidad):
        self.id=id             
        self.precio=precio
        self.stock=stock
        self.foto=foto
        self.descripcion=descripcion
        self.cantidad=cantidad
        
    def __str__(self):#implementar lo de a descripcion
        return str(self.id) + ", "+str(self.precio)+ ", "+str(self.stock)+ ", "+self.foto+ ", " +self.descripcion+", " + str(self.cantidad)


# class Producto:
#     id=0
#     precio=0
#     stock=0
#     foto=""     #ejemplo de foto
#     descripcion=""
#     def __init__(self,id,precio,stock,foto,descripcion):
#         self.id=id             
#         self.precio=precio
#         self.stock=stock
#         self.foto=foto
#         self.descripcion=descripcion
#     def __str__(self):
#         str(self.id) + ", " +str(self.precio) + ", " +str(self.stock) + ", " +self.foto + ", " +self.descripcion


# prod1 = Producto(1,2000,45,"completo+bebida.jpg","completo + bebida")
# prod2 = Producto(2,3600,54,"2completo+bebida.jpg","2 completo + bebida")
# prod3 = Producto(3,2000,70,"salchipapa +bebida.jpg","salchipapa + bebida")
# prod4 = Producto(4,5600,42,"chorrillana familiar+bebida.jpg","chorrillana familiar + bebida")
# prod5 = Producto(5,4500,56,"chorrillana+bebida.jpg","chorrillana + bebida")
# prod6 = Producto(6,8400,46,"chorrillana familiar+bebida.jpg","familiar + bebida")
# prod7 = Producto(7,4800,67,"churrasco+bebida.jpg","churrasco + bebida")
# prod8 = Producto(8,9000,82,"2 churrascos+bebida.jpg","2 churrascos + bebida")
# prod9 = Producto(9,16500,52,"4 churrascos+bebida.jpg","4 churrascos + bebida")
# prod10 = Producto(9,2500,33,"hamburguesa queso+bebida.jpg","hamburguesa queso + bebida")
# prod11 = Producto(11,8500,35,"4 hamburguesa queso + bebida.jpg","4 hamburguesa queso + bebida")
# prod12 = Producto(12,20000,30,"4 italianos + 2 bebidas individuales.jpg","4 italianos + 2 bebidas individuales")
# prod13 = Producto(13,4800,31,"2 salchipapas individual + bebida 1 lt.jpg","2 salchipapas individual + bebida 1 lt")
# prod14 = Producto(14,9000,36,"pizza individual + bebida individual.jpg","pizza individual + bebida individual")
# prod15 = Producto(15,16500,33,"pizza familiar + bebida 1 lt.jpg","pizza familiar + bebida 1 lt")
# prod16 = Producto(16,4800,54,"2 pizza familiar + bebida 3 lt.jpg","2 pizza familiar + bebida 3 lt")
# prod17 = Producto(17,9000,60,"2 pizza individual + 2 bebida individual.jpg","2 pizza individual + 2 bebida individual")
# prod18 = Producto(18,16500,43,"pizza individual + 4 empanadas + bebida individual.jpg","pizza individual + 4 empanadas + bebida individual")
# prod19 = Producto(19,4800,55,"pizza familiar + 16 empanadas + bebida 3 lt.jpg","pizza familiar + 16 empanadas + bebida 3 lt")
# prod20 = Producto(20,20000,56,"Big camello.png","2 completos italianos+ 2 churrascos italiano + bebida 3 lt.")

listaCarrito=[]

# listaProductosMain=[prod1,prod2,prod3,prod4,prod5,prod6,prod7,prod8,prod9,prod10,prod11,prod12,prod13,prod14,prod15
#                 ,prod16,prod17,prod18,prod19,prod20]

def index(request):
    print("hola estoy en index...")
    context ={}
    return render(request,'html/index.html',context)


def contacto(request):#contacto
    
    context ={}
    return render(request,'html/contacto.html',context)

def lista_productos(request):#listado productos
    listaProductosMain = Combo.objects.all()
    context ={"listaProductosMain":listaProductosMain}
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
#Para las tablas detalle ventas y venta
def tabla_ventas(request):
    consulta_ventas=Venta.objects.all()
    return render(request,'html/tabla_ventas.html',{'consulta_ventas':consulta_ventas})

#fin
def detalle(request,producto_id):
    consulta_productos=Combo.objects.all()
    for producto in consulta_productos:
            if producto.id_combo==producto_id:
                context={"producto":producto,"consulta_productos":consulta_productos}
                break
    if request.method == "POST":
        # Recolectar valores de los campos ocultos...
        idProd = request.POST.get("idProducto")
        precio = request.POST.get("precio")
        stock = request.POST.get("stock")
        foto = request.POST.get("foto")
        descripcion = request.POST.get("descripcion")
        cantidad = request.POST.get("cantidad")

        opc=request.POST.get("opc")
        
        if opc=="Agregar al Carrito":
            se_encontro=0
            print(opc)
            codigo=int(idProd)
            cantidad=int(cantidad)
            for itemCarrito in listaCarrito:
                print(codigo)
                print("se ingreso a item carrito")
                if itemCarrito.id==codigo:
                    print("Se encontro producto")
                    itemCarrito.cantidad=itemCarrito.cantidad+cantidad
                    se_encontro=1
                    break
                else:
                    print("no se encontro")
                    se_encontro=0
            if se_encontro==0:
                listaCarrito.append(Carrito(int(idProd),precio,stock,foto,descripcion,cantidad))
            context={"listaCarrito":listaCarrito,"consulta_productos":consulta_productos}
            return redirect('carrito')
    return render(request,'html/detalleProd.html',context)



def carrito(request):
    for i in listaCarrito:
        print(i)
    total_carrito = 0
    det_venta_objetos=[]
    for item in listaCarrito:
        producto = Combo.objects.get(id_combo=item.id)
        subtotal = producto.precio * item.cantidad
        total_carrito += subtotal
    consulta_productos = Combo.objects.all()
    
    if request.method == 'POST':
        usuario = request.user
        for itemCarrito in listaCarrito:
            producto = Combo.objects.get(id_combo=itemCarrito.id)
            cantidad = itemCarrito.cantidad
            subtotal = int(itemCarrito.cantidad) * int(itemCarrito.precio)

            det_venta_objetos.append(DetalleVenta(id_combo=producto,cantidad=cantidad,subtotal=subtotal))
            try:
                if request.user.is_authenticated:
                    det_venta_it = DetalleVenta(
                        # falta la id de detalle y tengo que instanciar el combo
                        id_combo=producto,
                        cantidad=cantidad,
                        subtotal=subtotal,
                    )
                    producto.stock -= cantidad
                    det_venta_it.save()
                    producto.save()
                else:
                    print("No se ha encontrado un usuario en la sesion al confirmar compra")
                    listaCarrito.clear()
            except:
                print("Ocurrió un error")
                return redirect('index')
        try:
            venta_it = Venta(
                total=total_carrito,
                id_detalle_venta=det_venta_it,
                id_usuario=User.objects.get(username=usuario)
            )
            venta_it.save()
            listaCarrito.clear()
            print("Se realizó compra")
            messages.success(request, 'Compra realizada exitosamente')
            return redirect('index')
        except:
            print("No se encuentra usuario en la sesión")
            return redirect('index')

    context = {
        "listaCarrito": listaCarrito,
        "consulta_productos": consulta_productos,
        "total_carrito": total_carrito
    }
    return render(request, 'html/carrito.html', context)

def vaciar_carro(request):
    listaCarrito.clear()
    context={"listaCarrito":listaCarrito}
    return render(request,'html/carrito.html',context)


@login_required
def agregar_producto_crud(request):
    if request.method=='GET':
        context={
            'formulario':FormularioCombo()
        }
    if request.method=='POST':
        datos_producto=FormularioCombo(data = request.POST)
        es_valido = datos_producto.is_valid()

        if es_valido:
            producto_creado= datos_producto.save(commit=False)
            producto_creado.usuario = request.user
            producto_creado.save()
        # A continuacion se mostraran los datos en el que se este equivocando el usuario
        context={
            'formulario':datos_producto
        }
        return render(request, 'html/crud_agregar.html', context)
    return render(request,'html/crud_agregar.html',context)
@login_required
def mostrar_producto_crud(request):
    consulta_productos=Combo.objects.all()
    context={"consulta_productos":consulta_productos}
    return render(request,'html/crud_lista.html',context)

def modificar_crud(request,producto_id):
    combo = get_object_or_404(Combo, pk=producto_id)
    if request.method == 'POST':
        form = FormularioCombo(request.POST, instance=combo)
        if form.is_valid():
            form.save()
            return redirect('mostrar_productos_crud')
    else:
        form = FormularioCombo(instance=combo)
    
    return render(request, 'html/crud_mod.html', {'form': form, 'combo': combo})

def eliminar_combo(request, producto_id):
    producto = get_object_or_404(Combo, id_combo=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('mostrar_productos_crud')
    return redirect('listar_combos')

#configuracion de inicio de sesion
# ESTO SE NECESITA ACTUALIZAR
# usuarios = [
# {'username': 'mati', 'password': '123'},
# {'username': 'alonso', 'password': '123'},
# ]
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         for usuario in usuarios:
#             if usuario['username'] == username and usuario['password'] == password:
#                 request.session['username'] = username  
#                 return redirect('index')  

#         error_message = 'Nombre de usuario o contraseña incorrectos.'
#         return render(request, 'html/login.html', {'error': error_message})
#     else:
#         return render(request, 'html/login.html')


# def logout_view(request):
#     logout(request)
#     request.session.clear()  
#     return redirect('login')

##Remaster LOGIN##

def mostrar_entrar(request):
    if request.method == 'GET':
        contexto = {
            'formulario':FormularioLogin(),
            'titulo':'Bienvenido',
            'formulario_original': FormularioLogin(),
        }
        return render(request, 'html/usuario_login.html',contexto)
    elif request.method == 'POST':
        datos_usuario = FormularioLogin(data=request.POST)
        print(datos_usuario.data)
        es_valido = datos_usuario.is_valid()
        print(datos_usuario.errors)
        if es_valido:
            username = datos_usuario.cleaned_data['username']
            password = datos_usuario.cleaned_data['password']
            print(username,password)
            usuario = authenticate(username=username,password=password)
            if usuario is not None:
                login(request,usuario)
                return redirect('index')
            else:
                # Mandar al lobby
                return redirect('mostrar_entrar')
        contexto = {
            'formulario_original': datos_usuario,
            'formulario':FormularioLogin()
        }
        return render(request, 'html/usuario_login.html',contexto)

def mostrar_registro(request):
    if request.method == 'GET':
        contexto = {
            'formulario': FormularioRegistro(),
            'mensaje': None  # Inicialmente establecido como None
        }
        return render(request, 'html/usuario_registro.html', contexto)
    if request.method == 'POST':
        datos_formulario = FormularioRegistro(data=request.POST)
        if datos_formulario.is_valid():
            usuario = datos_formulario.save()  # Guardar el usuario
            login(request, usuario)  # Iniciar sesión automáticamente
            return redirect('index')  # Redireccionar al index
        else:
            contexto = {
                'formulario': datos_formulario,
                'mensaje': 'Datos Incorrectos, revise el formulario que contenga valores válidos'  # No se muestra ningún mensaje en caso de errores de validación
            }
            return render(request, 'html/usuario_registro.html', contexto)
    
def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        print("Se ha salido de la sesión")
    #Siempre se manda a la pagina principal independiente de si el usuario esta ingresado en la pagina o no
    return redirect ('index')
from django.shortcuts import redirect, render
from .models import Producto, Categoria
from .forms import ProductoForm

# Create your views here.

def home(request):
    return render(request, "apoyo/home.html")

def producto(request, action, id):
    data = {"mesg": "", "form": ProductoForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡Producto agregado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos productos iguales!"

    elif action == 'upd':
        objeto = Producto.objects.get(idProducto=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El producto fue actualizado correctamente!"
        data["form"] = ProductoForm(instance=objeto)

    elif action == 'del':
        try:
            Producto.objects.get(idProducto=id).delete()
            data["mesg"] = "¡El producto fue eliminado correctamente!"
            return redirect(producto, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El producto ya estaba eliminado!"

    data["list"] = Producto.objects.all().order_by('idProducto')
    return render(request, "apoyo/producto.html", data)

def poblar_bd(request):
    Producto.objects.all().delete()
    Producto.objects.create(idProducto="0001", marca='Quix', nombreProducto="Lavaloza", precio='1990', stock='3',  imagen="images/volvosw.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(idProducto="0002", marca='Omo', nombreProducto="Detergente", precio='2190', stock='2',  imagen="images/volvosw.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(idProducto="0003", marca='Tucapel', nombreProducto="Arroz", precio='990', stock='5',  imagen="images/volvosw.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(idProducto="0004", marca='Luchetti', nombreProducto="Tallarines", precio='990', stock='5',  imagen="images/volvosw.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(idProducto="0005", marca='Jumbo', nombreProducto="Atún", precio='590', stock='9',  imagen="images/volvosw.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(idProducto="0006", marca='Jumbo', nombreProducto="Mayonesa", precio='1990', stock='2',  imagen="images/volvosw.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(idProducto="0007", marca='Elite', nombreProducto="Papel Higiénico", precio='1590', stock='9',  imagen="images/volvosw.jpg", categoria=Categoria.objects.get(idCategoria=3))
    return redirect(producto, action='ins', id = '-1')


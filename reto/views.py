from django.shortcuts import render, HttpResponse

# Create your views here.
html_base = """
    <h1> Unidad Educativa Eloy Alfaro</h1>
    <ul>
        <li>   <a href="/">Portada</a>              </li>
        <li>   <a href="/Unidad_Educativa/">Mision y Vision</a>   </li>
        <li>   <a href="/Administrador/">Gestion Academica y Alumnos</a>     </li>
        <li>   <a href="/LOGIN/">Usuario y Contraseña</a>     </li>
        <li>   <a href="/Carga_de_documentos/">Datos personales</a>     </li>
    </ul>
"""


def home (request):
    html_response = "<h1>Mi Web Personal</h1>"
    for i in range(10):
        html_response += "<h2>Portada</h2>"
    return HttpResponse(html_response);


# relaciona la parte vista con el template home.html


def Unidad_Educativa(request):
    html_responsde = "<h1>Mision y Vision</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def Administrador(request):
    html_responsde = "<h1>Gestion Academica y Alumnos </h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def LOGIN(request):
    html_responsde = "<h1>Usuario y Contraseña</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def Carga_de_documentos(request):
    html_responsde = "<h1>Datos personales</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


#def home(request, plantilla="home.html"):
 #   return render(request, plantilla);


#def contact(request, plantilla="contact.html"):
 #   return render(request, plantilla);


#def about(request, plantilla="about-me.html"):
 #   return render(request, plantilla);


from django.shortcuts import render

# Create your views here.

from ..models import Reportes

def get_reportes():
    queryset = Reportes.objects.all()
    return (queryset)

def create_reportes(form):
    reportes = form.save()
    reportes.save()
    return ()
from ..models import Boletin

def get_boletines():
    queryset = Boletin.objects.all()
    return (queryset)

def get_boletin(id):
    boletin = Boletin.objects.raw("SELECT * FROM boletines_boletin WHERE id=%s" % id)[0]
    return (boletin)

def create_boletin(form):
    boletin = form.save()
    boletin.save()
    return ()

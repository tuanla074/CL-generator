from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
from xhtml2pdf import pisa

from CLForm.models import Recruiter


def index(request):
    listing = Recruiter.objects.all()
    context = {
        'recruiters': listing,
    }
    return render(request, 'CLForm/index.html', context)


@csrf_exempt
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def generated(request, rec_id):
    fills_in = get_object_or_404(Recruiter.objects.all(), pk=rec_id)
    pdf = render_to_pdf('CLForm/cLetter.html', {'fill': fills_in})
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Tuan_Le_Cover_Letter.pdf"'
    return response

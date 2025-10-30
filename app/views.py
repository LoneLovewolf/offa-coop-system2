from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

def generate_report(request):
    # Your data logic here
    transactions = Transaction.objects.all()  # Example
    context = {'transactions': transactions}
    
    # Render HTML template
    html_string = render_to_string('app/report_template.html', context)
    
    # Convert to PDF
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()
    
    # Return PDF
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cooperative_report.pdf"'
    return response

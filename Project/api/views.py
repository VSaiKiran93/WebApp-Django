import nmap
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Item
import subprocess

# Create your views here.
@api_view(['GET'])
def nmap_scan(request, ip_address):
    # Create nmap object.
    scanner = nmap.PortScanner()

    # Store nmap scan.
    scanner.scan('192.168.0.45', arguments='-sS -sV -O')
    hosts = scanner.all_hosts()
    result = scanner.pdf()
    return Response({'hosts': hosts, 'result': result})


def run_command(request):
    command = "ls -l /var/log"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return HttpResponse(error)
    else:
        return HttpResponse(output)

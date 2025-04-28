import sys
import os
import logging
import azure.functions as func

# 🛠️ Agregamos HttpTrigger al sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from main import process_request

def main(req: func.HttpRequest) -> func.HttpResponse:
    return process_request(req)

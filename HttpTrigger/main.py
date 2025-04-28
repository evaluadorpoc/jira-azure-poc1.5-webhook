import azure.functions as func
from shared.logger_config import logger
from validators.orchestrator import orchestrate_validations

def process_request(req: func.HttpRequest) -> func.HttpResponse:
    logger.info("✅ Nueva solicitud HTTP recibida.")

    try:
        req_body = req.get_json()
        logger.info(f"📥 Cuerpo recibido: {req_body}")
    except ValueError as e:
        logger.error(f"❌ Error al parsear JSON: {e}")
        return func.HttpResponse(
            body='{"success": false, "message": "Invalid JSON payload."}',
            status_code=400,
            mimetype="application/json"
        )

    description = req_body.get('description', '').strip()

    if not description:
        logger.warning("⚠️ 'description' está vacío o no fue proporcionado.")
        return func.HttpResponse(
            body='{"success": false, "message": "Field \'description\' is missing or empty."}',
            status_code=400,
            mimetype="application/json"
        )

    validation_results = orchestrate_validations({"description": description})

    response_message = {
        "success": True,
        "message": "Request processed successfully.",
        "validation_results": validation_results,
        "data_received": req_body
    }

    logger.info(f"📤 Respuesta enviada: {response_message}")

    return func.HttpResponse(
        body=str(response_message),
        status_code=200,
        mimetype="application/json"
    )

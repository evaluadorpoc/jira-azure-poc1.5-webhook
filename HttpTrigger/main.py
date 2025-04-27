import azure.functions as func
from shared.logger_config import logger
from validators import validate_format

def process_request(req: func.HttpRequest) -> func.HttpResponse:
    logger.info("Received new HTTP request.")

    try:
        req_body = req.get_json()
        logger.info(f"Request body successfully parsed: {req_body}")
    except ValueError as e:
        logger.error(f"Failed to parse request JSON: {e}")
        return func.HttpResponse(
            "Invalid JSON payload.",
            status_code=400
        )

    # 🎯 Llamar al primer validador
    format_result = validate_format(req_body)

    response_message = {
        "message": "Request received successfully.",
        "format_validation": format_result,  # ← Agregamos resultado del validador
        "data_received": req_body
    }

    logger.info(f"Sending response: {response_message}")

    return func.HttpResponse(
        body=str(response_message),
        status_code=200,
        mimetype="application/json"
    )

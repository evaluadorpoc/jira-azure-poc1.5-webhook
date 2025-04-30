import azure.functions as func
from shared.logger_config import logger
from orchestrator.processor import process_jira_operations

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

    # ✅ Extraer campos desde estructura de Jira
    issue = req_body.get("issue", {})
    fields = issue.get("fields", {})

    extracted_data = {
        "issueKey": issue.get("key"),
        "description": fields.get("description", "").strip(),
        "custom_fields": {
            "customfield_10038": fields.get("customfield_10038")
        },
        "raw_fields": fields  # opcional: por si el orquestador quiere todo
    }

    if not extracted_data["issueKey"] or not extracted_data["description"]:
        logger.warning("⚠️ Faltan campos 'issueKey' o 'description'.")
        return func.HttpResponse(
            body='{"success": false, "message": "Missing issueKey or description."}',
            status_code=400,
            mimetype="application/json"
        )

    # 🧠 Lógica delegada al orquestador
    jira_result = process_jira_operations(
        extracted_data["issueKey"],
        extracted_data["description"]
    )

    response_message = {
        "success": True,
        "message": "Request processed and Jira updated.",
        "jira_result": jira_result,
        "data_received": extracted_data
    }

    logger.info(f"📤 Respuesta enviada: {response_message}")

    return func.HttpResponse(
        body=str(response_message),
        status_code=200,
        mimetype="application/json"
    )

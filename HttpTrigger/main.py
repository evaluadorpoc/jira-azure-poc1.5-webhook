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

    # ✅ Verificar si el campo 'description' fue modificado
    changelog = req_body.get("changelog", {})
    changed_fields = [item.get("field") for item in changelog.get("items", [])]
    if "description" not in changed_fields:
        logger.warning("⚠️ Cambio ignorado: 'description' no fue modificado.")
        return func.HttpResponse(
            body='{"success": false, "message": "Ignored: Description not updated."}',
            status_code=200,
            mimetype="application/json"
        )

    # ✅ Extraer campos necesarios
    issue = req_body.get("issue", {})
    issue_key = issue.get("key")
    description = issue.get("fields", {}).get("description", "")

    if not issue_key or not description:
        logger.warning("⚠️ Faltan campos 'issueKey' o 'description'.")
        return func.HttpResponse(
            body='{"success": false, "message": "Missing issueKey or description."}',
            status_code=400,
            mimetype="application/json"
        )

    jira_result = process_jira_operations(issue_key, description)

    response_message = {
        "success": True,
        "message": "Request processed and Jira updated.",
        "jira_result": jira_result,
        "data_received": req_body
    }

    logger.info(f"📤 Respuesta enviada: {response_message}")

    return func.HttpResponse(
        body=str(response_message),
        status_code=200,
        mimetype="application/json"
    )

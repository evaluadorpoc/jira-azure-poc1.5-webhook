# orchestrator/processor.py
from jira_connector.api_client import JiraClient
from shared.logger_config import logger
import shared.settings as settings

def process_jira_operations(issue_key: str, description: str):
    """
    Procesa las operaciones de Jira:
    - Cuenta caracteres del description
    - Agrega comentario
    - Actualiza campo personalizado
    """
    jira = JiraClient()

    # 🎯 Contar caracteres
    character_count = len(description)
    logger.info(f"✍️ Descripción tiene {character_count} caracteres.")

    # 🎯 Crear mensaje para comentario
    comment_message = f"📝 Esta historia tiene {character_count} caracteres en la descripción."

    # 🎯 Intentar agregar comentario
    comment_added = jira.add_comment(issue_key, comment_message)

    # 🎯 Intentar actualizar el campo personalizado
    field_updated = jira.update_custom_field(issue_key, character_count)


    # 🎯 Resultado
    result = {
        "comment_added": comment_added,
        "field_updated": field_updated,
        "character_count": character_count
    }

    logger.info(f"✅ Resultado procesamiento Jira: {result}")
    return result

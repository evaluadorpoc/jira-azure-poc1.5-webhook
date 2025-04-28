import requests
from shared.logger_config import logger
from shared.settings import JIRA_BASE_URL, JIRA_TOKEN, JIRA_EMAIL, CUSTOM_FIELDS

class JiraClient:
    def __init__(self):
        self.base_url = JIRA_BASE_URL
        self.auth = (JIRA_EMAIL, JIRA_TOKEN)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        logger.info("✅ JiraClient inicializado correctamente.")

    def add_comment(self, issue_key: str, comment_text: str) -> bool:
        url = f"{self.base_url}/rest/api/3/issue/{issue_key}/comment"

        # ✅ Formato correcto tipo Atlassian Document Format (ADF)
        payload = {
            "body": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": comment_text
                            }
                        ]
                    }
                ]
            }
        }

        try:
            response = requests.post(url, headers=self.headers, auth=self.auth, json=payload)
            response.raise_for_status()
            logger.info(f"✅ Comentario agregado en {issue_key}.")
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Error al agregar comentario en {issue_key}: {e}")
            return False

    def update_custom_field(self, issue_key: str, field_value: int) -> bool:
        url = f"{self.base_url}/rest/api/3/issue/{issue_key}"
        payload = {
            "fields": {
                CUSTOM_FIELDS["character_count"]: str(field_value)
            }
        }

        try:
            response = requests.put(url, headers=self.headers, auth=self.auth, json=payload)
            response.raise_for_status()
            logger.info(f"✅ Campo {CUSTOM_FIELDS['character_count']} actualizado en {issue_key} con valor {field_value}.")
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Error al actualizar campo en {issue_key}: {e}")
            return False

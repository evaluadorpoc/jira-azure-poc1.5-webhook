from shared.logger_config import logger

def validate_format(issue_data: dict) -> dict:
    """
    Validates if the 'summary' field of the issue starts with 'Como '.
    Returns a dict with 'passed' (bool) and 'details' (str).
    """
    summary = issue_data.get('summary', '')

    if not summary:
        logger.warning("Validation 'format' failed: 'summary' field is missing or empty.")
        return {
            "passed": False,
            "details": "Missing or empty summary field."
        }

    if summary.startswith("Como "):
        logger.info("Validation 'format' passed: summary starts correctly.")
        return {
            "passed": True,
            "details": "Summary starts with 'Como '."
        }
    else:
        logger.warning("Validation 'format' failed: summary does not start with 'Como '.")
        return {
            "passed": False,
            "details": "Summary does not start with 'Como '."
        }

# 🚀 PoC Azure - Integración Jira Azure IA

Prueba de concepto para validar y desplegar funciones serverless en Azure Functions, utilizando GitHub Actions para CI/CD automático.

---

## 🛠️ Stack Tecnológico

- **Backend sin servidor**: Azure Functions (Plan de Consumo, Linux)
- **CI/CD automático**: GitHub Actions conectado a Azure para despliegue continuo.
- **Lenguaje**: Python 3.11
- **Framework**: Azure Functions Python Library
- **Logs**: Integrados con Application Insights.

---

## 📂 Estructura del Proyecto

```plaintext
jira_azure_poc_hu/
├── HttpTrigger/
│   ├── __init__.py         # Dispatcher de la Azure Function
│   ├── main.py             # Lógica principal del procesamiento HTTP
│   ├── shared/             # Utilitarios compartidos (e.g., configuración de logger)
│   └── validators/         # Módulos de validación (e.g., format_validator)
├── requirements.txt        # Dependencias Python
├── host.json               # Configuración de host para Azure Functions
├── local.settings.json     # Variables de entorno para ejecución local
└── .github/workflows/      
    └── main_jira-azure-validator.yml  # Workflows de CI/CD para GitHub Actions
```

---

## ✨ Funcionalidad Principal

- **Endpoint**: `POST /api/HttpTrigger`
- **Entrada esperada**:
```json
{
  "summary": "Como usuario quiero poder registrarme fácilmente"
}
```
- **Validaciones actuales**:
  - Verifica que el `summary` comience con la palabra **"Como "**.
  - Retorna un objeto JSON con el resultado de la validación.

- **Respuesta ejemplo**:
```json
{
  "message": "Request received successfully.",
  "format_validation": {
    "passed": true,
    "details": "Summary starts with 'Como '."
  },
  "data_received": {
    "summary": "Como usuario quiero poder registrarme fácilmente"
  }
}
```

---

## 🛠️ Cómo desplegar cambios

Cada vez que se hace `push` o `merge` en la rama `main`:
- Se ejecuta automáticamente un flujo de trabajo GitHub Actions.
- El flujo despliega los cambios en la Azure Function llamada `jira-azure-validator`.

---

## 📈 Estado Actual

| Componente             | Estado           |
|-------------------------|------------------|
| Azure Function App      | ✅ Creada y activa |
| CI/CD GitHub Actions    | ✅ Configurado    |
| Application Insights    | ✅ Configurado    |
| Storage Account         | ✅ Configurado    |

---

## 📌 Notas

- El entorno de ejecución en Azure Functions es **Linux** debido al uso del plan gratuito de consumo.
- El desarrollo local se puede realizar utilizando **Visual Studio Code** y **Azure Functions Core Tools**.

---

## 🚀 Futuras Mejoras

- Validar otros campos de la historia de usuario (por ejemplo: descripción, aceptación, etc).
- Integrar validaciones semánticas usando **Azure AI Services**.
- Integrar flujos directos de Jira a Azure mediante **webhooks**.
- Expansión a más validaciones contextuales según criterios de calidad ágil.

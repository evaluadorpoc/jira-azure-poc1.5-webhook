# 📘 CHANGELOG - Proyecto Jira Azure Validator

## 🧪 PoC 1.5 – Integración Webhook Jira + Azure Function (29/04/2025)

### 🚀 Nuevas funcionalidades implementadas

- ✅ **Azure Function 2nd Gen desplegada con CI/CD**:
  - GitHub Actions con autenticación federada OIDC.
  - Despliegue manual ZIP funcional con `functions-action@v1`.

- 🔗 **Integración real-time con Jira Software Cloud**:
  - Webhook `issue.updated` registrado y funcionando correctamente.
  - Eventos entrantes parseados desde payload original de Jira.

- 🧠 **Control de cambios finos (nivel de campo)**:
  - Se filtran eventos **solo cuando cambia el campo `description`**, evitando ejecuciones innecesarias.

- 📝 **Automatización en Jira**:
  - Comentario automático con el número de caracteres del campo `description`.
  - Actualización del campo personalizado `customfield_10038` con el conteo de caracteres.

- 🛠️ **Código preparado para escalar**:
  - Refactorización de `process_request()` y `process_jira_operations()` para aceptar múltiples campos (`custom_fields`, `raw_fields`).
  - Arquitectura limpia y modular (HttpTrigger → Orchestrator → JiraClient).
  
### 📊 Resultados verificados
- ✔️ Solicitudes exitosas en Azure Function con status HTTP 200.
- 🧪 Pruebas reales en Jira (proyecto BTS), resultado visual validado:
  - Comentarios agregados correctamente.
  - Campo "contador description" actualizado en tiempo real.
- 🎯 Reducción de invocaciones innecesarias al validar cambios reales por `changelog`.

---

### 🧩 Próximo paso: PoC 2.0
> Comenzaremos con la integración de **Azure Cognitive Services** para analizar semánticamente la historia y generar una evaluación de calidad del texto. 

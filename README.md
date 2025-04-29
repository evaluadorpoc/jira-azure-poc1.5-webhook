## 🧪 PoC 1.5 – Escucha activa desde Jira

### 🎯 Objetivo

Implementar un flujo automatizado que permita **escuchar eventos de Jira** (creación y edición de historias de usuario) y, mediante una Azure Function, procesar el contenido del campo `description`, evaluarlo y registrar resultados directamente en el issue.

---

### 🧠 Descripción funcional

Cuando se crea o actualiza un issue en Jira:

1. Se dispara un **webhook** configurado para los eventos `issue_created` y `issue_updated`.
2. El webhook realiza una llamada HTTP `POST` a la Azure Function con el siguiente cuerpo JSON mínimo:

```json
{
  "issueKey": "ABC-123",
  "description": "Como usuario quiero registrarme para poder recibir promociones"
}
```

3. La Azure Function ejecuta las siguientes tareas:
   - Calcula la **cantidad de caracteres** del campo `description`.
   - Publica un **comentario** en el issue con el mensaje:
     > 📝 Esta historia tiene 58 caracteres en la descripción.
   - Actualiza el campo personalizado `customfield_10038` con el valor numérico `58`.

---

### ⚙️ Requisitos técnicos

- **Webhook en Jira configurado** con los eventos:
  - `issue_created`
  - `issue_updated`
- **Payload JSON** con al menos:
  - `"issueKey"` (clave del ticket)
  - `"description"` (contenido del campo)
- **Azure Function activa** y publicada con endpoint público.
- **Campo personalizado creado en Jira** (`customfield_10038`) de tipo número.
- Permisos adecuados en el API Token de Jira:
  - Crear comentarios
  - Editar campos

---

### 📌 Propósito estratégico

Esta prueba de concepto permite:

- Automatizar validaciones iniciales del contenido de historias de usuario.
- Establecer una **trazabilidad estructurada** a través de comentarios y campos.
- Habilitar una base operativa para futuras mejoras basadas en **inteligencia artificial**, como generación de recomendaciones o detección de calidad de historias.

---

🔄 Esta PoC se considera parte de la transición hacia modelos de calidad asistida en backlog y control ágil automatizado.

## [POC 1.5] Escucha de cambios desde Jira hacia Azure Function - CI/CD habilitado

### Añadido
- Nueva Azure Function `jira-azure-validator` diseñada para recibir eventos desde Jira (como edición o creación de issues).
- Implementación de webhook para invocar la función desde Jira con payloads personalizados.

### Corregido
- Error de autenticación con `azure/login@v2` en GitHub Actions: Se registró una aplicación en Azure Active Directory (`github-cicd-deploy`) y se configuró autenticación federada.
- Asignación del rol "Colaborador" a la aplicación para habilitar despliegue a través de CI/CD.

### Mejoras
- Pipeline actualizado para empaquetado manual de dependencias (`.python_packages`) en caso de que `oryx` falle.
- Separación de repositorio (`jira-azure-poc1.5-webhook`) para mantener trazabilidad por POC.

---

📅 Fecha: 2025-04-29  
👤 Responsable: @paulsanchez  

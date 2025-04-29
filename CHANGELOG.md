## [PoC 1.5] - 2025-04-29

### Added
- Configuración inicial de la PoC 1.5 para escuchar eventos `issue created` e `issue updated` desde Jira.
- Recepción y procesamiento de los campos `description`, `issueKey` y `customfield_10038` mediante Azure Functions.
- Funcionalidad para contar caracteres de la descripción y registrar el resultado como comentario y valor del custom field.

### Changed
- Se creó un nuevo repositorio independiente para aislar y controlar mejor el ciclo CI/CD por PoC.
- Implementación del despliegue manual via ZIP sin compilación en Azure (`scm-do-build-during-deployment: false`).

### Fixed
- Error de autenticación resuelto mediante configuración de credenciales federadas (OIDC) entre GitHub Actions y Azure.
- Se corrigió el login fallido mediante Service Principal al adoptar autenticación federada como mejor práctica.

### Notes
- Esta PoC marca la transición hacia una arquitectura más escalable y segura para integraciones Jira ↔ Azure.

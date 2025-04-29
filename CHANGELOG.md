# 📓 CHANGELOG - Jira Azure Validator

Todas las modificaciones relevantes de este proyecto serán documentadas aquí, siguiendo buenas prácticas de documentación de versiones.

---
## [1.0.0] - 2025-04-29
### Added
- CI/CD funcional con GitHub Actions para Azure Functions Python 3.11.
- Paquetes Python se instalan manualmente en `.python_packages/lib/site-packages`.

### Changed
- Se desactiva `remote-build` y `scm-do-build-during-deployment` en favor del empaquetado manual.

### Fixed
- Error 500 causado por falta de dependencias (`requests`, etc.) en despliegues anteriores.

### Notes
- Esta configuración será la base para futuras funciones Azure en este repositorio.
- El archivo `main_jira-azure-validator.yml` contiene la lógica de build/deploy validada.


## [0.1.0] - 2025-04-28

### 🎯 Added (Añadido)
- Despliegue exitoso de la primera Azure Function (`HttpTrigger`) en Azure (Plan de Consumo, Linux).
- Implementación de CI/CD automático utilizando GitHub Actions para despliegues a Azure.
- Configuración inicial de Application Insights para monitoreo de logs y métricas en producción.
- Arquitectura modular del proyecto:
  - `HttpTrigger/` como carpeta raíz de funciones.
  - `shared/logger_config.py` para configuración centralizada de logging.
  - `validators/` para validadores individuales.
  - Orquestador de validaciones (`validators/orchestrator.py`) para combinar y ejecutar todas las validaciones.
- Primeras validaciones implementadas:
  - Validación que el campo `description` comience con "Como ".
  - Validación que el campo `description` tenga mínimo 10 caracteres.
- Creación del archivo `requirements.txt` para manejo de dependencias Python.
- Configuración de archivos `host.json`, `local.settings.json` y `function.json` para la ejecución local y despliegue en Azure.
- Primer `README.md` documentando:
  - Stack tecnológico.
  - Estructura del proyecto.
  - Flujo de procesamiento.
  - Despliegue continuo (CI/CD).
  - Futuras mejoras planteadas.

---

### 🛠️ Changed (Modificado)
- Reorganización del `main.py` para delegar validaciones al orquestador, mejorando la mantenibilidad y escalabilidad del sistema.

---

### 🚑 Fixed (Corregido)
- Corrección del error inicial donde la validación operaba sobre `summary` en vez de `description`.
- Ajuste del modelo de logs para incluir mensajes de éxito y advertencia de manera más legible.

---

### 🔥 Removed (Eliminado)
- Eliminación de la validación interna acoplada directamente en `main.py` (antes de modularizar).

---

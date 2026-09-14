# DevOps CI/CD Demo

Aplicación de ejemplo utilizada en la Unidad II del curso DevOps. El repositorio comienza con un pipeline de integración continua deliberadamente sencillo y se ampliará en sesiones posteriores.

## Aplicación

La API expone dos endpoints:

- `GET /health`: verifica que el servicio responde.
- `GET /price?unit_price=10&quantity=10`: calcula el total de una compra. A partir de 10 unidades se aplica un descuento del 10 %.

## Ejecución local

Crear y activar un entorno virtual, y luego instalar las dependencias de desarrollo:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

En Windows PowerShell, la activación es:

```powershell
.\.venv\Scripts\Activate.ps1
```

Ejecutar las verificaciones:

```bash
pytest
flake8 app tests
```

Ejecutar la aplicación:

```bash
flask --app app.main run --debug
```

## Construcción de la imagen

```bash
docker build -t devops-ci-cd-demo:local .
docker run --rm -p 8080:8080 devops-ci-cd-demo:local
```

Después puede comprobarse:

```text
http://localhost:8080/health
http://localhost:8080/price?unit_price=10&quantity=10
```

## Pipeline inicial

El workflow `.github/workflows/ci.yml` produce tres verificaciones independientes:

- `test`: ejecuta las pruebas automatizadas;
- `lint`: ejecuta análisis estático mediante Flake8;
- `build`: comprueba que la imagen de contenedor puede construirse.

El pipeline es intencionalmente simple. No utiliza caché, matrices, artifacts, dependencias entre jobs ni mecanismos de despliegue; esas capacidades se incorporan en sesiones posteriores.

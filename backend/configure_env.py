"""Prepara el .env local sin mostrar ni guardar secretos en el repositorio."""
from pathlib import Path
import secrets


def main():
    root = Path(__file__).resolve().parent.parent
    env_path = root / ".env"
    if not env_path.exists():
        env_path.write_text((root / ".env.example").read_text(encoding="utf-8"), encoding="utf-8")

    lines = env_path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.startswith("DJANGO_SECRET_KEY="):
            if not line.split("=", 1)[1].strip():
                lines[index] = "DJANGO_SECRET_KEY=" + secrets.token_urlsafe(50)
            break
    else:
        lines.append("DJANGO_SECRET_KEY=" + secrets.token_urlsafe(50))

    env_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Entorno local preparado. La clave permanece en .env y no se muestra.")


if __name__ == "__main__":
    main()

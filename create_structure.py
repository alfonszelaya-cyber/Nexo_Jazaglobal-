import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(BASE_DIR, "app")

STRUCTURE = {
    "routers": [
        "__init__.py",
        "finance_router.py",
        "security_router.py",
        "operations_router.py",
        "reports_router.py",
        "integrations_router.py",
        "system_router.py"
    ],
    "schemas": [
        "__init__.py",
        "finance_schemas.py",
        "security_schemas.py",
        "operations_schemas.py",
        "reports_schemas.py",
        "system_schemas.py"
    ],
    "dependencies": [
        "__init__.py",
        "auth_dependency.py",
        "role_dependency.py",
        "db_dependency.py"
    ],
    "services": [
        "__init__.py",
        "finance_service.py",
        "security_service.py",
        "operations_service.py",
        "reports_service.py",
        "system_service.py"
    ]
}

def create_structure():
    for folder, files in STRUCTURE.items():
        folder_path = os.path.join(APP_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"# {file} — Enterprise 3.0\n")

    print("✅ Estructura enterprise creada correctamente.")

if __name__ == "__main__":
    create_structure()

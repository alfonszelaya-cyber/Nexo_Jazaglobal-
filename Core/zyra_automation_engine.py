# ============================================================
# zyra_automation_engine.py
# Motor de automatización del CORE ZYRA/NEXO
# ============================================================

import os
import json
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

AUTOMATION_FILE = os.path.join(DATA_DIR, "automation.json")

# -----------------------------
# Registro de tareas automatizadas
# -----------------------------
_tasks = []

def register_task(task_callable, description=""):
    """
    Registra una tarea automatizada que puede ejecutarse posteriormente
    """
    if callable(task_callable):
        _tasks.append({"task": task_callable, "description": description})

def remove_task(task_callable):
    """
    Elimina una tarea registrada
    """
    global _tasks
    _tasks = [t for t in _tasks if t["task"] != task_callable]

def clear_tasks():
    """
    Limpia todas las tareas registradas
    """
    global _tasks
    _tasks.clear()

def run_tasks():
    """
    Ejecuta todas las tareas registradas y guarda log en JSON
    """
    results = []
    for t in _tasks:
        try:
            res = t["task"]()
            results.append({"description": t["description"], "result": res, "ts": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        except Exception as e:
            results.append({"description": t["description"], "error": str(e), "ts": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

    # Guardar en archivo de automatización
    try:
        if os.path.exists(AUTOMATION_FILE):
            with open(AUTOMATION_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
        else:
            data = []
    except Exception:
        data = []

    data.extend(results)

    try:
        with open(AUTOMATION_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[AUTOMATION_ENGINE] Error al guardar resultados: {e}")

    return results
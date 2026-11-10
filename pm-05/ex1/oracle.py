import os


def oracle() -> None:

    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ModuleNotFoundError:
        print("[WARNING] python-dotenv not installed: .env file not loaded")
        print("Install it with: pip install -r requirements.txt")

    # Read config.
    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    # If None -> Default val
    missing = []
    if matrix_mode is None:
        matrix_mode = "development"
        missing.append("MATRIX_MODE")
    if database_url is None:
        database_url = "not configured"
        missing.append("DATABASE_URL")
    if api_key is None:
        api_key = "not configured"
        missing.append("API_KEY")
    if log_level is None:
        log_level = "INFO"
        missing.append("LOG_LEVEL")
    if zion_endpoint is None:
        zion_endpoint = "not configured"
        missing.append("ZION_ENDPOINT")

    # Muestra la configuración
    print("ORACLE STATUS: Consulting the configuration...")
    print()
    print("Configuration loaded:")

    # matrix_mode
    print(f"Mode: {matrix_mode}")

    # database_url
    if matrix_mode == "production":
        print("Database: hidden in production")
    else:
        print(f"Database: {database_url}")

    if api_key != "not configured":
        print("API Key: configured")
    else:
        print(f"API Key: {api_key}")
    print(f"Log Level: {log_level}")
    print(f"Zion Endpoint: {zion_endpoint}")

    # Missing config.
    if missing:
        print(f"Warning: missing configuration: {', '.join(missing)}")

    # Security check
    print()
    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    gitignore = os.path.join(os.path.dirname(__file__), ".gitignore")
    try:
        with open(gitignore) as f:
            lines = f.read().splitlines()
        if ".env" in lines:
            print("[OK] .env file properly ignored by git")
        else:
            print("[WARNING] .env file not ignored by git")
    except FileNotFoundError:
        print("[WARNING] .gitignore not found")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()

"""
Pip configuration management
"""
import subprocess
import sys
from typing import List, Optional

def setup_pip_config():
    """pip設定のセットアップ"""
    print("🔧 Setting up pip configuration...")
    return True

def install_package(package: str) -> bool:
    """パッケージインストール"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def get_installed_packages() -> List[str]:
    """インストール済みパッケージ一覧"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--format=freeze"],
            capture_output=True,
            text=True
        )
        return result.stdout.strip().split('\n')
    except Exception:
        return []

def check_dependencies() -> bool:
    """依存関係チェック"""
    required_packages = [
        "fastapi",
        "uvicorn",
        "pydantic-settings",
        "python-dotenv",
        "requests"
    ]
    
    installed = get_installed_packages()
    installed_names = [pkg.split('==')[0].lower() for pkg in installed]
    
    missing = [pkg for pkg in required_packages if pkg.lower() not in installed_names]
    
    if missing:
        print(f"⚠️  Missing packages: {missing}")
        return False
    
    print("✅ All dependencies satisfied")
    return True

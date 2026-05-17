import subprocess

def run_bob(prompt: str, cwd: str = ".", mode: str = "code", timeout: int = 500) -> dict:
    try:
        result = subprocess.run(
            [
                "bob",
                "--hide-intermediary-output",
                "--approval-mode", "auto_edit",  # <- yolo -> auto_edit
                "--chat-mode", mode,
            ],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=cwd
        )
        return {
            "success": result.returncode == 0,
            "output": result.stdout.strip(),
            "error": result.stderr.strip()
        }
    except subprocess.TimeoutExpired:
        return {"success": False, "output": "", "error": "Timeout 180s"}
    except FileNotFoundError:
        return {"success": False, "output": "", "error": "Bob Shell not found"}

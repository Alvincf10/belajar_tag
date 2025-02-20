# main_script.py
import subprocess
from helper import helper_function

def create_git_tag(tag_name, message=None):
    try:
        # Membuat tag baru
        command = ['git', 'tag']
        if message:
            command.extend(['-a', tag_name, '-m', message])
        else:
            command.append(tag_name)

        subprocess.run(command, check=True)
        print(f"Tag '{tag_name}' berhasil dibuat.")

        # Push tag ke remote repository
        push_command = ['git', 'push', 'origin', tag_name]
        subprocess.run(push_command, check=True)
        print(f"Tag '{tag_name}' berhasil di-push ke remote repository.")

    except subprocess.CalledProcessError as e:
        print(f"Terjadi kesalahan saat membuat atau mendorong tag: {e}")

if __name__ == "__main__":
    helper_function()  # Panggil fungsi dari modul bantuan
    create_git_tag("v1.0.2", "Release version 1.0.0")
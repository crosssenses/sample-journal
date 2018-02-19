import sys, os

sys.path.append(os.path.abspath("../../beautiful-reports/django"))


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

FROM python:3.10-slim

WORKDIR /app
COPY . .

CMD ["python", "-m", "program.py", "program_tests.py"]

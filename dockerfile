FROM python:3.12

WORKDIR /app

COPY student_grade.py .

CMD ["python", "student_grade.py"]
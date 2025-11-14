FROM python:3.11

RUN pip install tensorflow==2.15
RUN pip install Flask==3.0
RUN pip install pillow==12.0.0

COPY vgg16Variant.keras /vgg16Variant.keras
COPY api.py /api.py


CMD ["python", "api.py"]
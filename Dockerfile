FROM python:3.10-slim

ARG version="0.1.0"
ARG name="investbook"

ENV DIST="${name}-${version}-py3-none-any.whl"

WORKDIR /app

COPY dist/${DIST} ./

RUN pip install $DIST

COPY investbook /app/investbook

COPY investbook/app/front/images/ /app/front/images/

EXPOSE 8080

CMD ["python", "/app/investbook/__main__.py"]
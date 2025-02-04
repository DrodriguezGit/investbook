FROM python:3.10-slim
 
ARG version="0.1.1"
 
ARG name="investbook"
 
ENV DIST="${name}-${version}-py3-none-any.whl"
 
WORKDIR /app
 
COPY "dist/${DIST}" ./
 
RUN pip install $DIST

EXPOSE 8080

CMD ["python", "-m", "investbook"]
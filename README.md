# 📈 InvestBook

**Una aplicación web moderna para análisis y seguimiento de inversiones financieras**

InvestBook es una plataforma integral de análisis financiero que permite a los usuarios realizar seguimiento de acciones, visualizar datos históricos, analizar métricas financieras y mantenerse actualizado con las últimas noticias del mercado. Construida con Python y NiceGUI, ofrece una interfaz intuitiva y funcionalidades avanzadas para inversores de todos los niveles.

![InvestBook Logo](investbook/app/front/images/logo2.png)

## 🚀 Comenzando

Estas instrucciones te permitirán obtener una copia del proyecto funcionando en tu máquina local para propósitos de desarrollo y pruebas.

### 📋 Pre-requisitos

Que cosas necesitas para instalar el software y como instalarlas:

```bash
Python >= 3.8
Poetry (recomendado) o pip
Git
```

### 🔧 Instalación

Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutándose:

**1. Clona el repositorio**
```bash
git clone https://github.com/tu-usuario/investbook.git
cd investbook
```

**2. Instala las dependencias usando Poetry (recomendado)**
```bash
poetry install
```

O usando pip:
```bash
pip install -r requirements.txt
```

**3. Configura las variables de entorno**
```bash
cp .env.example .env
# Edita el archivo .env con tus API keys
```

**4. Configura tus API Keys**

Necesitarás obtener las siguientes API keys gratuitas:
- [Financial Modeling Prep (FMP)](https://financialmodelingprep.com/developer/docs)
- [Finnhub](https://finnhub.io/docs/api)

Agrega las keys en tu archivo `.env`:
```
FMP_API_KEY=tu_fmp_api_key_aqui
FINNHUB_API_KEY=tu_finnhub_api_key_aqui
```

**5. Ejecuta la aplicación**
```bash
poetry run python -m investbook
```

O con Python directamente:
```bash
python -m investbook
```

**6. Accede a la aplicación**

Abre tu navegador y ve a: `http://localhost:8080`

## ⚡ Uso

### Funcionalidades Principales

#### 🔐 Sistema de Autenticación
- Inicia sesión con credenciales de usuario
- Sistema de gestión de usuarios basado en JSON
- Persistencia de sesión durante la navegación

#### 📊 Dashboard Principal
- **Seguimiento de Portafolio**: Agrega y elimina acciones de tu lista personal
- **Visualización de Datos**: Gráficos interactivos con datos históricos
- **Métricas en Tiempo Real**: Precios actuales y cambios porcentuales
- **Búsqueda Inteligente**: Encuentra acciones por símbolo o nombre

#### 📈 Análisis Detallado
- **Información Fundamental**: Datos de la empresa, sector e industria
- **Métricas Financieras**: ROA, ROE, ratios de liquidez y más
- **Estados Financieros**: Cuenta de resultados y balance
- **Filtros Temporales**: Visualiza datos por períodos (1 semana a 1 año)

#### 📰 Noticias y Actualizaciones
- Últimas noticias de cada

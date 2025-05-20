# 🛡️ Protección Inteligente para Préstamos en Lendle.xyz

Este proyecto fue desarrollado como parte de un hackathon de Nucleo con el objetivo de ofrecer una solución automatizada para **proteger las posiciones de préstamo en el protocolo Lendle.xyz**, que opera sobre la red de Mantle.

## 🔍 ¿Qué hace?

El sistema monitorea en tiempo real el **Health Factor** de las posiciones de préstamo en Lendle, y ejecuta **acciones preventivas** cuando detecta riesgo de liquidación, tales como:

- 🔁 **Repagos parciales automáticos** (si se tiene liquidez disponible)
- 🧠 **Ajuste inteligente de colateral** mediante estrategias personalizadas

Con esta herramienta, los usuarios pueden **evitar pérdidas innecesarias**, mantenerse seguros y aprovechar al máximo sus activos sin tener que estar monitoreando constantemente.

## 🌐 Tecnologías utilizadas

- `Python` + `web3.py`: para conexión con smart contracts y monitoreo en tiempo real
- `Mantle Network`: red sobre la cual corre Lendle.xyz
- `Lendle.xyz`: protocolo DeFi utilizado para préstamos y colateral
- `Telegram Bot API` / `Discord Webhooks`: para notificaciones en tiempo real con Eliza OS

## 🚀 Configuración de Wallet
- En el archivo .env configurar wallet y llave privada de la que se realizaran las consultas de Healt Factor y la creción de Supply

```bash
   PRIVATE_KEY=0xPRIVATEKEY
   ADDRESS=0xPUBLICKEY
```

## 🚀 Cómo ejecutarlo

1. Clona el repositorio:
   ```bash
   git clone https://github.com/SergioFinix/DARVS_RISK_RADAR.git
   cd DARVS_RISK_RADAR
   pip install -r requirements.txt
   python \app.py
   ```


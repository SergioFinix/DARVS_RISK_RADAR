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

## 🚀 Cómo ejecutarlo

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/protector-lendle.git
   cd protector-lendle

import logging
import os
import subprocess
import atexit
from flask import Flask, jsonify

# Configuração de log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# App Flask
app = Flask(__name__)
bot_process = None

@app.route('/')
def home():
    return 'Bot GPT-4 no Telegram está rodando!'

@app.route('/status')
def status():
    return jsonify({"status": "active" if (bot_process and bot_process.poll() is None) else "inactive"})

def start_bot():
    global bot_process
    logger.info("Iniciando o processo do bot...")
    bot_process = subprocess.Popen(['python3', 'run_bot.py'])

    def cleanup():
        if bot_process:
            logger.info("Finalizando bot...")
            bot_process.terminate()

    atexit.register(cleanup)
    logger.info(f"Bot iniciado com PID {bot_process.pid}")

start_bot()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
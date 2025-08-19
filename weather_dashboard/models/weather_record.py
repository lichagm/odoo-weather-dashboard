import requests
import os
from dotenv import load_dotenv
from odoo import models, fields, api

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

API_KEY = os.getenv("API_WEATHER_KEY")

class WeatherRecord(models.Model):
    _name = "weather.record"
    _description = "Registro del clima"

    name = fields.Char(string="Ciudad", required=True)
    temperature = fields.Char(string="Temperatura (°C)", readonly=True)
    description = fields.Text(string="Descripción", readonly=True)
    last_update = fields.Datetime(string="Última actualización", readonly=True)

    def action_get_temperature(self):
        """Obtiene la temperatura de la ciudad especificada."""
        for record in self:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={record.name}&appid={API_KEY}&units=metric&lang=es"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                record.temperature = f"{data['main']['temp']} °C"
                record.last_update = fields.Datetime.now()
                record.description = (
                    f"Clima: {data['weather'][0]['description'].capitalize()}\n"
                    f"Humedad: {data['main']['humidity']}%\n"
                    f"Presión: {data['main']['pressure']} hPa\n"
                    f"Viento: {data['wind']['speed']} m/s\n"
                    f"Lluvia (última hora): {data.get('rain', {}).get('1h', 0)} mm"
                )
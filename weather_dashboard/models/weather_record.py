import requests
from odoo import models, fields, api

class WeatherRecord(models.Model):
    _name = "weather.record"
    _description = "Registro del clima"

    name = fields.Char(string="Ciudad", required=True)
    temperature = fields.Char(string="Temperatura (°C)", readonly=True)
    description = fields.Text(string="Descripción", readonly=True)
    last_update = fields.Datetime(string="Última actualización", readonly=True)
    api_key = fields.Char(string="API Key", default="884f14460febb7ede5a77fabff5dfcde")


    def action_get_temperature(self):
        """Obtiene la temperatura de la ciudad especificada."""
        api_key = self.api_key
        for record in self:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={record.name}&appid={api_key}&units=metric&lang=es"
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
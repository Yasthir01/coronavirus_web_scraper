import requests
import json

API_KEY = "t0VtJua_Mejx"
PROJECT_TOKEN = "tB-CUi7E7Uuw"
RUN_TOKEN = "tqP-Tupz4eRm"

# # we need to get the url from parsehub
# response = requests.get(f'http://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={'api_key': API_KEY})

# #loads the data
# data = json.loads(response.text)
# print(data)


class Data:
	"""A class representing the data from coronavirus cases"""
	def __init__(self, api_key, project_token):
		"""Initialize the attributes"""
		self.api_key = api_key
		self.project_token = project_token
		self.params = {
		'api_key' : self.api_key
		}
		self.get_data()

	def get_data(self):
		response = requests.get(f'http://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data', params=self.params)
		self.data = json.loads(response.text)


	def get_total_cases(self):
		"""returns total amount of corona cases"""
		data = self.data['total']

		for content in data:
			if content['name'] == 'Coronavirus Cases:':
				return content['value']

	def get_total_deaths(self):
		"""returns total amount of corona deaths"""
		data = self.data['total']

		for content in data:
			if content['name'] == 'Deaths:':
				return content['value']

	def get_country_data(self, country):
		data = self.data['country']

		for content in data:
			if content['name'].lower() == country.lower():
				return content



data = Data(API_KEY, PROJECT_TOKEN)
print(data.get_total_cases())




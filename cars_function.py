def make_car(manufacturer, model, **optional_info):
	car = {}
	car['manufacturer'] = manufacturer
	car['model'] = model
	for key,value in optional_info.items():
		car[key] = value
	return car
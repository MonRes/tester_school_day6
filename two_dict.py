device_names = {1: 'device_1', 2: 'device_2', 3: 'device_3'}
device_models = {1: 'Xeon', 2: 'Corsair', 3: 'Corsair'}

device_list = []

for dev_id, name in device_names.items():
    model = device_models[dev_id] #patrzymy co jest przypisane do klucza dev_id czyli model
    device_list.append({'id': dev_id, 'name': name, 'model': model}) #i przepisujemy do nowej tablicy


print(device_list)

model_dict = {}

for dev_id, model in device_models.items():
    if model in model_dict:
        model_dict[model].append(device_names[dev_id])
    else:
        model_dict[model] = [device_names[dev_id]]

print(model_dict)
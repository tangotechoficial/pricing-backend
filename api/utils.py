import csv
import io

def parse_csv_model(csvfile, model):
    reader = csv.DictReader(io.StringIO(csvfile))
    model_instances = []
    for row in reader:
        model_instance = model()
        for field in row.keys():
            setattr(model_instance, field, row[field])
        model_instances.append(model_instance)
    return model_instances

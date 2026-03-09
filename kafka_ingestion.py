import json
import time

def send_data():
    data = {
        "user": "Navneet",
        "event": "data_ingestion",
        "source": "kafka_pipeline"
    }

    print("Sending data to Kafka topic...")
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    send_data()
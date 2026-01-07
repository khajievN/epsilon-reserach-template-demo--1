from generated.models import create_dataset

def main():
    # Load the dataset
    dataset = create_dataset()
    print(f"Loaded {len(dataset)} records")

    # Your analysis code here
    for record in dataset:
        # Example: Access fields from your archetype
        # print(record.field_name)
        print("Health Rate" + record.vitals.healthrate)
        print("Blood Pressure" + record.vitals.bloodpressure)
        pass

    return {"result": "Analysis complete"}

if __name__ == "__main__":
    result = main()
    print(result)

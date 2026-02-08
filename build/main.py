from generated.models import create_dataset


def main():
    dataset = create_dataset()
    records = list(dataset)

    years = [int(r.enrollment.year) for r in records if r.enrollment.year]

    return {
        "total_records": len(records),
        "avg_enrollment_year": sum(years) / len(years) if years else 0,
        "min_year": min(years) if years else 0,
        "max_year": max(years) if years else 0,
        "unique_universities": len(set(r.enrollment.university for r in records if r.enrollment.university))
    }


if __name__ == "__main__":
    result = main()
    print(result)
from generated.models import create_dataset
from collections import Counter


def main():
    dataset = create_dataset()
    records = list(dataset)

    uni_counts = Counter(r.enrollment.university for r in records if r.enrollment.university)
    top_5 = dict(uni_counts.most_common(5))

    has_email = sum(1 for r in records if r.personal_info.email)

    return {
        "total_records": len(records),
        "records_with_email": has_email,
        "email_coverage_pct": round(has_email / len(records) * 100, 1) if records else 0,
        "top_5_universities": top_5,
        "distinct_universities": len(uni_counts)
    }


if __name__ == "__main__":
    result = main()
    print(result)

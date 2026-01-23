# Auto-generated Python classes from archetype
# Loads dummy data from CSV file for testing

import csv
import os
from typing import Any, Dict, List, Optional


def create_dataset(csv_file=None):
    """Create a dataset from CSV dummy data"""
    if csv_file is None:
        # Default to dummy CSV file
        csv_file = 'generated/data.csv'
    
    if not os.path.exists(csv_file):
        print(f'CSV file not found: {csv_file}')
        print('Run "epsilon archetypes <dataset_id>" to generate dummy data')
        return DatasetWrapper([])
    
    # Load CSV data
    records = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    
    print(f'Loaded {len(records)} dummy records from CSV')
    return DatasetWrapper(records)


class DatasetWrapper:
    """Wrapper for dataset records with easy access"""
    def __init__(self, records):
        self.records = records if isinstance(records, list) else [records]
    
    def __len__(self):
        return len(self.records)
    
    def __iter__(self):
        for record in self.records:
            yield Root(record)
    
    def __getitem__(self, index):
        return Root(self.records[index])
    
    @property
    def first(self):
        return Root(self.records[0]) if self.records else None


class Examinations:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def blood_pressure(self):
        # Try direct access first (JSON format)
        if 'blood_pressure' in self._data:
            return self._data['blood_pressure']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.blood_pressure'):
                return v
        return None

    @property
    def date(self):
        # Try direct access first (JSON format)
        if 'date' in self._data:
            return self._data['date']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.date'):
                return v
        return None

    @property
    def heart_rate(self):
        # Try direct access first (JSON format)
        if 'heart_rate' in self._data:
            return self._data['heart_rate']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.heart_rate'):
                return v
        return None


class Person:
    def __init__(self, data):
        self._data = data if data else {}


class Root:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def examinations(self):
        # Handle nested field access with dot notation
        if 'examinations' in self._data and isinstance(self._data['examinations'], dict):
            return Examinations(self._data['examinations'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'examinations.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Examinations(flattened)

    @property
    def person(self):
        # Handle nested field access with dot notation
        if 'person' in self._data and isinstance(self._data['person'], dict):
            return Person(self._data['person'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'person.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Person(flattened)

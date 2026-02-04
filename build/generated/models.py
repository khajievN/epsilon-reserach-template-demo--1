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


class Personal_Info:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def first_name(self):
        # Try direct access first (JSON format)
        if 'first_name' in self._data:
            return self._data['first_name']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.first_name'):
                return v
        return None

    @property
    def last_name(self):
        # Try direct access first (JSON format)
        if 'last_name' in self._data:
            return self._data['last_name']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.last_name'):
                return v
        return None

    @property
    def email(self):
        # Try direct access first (JSON format)
        if 'email' in self._data:
            return self._data['email']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.email'):
                return v
        return None


class Student:
    def __init__(self, data):
        self._data = data if data else {}


class Enrollment:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def university(self):
        # Try direct access first (JSON format)
        if 'university' in self._data:
            return self._data['university']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.university'):
                return v
        return None

    @property
    def year(self):
        # Try direct access first (JSON format)
        if 'year' in self._data:
            return self._data['year']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.year'):
                return v
        return None


class Root:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def personal_info(self):
        # Handle nested field access with dot notation
        if 'personal_info' in self._data and isinstance(self._data['personal_info'], dict):
            return Personal_Info(self._data['personal_info'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'personal_info.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Personal_Info(flattened)

    @property
    def student(self):
        # Handle nested field access with dot notation
        if 'student' in self._data and isinstance(self._data['student'], dict):
            return Student(self._data['student'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'student.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Student(flattened)

    @property
    def enrollment(self):
        # Handle nested field access with dot notation
        if 'enrollment' in self._data and isinstance(self._data['enrollment'], dict):
            return Enrollment(self._data['enrollment'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'enrollment.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Enrollment(flattened)

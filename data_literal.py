#THE GIANT JSON RESEMBLING BLOB OF DATA IM PRACTICING WITH
import pandas as pd

data = {
  "organization": {
    "id": "ORG-4421",
    "name": "Northwind Analytics",
    "fiscalYear": 2026,
    "departments": [
      {
        "id": "DPT-001",
        "name": "Engineering",
        "manager": "EMP-1001",
        "employees": [
          {
            "id": "EMP-1001",
            "firstName": "Alicia",
            "lastName": "Nguyen",
            "role": "Senior Backend Engineer",
            "salary": 142500,
            "hireDate": "2021-03-12",
            "skills": ["Python", "FastAPI", "PostgreSQL", "Docker"],
            "devices": [
              {
                "deviceId": "LTP-8831",
                "type": "Laptop",
                "model": "ThinkPad X1 Carbon",
                "os": "Windows 11",
                "assignedDate": "2023-01-15"
              },
              {
                "deviceId": "PHN-2219",
                "type": "Phone",
                "model": "iPhone 14",
                "os": "iOS 17",
                "assignedDate": "2023-02-01"
              }
            ],
            "projects": [
              {
                "projectId": "PRJ-9001",
                "name": "Telemetry Pipeline",
                "role": "Lead Developer",
                "startDate": "2023-04-01",
                "endDate": None,
                "status": "active"
              }
            ],
            "activityLog": [
              {
                "timestamp": "2026-02-01T09:14:22Z",
                "action": "commit",
                "details": {
                  "repository": "telemetry-api",
                  "branch": "main",
                  "linesAdded": 182,
                  "linesRemoved": 17
                }
              },
              {
                "timestamp": "2026-02-02T15:44:10Z",
                "action": "login",
                "details": {
                  "ip": "192.168.1.44",
                  "deviceId": "LTP-8831"
                }
              }
            ]
          },
          {
            "id": "EMP-1002",
            "firstName": "Marcus",
            "lastName": "Lee",
            "role": "Data Engineer",
            "salary": 128000,
            "hireDate": "2022-07-19",
            "skills": ["Python", "Airflow", "Spark", "AWS"],
            "devices": [
              {
                "deviceId": "LTP-8832",
                "type": "Laptop",
                "model": "MacBook Pro 14",
                "os": "macOS 14",
                "assignedDate": "2023-03-10"
              }
            ],
            "projects": [
              {
                "projectId": "PRJ-9002",
                "name": "Data Lake Migration",
                "role": "Pipeline Engineer",
                "startDate": "2023-06-01",
                "endDate": None,
                "status": "active"
              }
            ],
            "activityLog": [
              {
                "timestamp": "2026-02-01T11:02:55Z",
                "action": "pipeline_run",
                "details": {
                  "pipeline": "daily_ingest",
                  "durationSec": 442,
                  "recordsProcessed": 1284421
                }
              },
              {
                "timestamp": "2026-02-03T08:22:10Z",
                "action": "login",
                "details": {
                  "ip": "192.168.1.55",
                  "deviceId": "LTP-8832"
                }
              }
            ]
          }
        ]
      },
      {
        "id": "DPT-002",
        "name": "Product",
        "manager": "EMP-2001",
        "employees": [
          {
            "id": "EMP-2001",
            "firstName": "Jasmine",
            "lastName": "Ortiz",
            "role": "Product Manager",
            "salary": 118000,
            "hireDate": "2020-11-02",
            "skills": ["Roadmapping", "User Research", "Analytics"],
            "devices": [
              {
                "deviceId": "LTP-9921",
                "type": "Laptop",
                "model": "Surface Laptop 5",
                "os": "Windows 11",
                "assignedDate": "2023-05-22"
              }
            ],
            "projects": [
              {
                "projectId": "PRJ-9001",
                "name": "Telemetry Pipeline",
                "role": "Product Owner",
                "startDate": "2023-04-01",
                "endDate": None,
                "status": "active"
              },
              {
                "projectId": "PRJ-9003",
                "name": "Usage Dashboard",
                "role": "Product Owner",
                "startDate": "2024-01-15",
                "endDate": None,
                "status": "active"
              }
            ],
            "activityLog": [
              {
                "timestamp": "2026-02-01T16:10:44Z",
                "action": "meeting",
                "details": {
                  "topic": "Q2 Roadmap",
                  "durationMin": 45
                }
              }
            ]
          }
        ]
      }
    ]
  },
  "projects": [
    {
      "projectId": "PRJ-9001",
      "name": "Telemetry Pipeline",
      "budget": 450000,
      "status": "active",
      "milestones": [
        {
          "id": "MS-01",
          "name": "MVP Delivery",
          "dueDate": "2024-06-01",
          "completed": True
        },
        {
          "id": "MS-02",
          "name": "Scalability Upgrade",
          "dueDate": "2025-12-01",
          "completed": False
        }
      ]
    },
    {
      "projectId": "PRJ-9002",
      "name": "Data Lake Migration",
      "budget": 600000,
      "status": "active",
      "milestones": [
        {
          "id": "MS-01",
          "name": "S3 Replication",
          "dueDate": "2024-09-01",
          "completed": True
        }
      ]
    },
    {
      "projectId": "PRJ-9003",
      "name": "Usage Dashboard",
      "budget": 220000,
      "status": "active",
      "milestones": []
    }
  ]
}
#PRACTICE WORKING WITH DEEPLY NESTED DICTIONAIRES BY CHAINING INDEXING AND GET() METHOD
li = list(data.values())
print(len(li))
print(li[1][0].get('milestones')[0].get('id'))
print(li[0].get('departments')[1].get('employees')[0].get('projects')[1].get('projectId'))



sample = {"a":1, "b":2, "c":[1, 2, 3]}
df = pd.DataFrame([sample])
#print(df.head())

df2 = pd.DataFrame([data])
#print(df2.head())
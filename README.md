# 🛡️ GearGuard

<div align="center">

# ⚙️ GearGuard — Maintenance Intelligence for the Modern Workplace

**An Odoo-powered equipment maintenance platform that turns reactive repairs into a structured, trackable and increasingly preventive operation.**

[![Odoo](https://img.shields.io/badge/Odoo-18-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/) [![Python](https://img.shields.io/badge/Python-Odoo%20ORM-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/) [![Status](https://img.shields.io/badge/Status-Hackathon%20Build-00C853?style=for-the-badge)](#-project-status)

### 🏆 Odoo × Adani University Hackathon
**Built by Team GearGuard**

</div>

---

## ✨ Why GearGuard?

Equipment failure is not just a repair problem. It can mean **downtime, delayed operations, missed maintenance schedules and poor visibility into assets.**

GearGuard creates one operational layer for:

**Assets → Maintenance → Scheduling → Execution → Resolution → Insights**

Instead of treating maintenance as disconnected records, GearGuard connects the **equipment's operational state** to the **maintenance workflow**.

---

## 🚀 What Makes This Build Different?

This is not just an equipment CRUD module. GearGuard contains **real business rules, relational data and automation**.

| Capability | What happens |
|---|---|
| 🧰 Asset Management | Track equipment, serial numbers, locations, departments and lifecycle status |
| 📝 Maintenance Requests | Log issues, priorities, technicians, schedules and resolutions |
| 🔄 Workflow Engine | New → In Progress → Repaired with cancellation |
| 🔗 Live Status Sync | Starting work moves equipment to **Under Maintenance** |
| 🧠 Smart Validation | Invalid dates, workflow transitions and incomplete repairs are blocked |
| ⏰ Due Detection | Equipment and requests can be identified as due or overdue |
| 🔧 Preventive Plans | Define recurring maintenance schedules |
| ⚡ Automated Requests | Odoo cron can generate preventive maintenance requests |
| 📊 Operations Dashboard | Monitor equipment and maintenance KPIs |
| 📈 Analytics | Graph and Pivot views for maintenance operations |
| 🔐 Access Control | Odoo ACL permissions protect application models |

---

## 🧭 Product Flow

```text
                         ┌───────────────────────┐
                         │       EQUIPMENT       │
                         │ Asset • Serial • Site │
                         │ Status • Maintenance  │
                         └───────────┬───────────┘
                                     │
                              Issue / Schedule
                                     │
                                     ▼
                    ┌──────────────────────────────┐
                    │     MAINTENANCE REQUEST      │
                    │ Priority • Technician        │
                    │ Schedule • Issue • Resolution│
                    └──────────────┬───────────────┘
                                   │
             ┌─────────────────────┼────────────────────┐
             ▼                     ▼                    ▼
           NEW ─────────────► IN PROGRESS ──────────► REPAIRED
             │                     │                    │
             │                     ▼                    ▼
             │              Equipment =              Equipment =
             │            UNDER MAINTENANCE             ACTIVE
             ▼
         CANCELLED

        ─────────────────────────────────────────────────────
                     PREVENTIVE MAINTENANCE
        ─────────────────────────────────────────────────────
                    Plan → Due Date → Cron
                              │
                              ▼
                     Auto Maintenance Request
```

---

## 🧠 Core Business Logic

### 1. Equipment Intelligence
- Asset code and serial number tracking
- Location, department and maintenance team
- Current operational status
- Last and next maintenance dates
- Linked maintenance requests
- Open request count
- Maintenance-due state

Asset codes and serial numbers are protected against duplicates.

### 2. Controlled Maintenance Workflow

```text
NEW
 │
 │ Start Work
 ▼
IN PROGRESS
 │
 │ Resolution required
 │ Mark Repaired
 ▼
REPAIRED
```

Invalid transitions are rejected, and a repair requires a recorded resolution.

### 3. Preventive Maintenance

Maintenance plans support:
- Monthly
- Quarterly
- Every 6 Months
- Yearly

A scheduled Odoo job checks due plans and generates maintenance requests automatically. This moves GearGuard beyond purely reactive maintenance.

---

## 📊 Operations Dashboard

```text
┌─────────────────────────────────────────────────────────┐
│                  GEARGUARD OPERATIONS                   │
├──────────────────┬──────────────────┬───────────────────┤
│ TOTAL EQUIPMENT  │ ACTIVE ASSETS    │ UNDER MAINTENANCE │
│       📦         │       ✓          │        🔧         │
├──────────────────┼──────────────────┼───────────────────┤
│ MAINTENANCE DUE  │ OPEN REQUESTS    │ CRITICAL REQUESTS │
│       ⏰         │       📋         │        🚨         │
├──────────────────┴──────────────────┴───────────────────┤
│                  OVERDUE REQUESTS                        │
│                         ⚠️                              │
└─────────────────────────────────────────────────────────┘
```

The dashboard metrics are computed from Odoo records rather than static UI values.

---

## 🏗️ Architecture

```text
                         ┌─────────────────┐
                         │     ODOO UI     │
                         │ Forms / Lists   │
                         │ Search / Graph  │
                         └────────┬────────┘
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │       ODOO ORM          │
                    │ Business Rules / Models │
                    └───────────┬─────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
       ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
       │  Equipment  │◄─►│  Requests   │   │    Plans    │
       │    Model    │   │    Model    │   │ Preventive  │
       └─────────────┘   └─────────────┘   └──────┬──────┘
                                                   │
                                                   ▼
                                           ┌──────────────┐
                                           │ Odoo Cron    │
                                           │ Daily Check  │
                                           └──────┬───────┘
                                                  │
                                                  ▼
                                      Automatic Maintenance
                                             Request

                         ┌─────────────────────────┐
                         │       PostgreSQL        │
                         │      Odoo Database      │
                         └─────────────────────────┘
```

---

## 🧩 Project Structure

```text
GearGuard-Odoo-Hackathon/
│
├── __manifest__.py
├── __init__.py
│
├── models/
│   ├── __init__.py
│   ├── equipment.py
│   ├── maintenance_request.py
│   ├── maintenance_plan.py
│   └── maintenance_dashboard.py
│
├── views/
│   ├── equipment_view.xml
│   ├── maintenance_request_view.xml
│   ├── maintenance_request_graph.xml
│   ├── maintenance_plan_view.xml
│   ├── maintenance_dashboard_view.xml
│   └── gearguard_menu.xml
│
├── data/
│   └── maintenance_cron.xml
│
├── security/
│   └── ir.model.access.csv
│
└── README.md
```

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| ERP Framework | **Odoo** |
| Backend | **Python** |
| ORM | **Odoo ORM** |
| UI | **Odoo XML Views** |
| Database | **PostgreSQL** |
| Automation | **Odoo Scheduled Actions / Cron** |
| Security | **Odoo ACL** |
| Analytics | **Odoo Graph + Pivot Views** |

---

## 🔐 Engineering & Data Integrity

GearGuard uses application-level rules to keep maintenance data meaningful:

- Duplicate asset codes are rejected.
- Duplicate serial numbers are rejected.
- Scheduled dates cannot precede request dates.
- Only New requests can start.
- Only In Progress requests can be repaired.
- A repair requires a resolution.
- Completion date is recorded automatically.
- Last maintenance date is updated automatically.
- Equipment status is synchronized with active maintenance work.
- Cancellation checks for other open requests before restoring equipment status.

---

## 🎬 Suggested Demo Flow

**01 → Dashboard** — Show current operational KPIs.

**02 → Equipment** — Open an asset and show its maintenance information and open requests.

**03 → Create Request** — Report a high-priority equipment issue.

**04 → Start Work** — Click Start Work and show the equipment becoming Under Maintenance.

**05 → Resolve** — Enter the resolution and mark the request Repaired.

**06 → Preventive Plan** — Create a recurring maintenance plan.

**07 → Automation** — Explain how the scheduled Odoo job generates requests when plans become due.

**08 → Analytics** — Show Graph/Pivot views for operational reporting.

---

## 💼 Resume-Ready Description

> **GearGuard — Odoo Equipment Maintenance & Preventive Maintenance System**
> Built an Odoo-based maintenance management platform using Python/Odoo ORM with equipment lifecycle tracking, relational maintenance requests, state-driven workflows, validation rules, preventive maintenance plans, scheduled automation, KPI dashboards, Graph/Pivot analytics and ACL-based access control.

**Technical:** Python · Odoo ORM · PostgreSQL · XML Views · Scheduled Actions · Relational Models · Business Logic · Access Control · Analytics

---

## 🏆 Hackathon

Built for the **Odoo × Adani University Hackathon**.

### 👥 Team
| Role | Member |
|---|---|
| Team Leader | **Nirav Vala** |
| Team Member | **Shruti Soni** |

## 📌 Project Status

**Feature-Enhanced Hackathon Prototype**

Core equipment management, maintenance workflow, preventive scheduling, automation and operational analytics are implemented in the repository.

<div align="center">

### ⚙️ Track the Asset. Prevent the Failure. Keep Operations Moving.

**GearGuard**

</div>
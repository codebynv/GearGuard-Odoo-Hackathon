                                                                  # 🛠️ GearGuard

<div align="center">

## Smart Equipment Maintenance Tracker

**A focused Odoo workflow for tracking equipment, maintenance requests, technicians, priorities, and repair status.**

<p>
  <img src="https://img.shields.io/badge/Odoo-Framework-714B67?style=for-the-badge&logo=odoo&logoColor=white" alt="Odoo">
  <img src="https://img.shields.io/badge/Python-Backend-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/XML-Views-005C84?style=for-the-badge&logo=xml&logoColor=white" alt="XML">
  <img src="https://img.shields.io/badge/PostgreSQL-Odoo%20Data-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Status-Hackathon%20Prototype-success?style=for-the-badge" alt="Status">
</p>

**Odoo × Adani University Hackathon — Phase 1 / Online Round**

</div>

---

## 🎯 The Idea

Equipment-heavy organizations need a reliable way to know **what equipment exists, where it is, what condition it is in, and whether maintenance work is pending**.

When maintenance requests are scattered across messages, spreadsheets, or informal follow-ups, teams can lose track of responsibility and repair history.

**GearGuard** brings the core workflow into Odoo:

> **Register → Report → Assign → Work → Repair**

The project intentionally focuses on a compact, understandable maintenance workflow rather than an oversized enterprise system.

---

## ⚡ Core Features

| Area | What GearGuard provides |
|---|---|
| 🧰 Equipment | Asset code, serial number, location, department, team and status |
| 📝 Maintenance Requests | Issue, equipment, technician, dates, priority and resolution |
| 🔄 Workflow | **New → In Progress → Repaired** with cancellation support |
| 🔗 Status Sync | Equipment becomes **Under Maintenance** when work starts and returns to **Active** when repaired |
| 🔎 Search & Filters | Search equipment and requests using practical operational fields |
| 🔐 Access Control | Odoo model permissions through ACL configuration |
| 🧩 Modular Design | Separate models, views, security and menu configuration |

---

## 🧠 How It Works

~~~text
                         ┌─────────────────────┐
                         │      EQUIPMENT      │
                         │─────────────────────│
                         │ Asset Code          │
                         │ Serial Number       │
                         │ Location            │
                         │ Department          │
                         │ Maintenance Team    │
                         │ Status              │
                         └──────────┬──────────┘
                                    │
                                    │ maintenance request
                                    ▼
                         ┌─────────────────────┐
                         │ MAINTENANCE REQUEST │
                         │─────────────────────│
                         │ Issue / Subject     │
                         │ Technician          │
                         │ Priority            │
                         │ Schedule            │
                         │ Description         │
                         │ Resolution          │
                         │ Status              │
                         └──────────┬──────────┘
                                    │
                       ┌────────────┼────────────┐
                       ▼            ▼            ▼
                     NEW       IN PROGRESS    REPAIRED
                                    │
                                    ▼
                           Equipment Status
                         Under Maintenance
                                    │
                                    ▼
                                  Active
~~~

This connects the maintenance request directly with the operational state of the equipment.

---

## 🔄 Request Lifecycle

### 01 — New
A maintenance issue is recorded and linked to the affected equipment.

### 02 — In Progress
The technician starts the work. GearGuard changes the request state and marks the related equipment as **Under Maintenance**.

### 03 — Repaired
The request is marked repaired and the related equipment returns to **Active**.

### 04 — Cancelled
A request can be cancelled when maintenance is no longer required.

---

## 🧱 Odoo Architecture

~~~text
GearGuard-Odoo-Hackathon/
│
├── __manifest__.py
├── __init__.py
│
├── models/
│   ├── __init__.py
│   ├── equipment.py
│   └── maintenance_request.py
│
├── views/
│   ├── equipment_view.xml
│   ├── maintenance_request_view.xml
│   └── gearguard_menu.xml
│
├── security/
│   └── ir.model.access.csv
│
└── README.md
~~~

### Models

**gearguard.equipment**  
Represents physical equipment and its operational state.

**gearguard.request**  
Represents a maintenance request linked to an equipment record.

### Workflow Actions

~~~python
action_start()
action_repair()
action_cancel()
~~~

These actions update the request state and, where applicable, the related equipment status.

---

## 🗃️ Data Model

### Equipment

- Equipment name
- Unique asset code
- Serial number
- Location
- Department
- Maintenance team
- Equipment status
- Last maintenance date
- Next maintenance date
- Notes

### Maintenance Request

- Issue / request subject
- Related equipment
- Assigned technician
- Request date
- Scheduled date
- Priority
- Issue description
- Resolution / work completed
- Request status

Asset codes are enforced as unique to prevent duplicate equipment records.

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Framework | **Odoo** |
| Backend / ORM | **Python + Odoo ORM** |
| Views | **Odoo XML Views** |
| Database | **PostgreSQL through Odoo** |
| Security | **Odoo ACL / Access Control** |

---

## 🔐 Security & Access

GearGuard includes an Odoo access-control configuration for its two core models.

The module defines user permissions for:

- Read
- Write
- Create
- Delete

through the **security/ir.model.access.csv** configuration.

---

## 🚀 Installation

### 1. Place the module in your Odoo addons path
Copy the repository folder into the configured custom addons directory.

### 2. Restart Odoo
Restart the Odoo server so the module can be discovered.

### 3. Update the Apps list
Enable developer mode if required, then update the Apps list.

### 4. Install GearGuard
Search for:

~~~text
GearGuard - Smart Equipment Maintenance Tracker
~~~

and install the module.

> The repository is an Odoo addon and is not a standalone Python web application.

---

## 🏆 Hackathon Context

Built for the **Odoo × Adani University Hackathon — Phase 1 / Online Round**.

The prototype focuses on demonstrating:

- A practical equipment-maintenance workflow
- Odoo module structure
- Python/Odoo ORM usage
- Equipment-to-request relationships
- Operational status transitions
- Searchable list and form views
- Access-control configuration

The implementation is intentionally focused on the core workflow so it can be demonstrated clearly and extended later.

---

## 🔮 Future Scope

- 📅 Preventive maintenance scheduling
- 🔔 Automated maintenance reminders
- 📊 Maintenance KPI dashboards
- 🧾 Complete asset maintenance history
- 🧰 Spare-parts and inventory integration
- 👨‍🔧 Technician workload tracking
- ⏱️ SLA and response-time monitoring
- 📍 Plant/location-wise asset tracking
- 📈 Equipment downtime analysis
- 📑 Maintenance reports and exports

---

## 👥 Team

| Role | Member |
|---|---|
| Team Leader | **Nirav Vala** |
| Team Member | **Shruti Soni** |

---

## 📌 Project Status

**Hackathon Prototype — Online Round**

The current repository contains the focused GearGuard Odoo addon and its core equipment-to-maintenance workflow.

---

<div align="center">

### 🛠️ Track the asset. Manage the request. Keep the equipment running.

**GearGuard — Smart Equipment Maintenance Tracker**

</div>

# 🛠️ GearGuard — Smart Equipment Maintenance Tracker

<div align="center">

**A lightweight Odoo-based maintenance workflow designed for equipment-heavy organizations.**

### Odoo × Adani University Hackathon — Phase 1 / Online Round

<p>
  <img src="https://img.shields.io/badge/Odoo-Framework-714B67?style=for-the-badge&logo=odoo&logoColor=white" alt="Odoo">
  <img src="https://img.shields.io/badge/Python-Backend-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/XML-Views-005C84?style=for-the-badge&logo=xml&logoColor=white" alt="XML">
  <img src="https://img.shields.io/badge/Status-Hackathon%20Prototype-success?style=for-the-badge" alt="Status">
</p>

</div>

---

## 🎯 Problem Statement

Equipment maintenance in large organizations can become difficult to manage when requests are handled through disconnected communication, spreadsheets, or informal follow-ups.

This can lead to:

- Delayed maintenance
- Unclear responsibility
- Poor visibility of equipment status
- Missing maintenance history
- Difficulty prioritizing critical issues

**GearGuard** approaches this problem by creating a centralized maintenance workflow inside Odoo where equipment and maintenance requests can be tracked through a clear lifecycle.

---

## 💡 Our Approach

For the hackathon online round, the focus was on building a **small but meaningful working core** rather than trying to implement an oversized maintenance platform.

The solution is organized around two connected entities:

```text
                 ┌─────────────────────┐
                 │      Equipment      │
                 │─────────────────────│
                 │ Asset Code          │
                 │ Serial Number       │
                 │ Location            │
                 │ Department          │
                 │ Maintenance Team    │
                 │ Equipment Status    │
                 └──────────┬──────────┘
                            │
                            │ linked equipment
                            ▼
                 ┌─────────────────────┐
                 │ Maintenance Request │
                 │─────────────────────│
                 │ Issue / Subject     │
                 │ Technician          │
                 │ Priority            │
                 │ Schedule            │
                 │ Status               │
                 │ Resolution          │
                 └──────────┬──────────┘
                            │
                 ┌──────────┴──────────┐
                 ▼          ▼           ▼
               New     In Progress   Repaired
```

This keeps the workflow understandable while leaving a clean foundation for future expansion.

---

## 🚀 Core Features

### 1. Equipment Management

Each asset can be registered with useful operational information:

- Equipment name
- Unique asset code
- Serial number
- Location
- Department
- Maintenance team
- Current equipment status
- Last maintenance date
- Next maintenance date
- Internal notes

Asset codes are enforced as unique to avoid duplicate equipment records.

### 2. Maintenance Requests

A request can be created against a specific equipment record and assigned to a technician.

It captures:

- Issue / request subject
- Related equipment
- Assigned technician
- Request date
- Scheduled date
- Priority
- Issue description
- Resolution / work completed

### 3. Clear Request Workflow

The prototype follows a simple operational lifecycle:

**New → In Progress → Repaired**

A request can also be cancelled when required.

The workflow actions are implemented directly in the Odoo model, so the status transition is part of the application logic rather than being only a visual field.

### 4. Equipment Status Sync

When work begins, the related equipment is marked **Under Maintenance**.

When the request is marked repaired, the equipment returns to **Active**.

This connects the maintenance workflow back to the actual asset status.

### 5. Search & Filtering

Both equipment and maintenance requests have searchable list views with practical filters such as:

- Active equipment
- Equipment under maintenance
- New requests
- In-progress requests
- Repaired requests
- Priority and status filtering

---

## 🧱 Odoo Module Structure

```text
GearGuard-Odoo-Hackathon/
│
├── __manifest__.py
├── init__.py
│
├── models/
│   ├── init__.py
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
```

The module now follows a more complete Odoo addon structure with model initialization, access rights, navigation, list/form/search views and a manifest that loads the components in the correct order.

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Framework | **Odoo** |
| Backend / ORM | **Python + Odoo ORM** |
| Interface | **Odoo XML Views** |
| Data Model | **Odoo ORM / PostgreSQL through Odoo** |
| Access Control | **Odoo Security / ACL** |

---

## 🔍 Implementation Highlights

The main design decision was to keep the system **modular and extendable**.

### Equipment model

`gearguard.equipment` represents physical assets and stores their operational state.

### Maintenance request model

`gearguard.request` represents maintenance work linked to an equipment record.

### Workflow methods

The backend exposes simple actions:

```python
action_start()
action_repair()
action_cancel()
```

These methods make the maintenance workflow explicit and also update equipment status where appropriate.

---

## 🏆 Hackathon Context

This project was developed for the **Odoo × Adani University Hackathon — Phase 1 / Online Round**.

The goal during the round was to demonstrate:

1. Understanding of the maintenance problem
2. A practical approach instead of unnecessary complexity
3. Odoo module structure and ORM usage
4. Equipment-to-request data relationships
5. A clear maintenance workflow
6. A foundation that could be extended into a larger enterprise solution

The current repository represents the **working prototype / core approach submitted for the online round**, not a claim of a full enterprise maintenance-management suite.

---

## 🔮 Future Scope

With more development time, GearGuard can evolve into a more complete maintenance platform with:

- 📅 Preventive maintenance scheduling
- 🔔 Automated maintenance reminders
- 📊 KPI dashboards and maintenance analytics
- 🧾 Maintenance history per asset
- 🧰 Spare-parts and inventory integration
- 👨‍🔧 Technician workload tracking
- ⏱️ SLA and response-time monitoring
- 📍 Location / plant-wise asset tracking
- 📈 Equipment downtime analysis
- 🔐 Role-based maintenance permissions
- 📑 Reports and exportable maintenance summaries

---

## 👥 Team

- **Team Leader:** Nirav Vala
- **Team Member:** Shruti

---

## 📌 Project Status

**Hackathon Prototype — Online Round**

The repository has been kept intentionally focused on the core maintenance workflow so the underlying approach remains easy to understand, demonstrate and extend.

---

<div align="center">

### 🛠️ Track the asset. Manage the request. Keep the equipment running.

**GearGuard — Smart Equipment Maintenance Tracker**

</div>

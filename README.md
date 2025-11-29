# F1 – Emissions 2026

A project exploring the environmental impact of Formula 1 under the 2026 regulations, focusing on emissions modelling, data analysis, and interactive tooling.  
This repository combines **TypeScript**, **Python**, **JavaScript**, and **CSS** to deliver both analytical backends and user-facing visualizations.

> Note: This README is a template based on the repository name and tech stack.  
> Update any placeholder sections (marked clearly) with details from your actual implementation.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [Data & Methodology](#data--methodology)
- [Development](#development)
- [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The **F1 – Emissions 2026** project aims to:

- Quantify and visualize the carbon emissions associated with Formula 1 under the upcoming **2026 regulations**.
- Provide tools for **scenario analysis** (e.g., different fuel mixes, power unit configurations, calendar changes).
- Offer a clear, interactive way to communicate environmental impacts to both technical and non‑technical audiences.

You can use this repository as:

- A reference for **sports-related emissions modelling**.
- A playground for **data science + web front-end** integration.
- A basis for further academic or hobbyist analysis of motorsport sustainability.

---

## Features

Update this list as you build things out.

- 🌍 **Emissions Modelling (Planned/Implemented)**  
  - Calculate emissions by **race**, **season**, or **team**.
  - Break down emissions by **travel**, **power unit usage**, **operations**, etc.

- 📊 **Visual Dashboards (TS/JS + CSS)**  
  - Interactive charts for emissions over time and per circuit.
  - Comparative views: pre‑2026 vs 2026‑onwards scenarios.

- 🧮 **Python Analytics**  
  - Data ingestion and cleaning pipelines.
  - Statistical summaries and scenario simulations.

- ⚙️ **Configurable Scenarios**  
  - Adjust input parameters (fuel type, logistics assumptions, calendar) and instantly recompute estimates.

---

## Tech Stack

Based on the language composition:

- **TypeScript** (~58.5%)  
  Likely used for the main application logic (e.g., frontend app or Node-based tools).

- **Python** (~36.8%)  
  For data processing, analysis, and modelling scripts.

- **JavaScript** (~2.5%)  
  For supplemental browser logic or legacy scripts.

- **CSS** (~2.2%)  
  For styling the user interface and visualizations.


---

## Project Structure

```text
f1-emissions-2026/
├─ src/                     # TypeScript / JavaScript source code
│  ├─ components/           # UI components (charts, tables, controls)
│  ├─ pages/                # App pages or views
│  ├─ utils/                # Shared utilities (formatting, math, etc.)
│  └─ ...                   
├─ public/                  # Static assets (images, icons, etc.)
├─ package.json             # JS/TS dependencies and scripts
├─ requirements.txt         # Python dependencies (if used)
└─ README.md                # This file
```

---

## Getting Started

### Prerequisites

- **Node.js** (e.g. ≥ 18.x) and **npm** or **pnpm/yarn**


### Installation

Clone the repository:

```bash
git clone https://github.com/KashyapHegdeKota/f1-emissions-2026.git
cd f1-emissions-2026/frontend/paddockjet-ui
```

Install JavaScript/TypeScript dependencies:

```bash
npm install
# or
pnpm install
# or
yarn install
```


---

### Running the Project

_Replace these commands with your actual scripts in `package.json` / your tooling._

Start the frontend / main app:

```bash
npm run dev
```

---

## Data & Methodology

_Describe your modelling approach here. For now, this is a template._

- **Scope**  
  - Races covered: `e.g., 2023–2026 calendars`
  - Emission sources: `e.g., logistics, track operations, power units, freight, personnel travel`.

- **Data Sources**  
  - Official F1 calendars and regulations documentation.  
  - Public datasets or estimates for fuel usage, logistics distances, and emission factors.  
  - Any assumptions or third‑party reports used.

- **Methodology (Example)**  
  1. Estimate travel distances per race (teams, equipment, freight).  
  2. Assign emission factors (kg CO₂e per km or per liter of fuel).  
  3. Compute total emissions by category and aggregate by race/season.  
  4. Model 2026 changes (e.g., new power unit rules, sustainable fuels, calendar shifts).  
  5. Visualize comparative results.

Add formulas, references, or detailed methodology once finalized.


---

## Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the project
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

If you plan bigger changes, consider opening an issue to discuss ideas first.

---

## License

_Add your license here (e.g. MIT, Apache 2.0, etc.)._

For example:

```text
MIT License – see LICENSE file for details.
```

If you haven’t chosen a license yet, you can use [GitHub’s license chooser](https://choosealicense.com/).

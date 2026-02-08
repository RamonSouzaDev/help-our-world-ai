# Legal & Regulatory Compliance Statement
## Health Sentinel: Adherence to Brazilian Law & International Standards

**Date**: February 2026
**Jurisdiction**: Federative Republic of Brazil
**Classification**: Software as a Medical Device (SaMD) - Class II (ANVISA)

---

### 1. LGPD (Lei Geral de Proteção de Dados - 13.709/2018)
This project is designed with **Privacy by Design** principles as mandated by the Brazilian Data Protection Authority (ANPD).

#### 1.1 Lawful Basis for Processing (Art. 7)
-   **Health Protection (Inciso VIII)**: Data processing is carried out exclusively for the protection of life and physical safety of the data subject.
-   **Consent (Inciso I)**: The architecture requires explicit, granular opt-in from the user before telemetry begins.

#### 1.2 Data Rights & Anonymization (Art. 12)
-   **Pseudonymization**: All internal processing uses UUIDs (e.g., `PATIENT-X-99`) instead of CPF/RG. Re-identification keys are stored in a separate, air-gapped database (not included in this repo).
-   **Data Minimization**: The system collects *only* physiological signals (HR, SpO2, Temp). No geolocational tracking or behavioral data is stored without specific epidemiological necessity.

---

### 2. ANVISA Regulatory Framework
The software adheres to **RDC No. 751/2022** regarding Medical Device Notification.

-   **Intended Use**: "Auxiliary tool for monitoring physiological parameters and early detection of sepsis risk markers."
-   **Risk Classification**: **Class II (Medium Risk)**.
    -   *Justification*: The software provides information for decision-making but does not directly control therapeutic actions.
-   **Labeling**: The UI explicitly states: *"This system is for informational purposes only and does not replace professional medical diagnosis."*

---

### 3. Telemedicine Law (Lei 14.510/2022)
-   **Role of AI**: The "Dr. Sentinel" module operates as a **Health Education Agent**, providing general wellness advice.
-   **Limitation of Liability**: The algorithms do not prescribe medication. All critical alerts ("Emergency Intervention Required") are directives to *seek human medical care*, not automated treatment orders.

---

### 4. International Standards (ISO/IEC)
1.  **ISO 13485:2016** (Medical Devices - Quality Management):
    *   The project maintains a version-controlled codebase with traceability of changes (Git History serves as the Design History File).
2.  **IEC 62304** (Medical Software Lifecycle):
    *   **Software Safety Class B**: Non-serious injury is possible if the software fails (e.g., missed diagnosis leading to delayed care).
    *   **Mitigation**: The system includes "Fail-Safe" modes (e.g., standard monitoring if AI fails) and explicit error logging.

### 5. Ethical AI Guidelines (UNESCO/WHO)
-   **Transparency**: The decision logic (qSOFA criteria) is open-source and deterministic, avoiding "Black Box" bias.
-   **Equity**: The system uses low-compute models to ensure accessibility on older devices, preventing technological discrimination.

---

### 6. Compliance with Brazilian Government Digital Health Strategy (ESD 2028)
This project is aligned with the **Estratégia de Saúde Digital para o Brasil 2020-2028 (ESD 28)** published by the Ministry of Health.

#### 6.1 RNDS Integration (Rede Nacional de Dados em Saúde)
-   **Legal Basis**: Portaria GM/MS nº 1.434/2020 (Institutes the Conecte SUS Program).
-   **Interoperability Standard**: The system uses **HL7 FHIR Release 4** for all data exchange, as mandated by the Brazilian standard for health information.
-   **Structured Data**: Clinical findings (e.g., Sepsis Alert) are mapped to **CID-10 / CIAP-2** codes for seamless integration with e-SUS APS.

#### 6.2 National Policy on Health Information & Informatics (PNIIS)
-   **Objective**: To support decision-making in public health management.
-   **Alignment**: The aggregated, anonymized epidemiological data feeds directly into the surveillance goals of **SVS (Secretaria de Vigilância em Saúde)** for disease outbreak monitoring.


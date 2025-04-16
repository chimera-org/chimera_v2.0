# Software as a Medical Device (SaMD) Classification for Chimera

<div align="center">
<img src="https://img.shields.io/badge/-%F0%9F%A7%A0%20CHIMERA%20SAMD%20CLASSIFICATION%20%F0%9F%A6%BE-6236FF?style=for-the-badge&labelColor=1A1A2E" alt="Chimera SaMD Classification"/>

**Version 1.0 | April 2025**

[![FDA Compliance](https://img.shields.io/badge/FDA-SaMD%20Framework-green?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJDNi41IDIgMiA2LjUgMiAxMnM0LjUgMTAgMTAgMTAgMTAtNC41IDEwLTEwUzE3LjUgMiAxMiAyem0tMSAxNkg3di0yaDR2MnptNi40LTRINi42Yy0uOSAwLTEuNi0uNy0xLjYtMS42VjYuNkM1IDUuNyA1LjcgNSA2LjYgNWgxMC44Yy45IDAgMS42LjcgMS42IDEuNnY1LjhjMCAuOS0uNyAxLjYtMS42IDEuNnoiIGZpbGw9IndoaXRlIi8+PC9zdmc+)](https://www.fda.gov/medical-devices/digital-health-center-excellence/software-medical-device-samd)
[![IMDRF](https://img.shields.io/badge/IMDRF-SaMD%20Framework-blue?style=flat-square)](http://www.imdrf.org/docs/imdrf/final/technical/imdrf-tech-131209-samd-framework-key-definitions-140901.pdf)
[![IEC 62304](https://img.shields.io/badge/IEC%2062304-Compliant-blue?style=flat-square)](https://www.iso.org/standard/38421.html)
</div>

## 1. Executive Summary

This document provides a comprehensive classification analysis of the Chimera Brain-Computer Interface (BCI) software system as a Software as a Medical Device (SaMD) according to FDA and International Medical Device Regulators Forum (IMDRF) frameworks. The classification determines the regulatory pathway, documentation requirements, and quality system controls necessary for market approval.

Based on our analysis, the Chimera BCI software is classified as:

- **FDA Classification**: Class II Software as a Medical Device
- **IMDRF SaMD Risk Category**: Category III (Medium impact on patient health)
- **Software Safety Classification (IEC 62304)**: Class C (highest risk level)
- **Level of Concern (FDA)**: Major Level of Concern

This classification informs our regulatory strategy, development processes, and quality management system to ensure compliance with all applicable regulations while supporting our billion-dollar funding goals through demonstrated regulatory viability.

## 2. Software Description and Intended Use

### 2.1 Software Description

The Chimera software system consists of the following components:

1. **Signal Acquisition Module**: Captures and filters EEG signals from the user's brain
2. **Signal Processing Module**: Processes raw EEG data to extract relevant features
3. **Intent Classification Module**: Uses machine learning algorithms to classify user's movement intentions
4. **Control Command Module**: Translates classified intentions into exoskeleton control commands
5. **Safety Monitoring Module**: Continuously monitors system performance and user safety
6. **User Interface Module**: Provides feedback and control options to users and clinicians

### 2.2 Intended Use Statement

"The Chimera BCI software is intended to process electroencephalography (EEG) signals to detect and classify movement intentions and translate them into control commands for a powered exoskeleton, enabling mobility assistance for individuals with spinal cord injuries, stroke, or other mobility impairments. The software is intended for use in clinical settings under the supervision of trained healthcare professionals."

### 2.3 Indications for Use

The Chimera BCI software is indicated for use:

- In patients with spinal cord injuries at levels C5 to T12
- In patients with stroke-related mobility impairments
- In patients with other neurological conditions affecting mobility
- In conjunction with the Chimera powered exoskeleton hardware
- In rehabilitation facilities and clinical settings
- Under the supervision of trained healthcare professionals

### 2.4 Target Patient Population

- Adults (18-65 years) with mobility impairments due to:
  - Spinal cord injury (C5-T12)
  - Stroke with hemiparesis
  - Other neurological conditions affecting mobility
- Cognitive function sufficient to understand and follow instructions
- No contraindications for EEG recording (e.g., open skull defects)
- No seizure disorders or history of epilepsy

## 3. SaMD Classification Analysis

### 3.1 FDA SaMD Classification

According to FDA's regulatory framework for Software as a Medical Device:

| Classification Factor | Chimera BCI Software Assessment |
|------------------------|--------------------------------|
| **Device Class** | Class II |
| **Product Code** | QJK (Neurology Software) |
| **Regulation Number** | 21 CFR 882.5050 |
| **Review Pathway** | 510(k) with potential De Novo elements |
| **Level of Concern** | Major Level of Concern |

**Rationale for Class II Designation**:
- The software directly influences the operation of a Class II medical device (powered exoskeleton)
- The software interprets physiological signals (EEG) to inform clinical decisions
- Malfunction could lead to minor to moderate injury, but not life-threatening situations
- Similar devices (BCI systems, neurology software) are classified as Class II

### 3.2 IMDRF SaMD Risk Categorization

According to the IMDRF SaMD Risk Categorization Framework:

| IMDRF Factor | Chimera BCI Software Assessment |
|--------------|--------------------------------|
| **Healthcare Situation or Condition** | Non-serious (mobility impairment is not immediately life-threatening) |
| **Significance of Information Provided by SaMD** | Treat or diagnose (software directly controls treatment via exoskeleton) |
| **SaMD Risk Category** | Category III (Medium impact on patient health) |

**Risk Category Justification**:
- The software provides information to treat a non-serious healthcare situation
- The software directly drives clinical management by controlling the exoskeleton
- Incorrect information could lead to improper treatment but not immediate serious injury

### 3.3 IEC 62304 Software Safety Classification

According to IEC 62304 Medical Device Software Lifecycle Processes:

| IEC 62304 Factor | Chimera BCI Software Assessment |
|------------------|--------------------------------|
| **Software Safety Class** | Class C |
| **Rationale** | Software failure could directly result in harm to the patient through incorrect exoskeleton movement |
| **Required Documentation** | Full documentation per IEC 62304 Class C requirements |

**Class C Justification**:
- Software directly controls a physical medical device (exoskeleton)
- Software failure could result in physical injury to the user
- No redundant hardware safety mechanisms can fully mitigate software failure risks

## 4. Regulatory Requirements Based on Classification

### 4.1 Documentation Requirements

Based on the classifications above, the following documentation is required:

| Documentation Type | Requirement | Status |
|-------------------|-------------|--------|
| Software Requirements Specification | Required | In Development |
| Software Architecture | Required | In Development |
| Software Design Specification | Required | In Development |
| Software Development Plan | Required | In Development |
| Risk Management File | Required | In Development |
| Software Verification & Validation Plan | Required | In Development |
| Software Verification & Validation Results | Required | Planned |
| Cybersecurity Documentation | Required | In Development |
| Usability Engineering File | Required | In Development |
| Software Maintenance Plan | Required | In Development |
| Software Configuration Management Plan | Required | In Development |
| Software Problem Resolution Process | Required | In Development |

### 4.2 Quality System Requirements

The following quality system elements are required based on our classification:

| Quality System Element | Requirement | Implementation Approach |
|------------------------|-------------|------------------------|
| Design Controls | Full implementation per 21 CFR 820.30 | Comprehensive design control process with stage-gate reviews |
| Document Controls | Full implementation per 21 CFR 820.40 | Electronic document management system with version control |
| Software Validation | Comprehensive validation per 21 CFR 820.70(i) | Multi-level testing strategy with independent verification |
| Risk Management | Full implementation per ISO 14971 | Comprehensive risk management process with regular reviews |
| Configuration Management | Full implementation | Git-based version control with branching strategy |
| Problem Resolution | Formal process required | Issue tracking system with root cause analysis |
| Change Management | Formal process required | Change control board with impact analysis |

### 4.3 Clinical Evidence Requirements

Based on our classification, the following clinical evidence is required:

| Clinical Evidence Type | Requirement | Planned Approach |
|------------------------|-------------|------------------|
| Literature Review | Required | Comprehensive review of BCI and exoskeleton literature |
| Usability Testing | Required | Formative and summative usability studies |
| Clinical Validation | Required | Pilot and pivotal clinical studies |
| Human Factors Validation | Required | Comprehensive human factors validation study |
| Post-Market Surveillance | Required | Real-world performance monitoring system |

## 5. AI/ML Specific Classification Considerations

### 5.1 AI/ML Algorithm Type

The Chimera BCI software incorporates the following AI/ML elements:

| AI/ML Component | Algorithm Type | Learning Approach | Regulatory Consideration |
|-----------------|---------------|-------------------|--------------------------|
| Feature Extraction | Supervised ML | Locked algorithm | Traditional SaMD approach |
| Intent Classification | Deep Learning | Locked algorithm with planned updates | Predetermined Change Control Plan |
| Adaptive Calibration | Reinforcement Learning | Continuous learning (user-specific) | SaMD Pre-Specifications (SPS) |

### 5.2 FDA AI/ML Framework Alignment

Our AI/ML approach aligns with the FDA's proposed regulatory framework for AI/ML-based SaMD:

1. **SaMD Pre-Specifications (SPS)**:
   - Clearly defined performance metrics
   - Specified input data characteristics
   - Defined algorithm update boundaries
   - Established retraining triggers

2. **Algorithm Change Protocol (ACP)**:
   - Validation methodology for algorithm updates
   - Performance monitoring approach
   - Update implementation procedures
   - Risk management for algorithm changes

3. **Good Machine Learning Practice (GMLP)**:
   - Data quality assurance
   - Algorithm validation protocols
   - Clinical validation methodology
   - Performance monitoring systems

## 6. International Classification Considerations

| Regulatory Body | Classification | Requirements | Chimera Status |
|-----------------|---------------|--------------|----------------|
| **FDA (US)** | Class II SaMD | 510(k) or De Novo | Primary target |
| **EU MDR** | Class IIa | CE Mark via Notified Body | Planned |
| **Health Canada** | Class II | Medical Device License | Planned |
| **TGA (Australia)** | Class IIa | ARTG inclusion | Planned |
| **PMDA (Japan)** | Class II | Shonin approval | Future consideration |
| **NMPA (China)** | Class II | Registration | Future consideration |

## 7. Classification Impact on Development Process

### 7.1 Development Lifecycle Requirements

Based on our classification, our software development lifecycle must include:

- Formal requirements management
- Documented design reviews
- Traceability throughout the development lifecycle
- Comprehensive verification and validation
- Formal risk management
- Configuration management and change control
- Defect management and resolution

### 7.2 Testing Requirements

Our classification necessitates the following testing approach:

| Test Type | Requirement | Approach |
|-----------|-------------|----------|
| Unit Testing | Required | Automated testing with >90% code coverage |
| Integration Testing | Required | Automated and manual testing of component interfaces |
| System Testing | Required | Comprehensive testing of full system functionality |
| Performance Testing | Required | Stress testing and performance benchmarking |
| Security Testing | Required | Penetration testing and vulnerability assessment |
| Usability Testing | Required | Formative and summative usability studies |
| Clinical Validation | Required | Controlled clinical studies |

## 8. Conclusion and Next Steps

Based on our comprehensive SaMD classification analysis, the Chimera BCI software is classified as a Class II medical device with IMDRF Risk Category III and IEC 62304 Software Safety Class C. This classification informs our regulatory strategy, development processes, and quality management system.

### 8.1 Next Steps

1. **Documentation Development**: Complete all required documentation per Section 4.1
2. **Quality System Implementation**: Ensure full compliance with requirements in Section 4.2
3. **Clinical Evidence Generation**: Execute clinical evidence plan per Section 4.3
4. **AI/ML Framework Implementation**: Implement SPS and ACP for AI/ML components
5. **Pre-Submission Meeting**: Schedule FDA pre-submission meeting to confirm classification

### 8.2 Impact on Billion-Dollar Funding Goal

This classification analysis supports our billion-dollar funding goal by:

1. Demonstrating regulatory sophistication to potential investors
2. Providing a clear pathway to market approval
3. Identifying and mitigating regulatory risks early
4. Establishing a foundation for global market access
5. Ensuring alignment with FDA's latest thinking on AI/ML-based medical devices

---

<div align="center">
<p><strong>Document Control</strong></p>

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | April 16, 2025 | Chimera Regulatory Team | Initial version |

<p><em>This document is confidential and proprietary to Chimera. It may not be reproduced or distributed without permission.</em></p>
</div>

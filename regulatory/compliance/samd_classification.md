# Software as a Medical Device (SaMD) Classification for Chimera

<div align="center">
<img src="https://img.shields.io/badge/-%F0%9F%A7%A0%20CHIMERA%20SAMD%20CLASSIFICATION%20%F0%9F%A6%BE-6236FF?style=for-the-badge&labelColor=1A1A2E" alt="Chimera SaMD Classification"/>

**Version 2.0 | April 2025**

[![CDSCO Compliance](https://img.shields.io/badge/CDSCO-SaMD%20Framework-green?style=flat-square)](https://cdsco.gov.in/opencms/opencms/en/Medical-Device-Diagnostics/)
[![IMDRF](https://img.shields.io/badge/IMDRF-SaMD%20Framework-blue?style=flat-square)](http://www.imdrf.org/docs/imdrf/final/technical/imdrf-tech-131209-samd-framework-key-definitions-140901.pdf)
[![IEC 62304](https://img.shields.io/badge/IEC%2062304-Compliant-blue?style=flat-square)](https://www.iso.org/standard/38421.html)
</div>

## 1. Executive Summary

This document provides a comprehensive classification analysis of the Chimera Brain-Computer Interface (BCI) software system as a Software as a Medical Device (SaMD) according to Central Drugs Standard Control Organization (CDSCO) and International Medical Device Regulators Forum (IMDRF) frameworks. The classification determines the regulatory pathway, documentation requirements, and quality system controls necessary for market approval in India.

Based on our analysis, the Chimera BCI software is classified as:

- **CDSCO Classification**: Class C Medical Device (moderate-high risk)
- **IMDRF SaMD Risk Category**: Category III (Medium impact on patient health)
- **Software Safety Classification (IEC 62304)**: Class C (highest risk level)
- **Risk Classification**: Moderate-High Risk

This classification informs our regulatory strategy, development processes, and quality management system to ensure compliance with all applicable Indian regulations while supporting our billion-dollar funding goals through demonstrated regulatory viability for an Indian startup developing an exoskeleton for home use without professional supervision after training.

## 2. Software Description and Intended Use

### 2.1 Software Description

The Chimera software system consists of the following components:

1. **Signal Acquisition Module**: Captures and filters EEG signals from the user's brain
2. **Signal Processing Module**: Processes raw EEG data to extract relevant features
3. **Intent Classification Module**: Uses machine learning algorithms to classify user's movement intentions
4. **Control Command Module**: Translates classified intentions into exoskeleton control commands
5. **Safety Monitoring Module**: Continuously monitors system performance and user safety
6. **User Interface Module**: Provides feedback and control options to users and caregivers
7. **Home Use Safety Module**: Provides additional safety features for unsupervised home use

### 2.2 Intended Use Statement

"The Chimera BCI software is intended to process electroencephalography (EEG) signals to detect and classify movement intentions and translate them into control commands for a powered exoskeleton, enabling mobility assistance for individuals with spinal cord injuries, stroke, or other mobility impairments. The software is intended for home use in daily social life without professional supervision after appropriate training."

### 2.3 Indications for Use

The Chimera BCI software is indicated for use:

- In patients with spinal cord injuries at levels C5 to T12
- In patients with stroke-related mobility impairments
- In patients with other neurological conditions affecting mobility
- In conjunction with the Chimera powered exoskeleton hardware
- In home environments and community settings
- Without professional supervision after appropriate training

### 2.4 Target Patient Population

- Adults (18-65 years) with mobility impairments due to:
  - Spinal cord injury (C5-T12)
  - Stroke with hemiparesis
  - Other neurological conditions affecting mobility
- Cognitive function sufficient to understand and follow instructions
- No contraindications for EEG recording (e.g., open skull defects)
- No seizure disorders or history of epilepsy
- Completed appropriate training program for home use

## 3. SaMD Classification Analysis

### 3.1 CDSCO SaMD Classification

According to India's Medical Devices Rules, 2017 and CDSCO's classification of software as medical devices:

| Classification Factor | Chimera BCI Software Assessment |
|------------------------|--------------------------------|
| **Device Class** | Class C (moderate-high risk) |
| **Category** | Software |
| **Regulatory Pathway** | Manufacturing License under Form MD-5 |
| **Risk Level** | Moderate-High Risk |

**Rationale for Class C Designation**:
- The software directly influences the operation of a Class C medical device (powered exoskeleton)
- The software interprets physiological signals (EEG) to inform clinical decisions
- The software is intended for home use without professional supervision
- Malfunction could lead to moderate injury
- Similar devices (BCI systems, neurology software) are classified as Class C in India

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
- Home use without supervision increases the risk profile

### 3.3 IEC 62304 Software Safety Classification

According to IEC 62304 Medical Device Software Lifecycle Processes:

| IEC 62304 Factor | Chimera BCI Software Assessment |
|------------------|--------------------------------|
| **Software Safety Class** | Class C |
| **Rationale** | Software failure could directly result in harm to the patient through incorrect exoskeleton movement, especially in home use without supervision |
| **Required Documentation** | Full documentation per IEC 62304 Class C requirements |

**Class C Justification**:
- Software directly controls a physical medical device (exoskeleton)
- Software failure could result in physical injury to the user
- Home use without professional supervision increases risk
- No redundant hardware safety mechanisms can fully mitigate software failure risks

## 4. Regulatory Requirements Based on Classification

### 4.1 Documentation Requirements

Based on the classifications above and CDSCO requirements, the following documentation is required:

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
| Home Use Validation Documentation | Required | Planned |

### 4.2 Quality System Requirements

The following quality system elements are required based on our classification under Indian regulations:

| Quality System Element | Requirement | Implementation Approach |
|------------------------|-------------|------------------------|
| Design Controls | Full implementation per ISO 13485:2016 | Comprehensive design control process with stage-gate reviews |
| Document Controls | Full implementation per ISO 13485:2016 | Electronic document management system with version control |
| Software Validation | Comprehensive validation | Multi-level testing strategy with independent verification |
| Risk Management | Full implementation per ISO 14971 | Comprehensive risk management process with regular reviews |
| Configuration Management | Full implementation | Git-based version control with branching strategy |
| Problem Resolution | Formal process required | Issue tracking system with root cause analysis |
| Change Management | Formal process required | Change control board with impact analysis |

### 4.3 Clinical Evidence Requirements

Based on our classification under CDSCO requirements, the following clinical evidence is required:

| Clinical Evidence Type | Requirement | Planned Approach |
|------------------------|-------------|------------------|
| Literature Review | Required | Comprehensive review of BCI and exoskeleton literature |
| Usability Testing | Required | Formative and summative usability studies in home settings |
| Clinical Validation | Required | Pilot and pivotal clinical studies in India |
| Human Factors Validation | Required | Comprehensive human factors validation study for home use |
| Post-Market Surveillance | Required | Real-world performance monitoring system |
| Home Use Validation | Required | Specific studies to validate safety in home environments |

## 5. AI/ML Specific Classification Considerations

### 5.1 AI/ML Algorithm Type

The Chimera BCI software incorporates the following AI/ML elements:

| AI/ML Component | Algorithm Type | Learning Approach | Regulatory Consideration |
|-----------------|---------------|-------------------|--------------------------|
| Feature Extraction | Supervised ML | Locked algorithm | Traditional SaMD approach |
| Intent Classification | Deep Learning | Locked algorithm with planned updates | Predetermined Change Control Plan |
| Adaptive Calibration | Reinforcement Learning | Continuous learning (user-specific) | SaMD Pre-Specifications (SPS) |
| Home Safety Monitoring | Supervised ML | Locked algorithm | Traditional SaMD approach |

### 5.2 AI/ML Framework Alignment

Our AI/ML approach aligns with international best practices for AI/ML-based SaMD:

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

## 6. Home Use Specific Classification Considerations

### 6.1 Home Use Risk Factors

The following additional risk factors are considered due to the intended home use without professional supervision:

| Risk Factor | Mitigation Approach | Classification Impact |
|-------------|---------------------|----------------------|
| Lack of professional oversight | Enhanced safety monitoring algorithms | Increases risk classification |
| Variable home environments | Environmental sensing and adaptation | Additional validation requirements |
| User error | Comprehensive training program and intuitive interface | Enhanced usability requirements |
| Emergency situations | Automatic safety features and emergency protocols | Additional safety requirements |
| Technical failures | Remote monitoring and diagnostics | Additional reliability requirements |

### 6.2 Home Use Classification Impact

The intended home use without professional supervision impacts our classification in the following ways:

1. **Risk Classification**: Elevated to Class C due to home use considerations
2. **Validation Requirements**: Additional validation specific to home environments
3. **Safety Features**: Enhanced safety monitoring and fail-safe mechanisms
4. **User Training**: Comprehensive training program validation
5. **Post-Market Surveillance**: Enhanced monitoring for home use scenarios

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
- Home use specific validation

### 7.2 Testing Requirements

Our classification necessitates the following testing approach:

| Test Type | Requirement | Approach |
|-----------|-------------|----------|
| Unit Testing | Required | Automated testing with >90% code coverage |
| Integration Testing | Required | Automated and manual testing of component interfaces |
| System Testing | Required | Comprehensive testing of full system functionality |
| Performance Testing | Required | Stress testing and performance benchmarking |
| Security Testing | Required | Penetration testing and vulnerability assessment |
| Usability Testing | Required | Formative and summative usability studies in home settings |
| Clinical Validation | Required | Controlled clinical studies in India |
| Home Use Validation | Required | Testing in simulated and actual home environments |

## 8. Conclusion and Next Steps

Based on our comprehensive SaMD classification analysis, the Chimera BCI software is classified as a Class C medical device under CDSCO regulations with IMDRF Risk Category III and IEC 62304 Software Safety Class C. This classification informs our regulatory strategy, development processes, and quality management system for the Indian market.

### 8.1 Next Steps

1. **Documentation Development**: Complete all required documentation per Section 4.1
2. **Quality System Implementation**: Ensure full compliance with requirements in Section 4.2
3. **Clinical Evidence Generation**: Execute clinical evidence plan per Section 4.3
4. **AI/ML Framework Implementation**: Implement SPS and ACP for AI/ML components
5. **Pre-Submission Meeting**: Schedule CDSCO pre-submission meeting to confirm classification
6. **Home Use Validation**: Develop and execute comprehensive home use validation plan

### 8.2 Impact on Billion-Dollar Funding Goal

This classification analysis supports our billion-dollar funding goal by:

1. Demonstrating regulatory sophistication to potential investors
2. Providing a clear pathway to market approval in India
3. Identifying and mitigating regulatory risks early
4. Establishing a foundation for the Indian market access
5. Ensuring alignment with international best practices for AI/ML-based medical devices
6. Addressing the unique considerations for home use without professional supervision

---

<div align="center">
<p><strong>Document Control</strong></p>

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | April 16, 2025 | Chimera Regulatory Team | Initial version (FDA focus) |
| 2.0 | April 17, 2025 | Chimera Regulatory Team | Updated for Indian regulations and home use |

<p><em>This document is confidential and proprietary to Chimera. It may not be reproduced or distributed without permission.</em></p>
</div>

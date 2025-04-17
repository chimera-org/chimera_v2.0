# Data Dictionary

## 📋 General Information

| **Document Information** |                                                |
|--------------------------|------------------------------------------------|
| **Document ID**          | DATA-DICT-001                                  |
| **Version**              | 1.0.0                                          |
| **Date Created**         | April 17, 2025                                 |
| **Last Updated**         | April 17, 2025                                 |
| **Author**               | Chimera Data Governance Team                   |
| **Reviewers**            | Technical Lead, Clinical Director, Data Scientist |
| **Status**               | Approved                                       |

## 🎯 Purpose and Scope

### Purpose

This Data Dictionary provides a comprehensive reference for all data elements used within the Chimera neural interface system. It establishes standardized definitions, formats, and metadata for data elements to ensure consistency, interoperability, and regulatory compliance across all system components and documentation.

### Scope

This document covers:

- Neural signal data elements and metadata
- Patient and clinical data elements
- System configuration and operational data
- Research and analytical data elements
- Data element relationships and hierarchies
- Data quality attributes and constraints
- Regulatory and compliance considerations

## 📊 Neural Signal Data Elements

### Raw Signal Data

| Data Element | Description | Data Type | Format | Units | Valid Range | Source |
|--------------|-------------|-----------|--------|-------|-------------|--------|
| SignalID | Unique identifier for signal recording | String | UUID | N/A | Valid UUID | System Generated |
| ChannelID | Identifier for recording channel | Integer | 1-999 | N/A | 1-256 | Device Configuration |
| Timestamp | Time point of signal sample | DateTime | ISO 8601 | UTC | Valid timestamp | System Clock |
| AmplitudeValue | Amplitude of neural signal | Float | Decimal | μV | -5000 to 5000 | Neural Sensor |
| SamplingRate | Rate of signal acquisition | Integer | Decimal | Hz | 250-10000 | Device Configuration |
| ImpedanceValue | Electrode impedance | Float | Decimal | kΩ | 0-1000 | Impedance Measurement |
| SignalQualityIndex | Quality metric for signal | Float | Decimal | N/A | 0.0-1.0 | Signal Processing |

### Processed Signal Data

| Data Element | Description | Data Type | Format | Units | Valid Range | Source |
|--------------|-------------|-----------|--------|-------|-------------|--------|
| ProcessedSignalID | Identifier for processed signal | String | UUID | N/A | Valid UUID | System Generated |
| FilterParameters | Parameters of applied filters | JSON | Object | Various | Valid parameters | Signal Processing |
| FrequencyBand | Frequency range of processed signal | String | Text | Hz | Valid band name | Signal Processing |
| PowerSpectralDensity | Power distribution across frequencies | Array | Float Array | μV²/Hz | ≥ 0 | Spectral Analysis |
| FeatureVector | Extracted signal features | Array | Float Array | Various | Valid features | Feature Extraction |
| ArtifactFlag | Indicator of signal artifact | Boolean | True/False | N/A | True/False | Artifact Detection |
| ProcessingAlgorithmVersion | Version of processing algorithm | String | Semantic Version | N/A | Valid version | System Configuration |

### Neural Classification Data

| Data Element | Description | Data Type | Format | Units | Valid Range | Source |
|--------------|-------------|-----------|--------|-------|-------------|--------|
| ClassificationID | Identifier for classification result | String | UUID | N/A | Valid UUID | System Generated |
| IntentClass | Classified neural intent | String | Text | N/A | Valid intent class | Neural Classifier |
| ConfidenceScore | Confidence in classification | Float | Decimal | N/A | 0.0-1.0 | Neural Classifier |
| ClassificationLatency | Time taken for classification | Integer | Decimal | ms | ≥ 0 | System Measurement |
| ModelID | Identifier of classification model | String | UUID | N/A | Valid UUID | Model Repository |
| FeatureImportance | Importance of features in classification | JSON | Object | N/A | Valid values | Neural Classifier |
| ClassificationTimestamp | Time of classification | DateTime | ISO 8601 | UTC | Valid timestamp | System Clock |

## 👤 Patient and Clinical Data Elements

### Patient Demographics

| Data Element | Description | Data Type | Format | Units | Valid Range | Source |
|--------------|-------------|-----------|--------|-------|-------------|--------|
| PatientID | De-identified patient identifier | String | UUID | N/A | Valid UUID | System Generated |
| AgeGroup | Age range of patient | String | Text | Years | Valid age group | Clinical Assessment |
| BiologicalSex | Biological sex of patient | String | Text | N/A | Male/Female/Other | Clinical Assessment |
| HandDominance | Dominant hand of patient | String | Text | N/A | Right/Left/Ambidextrous | Clinical Assessment |
| Height | Patient height | Integer | Decimal | cm | 50-250 | Clinical Assessment |
| Weight | Patient weight | Float | Decimal | kg | 10-250 | Clinical Assessment |
| DiagnosisCode | Primary diagnosis code | String | ICD-10/11 | N/A | Valid code | Clinical Assessment |

### Clinical Assessment Data

| Data Element | Description | Data Type | Format | Units | Valid Range | Source |
|--------------|-------------|-----------|--------|-------|-------------|--------|
| AssessmentID | Identifier for clinical assessment | String | UUID | N/A | Valid UUID | System Generated |
| AssessmentType | Type of clinical assessment | String | Text | N/A | Valid assessment type | Clinical Protocol |
| AssessmentDate | Date of assessment | Date | ISO 8601 | UTC | Valid date | Clinical Assessment |
| ClinicianID | Identifier of assessing clinician | String | UUID | N/A | Valid UUID | System Generated |
| ScoreValue | Numerical assessment score | Float | Decimal | Various | Valid for assessment | Clinical Assessment |
| FunctionalCategory | Functional category assessed | String | Text | N/A | Valid category | Clinical Protocol |
| AssessmentNotes | Clinical notes on assessment | String | Text | N/A | N/A | Clinician Input |

### Medical History Data

| Data Element | Description | Data Type | Format | Units | Valid Range | Source |
|--------------|-------------|-----------|--------|-------|-------------|--------|
| MedicalHistoryID | Identifier for medical history entry | String | UUID | N/A | Valid UUID | System Generated |
| ConditionCode | Code for medical condition | String | ICD-10/11 | N/A | Valid code | Clinical Assessment |
| OnsetDate | Date of condition onset | Date | ISO 8601 | UTC | Valid date | Clinical Assessment |
| Severity | Severity of condition | String | Text | N/A | Mild/Moderate/Severe | Clinical Assessment |
| TreatmentStatus | Status of treatment | String | Text | N/A | Valid status | Clinical Assessment |
| RelevanceToNeural | Relevance to neural function | String | Text | N/A | High/Medium/Low/None | Clinical Assessment |
| MedicationList | List of current medications | Array | String Array | N/A | Valid medications | Clinical Assessment |

## ⚙️ System Configuration and Operational Data

### Device Configuration

| Data Element | Description | Data Type | Format | Units | Valid Range | Source |
|--------------|-------------|-----------|--------|-------|-------------|--------|
| DeviceID | Unique identifier for device | String | UUID | N/A | Valid UUID | System Generated |
| FirmwareVersion | Version of device firmware | String | Semantic Version | N/A | Valid version | Device |
| HardwareVersion | Version of device hardware | String | Semantic Version | N/A | Valid version | Device |
| ChannelConfiguration | Configuration of channels | JSON | Object | N/A | Valid configuration | System Configuration |
| SamplingConfiguration | Configuration of sampling | JSON | Object | Hz | Valid configuration | System Configuration |
| FilterConfiguration | Configuration of filters | JSON | Object | Various | Valid configuration | System Configuration |
| PowerSettings | Power management settings | JSON | Object | Various | Valid settings | System Configuration |

### System Performance Data

| Data Element | Description | Data Type | Format | Units | Valid Range | Source |
|--------------|-------------|-----------|--------|-------|-------------|--------|
| PerformanceLogID | Identifier for performance log | String | UUID | N/A | Valid UUID | System Generated |
| LogTimestamp | Time of performance measurement | DateTime | ISO 8601 | UTC | Valid timestamp | System Clock |
| ProcessorUtilization | CPU utilization percentage | Float | Decimal | % | 0-100 | System Monitoring |
| MemoryUtilization | Memory utilization percentage | Float | Decimal | % | 0-100 | System Monitoring |
| BatteryLevel | Battery charge level | Float | Decimal | % | 0-100 | Device |
| SignalQualityMetric | Overall signal quality metric | Float | Decimal | N/A | 0.0-1.0 | Signal Processing |
| OperatingTemperature | Device operating temperature | Float | Decimal | °C | 0-60 | Device Sensor |

### Calibration Data

| Data Element | Description | Data Type | Format | Units | Valid Range | Source |
|--------------|-------------|-----------|--------|-------|-------------|--------|
| CalibrationID | Identifier for calibration session | String | UUID | N/A | Valid UUID | System Generated |
| CalibrationTimestamp | Time of calibration | DateTime | ISO 8601 | UTC | Valid timestamp | System Clock |
| CalibrationParameters | Parameters from calibration | JSON | Object | Various | Valid parameters | Calibration Process |
| BaselineValues | Baseline signal values | Array | Float Array | μV | Valid range | Calibration Process |
| CalibrationQuality | Quality of calibration | Float | Decimal | N/A | 0.0-1.0 | Calibration Process |
| CalibrationDuration | Duration of calibration | Integer | Decimal | seconds | > 0 | System Measurement |
| UserFeedback | User feedback on calibration | String | Text | N/A | N/A | User Input |

## 📈 Research and Analytical Data Elements

### Experiment Metadata

| Data Element | Description | Data Type | Format | Units | Valid Range | Source |
|--------------|-------------|-----------|--------|-------|-------------|--------|
| ExperimentID | Identifier for research experiment | String | UUID | N/A | Valid UUID | System Generated |
| ExperimentTitle | Title of experiment | String | Text | N/A | N/A | Researcher Input |
| ResearcherID | Identifier of primary researcher | String | UUID | N/A | Valid UUID | System Generated |
| ExperimentProtocol | Protocol identifier | String | Text | N/A | Valid protocol | Research Protocol |
| StartTimestamp | Start time of experiment | DateTime | ISO 8601 | UTC | Valid timestamp | System Clock |
| EndTimestamp | End time of experiment | DateTime | ISO 8601 | UTC | Valid timestamp | System Clock |
| ExperimentConditions | Experimental conditions | JSON | Object | Various | Valid conditions | Researcher Input |

### Model Training Data

| Data Element | Description | Data Type | Format | Units | Valid Range | Source |
|--------------|-------------|-----------|--------|-------|-------------|--------|
| ModelID | Identifier for ML model | String | UUID | N/A | Valid UUID | System Generated |
| ModelType | Type of machine learning model | String | Text | N/A | Valid model type | Model Repository |
| TrainingDatasetID | Identifier of training dataset | String | UUID | N/A | Valid UUID | System Generated |
| ValidationDatasetID | Identifier of validation dataset | String | UUID | N/A | Valid UUID | System Generated |
| HyperParameters | Model hyperparameters | JSON | Object | Various | Valid parameters | Training Process |
| TrainingAccuracy | Accuracy on training data | Float | Decimal | N/A | 0.0-1.0 | Training Process |
| ValidationAccuracy | Accuracy on validation data | Float | Decimal | N/A | 0.0-1.0 | Validation Process |

### Performance Analytics

| Data Element | Description | Data Type | Format | Units | Valid Range | Source |
|--------------|-------------|-----------|--------|-------|-------------|--------|
| AnalyticsID | Identifier for analytics record | String | UUID | N/A | Valid UUID | System Generated |
| AnalyticsTimestamp | Time of analytics generation | DateTime | ISO 8601 | UTC | Valid timestamp | System Clock |
| PerformanceMetrics | Set of performance metrics | JSON | Object | Various | Valid metrics | Analytics Engine |
| UserEfficiency | Efficiency of user interaction | Float | Decimal | N/A | 0.0-1.0 | Analytics Engine |
| ErrorRates | Rates of different error types | JSON | Object | % | 0.0-100.0 | Analytics Engine |
| UsagePatterns | Patterns of system usage | JSON | Object | Various | Valid patterns | Analytics Engine |
| ImprovementTrend | Trend in performance improvement | Float | Decimal | N/A | -1.0-1.0 | Analytics Engine |

## 🔄 Data Relationships and Hierarchies

### Data Hierarchy

1. **Patient Level**
   - Patient Demographics
   - Medical History
   - Clinical Assessments

2. **Session Level**
   - Session Metadata
   - Device Configuration
   - Calibration Data
   - System Performance

3. **Recording Level**
   - Raw Signal Data
   - Processed Signal Data
   - Classification Results

4. **Analysis Level**
   - Feature Extractions
   - Model Predictions
   - Performance Analytics

### Key Relationships

| Primary Entity | Relationship | Related Entity | Cardinality | Description |
|----------------|--------------|----------------|-------------|-------------|
| Patient | has many | Sessions | 1:N | A patient can have multiple sessions |
| Session | has many | Recordings | 1:N | A session can have multiple recordings |
| Recording | has many | Channels | 1:N | A recording can have multiple channels |
| Channel | has many | Samples | 1:N | A channel can have many signal samples |
| Patient | has many | Assessments | 1:N | A patient can have multiple clinical assessments |
| Model | trained on | Dataset | N:M | Models can be trained on multiple datasets |
| Classification | uses | Model | N:1 | Multiple classifications can use the same model |
| Device | has | Configuration | 1:1 | A device has one active configuration |

## 🔍 Data Quality Attributes

### Data Quality Dimensions

| Dimension | Description | Measurement Method | Target |
|-----------|-------------|-------------------|--------|
| Completeness | Presence of all required data | Percentage of required fields populated | ≥ 99% |
| Accuracy | Correctness of data values | Error rate in validation checks | ≤ 0.1% |
| Consistency | Uniformity of data across the system | Cross-reference validation rate | ≥ 99.5% |
| Timeliness | Recency of data | Latency measurement | ≤ 100ms |
| Validity | Conformance to data rules | Validation rule pass rate | ≥ 99.9% |
| Integrity | Maintenance of data relationships | Referential integrity check | 100% |
| Uniqueness | Absence of duplication | Duplicate detection rate | ≤ 0.01% |

### Data Constraints

| Constraint Type | Description | Implementation | Validation |
|-----------------|-------------|----------------|------------|
| Primary Key | Unique identifier constraint | Database constraint | System validation |
| Foreign Key | Referential integrity constraint | Database constraint | System validation |
| Value Range | Limit on allowed values | Application validation | Range checking |
| Format | Required data format | Application validation | Format checking |
| Mandatory | Required field presence | Application validation | Null checking |
| Uniqueness | No duplicate values allowed | Database constraint | Duplicate checking |
| Business Rule | Complex domain-specific rules | Application logic | Business rule engine |

## 🔐 Data Security Classification

### Security Levels

| Level | Description | Examples | Protection Requirements |
|-------|-------------|----------|------------------------|
| Critical | High
(Content truncated due to size limit. Use line ranges to read in chunks)

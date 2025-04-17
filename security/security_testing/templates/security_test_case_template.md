# Security Test Case Template

## 📋 General Information

| **Test Case Information** |                                                |
|---------------------------|------------------------------------------------|
| **Test Case ID**          | SEC-TC-[ID]                                    |
| **Version**               | 1.0                                            |
| **Created By**            | [Tester Name]                                  |
| **Creation Date**         | [YYYY-MM-DD]                                   |
| **Last Updated**          | [YYYY-MM-DD]                                   |
| **Executed By**           | [Tester Name]                                  |
| **Execution Date**        | [YYYY-MM-DD]                                   |
| **Test Environment**      | [Development/Testing/Staging]                  |
| **Test Category**         | [Authentication/Authorization/Encryption/etc.] |
| **Risk Level**            | [Critical/High/Medium/Low]                     |
| **Status**                | [Not Started/In Progress/Completed/Failed]     |

## 🎯 Test Objective

[Clearly state the security objective this test case is designed to verify. Describe what security control or requirement is being tested.]

## 📝 Test Description

[Provide a detailed description of the security test, including the specific security vulnerability or control being tested. Include references to relevant security requirements or standards.]

## 🔍 Preconditions

1. [List all preconditions that must be met before executing the test]
2. [Include system state, required accounts, data setup, etc.]
3. [Specify any tools or special configurations needed]

## 📋 Test Steps

| # | Step Description | Expected Result | Actual Result | Status |
|---|------------------|-----------------|---------------|--------|
| 1 | [Detailed step] | [Expected security behavior] | [To be filled during execution] | [Pass/Fail] |
| 2 | [Detailed step] | [Expected security behavior] | [To be filled during execution] | [Pass/Fail] |
| 3 | [Detailed step] | [Expected security behavior] | [To be filled during execution] | [Pass/Fail] |
| 4 | [Detailed step] | [Expected security behavior] | [To be filled during execution] | [Pass/Fail] |
| 5 | [Detailed step] | [Expected security behavior] | [To be filled during execution] | [Pass/Fail] |

## 📊 Test Data

| Data Item | Value | Description |
|-----------|-------|-------------|
| [Data item name] | [Value] | [Description of test data] |
| [Data item name] | [Value] | [Description of test data] |
| [Data item name] | [Value] | [Description of test data] |

## 🔒 Security Controls Tested

| Control ID | Control Name | Description |
|------------|--------------|-------------|
| [Control ID] | [Control Name] | [Brief description of the security control being tested] |
| [Control ID] | [Control Name] | [Brief description of the security control being tested] |

## 📝 Test Results

### Summary

| Total Steps | Passed | Failed | Blocked | Not Executed |
|-------------|--------|--------|---------|--------------|
| [Number]    | [Number] | [Number] | [Number] | [Number]    |

### Issues Found

| Issue ID | Description | Severity | Recommendation |
|----------|-------------|----------|----------------|
| [Issue ID] | [Description of security issue found] | [Critical/High/Medium/Low] | [Recommended fix] |
| [Issue ID] | [Description of security issue found] | [Critical/High/Medium/Low] | [Recommended fix] |

### Evidence

[Include screenshots, logs, or other evidence collected during testing. For security testing, evidence is crucial to demonstrate vulnerabilities or compliance.]

## 📋 Regulatory Compliance

| Regulation/Standard | Requirement ID | Compliance Status |
|---------------------|----------------|-------------------|
| [FDA/CDSCO/IEC 62304/etc.] | [Requirement ID] | [Compliant/Non-Compliant/Partially Compliant] |
| [FDA/CDSCO/IEC 62304/etc.] | [Requirement ID] | [Compliant/Non-Compliant/Partially Compliant] |

## 📝 Notes and Observations

[Include any additional notes, observations, or context that might be relevant to the security test. Document any anomalies or unexpected behaviors observed during testing.]

## 🔄 Retest Information

| Retest Number | Date | Tester | Status | Notes |
|---------------|------|--------|--------|-------|
| 1 | [YYYY-MM-DD] | [Tester Name] | [Pass/Fail] | [Notes about retest] |
| 2 | [YYYY-MM-DD] | [Tester Name] | [Pass/Fail] | [Notes about retest] |

## 📚 Related Documents

- [Security Testing Plan](/security/security_testing/security_testing_plan.md)
- [Security Checklists](/security/security_testing/checklists/)
- [Secure Coding Guidelines](/security/secure_coding_guidelines.md)
- [Threat Models](/security/threat_models/)

## 📜 Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Test Lead | [Name] | _____________ | [YYYY-MM-DD] |
| Security Officer | [Name] | _____________ | [YYYY-MM-DD] |
| Quality Assurance | [Name] | _____________ | [YYYY-MM-DD] |

---

*This document is part of the Chimera Security Framework and should be used in conjunction with the Security Testing Plan and other security documentation.*


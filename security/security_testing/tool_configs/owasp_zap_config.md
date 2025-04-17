# OWASP ZAP Configuration

## 📋 General Information

| **Configuration Information** |                                                |
|-------------------------------|------------------------------------------------|
| **Document ID**               | SEC-TOOL-CFG-ZAP-001                          |
| **Version**                   | 1.0.0                                          |
| **Date Created**              | April 17, 2025                                 |
| **Last Updated**              | April 17, 2025                                 |
| **Author**                    | Chimera Security Team                          |
| **Status**                    | Approved                                       |

## 🎯 Purpose

This document provides the standard configuration for OWASP Zed Attack Proxy (ZAP) when used for security testing of the Chimera neural interface system. It ensures consistent, thorough, and appropriate security testing while minimizing potential impacts on the system under test.

## 🔍 Tool Overview

OWASP ZAP (Zed Attack Proxy) is an open-source web application security scanner used to find vulnerabilities in web applications. It is designed to be used by people with a wide range of security experience and is ideal for developers and functional testers who are new to penetration testing.

## ⚙️ Standard Configuration

### General Settings

```json
{
  "connection.timeoutInSecs": 60,
  "connection.socksSizeInMbs": 10,
  "api.disablekey": false,
  "api.addrs.addr.name": ".*",
  "api.addrs.addr.regex": true,
  "api.key": "chimera-zap-api-key-2025",
  "scanner.attackStrength": "medium",
  "scanner.alertThreshold": "medium"
}
```

### Proxy Configuration

```json
{
  "proxy.ip": "127.0.0.1",
  "proxy.port": 8080,
  "proxy.reverseProxy.use": false,
  "proxy.decodeGzip": true,
  "proxy.removeUnsupportedEncodings": true,
  "proxy.timeoutInSecs": 120
}
```

### Active Scan Configuration

```json
{
  "ascan.attackStrength": "medium",
  "ascan.alertThreshold": "medium",
  "ascan.maxRuleDurationInMins": 5,
  "ascan.maxScanDurationInMins": 60,
  "ascan.threadPerHost": 2,
  "ascan.maxResultsToList": 1000,
  "ascan.allowAttackOnStart": false,
  "ascan.defaultPolicy": "chimera-medical-device-policy",
  "ascan.delay": 0,
  "ascan.injectPluginIdInHeader": false
}
```

### Passive Scan Configuration

```json
{
  "pscan.alertThreshold": "medium",
  "pscan.maxAlertsPerRule": 100,
  "pscan.scanOnlyInScope": true,
  "pscan.scanFuzzerMessages": true,
  "pscan.maxBodySizeInBytes": 1048576
}
```

### Authentication Configuration

```json
{
  "auth.loginUrl": "https://chimera-test.example.com/login",
  "auth.loginRequestData": "username={%username%}&password={%password%}",
  "auth.loginIndicator": "Logout",
  "auth.logoutUrl": "https://chimera-test.example.com/logout",
  "auth.logoutIndicator": "Login",
  "auth.autoDetectLoginRequests": true
}
```

### Session Management

```json
{
  "session.type": "cookie",
  "session.cookieName": "CHIMERA_SESSION",
  "session.timeout": 30
}
```

## 🔒 Custom Scan Policies

### Chimera Medical Device Policy

This custom policy is specifically designed for testing medical device web interfaces with appropriate risk levels.

#### Included Rules

| Rule ID | Rule Name | Risk Level | Enabled |
|---------|-----------|------------|---------|
| 40012 | Cross Site Scripting (Reflected) | High | Yes |
| 40014 | Cross Site Scripting (Persistent) | High | Yes |
| 40016 | Cross Site Scripting (DOM Based) | High | Yes |
| 40018 | SQL Injection | High | Yes |
| 40019 | SQL Injection - MySQL | High | Yes |
| 40020 | SQL Injection - PostgreSQL | High | Yes |
| 40021 | SQL Injection - Oracle | High | Yes |
| 40022 | SQL Injection - SQLite | High | Yes |
| 90019 | Server Side Include | High | Yes |
| 90020 | Remote OS Command Injection | High | Yes |
| 20012 | Anti-CSRF Tokens Check | Medium | Yes |
| 20014 | HTTP Parameter Pollution | Medium | Yes |
| 20015 | Heartbleed OpenSSL Vulnerability | High | Yes |
| 20016 | Cross-Domain Misconfiguration | Medium | Yes |
| 20017 | Source Code Disclosure - CVE-2012-1823 | Medium | Yes |
| 20018 | Remote Code Execution - CVE-2012-1823 | High | Yes |
| 30001 | Buffer Overflow | High | Yes |
| 30002 | Format String Error | High | Yes |
| 40003 | CRLF Injection | Medium | Yes |
| 40008 | Parameter Tampering | Medium | Yes |
| 40009 | Server Side Include | High | Yes |
| 40023 | XML External Entity Attack | High | Yes |
| 40024 | Generic Padding Oracle | High | Yes |
| 40025 | Expression Language Injection | High | Yes |
| 40026 | SOAP Action Spoofing | High | Yes |
| 40027 | Session Fixation | High | Yes |
| 40028 | ELMAH Information Leak | Medium | Yes |
| 90001 | Insecure JSF ViewState | Medium | Yes |
| 90011 | Charset Mismatch | Low | Yes |
| 90022 | Application Error Disclosure | Medium | Yes |
| 90024 | Generic Padding Oracle | High | Yes |
| 90025 | Strict Transport Security | Medium | Yes |
| 90028 | Insecure HTTP Method | Medium | Yes |
| 90030 | WSDL File Detection | Low | Yes |
| 90033 | Loosely Scoped Cookie | Low | Yes |

#### Excluded Rules

| Rule ID | Rule Name | Reason for Exclusion |
|---------|-----------|----------------------|
| 40013 | Session Fixation | Handled by custom authentication |
| 40031 | User Agent Fuzzer | Can cause system instability |
| 40032 | CORS Header | Configured intentionally for our architecture |
| 90021 | XPath Injection | Not applicable to our architecture |

## 📊 Reporting Configuration

```json
{
  "report.title": "Chimera Security Scan Report",
  "report.template": "chimera-template",
  "report.description": "Security scan of Chimera neural interface system",
  "report.display.report": true,
  "report.generate.onfinish": true,
  "report.format": "html",
  "report.customname": "chimera-zap-report-${datetime}"
}
```

## 🔄 Integration Configuration

### CI/CD Pipeline Integration

```json
{
  "automation.enabled": true,
  "automation.jobid": "chimera-security-scan",
  "automation.pollingIntervalInSecs": 20,
  "automation.maxDurationInMins": 60,
  "automation.onFail": "continue",
  "automation.notifyUrl": "https://ci.chimera.example.com/api/notify",
  "automation.notifyData": "scanid=${scanId}&result=${result}"
}
```

### Issue Tracker Integration

```json
{
  "issuetracker.type": "jira",
  "issuetracker.url": "https://jira.chimera.example.com",
  "issuetracker.project": "CHIMSEC",
  "issuetracker.issuetype": "Security Bug",
  "issuetracker.username": "zap-integration",
  "issuetracker.password": "encrypted:a1b2c3d4e5f6g7h8i9j0",
  "issuetracker.raiseOnlyHighIssues": false
}
```

## 🛡️ Safe Testing Guidelines

1. **Always use test environments**: Never run active scans against production environments.

2. **Start with low intensity**: Begin with passive scans and low-intensity active scans before increasing intensity.

3. **Use proper authentication**: Ensure ZAP is properly authenticated to avoid false positives from authentication barriers.

4. **Limit scope**: Configure proper scope to avoid testing unintended targets.

5. **Monitor system during testing**: Watch for unexpected system behavior during scanning.

6. **Schedule during low-usage periods**: Run intensive scans during maintenance windows or low-usage periods.

7. **Backup before testing**: Ensure database and configuration backups exist before testing.

8. **Review results carefully**: Manually verify findings to eliminate false positives.

## 📚 Related Documents

- [Security Testing Plan](/security/security_testing/security_testing_plan.md)
- [API Security Checklist](/security/security_testing/checklists/api_security_checklist.md)
- [Security Test Case Template](/security/security_testing/templates/security_test_case_template.md)
- [Secure Coding Guidelines](/security/secure_coding_guidelines.md)

## 📜 References

1. OWASP ZAP Official Documentation
2. OWASP Testing Guide
3. FDA Guidance on Cybersecurity for Medical Devices
4. IEC 62304: Medical Device Software Lifecycle Processes
5. NIST SP 800-115: Technical Guide to Information Security Testing and Assessment

---

*This document is part of the Chimera Security Framework and should be used in conjunction with the Security Testing Plan and other security documentation.*


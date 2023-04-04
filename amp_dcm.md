# Direct Change Mode (DCM)

## Table of contents
- [Direct Change Mode (DCM)](#direct-change-mode-dcm)
  - [Table of contents](#table-of-contents)
  - [Note:](#note)
    - [What is DCM?](#what-is-dcm)
    - [What can it be used for?](#what-can-it-be-used-for)
    - [Who has access?](#who-has-access)
    - [Additional Reading](#additional-reading)

## Note:
To acces the links from this document, you will require an AMP container or use your AMP laptop to access.

### What is DCM?

DCM will allow Cloud COE and VMS engineers the ability to provision and update AMS-supported resources without have to go directly through the AMS change management process (RFC) while still adhering to the AMP change process.

Resources:
- [Getting Started](https://docs.aws.amazon.com/managedservices/latest/userguide/dcm-get-started.html)


### What can it be used for?

The Cloud-X environment is managed by AMS (Amazon Managed Services), which forces CCoE team to comply with the change management they have in place before any updates to their infrastructure are made.

**Note:** Cloud-2 and CloudPE environments do not use DCM as these *are not* AMS managed, these are managed by the CCoE team and as a result, we have Admin access by proxy.

- [Policy Simulator](https://policysim.aws.amazon.com/home/index.jsp?#roles/AMPManagedServicesUpdateRole)
- [Solution Design](https://teamtools.amp.com.au/confluence/display/C2/2022-02-28+-+HLSA+-+Cloud+X+-+AMS+DCM)

### Who has access?

- [How to request access DCM](https://teamtools.amp.com.au/confluence/display/C2/HowTo%3A+Request+the+access+to+DCM+roles)
- [How to assume DCM role in CX](https://teamtools.amp.com.au/confluence/display/C2/HowTo%3A+Assume+DCM+roles+in+Cloud+X+accounts)

### Additional Reading

- [DCM Issues and Improvements Tracker](https://teamtools.amp.com.au/confluence/display/C2/Cloud+X+DCM+and+GHA+Issues+and+Improvements)
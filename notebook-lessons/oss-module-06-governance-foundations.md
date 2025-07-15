# Module 6: Governance

## Goals

In this lesson, you will learn the following:

* Concepts of open source governance and how it is used to maintain open source projects
* Different types of open source foundations, their governance models, and how this impacts open source projects

#### 5.7: [Python Software Foundation](https://www.python.org/psf-landing/)
The Python Software Foundation (PSF) is a non-profit organization that manages and supports the Python programming language and its global community. Like many modern open source foundations, the PSF builds on governance models and licensing concepts pioneered by the FSF. It plays a critical role in maintaining Python's development, promoting its use, and supporting its community through funding, infrastructure, and outreach.ontents
- [1: What is open source governance?](#1:-What-is-open-source-governance?)
- [2: Models of Governance](#2:-Models-of-Governance)
- [3: Cathedral vs. Bazaar](#3:-Cathedral-vs.-Bazaar)
- [4: Common Governance Models](#4:-Common-Governance-Models)
  * [4.1: Do-ocracy](#4.1:-Do-ocracy)
  * [4.2: Founder-leader (BDFL)](#4.2:-Founder-leader-(BDFL))
  * [4.3: Self-appointed technical council](#4.3:-Self-appointed-technical-council)
  * [4.4: Electoral](#4.4:-Electoral)
  * [4.5: Single-vendor Backed](#4.5:-Single-vendor-Backed)
  * [4.6: Foundation-backed](#4.6:-Foundation-backed)
- [5: Open Source Foundations](#5:-Open-Source-Foundations)
  * [5.1: Apache Foundation](#5.1:-Apache-Foundation)
  * [5.2: Free Software Foundation](#5.2:-Free-Software-Foundation)
  * [5.3: Linux Foundation](#5.3:-Linux-Foundation)
  * [5.4: CNCF - Cloud Native Computing Foundation](#5.4:-CNCF---Cloud-Native-Computing-Foundation)
  * [5.5: GNOME](#5.5:-GNOME)
  * [5.6: Eclipse](#5.6:-Eclipse)
  * [5.7: Python Software Foundation](#5.7:-Python-Software-Foundation)
  * [5.8: LLVM Foundation](#5.8:-LLVM-Foundation)

## Sources
* John Mertic. [_Open Source Projects - Beyond Code_](https://learning.oreilly.com/library/view/open-source-projects/9781837636884/). O`Reilly Media, 2023.  Metric is the current director of program management for The Linux Foundation.
* Dave Neary, Josh Berkus, Katrina Novakovic, Bryan Behranshausen.  ["Understanding open source governance models"](https://www.redhat.com/en/blog/understanding-open-source-governance-models), Red Hat Blog, 2020.  Authors are from Red Hat's Open Source Programming Office.
* Ross Gardler and Gabriel Hanganu. ["Governance Models"](http://oss-watch.ac.uk/resources/governancemodels).  OSS Watch, 2013.  Gardler is the former President of the Apache Foundation.
* JLC Izquierdo [A Survey of Software Foundations in Open Source](https://arxiv.org/pdf/2004.10063), 2020
* Free Software Foundation. ["What is free software?"](https://www.gnu.org/philosophy/free-sw.html) and ["GNU Project Philosophy"](https://www.gnu.org/philosophy/). The FSF, founded by Richard Stallman in 1985, is one of the oldest organizations promoting software freedom.

## 1: What is open source governance?

*Governance* describes the decision-making that an open source projects need to function. This is how policies and processes are defined. The concept of formal governance in free and open source software was significantly influenced by early organizations like the Free Software Foundation (FSF), which established many of the foundational principles still used today. The FSF, founded in 1985, was the original organization promoting software freedom - what we now call "open source" emerged later in 1998, building on the philosophical and practical foundations laid by the free software movement. Some examples of policies are:

* **Roles and responsibilities**
  - Who gets to do what?
* **Accepting code**
  - What are the policies to ensure code stability and quality?
  - What are the policies to ensure supply-chain security?
* **Releasing code?**
  - What are the criteria for a stable release?
  - What is the release cadence?
* **Getting new contributors involved**
  - Is the contributor qualified?
  - Is the contributor trusted?
* **Communication**
  - How do users report bugs and feature requests?
  - Who can speak on behalf of the project?
  - How are interpersonal disputes resolved?
 
There is no one-size-fits-all solution for all projects, so different projects may require different governance models.

## 2: Models of Governance

Models of governance differ primarily on:
* Who gets to make decisions
* How decisions get made

## 3: Cathedral vs. Bazaar

An older model, first described in Linux community around 1999.  Describes both **governance** (who gets to make decisions) and **contribution** (who gets to add new code).

![chapel_and_bazaar](http://oss-watch.ac.uk/img/governancevcontrib.png)

* Two extremes of **governance**:
  - Benevolent Dictator: Single individual or organization makes policy decisions
  - Meritocracy: Ability to make decisions is given to significant contributors
* Two extremes of **contribution**:
  - Bazaar: Project accepts code from many external developers
  - Cathedral: Project has a group of core developers

## 4: Common Governance Models

Many recent OSS advocates describe five or six models for open source governance:

1. Do-ocracy (a.k.a Meritocracy)
2. Founder-leader (a.k.a, Benevolent Dictator for Life, )
3. Self-appointed technical council
4. Electoral
5. Vendor-backed
6. Foundation-backed

These models are not mutually-exclusive.  Within one project, different policies may be decided through different models.  

### 4.1: Do-ocracy

* The people doing the work are the ones making decisions
  - Often no formal governance.  Just implicit governance in group's interactions
  - Usually still have contribution guidelines (peer review of code, etc.)

#### Example

* Apache Web Server: https://httpd.apache.org/ABOUT_APACHE.html
  
#### Pros
* Easy for small teams with few stakeholders

#### Cons
* Decision-making usually does not scale with more contributors and stakeholders
* Can be difficult for newcomers to integrate with the project

### 4.2: Founder-leader (BDFL)

* One person who started the project is the ultimate decision-maker
* Leader determines projects priorities and vision, settles disputes among other
    contributors, and decides which contributions are merged

#### Examples
* Linux and Linus Torvalds
* Python and Guido van Rossum : a BDFL early-on, and van Rossum is still "honorary" BDFL.
  But now has foundation-backed governance
* GNU Project and Richard Stallman: As founder of the Free Software Foundation (FSF) and the GNU Project, Stallman served as a BDFL for many GNU tools and established fundamental principles of software freedom that influenced the entire open source movement. Notably, Linux's success would not have been possible without the FSF's GNU tools (GCC compiler, GNU coreutils, etc.) that provided the essential userland components for a complete operating system

#### Pros
* Easy for small teams with few stakeholders
* Common for most projects to start this way
* A humble, inclusive, constructive leader can set a positive tone
    for how community can function.
  
#### Cons
* Does not scale with more contributors and stakeholders
  - Problems with patches getting dropped were a frequent complaint in Linux until
    Torvalds distributed responsibilities more [see examples in mailing list archives](https://lwn.net/2002/0131/a/patch-penguin.php3)
  - A BDFL may not-be-so-benevolent.  Contributors who have disputes with founder do not have other
    recourse, and projects can get forked.
  - Founders' personal views may affect public perception of project.

### 4.3: Self-appointed technical council

- A small group determine's project priorities, decides which contributions will be merged, etc.
- The council also decides who will can join the council
- A midpoint between Meritocracy and Founder-leader model
- Many names for this type of group: technical council, steering committee, ...

#### Examples

* The Apache Software Foundation: https://www.apache.org/foundation/governance/
  - Several councils with different roles/responsibilities.  Mostly business, stakeholder relations, etc.
  - Individual software projects are meritocratic
* OpenAPI: https://www.openapis.org/participate/how-to-contribute/governance
  - A open standard, not an actual piece of software
  - Several councils with different roles/responsibilities: Technical Steering Committee,
    Technical Oversight Committee, Business Governance Board
* Councils are quite common with open standards

#### Pros

* Scales better for larger projects with many stakeholders
* Decision-making is efficient

#### Cons

* Member selection process may exclusionary
* May create self-reinforcing leadership structure
* May create disconnect between leadership and community

### 4.4: Electoral

Governance members are selected through a wider community vote, either from sponsoring organizations or members. This model is often combined with the steering committee model.

Examples

* [Kubernetes Steering Elections](https://github.com/kubernetes/steering/blob/main/elections.md) 
* [RISC-V Technical Steering Committee (TSC) Community Elections](https://lists.riscv.org/g/tech-announce/topic/2025_tsc_elected/112650228) - note that RISC-V TSC has some permanent and elected members

#### Pros
- Allows for more engagement with a wider community and acknowledgement of engaged community members

#### Cons
- In mixed steering committees with permanent members, elected members may have limited impact on the direction of a project. 

### 4.5: Single-vendor Backed

A company may decide to open source a project for a variety of reasons
- Releasing open source code that seems useful to the community
- Providing an early version of a product to gauge user interest and engagement. 
  * E.g., Kubernetes was released by Google and user interest led to the creation of the Cloud Native Computing Foundation
- Creating a "freemium" version of a product

Community contributions are welcomed but the vision for the project is typically controlled by one primary stakeholder
- Over time, governance may shift to another model as community engagement grows

#### Examples

- Kubernetes (pre-CNCF): https://kubernetes.io/community/
- Android
- MySQL

It can be hard to find governance documents for this model as it may be internally defined by the vendor.

#### Pros
- Similar to Founder-Leader but with a larger amount of resources behind development
- Quality of open source code benefits from professional software engineer support

#### Cons
- Similar to Founder-Leader, a company's vision for a project may differ from that of the community
- Lack of investment from the vendor can cause the project to stagnate and lose community involvement

### 4.6: Foundation-backed

Open-source projects often hit a glass ceiling, with many of the following attributes:

* It’s not clear how a project is funded or how it operates, or there is a perception that it primarily benefits a single vendor
* There isn’t a neutral owner of assets, such as the project name, logo, domain names, social accounts, and other assets
* The copyright holder of the project is a single entity, giving them unilateral control to change the license and intellectual property policies without the community’s input
* Vendors leveraging the technology don’t feel they have a space to fairly collaborate, especially if they are competitors
* The legal, fiduciary, and financial aspects of the project are managed by one organization without transparency or given processes


#### Examples

* Python Language Foundation:  https://www.python.org/psf/about/
* Rust Foundation:  https://foundation.rust-lang.org/about/
* PHP Foundation:  https://thephp.foundation/foundation/
* Ruby Central:  https://www.rubycentral.org/
* Free Software Foundation:  https://www.fsf.org/about/ - The original organization promoting software freedom (founded 1985), which predates and enabled most other foundations. The FSF established the philosophical and legal frameworks that made modern open source possible

#### Pros

* Solves the above-mentioned issues

#### Cons
* It's a lot of work to form a legal entity
  - Funding: The above-mentioned projects are non-profit entities backed by donations and/or corporate sponsorship
  - Staffing: Usually need committed staff to operate


## 5: Open Source Foundations
Most Open Source Software (OSS) projects rely on volunteer developer contribution to evolve and largely depends on its developer retention and community building. But many OSS projects lack formal models to structure and manage the community around them. Software foundations can 
* provide the legal and funding infrastructure for an OSS community
* define internal regulations for activities, membership, and decision-making process
* provide the grounds for open and collaborative software development through mentoring 

Many foundations exist primarily to promote free software or handle the legal and fundraising aspects of a project without engaging in the daily project operations. The Free Software Foundation (FSF), established in 1985, was the original organization promoting software freedom and created the foundational infrastructure that enabled the entire ecosystem of open source organizations that followed. The term "open source" was coined in 1998, building on more than a decade of free software principles and practices established by the FSF. Most modern foundations can trace their philosophical, legal, and practical foundations back to the FSF's pioneering work. As an example, Linux Foundation suggests the Apache License for hosted projects but does not necessarily require it, as is the case with Apache Foundation projects. Different foundations may suggest or require different governance and operation models.

### 5.1: [Apache Foundation](https://www.apache.org/)
The Apache Software Foundation (ASF) is one of the largest and most influential open-source organizations in the world, building on the foundation laid by the FSF's earlier work in establishing software freedom principles.

The ASF provides support, governance, and infrastructure for hundreds of open-source projects and communities. It offers the infrastructure, public relations and travel assistance, legal and trademark services. Projects enter the foundation through their incubator program, which includes mentoring for the project's growth. 

### 5.2: [Free Software Foundation](https://www.fsf.org/)
The Free Software Foundation (FSF) is a nonprofit organization founded in 1985 by Richard Stallman and represents the original organization promoting software freedom. The FSF predates the "open source" movement by over a decade - the term "open source" was coined in 1998, building on the philosophical and practical foundations established by the free software movement. The FSF is historically significant as the foundational organization that made all subsequent open source organizations and projects possible.

The FSF's contributions to the software ecosystem are fundamental and far-reaching. Linux's success, for example, would not have been possible without the FSF's GNU tools: the GCC compiler, GNU coreutils, bash shell, and other essential components that provided the complete userland for a functioning operating system. When Linus Torvalds created the Linux kernel, he built upon a decade of FSF infrastructure.

The FSF maintains the GNU General Public License (GPL) family of licenses, which are among the most widely used free software licenses and served as templates for many other open source licenses. The organization also oversees the GNU Project, which develops a complete free operating system and essential tools. Key activities include:

- **License stewardship**: Maintaining and updating the GPL, LGPL, and other free software licenses that became the foundation for modern open source licensing
- **GNU Project governance**: Overseeing development of GNU tools like GCC, Emacs, and other core Unix-like system components that enabled projects like Linux
- **Advocacy and education**: Promoting software freedom through campaigns, educational resources, and policy advocacy that established the principles later adopted by the broader open source movement
- **Legal support**: Providing guidance on license compliance and defending software freedom in legal contexts

The FSF's governance model combines foundation-backed structure with strong ideological principles, emphasizing user freedom over pragmatic development concerns. This model influenced how many subsequent foundations approach the balance between technical and philosophical considerations. 


### 5.3: [Linux Foundation](https://www.linuxfoundation.org/)
The Linux Foundation (LF) is a non-profit technology consortium that supports and promotes the growth of open source software, particularly in enterprise, infrastructure, and emerging technologies.

It mainly acts as umbrella for a number of smaller foundations, where inner organizations generally work in a stand-alone way (e.g., *OpenAPI initiative* or *Kubernetes*)

- [Linux Foundation Code Checklist](https://github.com/Call-for-Code/Linux-Foundation-Checklist)

### 5.4: [CNCF - Cloud Native Computing Foundation](https://www.cncf.io/)
It is part of Linux Foundation and plays major role in he cloud and DevOps ecosystem, its mission is to make cloud native computing ubiquitous. It is a vendor-neutral, non-profit organization that promotes the adoption of cloud-native technologies. It provides open source project hosting and governance; education and certification; community building and ecosystem development; security and best practices; research, landscape and tools. 

### 5.5: [GNOME](https://foundation.gnome.org/)
The GNOME Foundation is a non-profit organization that supports the development and promotion of the GNOME desktop environment, a popular free and open-source graphical user interface used primarily on Linux systems. It provides technical and infrastructure support; Financial and Legal Support; Community Building; Promotion and Advocacy. 

### 5.6: [Eclipse](https://www.eclipse.org/)
The Eclipse Foundation is a non-profit organization that supports a global community of open-source projects, especially in the areas of software development tools, IoT, automotive, edge computing, and enterprise software. While originally known for the Eclipse IDE, it now hosts a wide variety of projects across multiple domains. 
The Eclipse Foundation supports innovation in open source by providing:

    - Project hosting and governance
    - Legal, IP, and infrastructure support
    - Industry collaboration through working groups
    - Developer tools like Eclipse IDE, Che, and Theia
    - Focus on key areas: IDEs, IoT, automotive, Java, and cloud-native

### 5.7: [Python Software Foundation](https://www.python.org/psf-landing/)
The Python Software Foundation (PSF) is a non-profit organization that manages and supports the Python programming language and its global community. It plays a critical role in maintaining Python’s development, promoting its use, and supporting its community through funding, infrastructure, and outreach.

### 5.8: [LLVM Foundation](https://foundation.llvm.org/)
It is a nonprofit organization dedicated to supporting the long-term health and growth of the LLVM Project, with core missions on supporting education in the field of compilers and tools; Fosters collaboration through meetups, forums, and mentorship; Maintains the technical infrastructure (e.g. servers, CI systems) and ensurs the project remains vendor-neutral and community-driven; Manages donations and sponsorships to fund the development. 

| Foundation Name | Focus Area | Open Source Hosting | Governance     | Community Building| Training      | Financial and Legal Support| Promotion and Advocacy|
| ------------------- | ---------- | -------------| ------------ | ----------- | ---------- |---------- | ---------- |
| Free Software Foundation | GNU Project, software freedom advocacy, GPL licensing - **ORIGINAL** organization (1985)|Yes|Yes|Yes|No|Yes|Yes|
| Apache Foundation | HTTP servers, Hadoop, Kafka, Maven, Tomcat|Yes, incubating|No|No|No|Yes|No|
| Linux Foundation|Linux, cloud computing, security, blockchain, AI, networking|Yes|No|Yes|Yes|Yes|Yes|
| CNCF Foundation | Cloud computing|Yes,incubating|No|Yes|Yes|No|No|
| Gnome Foundation | GNOME desktop |Yes|Yes|Yes|No| Yes|Yes|
| Eclipse Foundation | IDE, IoT and Edge, Cloud, Java Runtime |Yes|No|Yes|No|No|No|
| Python Software Foundation | Python Language | Yes | Yes| Yes| No|Yes|Yes|
| LLVM Foundation | Compilers and Tools|Yes|No|Yes|Yes|Yes|No|

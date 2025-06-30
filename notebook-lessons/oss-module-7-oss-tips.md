# Lesson Learned from OSS projects

## Goals

In this lesson, attendees will learn the following:
* Different types of open source foundations and how they interact with open source projects
* Tips for a successful open source project
* Lessons learned from long-term succssful projects

## Sources
* Eddie Jaoude [ Open Source Tips ](https://eddiejaoude.github.io/book-open-source-tips/), 2025
* JLC Izquierdo [ A Survey of Software Foundations in Open Source](https://arxiv.org/pdf/2005.10063), 2020
* [Open Source Project Maturity Model](https://www.usdigitalresponse.org/resources/cms-open-source-software)
* [Schmidt Academy for Software Engineering](https://sase.caltech.edu/resources/index.html)
* [Linux Professional Institution Open Source Essiential Training Material](https://learning.lpi.org/en/learning-materials/050-100/)
* [pyOpenSci Peer Review](https://www.pyopensci.org/)

## Open Source Foundations
Most Open Source Software (OSS) projects rely on volunteer developer's contribution to evolve and largely depends on its developer retaintion and community building. But many OSS projects lack formal models to structure and manage the community around them. Software foundations can 
* provide the legal and economical infrastructure for a OSS community
* define internal regulations for activities, membership and decision-making process
* provide the grounds for open and collaborative software development through mentoring 

However, there is a high variety of services and development strategies offered by software foundations. 

### [Apache Foundation](https://www.apache.org/)
The Apache Software Foundation (ASF) is one of the largest and most influential open-source organizations in the world. It provides support, governance, and infrastructure for hundreds of open-source projects and communities. It acts as a Subversion Coprporation.  
It offers the infrastructure, public relation and travel assistant, legal and trademark servervice.  Project entries the foundation through incubator, there are 60 projects in the incububator. Mentoring is built in incubator. 

### [Linux Foundation](https://www.linuxfoundation.org/)
It mainly acts as umbrella for a number of smaller foundations, where inner organizations generally work in a stand-alone way (e.g., *OpenAPI initiative* or *Kubernetes*)

### [CNCF - Cloud Native Computing Foundation](https://www.cncf.io/)
It is part of Linux Foundation and plays major role in he cloud and DevOps ecosystem, its mission is to make cloud native computing ubiquitous. It is a vendor-neutral, non-profit organization that promotes the adoption of cloud-native technologies. It provides open source project hosting and governance; education and certification; community building and ecosystem development; security and best practices; research, landscape and tools. 

### [GNOME](https://foundation.gnome.org/)
The GNOME Foundation is a non-profit organization that supports the development and promotion of the GNOME desktop environment, a popular free and open-source graphical user interface used primarily on Linux systems. It provides technical and infrastructure support; Financial and Legal Support; Community Building; Promotion and Advocacy. 

### [Eclipse](https://www.eclipse.org/)
The Eclipse Foundation is a non-profit organization that supports a global community of open-source projects, especially in the areas of software development tools, IoT, automotive, edge computing, and enterprise software. While originally known for the Eclipse IDE, it now hosts a wide variety of projects across multiple domains. 
The Eclipse Foundation supports innovation in open source by providing:

    - Project hosting and governance
    - Legal, IP, and infrastructure support
    - Industry collaboration through working groups
    - Developer tools like Eclipse IDE, Che, and Theia
    - Focus on key areas: IDEs, IoT, automotive, Java, and cloud-native
### Python Software Foundation

| Foundation Name | Focuse Area | Open Source Hosting | Govenance     | Community Building| Training      | Financial and Legal Support| Promotion and Advocacy|
| ------------------- | ---------- | -------------| ------------ | ----------- | ---------- |---------- | ---------- |
| Apache Foundation | HTTP Server, Hadoop, Kafka, Maven, Tomcat|Yes, incubating|No|No|No|Yes|No|
| Linux Foundation||||||||
| CNCF Foundation | Cloud native|Yes,incubating|No|Yes|Yes|No|No|
| Gnome Foundation | GNOME desktop |Yes|Yes|Yes|No| Yes|Yes|
| Eclipse Foundation | IDE, IoT and Edge, Cloud, Java Runtime |Yes|No|Yes|No|No|No|

                  




## Open Source Tips
This session contains some common DOs and Don'ts for Open Source software, these tips help the newcomers to avoid the pitfalls of Open Source development and learn from the community's collective wisdom. 

### Start OSS Project with the following steps: 

* Start every project with at least a `README.md`, which includes project description & quickstart guide
* Use syntax hightlighting in documentation
* Add `CONTRIBUTING.md` in the `.github` folder of your project root direcotry, which succinctly communicates the maintainer's guidelines, examples such as [puppet project's contributor guide](https://github.com/puppetlabs/.github/blob/main/CONTRIBUTING.md)
* Add `CODE_OF_CONDUCT.md` in the root of your project to ensure a safe diverse & inclusive, examples such as [puppet project's CODE Of Conduct](https://github.com/puppetlabs/puppet/blob/main/CODE_OF_CONDUCT.md)
* Add GitHub Issue & Pull Request templates namely `ISSUE_TEMPLATE.md` in the `.github` folder of your project root directory, which helps keeping the project consistent & reminds 
* Chose a license, GT OSPO creates a flowchart on helping you identify an approriate license at [here](https://ospo.cc.gatech.edu/open-source-software-licensing/), you can find more useful guidance at [here](https://choosealicense.com/)
* Add a .gitignore file at the root of repository to avoid checking in non-source code files, e.g. `__py_cache__`

### Contriute to OSS projects
* Make Git commits small and atomic, limit commit message subject line to $50$ characters, no period at the end of subject line, put longer discription in the message body, wrap the body at $72$ characters, use the body to explain *why* not *how*
* Keep GitHub Issue/Task small, add list of task in a sub task checklist by 
```
    - [ ] subtask 1
    - [ ] subtask 2
```
* Always response Issue and Pull Request timely
* Add the a description to your Pull Request to make it easier for reviewer to digest your work
* Raise an Issue first so a plan of action can be discussed before you begin the work.
* Always have another person to Review the Pull Request which allows a second pair of eyes picking up oversights
* Automate everything through Tests, CI/CD
* Utilize GitHub Labels, Milestones, Releases/Tags, align Release versions with Milestones
* Use Branching to work with a wider team, project main branch (`mastter` or `develop`), everything must go via a feature branch and a Pull Request


### Things to avoid
* Big bang project, finishing the project in a weekend, then ignore it for the next year. 
* God commit, is difficult to understand and review
* God Pull Request, similar to God commit, leaves room for skim reviewing and leads to mistakes
* CV Driven Development, do not try every new technology you want to learn on the same project
* Weakest Dependency


## Open Source Projects Maturity Model
[Open Source Repository Maturity Model](https://github.com/dsacms/repo-scaffolder/blob/main/maturity-model-tiers.md) presents a framework that determines what and how much documentation is needed based on the project's size, community involvement, and goals.
The framework consists of five tiers (0-4), each representing different stages of a projects maturity:
* [Tier 0](https://github.com/DSACMS/repo-scaffolder/blob/main/tier0/README.md) includes experimental private repositories usually with single developer
* [Tier 1](https://github.com/DSACMS/repo-scaffolder/blob/main/tier1/README.md) includes an informational or historical project that has been released publicly once, without any planned future updates. Main purpose of a Tier 1 project is to share knowledge.
* [Tier 2](https://github.com/DSACMS/repo-scaffolder/blob/main/tier2/README.md) is a collaborative project within a team, which is not meant for broad public contribution but rather for internal collaboration. E.g. 
* [Tier 3](https://github.com/DSACMS/repo-scaffolder/blob/main/tier3/README.md) is an open collaboration effort with limited external contributions. Althought it is open source, the direction and maintenance are still controlled by a smaller group or team.
* [Tier 4](https://github.com/DSACMS/repo-scaffolder/blob/main/tier4/README.md) is a fully open and collaborative project that operates under a community governance model. The governance structure is open to a broad community

There is also a commandline tool which can guide users through a series of questions and recommends the appropriate templates should be used based on the tiers - [CookieCutter](https://github.com/DSACMS/repo-scaffolder?tab=readme-ov-file#need-help-picking-a-tier)

## Open Source Project template 
Here you can find [template files](https://github.com/DSACMS/repo-scaffolder/tree/main/tier4/%7B%7Bcookiecutter.project_slug%7D%7D) you can use for your project.  

## Successful OSS Projects

### Linux

### emacs/vim

### Python

### rust

### LLVM

### neovim

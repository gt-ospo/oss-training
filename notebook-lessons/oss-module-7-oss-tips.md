# Lesson Learned from OSS projects

## Goals

In this lesson, attendees will learn the following:
* Different types of open source foundations and how they interact with open source projects
* Tips for a successful open source project
* Lessons learned from long-term succssful projects

## Sources
* Eddie Jaoude [ Open Source Tips ](https://eddiejaoude.github.io/book-open-source-tips/), 2025
* JLC Izquierdo [ A Survey of Software Foundations in Open Source](https://arxiv.org/pdf/2005.10063), 2020

## Open Source Foundations
Most Open Source Software (OSS) projects rely on volunteer developer's contribution to evolve and largely depends on its developer retaintion and community building. But many OSS projects lack formal models to structure and manage the community around them. Software foundations can 
* provide the legal and economical infrastructure for a OSS community
* define internal regulations for activities, membership and decision-making process
* provide the grounds for open and collaborative software development through mentoring 

However, there is a high variety of services and development strategies offered by software foundations. 

### Apache Foundation
It acts as a Subversion Coprporation.  
It offers the infrastructure, public relation and travel assistant, legal and trademark servervice,  Project entries the foundation through incubator, there are 60 projects in the incububator. Mentoring is built in incubator. 

### Linux Foundation
It mainly acts as umbrella for a number of smaller foundations, where inner organizations generally work in a stand-alone way (e.g., *OpenAPI initiative* or *Kubernetes*)

### CNCF - Cloud Native Computing Foundation
It is part of Linux Foundation, its mission is to make cloud native computing ubiquitous

### GNOME

### Eclipse

### Python Software Foundation

### Plone Foundation

### OSI

### FSF



## Open Source Tips
This session contains some common DOs and Don'ts for Open Source software, these tips help the newcomers to avoid the pitfalls of Open Source development and learn from the community's collective wisdom. 

### Start OSS Project with the following steps: 

* Start every project with at least a `README.md`, which includes project description & quickstart guide
* Use syntax hightlighting in documentation
* Add `CONTRIBUTING.md` in the `.github` folder of your project root direcotry, which succinctly communicates the maintainer's guidelines, examples such as (puppet project's contributor guide)[https://github.com/puppetlabs/.github/blob/main/CONTRIBUTING.md]
* Add `CODE_OF_CONDUCT.md` in the root of your project to ensure a safe diverse & inclusive, examples such as (puppet project's CODE Of Conduct)[https://github.com/puppetlabs/puppet/blob/main/CODE_OF_CONDUCT.md]
* Add GitHub Issue & Pull Request templates namely `ISSUE_TEMPLATE.md` in the `.github` folder of your project root directory, which helps keeping the project consistent & reminds 
* Chose a license, GT OSPO creates a flowchart on helping you identify an approriate license at (here)[https://ospo.cc.gatech.edu/open-source-software-licensing/], you can find more useful guidance at (here)[https://choosealicense.com/]

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



## Successful OSS Projects

### Linux

### emacs/vim

### Python

### rust

### LLVM

### neovim

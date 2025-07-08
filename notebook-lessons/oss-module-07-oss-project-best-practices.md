# OSS Project Best Practices

## Goals

In this lesson, attendees will learn the following:
* Tips for a successful open source project
* Lessons learned from long-term successful projects

## Sources
* Eddie Jaoude - [Open Source Tips ](https://eddiejaoude.github.io/book-open-source-tips/), 2025
* [Open Source Project Maturity Model](https://www.usdigitalresponse.org/resources/cms-open-source-software)
* [Schmidt Academy for Software Engineering](https://sase.caltech.edu/resources/index.html)- provides best practices for software engineering in OSS.
* [Linux Professional Institution Open Source Essential Training Material](https://learning.lpi.org/en/learning-materials/050-100/)


             
## Open Source Tips
This session contains some common DOs and Don'ts for Open Source software, these tips help the newcomers to avoid the pitfalls of Open Source development and learn from the community's collective wisdom. 

### Start your OSS Project:

These tips can be important to make your project welcoming for new users and potential contributors.

* Use [git](https://swcarpentry.github.io/git-novice/) or a similar revision control system (RCS) to maintain the project's history  
* Start every project with at least a `README.md`, which includes project description & quickstart guide
* Use syntax highlighting in documentation as well as [MarkDown Alerts](https://github.blog/changelog/2023-12-14-new-markdown-extension-alerts-provide-distinctive-styling-for-significant-content/) to call out important information.
* Add `CONTRIBUTING.md` in the `.github` folder of your project root directory, which succinctly communicates the maintainer's guidelines, examples such as [puppet project's contributor guide](https://github.com/puppetlabs/.github/blob/main/CONTRIBUTING.md)
* Add `CODE_OF_CONDUCT.md` in the root of your project to ensure a safe diverse & inclusive, examples such as [puppet project's CODE Of Conduct](https://github.com/puppetlabs/puppet/blob/main/CODE_OF_CONDUCT.md)
* Add GitHub Issue & Pull Request templates (e.g., `ISSUE_TEMPLATE.md`) in the `.github` folder of your project root directory, which helps keeping the project consistent & reminds 
* Choose a license! The OSPO has a flowchart on helping you identify an appropriate license at [here](https://ospo.cc.gatech.edu/open-source-software-licensing/) and this brief recommendation page](). 
    * You can find more useful guidance on different types of licenses [here](https://choosealicense.com/)
* Add a .gitignore file at the root of repository to avoid checking in non-source code files, e.g. `__py_cache__` and `.DS_Store`

### Contribute to OSS projects
* Make Git commits small and atomic.
    * Limit commit message subject line to ~$50$ characters and put longer descriptions in the message body.
    * Use the body to explain *why* not *how*
* Keep GitHub Issues and Tasks small; you can add a sub task checklist using open brackets. 
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
* Use Branching to work with a wider team, project main branch (`main` or `develop`), everything must go via a feature branch and a Pull Request
* Ensure the clean code style and variable and method names [link](https://www.freecodecamp.org/news/the-junior-developers-guide-to-writing-super-clean-and-readable-code-cd2568e08aae/), and best practices for Coding, Organization, and Documentation [link](https://mitcommlab.mit.edu/broad/commkit/best-practices-for-coding-organization-and-documentation/)
* Keep documenting the important decisions about how the software is constructed, [best practice on documenting project](https://helpjuice.com/blog/software-documentation)


### Tips on what *Not* to do with your open source project to avoid

* Large Commits and Pull Requests - As mentioned in the code review lesson, smaller commits reduce errors and allow for better code review dialog.
* Set It and Forget It - If you are actively seeking contributors to a project you maintain, you need to be engaged with the issue and pull request process.
* Not Investing in Automation - We don't necessarily mean using AI here! It's important to automate common tasks like issue generation, pull requests, and testing of your code via CI/CD pipelines. Make it easy for others to contribute and for you to accept new code.
* Ignoring your own Code of Conduct - Maintaining an OSS project requires treating users and contributors with respect. Set a code of conduct and make sure to lead by example. Define clear rules on commits, discussion, and community engagement so there is no ambiguity in how others interact with your project.  


## Open Source Project Maturity Model

The [Open Source Repository Maturity Model](https://github.com/dsacms/repo-scaffolder/blob/main/maturity-model-tiers.md) from the Digital Services Administration at the Centers for Medicare and Medicaid Services (DSACMS) presents a framework that determines what and how much documentation is needed based on the project's size, community involvement, and goals.

The framework consists of five tiers (0-4), each representing different stages of a projects maturity:
* [Tier 0](https://github.com/DSACMS/repo-scaffolder/blob/main/tier0/README.md) includes experimental private repositories usually with single developer
* [Tier 1](https://github.com/DSACMS/repo-scaffolder/blob/main/tier1/README.md) includes an informational or historical project that has been released publicly once, without any planned future updates. Main purpose of a Tier 1 project is to share knowledge.
* [Tier 2](https://github.com/DSACMS/repo-scaffolder/blob/main/tier2/README.md) is a collaborative project within a team, which is not meant for broad public contribution but rather for internal collaboration. E.g. 
* [Tier 3](https://github.com/DSACMS/repo-scaffolder/blob/main/tier3/README.md) is an open collaboration effort with limited external contributions. Although it is open source, the direction and maintenance are still controlled by a smaller group or team.
* [Tier 4](https://github.com/DSACMS/repo-scaffolder/blob/main/tier4/README.md) is a fully open and collaborative project that operates under a community governance model. The governance structure is open to a broad community

There is also a commandline tool which can guide users through a series of questions and recommends the appropriate templates should be used based on the tiers - [CookieCutter](https://github.com/DSACMS/repo-scaffolder?tab=readme-ov-file#need-help-picking-a-tier)

## Open Source Project template
Here you can find [template files](https://github.com/DSACMS/repo-scaffolder/tree/main/tier4/%7B%7Bcookiecutter.project_slug%7D%7D) you can use for your project.  

## Successful OSS Projects

There are many successful open source projects, which we can use as a resource for best practices. 

### Linux

Linux is a GNU General Public License version 2 (GPLv2) project that has a strong track record of community-driven development:

- Structure of the Linux Community, with trusted maintainers responsible for specific subsystems and approves the patches; thousands of developer worldwide from individuals to employees of companies like Intel, Red Hat, Google and IBM
- Well defined development process, developers submit patches via Linux Kernel Mailing List (LKML); Maintainer review patches for qualify, style and correctness through automated tools and CI system test patches; Merging into maintainer trees first and eventually to Linus Torvalds's mainline tree and Release Cycle roughly every 9-10 weeks
- Tools and Platforms used, Linux was the reason Git was created; use LKML for discussion and patch submission; use Bugzilla, KernelCI, Patchwork for bug tracking, testing and patch management
- Community and Governance, influence is earned through quality contributions; ensures respectful collaboration through Code of Conduct; Encourages mentorship, documentation and open discussion
- Corporate involvement, companies contribute to Linux to ensure it supports their hardware/software; the Linux Foundation supports the ecosystem with funding, training and events 

### [emacs/vim](https://github.com/emacs-mirror/emacs)

- Development Workflow, contributor submits the patches via email to emacs-devel mailing list or through Savannah - the GNU project's hosting platform; patches are reviewed by maintainers and other contributors; contributors are expected to write tests for new features and bug fixes to add to build-in test suite for testing; Merge and Release Cycle follows a major release every 1-2 years.
- Package Ecosystem, supports third-party packages via package managers like MELPA(community-driven), ELPA(official GNU repository)
- Tools and Infrastructure, use Git for version control; Bug Tracker is hosted on Debbugs (GNU's bug tracking system); uses mailing list for primary communication channel; documentation is maintained alongside with code, often updated with each patch
- Community and Culture, has strong culture of learning, mentorship and documentation; the community values code clarity, backward compatibility and user freedom. 

### [LLVM](https://github.com/llvm/llvm-project)

LLVM (originally "Low-Level Virtual Machine") is a modular, open-source compiler infrastructure used to build compilers and toolchains. 

- LLVM Core is an umbrella project, which contains LLVM Core (intermediate representation, optimizer, and code generator), Clang (A frontend for C, C++ and Objective C), LLD (linker), libc++ (the C++ standard library), e.t.c.
- LLVM Foundation oversees the project and ensures its sustainability; Maintainers are responsible for specific components; Contributors include individuals and companies like Apple, Google, Intel, AMD and Meta
- Code contribution are submitted via GitHub pull requests or Phabricator (legacy), code reviews are mandatory and often involve detailed discussions; has a comprehensive test suite; with major releases every 6 months
- Use mailing lists for discussions and announcements; Use discord and meetups for real-time collaboration; use GitHub for bug tracker; Maintain the extensive and well maintained documentation, including tutorials and design docs. 

### Python

The development of the Python programming language is a structured, community-driven process that balances openness with careful governance. 

- Governance and Leadership, a group of five core developers elected annually forms **Python Steering Council**, who make final decisions on language changes and project direction
    - **Python Software Foundation (PSF)** manages the intellectual property and supports community, but does not control development decisions
- Contribution team includes Core Developers with commit access to the main repository and Community Contributors who can propose changes, report bugs or submit patches via GitHub, and discussions on mailing lists or discord
- Python Enhancement Proposals (PEP) are formal documents that describe new features, implementation details, or changes to the language
- Development workflow includes proposal, discussion, review, testing, merge and release. Python follows a 12-month release cycle for major versions through Alpha, Beta, Release Candidate (RC) and Final Release Cycles
- Python uses automated CI/CD pipelines (e.g. Github Actions) to test across platforms; Tools like pytest, unittest, and coverage.py are commonly used
- Vast ecosystem of libraries, Python Package Index (PyPI) hosts over 400,000 packages
- Conferences like PyCon and EuroPython foster collaboration and learning.
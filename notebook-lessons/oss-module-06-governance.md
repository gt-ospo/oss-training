# Module 6: Governance

## Sources
* John Metric. [_Open Source Projects - Beyond Code_](https://learning.oreilly.com/library/view/open-source-projects/9781837636884/). O`Reilly Media, 2023.  Metric is the current director of program management for The Linux Foundation.
* Dave Neary, Josh Berkus, Katrina Novakovic, Bryan Behranshausen.  ["Understanding open source governance models"](https://www.redhat.com/en/blog/understanding-open-source-governance-models), Red Hat Blog, 2020.  Authors are from Red Hat's Open Source Programming Office.
* Ross Gardler and Gabriel Hanganu. ["Governance Models"](http://oss-watch.ac.uk/resources/governancemodels).  OSS Watch, 2013.  Gardler is the former President of the Apache Foundation.

## What is open source governance?

*Governance* describes the decision-making that an open source projects need to function. This is how policies and processes are defined.  Some examples of policies are:

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
 
There is no one-size-fits-all solution

## Models of Governance

Models of governance differ primarily on:
* Who gets to make decisions
* How decisions get made

## Cathedral vs. Bazaar

An older model, first described in Linux community around 1999.  Describes both **governance** (who gets to make decisions) and **contribution** (who gets to add new code).

![chapel_and_bazaar](http://oss-watch.ac.uk/img/governancevcontrib.png)

* Two extremes of **governance**:
  - Benevolent Dictator: Single individual or organization makes policy decisions
  - Meritocracy: Ability to make decisions is given to significant contributors
* Two extremes of **contribution**:
  - Bazaar: Project accepts code from many external developers
  - Cathedral: Project has a group of core developers

## Five Recent Models

Many recent OSS advocates describe 5 models:

1. Do-ocracy (a.k.a Meritocracy)
2. Founder-leader (a.k.a, Benevolent Dictator for Life, )
3. Technical council
4. Electoral
5. Vendor-backed
6. Foundation-backed

### 1. Do-ocracy

* The people doing the work are the ones making decisions
  - Often no formal governance.  Just implicit governance in group's interactions
  - Usually still have contribution guidelines (peer review of code, etc.)
* Pros
  - Easy for small teams with few stakeholders
* Cons
  - Decision-making usually does not scale with more contributors and stakeholders
  - Can be difficult for newcomers to integrate with the project
* I couldn't find an example of a large successful project that does this

### 2. Founder-leader (BDFL)

* One person (or a small group) who started the project is the ultimate decision-maker
* Leader determines projects priorities and vision, settles disputes among other
    contributors, and decides which contributions are merged

#### Examples
* Linux and Linus Torvalds
* Python and Guido van Rossum : a BDFL early-on, and van Rossum is still "honorary" BDFL.
  But now has foundation-backed governance

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


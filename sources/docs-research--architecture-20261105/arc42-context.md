# Architecture documentation evidence: arc42-context

Source: https://docs.arc42.org/section-3/
Resolved URL: https://docs.arc42.org/section-3/
Retrieved: 2026-11-05
Extraction: HTML main-content text; link targets, diagram content and code indentation may be lost

On this page
#
3. Context and Scope
##
Content
System scope and context - as the name suggests - delimits your system (i.e. your scope) from all its communication partners (neighboring systems and users, i.e. the context of your system). It thereby specifies the external interfaces.
If necessary, differentiate the business context (domain specific inputs and outputs) from the technical context (channels, protocols, hardware).
##
Motivation
The domain interfaces and technical interfaces to communication partners are among
your system’s most critical aspects. Make sure that you completely understand them.
##
Form
Various context diagrams
Lists of communication partners and their interfaces.
##
Examples
See below, separated into business- and technical context.
##
3.1 Business context
###
Content
Specification of
all
communication partners (users, IT-systems, …) with explanations of domain specific inputs and outputs or interfaces. 
Optionally you can add domain specific formats or communication protocols.
###
Motivation
All stakeholders should understand which data are exchanged with the environment of the system.
###
Form
All kinds of diagrams that show the system as a black box and specify the domain interfaces to communiations partners.
Alternatively (or additionally) you can use a table. The title of the table is the name of your system, the three columns contain the name of the communication partner, the inputs, and the outputs.
###
Examples
:Example Business Context: HTML Sanity Checker
:Example Business Context: MaMa
:Example Business Context: TrafficPursuitUnit
:Example Business Context: status.arc42.org
Want to see this section inside a whole document?
Read
the context and scope of real systems
at examples.arc42.org.
###
<insert diagram or table>
###
<(optionally:) insert explanation of external domain interfaces>
##
3.2 Technical context
###
Contents
Technical interfaces (channels and transmission media) linking your system to its environment. 
In addition a mapping of domain specific input/output to the channels, i.e. an explanation with I/O uses which channel.
###
Motivation
Many stakeholders make architectural decision based on the technical interfaces between the system and its context. Especially infrastructure or hardware designers decide these technical interfaces.
###
Form
E.g. UML deployment diagram describing channels to neighboring systems, together with a mapping table showing the relationships between channels and input/output.
###
Examples
:Example Technical Context: HTML Sanity Checker
:Example Technical Context: TrafficPursuitUnit
###
<insert diagram or table>
###
<(optionally:) insert explanation of technical interfaces>
###
<insert mapping of input/output to channels>
##
Practical Tips
Tip 3-1: Explicitly demarcate your system from its environment!
#context
#external-interface
Tip 3-2: Show the context as diagram!
#context
#external-interface
#essential
Tip 3-3: Combine the context diagram with a table!
#context
#essential
Tip 3-4: Explicitly indicate risks in the context!
#context
#risk
Tip 3-5: Restrict the context to an overview, avoid too many details!
#context
#essential
#lean
Tip 3-6: Simplify the context by categorization!
#context
#external-interface
#lean
Tip 3-7:  If many external systems are involved, aggregate (cluster) them by explicit criteria!
#context
#cluster
#criteria
Tip 3-8: Aggregate (cluster) similar neighbour systems with ports!
#context
#port
Tip 3-9: Show all (all!) external interfaces!
#context
#external-interface
#essential
Tip 3-10: Differentiate business and technical context!
#context
#technical-context
#business-context
Tip 3-11: In the business context, show data flows (instead of dependencies)!
#context
#business-context
Tip 3-12: Show external influences in the context!
#context
Tip 3-13: Show transitive dependencies in the context!
#context
Tip 3-14: Pay attention to quality requirements at external interfaces!
#context
#quality-goal
#external-interface
Tip 3-15: Show the technical context (in case hardware is central to your system)!
#context
#technical-context
Tip 3-16: Use the technical context to describe protocols or channels!
#context
#thorough
#technical-context
Tip 3-17: Combine business context with technical information!
#context
#technical-context
#business-context
#infrastructure
#lean
Tip 3-18: Explain the relationship between domain interfaces and their technical realization!
#context
#interface
Tip 3-19: Defer technical context to the deployment view!
#context
#technical-context
#deployment-view
#lean
###
Related Questions
See
here for questions related to context, scope and external interfaces
.
###
Complete Examples
See
the context and scope of real systems
, documented in full at examples.arc42.org.
####
Prefer to learn arc42 hands-on?
Practical architecture training, most classes taught by Peter Hruschka
        and Gernot Starke — the people who created arc42 and maintain this free
        reference (dates with other trainers say so) — and solid preparation for
iSAQB
certifications.
Next dates
24–26 Nov 2026
DE
IMPROVE
· Hamburg
waitlist
evolve and maintain systems · with Carola Lilienthal & Gernot Starke
1–4 Dec 2026
DE
MSA
· München
waitlist
perfect preparation for iSAQB CPSA-Foundation certification
23–25 Feb 2027
EN
MSA
· online
perfect preparation for iSAQB CPSA-Foundation certification · with Wolfgang Reimesch
2–5 Mar 2027
DE
MSA
· München
perfect preparation for iSAQB CPSA-Foundation certification
9–11 Mar 2027
DE
Req4Arc
· München
getting your requirements right
13–15 Apr 2027
EN
IMPROVE
· online
evolve and maintain systems · with Wolfgang Reimesch
2–3 Jun 2027
DE
ADOC
· Mannheim
architecture documentation · with Dr. Gernot Starke
8–11 Jun 2027
DE
MSA
· Mannheim
perfect preparation for iSAQB CPSA-Foundation certification
All courses and dates:
trainings.arc42.org
· as of 20 Oct 2026

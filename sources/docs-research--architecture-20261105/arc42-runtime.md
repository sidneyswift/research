# Architecture documentation evidence: arc42-runtime

Source: https://docs.arc42.org/section-6/
Resolved URL: https://docs.arc42.org/section-6/
Retrieved: 2026-11-05
Extraction: HTML main-content text; link targets, diagram content and code indentation may be lost

On this page
#
6. Runtime View
##
Content
The runtime view describes concrete behavior and interactions of the system’s building blocks in form of scenarios from the following areas:
important use cases or features: how do building blocks execute them?
interactions at critical external interfaces: how do building blocks cooperate with users and neighbouring systems?
operation and administration: launch, start-up, stop
error and exception scenarios
Remark: The main criterion for the choice of possible scenarios (sequences, workflows) is their
architectural relevancy
. It is
not
important to describe a large number of scenarios. You should rather document a representative selection.
##
Motivation
You should understand how (instances of) building blocks of your system perform their job and communicate at runtime.
You will mainly capture scenarios in your documentation to communicate your architecture to stakeholders that are less willing or able to read and understand the static models (building block view, deployment view).
##
Form
There are many notations for describing scenarios, e.g.
numbered list of steps (in natural language)
activity diagrams or flow charts
sequence diagrams
BPMN or EPCs (event process chains)
state machines
…
###
Examples
:Example Runtime View: HTML Sanity Checker
:Example Runtime View: MaMa
:Example Runtime View: TrafficPursuitUnit
Want to see this section inside a whole document?
Read
the runtime view of real systems
at examples.arc42.org.
###
6.1
<Runtime Scenario 1>
< insert runtime diagram or textual description of the scenario>
< insert description of the notable aspects of the interactions between the
building block instances depicted in this diagram. >
###
6.2
<Runtime Scenario 2>
###
…
###
6.n
<Runtime Scenario n>
##
Practical Tips
Tip 6-1: Always map existing building blocks to the activities within runtime scenarios!
#scenario
#runtime-view
#essential
#runtime-scenario
Tip 6-2: Document only a few runtime scenarios!
#scenario
#runtime-view
#lean
#essential
#runtime-scenario
Tip 6-3: Document 'schematic' (instead of detailed) scenarios!
#scenario
#runtime-view
#lean
#runtime-scenario
Tip 6-4: Document detailed scenarios (with caution)!
#scenario
#runtime-view
#thorough
#runtime-scenario
Tip 6-5: Use scenarios primarily to `discover` building blocks, not so much for documentation!
#runtime-view
#scenario
Tip 6-6: Describe excerpts of scenarios (partial scenarios)!
#runtime-view
#scenario
#sequence-diagram
Tip 6-7: Use activity diagrams with swimlanes to describe or specify runtime scenarios!
#runtime-view
#scenario
#activity-diagram
Tip 6-8: Use activity diagrams with partitions to describe or specify runtime scenarios!
#runtime-view
#scenario
#activity-diagram
Tip 6-9: Use a textual notation to describe runtime scenarios!
#runtime-view
#scenario
#lean
Tip 6-10: Use both small and large building blocks in scenarios!
#runtime-view
#scenario
#building-block
#lean
Tip 6-11: Use sequence diagrams to describe or specify runtime scenarios!
#runtime-view
#scenario
#sequence-diagram
###
Related Questions
See
here for questions related to runtime scenarios
.
###
Complete Examples
See
the runtime view of real systems
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

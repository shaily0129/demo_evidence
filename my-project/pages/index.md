---
title: Welcome to API Services
---

<Details title='Intro '>
  A service that facilitates uniform interaction for users with agents and LLMS across the real estate sector.

</Details>

<Details title='Services '>
<Accordion>
  <AccordionItem title="Content Service">

This service fetchs documents by entering user ID. When user request documents, it sends back a list of pages from a specific document called [Prolonged_Casualty_Care_Guidelines](/static/21-12_JTS_Prolonged_Casualty_Care_Guidelines.pdf)

Each page has a link that you can click to view it. This helps to easily access important documents you need, making it straightforward to find and use information in the real estate field.

  </AccordionItem>
  <AccordionItem title="Rating Service">

This service allows users to rate their service experience. By sending a request with their user ID, rating, and comment, users can provide feedback.
    
This confirms receipt with a <b>message</b> including the date and time of the rating.

  </AccordionItem>
  <AccordionItem title="Agent Interaction">


    This service allows users to submit messages or questions, which are then classified into different categories such as <b>"triage"</b> for medical emergencies, <b>"evacuation planning"</b> for disaster scenarios, <b>"greetings"</b> for social interactions, and <b>"other"</b> for general queries.

Depending on the category, messages classified under `greetings` or `other` are handled by a generic agent utilizing _LLM_ tools to provide knowledge-based or generic responses. For messages related to `evacuation plans` or `medical` issues, they are routed to a Prediction Guard agent. This agent accesses data from a _RAG_(Retrieve, Augment, Generate) model that has pre-fetched knowledge. It offers detailed steps and even provides the relevant page numbers from the casualty care guideline PDF, ensuring users receive accurate and actionable information in critical situations.

  </AccordionItem>


  <AccordionItem title="Holiday Booking Service">

This service helps to book a holiday by entering age, name, and country under a unique request id. If you're aged 50 or older, you can also specify your insurance preference. After you submit these details, it confirms your booking and provides a unique <b>booking ID</b> for your holiday reservation.

  </AccordionItem>

</Accordion>
</Details>

<Details title='Apps'>

- Mission Final Asset

- Mission Final CF

- Mission Options Asset

- Mission Options CF

- Patient Matrix

- Triage Category 

- Triage Score


</Details>

<Details title='References '>

- [Github](https://github.com/SimWerx/gt-demo-interaction)

- [GT Agent Services](http://100.25.26.186:8003/docs)

- [GT Service Tools Demo](http://100.25.26.186:8002/docs)

- [GT Service Status Page](http://35.153.66.97:8500/status/gt)

</Details>

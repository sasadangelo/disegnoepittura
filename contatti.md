---
title: "Contatti"
date: 2009-01-12 12:29:37
categories: []
tags: []
layout: single
---

Se desideri contattarmi puoi inviare un messaggio tramite il seguente modulo. Considera che, generalmente, leggo tutti i messaggi inviati tramite questa pagina web e, se possibile, cerco di rispondere nel giro di 24 ore. Potrebbe accadere, però, che per problemi personali, per impegni o per altri motivi la mia risposta possa arrivare un po’ in ritardo. In tali casi chiedo solo di pazientare un po’ perché, nel limite delle mie possibilità, cerco sempre di rispondere a tutti.

<form action="https://formspree.io/f/mregbqae" method="POST">
  <input type="text" name="name" size="38" placeholder="Your Name" required=""/>
  <input type="email" name="email" size="38" placeholder="Your email (email@domain.tld)" required=""/>
  <input type="text" name="subject" size="38" placeholder="Subject" required=""/>
  <textarea name="message" rows="10" cols="30" placeholder="Your Message"></textarea>
  <input type="hidden" name="_next" value="{{ site.url }}{{ site.baseurl }}/contacts/">
  <input type="hidden" name="_subject" value="Disegno & Pittura Contact Form Submission">
  <br/>
  <button type="submit">Invia</button>
  <br/>
</form>

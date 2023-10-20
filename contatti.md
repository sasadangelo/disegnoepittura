---
layout: page
title: Contatti
slug: contatti
excerpt: Se desideri contattarmi puoi inviare un messaggio tramite il seguente modulo. Considera che, generalmente, leggo tutti i messaggi inviati tramite questa pagina.
javascript_urls:
- https://www.google.com/recaptcha/api.js?hl=it
---
# Contatti

Se desideri contattarmi puoi inviare un messaggio tramite il seguente modulo. Considera che, generalmente, leggo tutti i messaggi inviati tramite questa pagina web e, se possibile, cerco di rispondere nel giro di 24 ore. Potrebbe accadere, però, che per problemi personali, per impegni o per altri motivi la mia risposta possa arrivare un po’ in ritardo. In tali casi chiedo solo di pazientare un po’ perché, nel limite delle mie possibilità, cerco sempre di rispondere a tutti.

<form class="contact-form" action="https://formspree.io/f/mvongqkp" method="POST">
  <div class="contact-form-item">
  <input type="text" name="name" size="38" placeholder="Il tuo Nome" required=""/>
  </div>
  <div class="contact-form-item">
  <input type="email" name="email" size="38" placeholder="La tua email (email@domain.tld)" required="">
  </div>
  <div class="contact-form-item">
  <input type="text" name="subject" size="38" placeholder="Soggetto" required="">
  </div>
  <div class="contact-form-item">
  <textarea name="message" rows="10" cols="30" placeholder="Il tuo Messaggio"></textarea>
  </div>
  <input type="hidden" name="_next" value="{{ site.url }}{{ site.baseurl }}/contacts/">
  <input type="hidden" name="_subject" value="Disegno & Pittura Contact Form Submission">
    <!-- your other form fields go here -->
  <div class="g-recaptcha" data-callback='onSubmit' data-sitekey="6LeRCxQkAAAAAJdgsSr0HMPqOXN8aQm-1fGmQ0Q0"></div>
  <br/>
  <div class="contact-form-item">
  <button type="submit">Invia</button>
  </div>
  <br/>
</form>
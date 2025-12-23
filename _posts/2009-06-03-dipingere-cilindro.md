---
title: "Come disegnare e colorare un cilindro con Microsoft Paint"
date: 2009-06-03 07:32:47
categories: ['Pittura']
tags: ['arte digitale', 'chiaroscuro']
layout: single
---

![cilindro](/wp-content/uploads/cylinder9.bmp "cilindro")

Nell’articolo [Come un artista deve usare il chiaroscuro per simulare la percezione del volume](https://www.disegnoepittura.it/percezione-volume/), abbiamo visto come la prospettiva e il chiaroscuro contribuiscono a fornire una percezione del volume. Gli esempi che abbiamo visto sono semplici disegni prospettici o in toni di grigio. La domanda che ci poniamo ora è: cosa succede se l’oggetto da ritrarre è colorato? Per rispondere a questa domanda ho realizzato questo semplice tutorial con Microsoft Paint i cui concetti base, però, valgono per qualsiasi medium sia esso classico (olio, acrilico, matite colorate, ecc.) che digitale (ms paint, gimp, photoshop, ecc.). L’esercizio prevede la colorazione di un cilindro verde. Cominciamo con il disegnare il nostro cilindro.

![disegnare cilindro](/wp-content/uploads/cylinder1.jpg "disegnare cilindro")

Definiamo la posizione della sorgente di luce. Notate sull’elisse superiore come la perpendicolare alla retta che descrive la direzione della luce aiuta ad individuare esattamente dove inizia la zona d’ombra. La zona di massima luce molto stretta sta in un intorno della linea di direzione della luce. La linea che taglia la zona di luce da quella di penombra è esattamente al centro tra queste due linee. Infine, si separi la zona d’ombra da quella più scura. Abbiamo così definito i nostri 5 piani facciali.

![cilindro](/wp-content/uploads/cylinder2.jpg "cilindro")

I pittori Rinascimentali prima di eseguire le loro opere con i colori realizzavano un chiaroscuro del soggetto. Realizziamo il chiaroscuro del nostro cilindro associando a ciascun piano facciale un tono che rimarrà sempre lo stesso nel corso del nostro esercizio. In MS Paint è possibile personalizzare la palette dei colori definendoli sia in formato Red Green Blue (RGB) che Hue Saturation Value (HSV) . In questo esercizio considereremo il modello HSV dove il campo Value rappresenta proprio il tono del colore. I toni scelti sono:

* 195 (corrisponde circa ad un tono 8);
* 158 (tono 6);
* 120 (tono 5);
* 89 (tono 3);
* 69 (tono 2).

In più c’è il tono del lato superiore del cilindro che è una via di mezzo tra il tono della zona in luce e quella in penombra. I campi Hue e Saturation, in questa fase devono rimanere costanti per tutti e 6 i colori. In particolare, Saturation deve essere uguale a 0 (zero) altrimenti non avremo una scala di grigi, bensì una scala monocromatica colorata. Qualiasi valore mettiate per lo Hue MS Paint lo imposta sempre a 160, tanto quando Saturation è uguale a zero il valore di Hue è ininfluente.

![charoscuro](/wp-content/uploads/cylinder3.jpg "chiaroscuro")

A questo punto assegniamo a Hue un valore pari a 80 che corrisponde ad un verde e a Saturation un valore pari a 100, ossia un valore di media saturazione. Definiamo la scala dei nostri 5 colori in cui Hue e Saturation rimangono costanti e varia solo Value (ossia il tono) con i valori descritti sopra. Avremo così i 5 colori:

* Colore max luce=(80, 100, 195)
* Colore luce=(80, 100, 158)
* Colore locale=(80, 100, 120)
* Colore ombra=(80, 100, 89)
* Colore ombra più scura=(80, 100, 69)

Stesso discorso vale per il colore sulla superficie superiore del cilindro. Coloriamo quindi le facce del nostro cilindro utilizzando il tool “Riempi” di **MSPaint**. Il risultato è un cilindro di colore verde le cui variazioni tonali sono analoghi a quelle del cilindro in chiaroscuro visto sopra.

![colore monocromatico](/wp-content/uploads/cylinder4.jpg "colore monocromatico")

Il risultato è sicuramente apprezzabile ma è monocromatico ossia nei colori utilizzati la sola componente a variare è il tono mentre gli altri due rimangono costanti. Per dar maggior vigore al nostro lavoro facciamo qualche piccolo ritocco alla saturazione dei nostri 5 colori tenendo in considerazione il seguente principio:

* La saturazione del colore di un oggetto aumenta nelle aree illuminate e diminuisce in quelle in ombra.

Ecco quindi le variazioni applicate alle nostre 5 tinte:

* Colore max luce=(80, 200, 195)
* Colore luce=(80, 140, 158)
* Colore locale=(80, 100, 120)
* Colore ombra=(80, 80, 89)
* Colore ombra più scura=(80, 60, 69)

Notate come la saturazione (il valore centrale) sia stato aumentato a 200 per il colore di max luce e 140 per quello in luce. Invece, il valore è stato diminuito a 80 e 60 per le zone in ombra. Per la superficie superiore del cilindro un buon valore di saturazione è 120.

![dipingere cilindro](/wp-content/uploads/cylinder6.jpg "dipingere cilindro")

Il colore di un oggetto è influenzato anche dal colore della luce. Sappiamo che le luci possono essere calde (es. lampadine incandescenza o il sole) o fredde (es. neon). Nel primo caso le tinte dell’oggetto subiscono uno shift dello hue verso il giallo nelle aree in luce e verso il blue in quelle in ombra. Il contrario avviene per le luci fredde. Supponendo che il cilindro sia illuminato da una sorgente luminosa calda effettuiamo anche uno shift dello hue dei colori verso il giallo per le aree in luce e verso il blu per le aree in ombra. In termini pratici lo hue va diminuito nelle aree in luce e aumentato in quelle in ombra.

* Colore max luce=(60, 200, 195)
* Colore luce=(70, 140, 158)
* Colore locale=(80, 100, 120)
* Colore ombra=(85, 80, 89)
* Colore ombra più scura=(90, 60, 69)

La superficie superiore del cilindro avrà un valore di hue pari a 75. Rimuoviamo anche le linee di contorno del cilindro e dei piani facciali.

![dipingere cilindro](/wp-content/uploads/cylinder7.jpg "dipingere cilindro")

A questo punto bisogna sfumare i colori dei diversi piani facciali tra loro. Purtroppo, però, MS Paint non ha le funzionalità di sfumatura che possono avere programmi come gimp e photoshop, per cui l’unico modo per sfumare due colori tra loro è quello di utilizzare la tecnica del dithering. Con questa tecnica la sfumatura di due colori avviene distribuendo opportunamente pixel dell’uno e dell’altro colore nella zone di confine in modo tale che l’occhio umano percepisca un passaggio graduale dall’uno all’altro colore. Questa immagine è l’ingrandimento della zona di confine di due piani facciali. Notate come sono stati disposti i pixel.

![dithering](/wp-content/uploads/patterns.jpg "dithering")

Questo è il risultato finale.

![cilindro](/wp-content/uploads/cylinder9.bmp "cilindro")

Fonte: [ispirato al seguente tutorial di pixel-art su deviant art](http://lollige.deviantart.com/art/Pixelart-Noobtorials-73577025)
---
layout: single
title: "Come dipingere il chiaroscuro di un paesaggio con l&#8217;aiuto di Gimp"
date: 2010-11-23 08:00:26
categories: ['Pittura']
tags: ['arte digitale', 'chiaroscuro', 'corso pittura ad olio']
feature_image: "/wp-content/uploads/paesaggio-chiaroscuro-16.PNG"
---

*Questa è la Lezione 12 del *[corso di pittura ad olio per artisti principianti]({{ site.baseurl }}/corso-pittura-olio-artisti-principianti-2/).**

In questa lezione impareremo a riconoscere i toni in un paesaggio in modo da riuscire a dipingerlo in chiaroscuro. Nel precedente articolo abbiamo visto [come eseguire il chiaroscuro]({{ site.baseurl }}/corso-pittura-olio-artisti-principianti-chiaroscuro-forme-geometriche-base/) di alcuni oggetti di base. Ora però è tempo di applicare quei concetti ad un vero paesaggio che, come sappiamo, è il soggetto che sempre utilizzeremo durante questo corso.

Un principiante può prendere spunto per i suoi paesaggi:

1. dal vero;
2. da fotografie.

Nel primo caso sarà necessario recarsi sul posto e dipingere en plein air. Sicuramente un modo di dipingere romantico, suggestivo e avventuroso ma forse poco adatto ad un principiante per diversi motivi:

1. difficoltà nel gestire i materiali;
2. presenza di curiosi che possono disturbare la concentrazione;
3. difficoltà nel gestire i cambi di luce e atmosferici;

Quindi il modo più semplice per un principiante è quello di cominciare dalle fotografie. **Ma come è possibile realizzare il chiaroscuro di un paesaggio partendo da una fotografia?**

Per rispondere a questa domanda partiremo da una foto di un paesaggio e vedremo, con l’ausilio di [Gimp]({{ site.baseurl }}/digital-painting-gimp/), come individuare i diversi toni in esso presenti.

![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro.PNG "Chiaroscuro di un Paesaggio")

Questa sarà la nostro foto di partenza. Nei corsi tradizionali di pittura spesso si consiglia agli studenti di chiudere leggermente gli occhi  così da individuare le principali zone di luce e ombra. Questo è sicuramente un metodo valido anche se molto soggettivo da un punto di vista didattico perchè poi ognuno vede con i propri occhi cose diverse. Vediamo, invece, come  [Gimp]({{ site.baseurl }}/digital-painting-gimp/) può aiutarci a svolgere lo stesso lavoro in maniera meno soggettiva.

![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-1.PNG "Chiaroscuro di un Paesaggio")

Per prima cosa eliminiamo dalla nostro foto tutti i colori convertendola in bianco e nero. In termini tecnici si dice *desaturare la foto* perchè per ogni colore il valore di saturazione viene portato a zero. Aprite la foto con Gimp e cliccate su Colori -> Desaturazione.

![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-2.PNG "Chiaroscuro di un Paesaggio")

Apparirà un dialog box con tre radio button. Scegliete il secondo, ossia Luminosità.

![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-3.PNG "Chiaroscuro di un Paesaggio")

A questo punto la foto è bianco e nero e i toni sono più evidenti. Il problema, però, è che il numero dei toni presenti in questa foto è altissimo e non riusciamo a classificarli in una scala più ridotta come quella da 0 a 10 tipica del sistema di munsell. Vedremo ora 3 metodi per riuscire ad individuarli con l’ausilio di Gimp.

1. **Metodo della sfocatura**

   ![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-4.PNG "Chiaroscuro di un Paesaggio")

   Precedentemente ho accennato al tradizionale metodo di chiudere leggermente gli occhi per individuare le principali zone di luce ed ombra. Questo metodo è applicabile digitalmente applicando alla foto il cosiddetto filtro Blur. Per ottenere ciò cliccate su Filtri -> Sfocature -> Gaussiana.

   ![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-5.PNG "Chiaroscuro di un Paesaggio")

   Comparirà una dialog box dove potete regolare il raggio di sfocatura. Praticamente aumentando o diminuendo tali valori equivale a chiudere o aprire maggiormente gli occhi.

   ![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-6.PNG "Chiaroscuro di un Paesaggio")

   Questa è una foto uguale a quella precedente ma più sfocata e dove è più facile individuare i diversi toni. Tuttavia, questo metodo non lo amo molto perchè poi diventa per me difficile e vago riportare tali toni su un quadro vero. Il metodo che preferisco è quello della posterizzazione, ossia la tecnica usata nella Pop Art da Andy Warhol.
2. **Metodo della posterizzazione automatica**

   ![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-7.PNG "Chiaroscuro di un Paesaggio")

   Tutti i programmi di fotoritocco hanno la funzionalità di posterizzazione. Per attivarla in Gimp bisogna cliccare su Colori -> Posterizza. Ovviamente bisogna ripartire dalla foto bianco e nero non sfuocata.

   ![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-8.PNG "Chiaroscuro di un Paesaggio")

   Apparirà un dialog box dove sarà possibile specificare il numero di toni desiderato, in questo caso ho inserito 10.

   ![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-9.PNG "Chiaroscuro di un Paesaggio")

   Questo è il risultato. Rispetto alla tecnica della sfocatura le aree con i toni sono ben delineate. Basterebbe associare a ciascun area un numero di tono e dipingerle su tela così come appaiono (con qualche approssimazione ovviamente). [Poi la fase di sfumatura]({{ site.baseurl }}/corso-pittura-olio-artisti-principianti-chiaroscuro-forme-geometriche-base/) provvederà a creare la transizione dolce da un tono all’altro. Questo metodo, però, seppur molto rapido non sempre mi soddisfa perchè mi da poco controllo sulle diverse aree di tono.

   Ora andrò ad illustrarvi un metodo un pò più lento ma che vi darà maggior controllo sulle diverse aree tonali potendole creare più strette o larghe in base ai vostri gusti.
3. **Metodo della posterizzazione manuale**

   ![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-10.PNG "Chiaroscuro di un Paesaggio")

   Individuate un’area che potrebbe sembrarvi un’area tonale della vostra foto. In questo caso, ad esempio, comincio dalla zona più bianca delle nuvole. Catturo il colore con il Contagocce presente nella barra degli strumenti. Per fare ciò seleziono il Contagocce e clicco sulla zona evidenziata dal cerchio rosso. Il colore di quell’area comparirà nel box del colore di foreground (vedi freccia rossa in basso a destra).

   ![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-11.PNG "Chiaroscuro di un Paesaggio")

   Dalla barra degli strumenti selezioniamo lo strumento di Riempimento del Colore.

   ![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-12.PNG "Chiaroscuro di un Paesaggio")

   Clicchiamo nello stesso punto (approssimativamente) dove avevamo preso il colore con il Contagocce. Noterete che l’area si tingerà dello stesso colore e sarà più ampia e uniforme di quanto lo era in origine. E’ possibile regolare l’estensione di tale area con il valore di Soglia evidenziato dalla freccia rossa nella barra degli strumenti. Maggiore è questo valore e più ampia sarà la zona. Ad esempio, se quel valore è 15 significa che tutti i toni in un intorno di 15 verranno considerati come un medesimo tono.

   ![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-13.PNG "Chiaroscuro di un Paesaggio")

   Ripetiamo il procedimento spostandoci sempre sulla nuvola un pò più a lato rispetto alla nuovo tono che abbiamo creato, creeremo così un nuovo tono contiguo. Ripetiamo il processo per il cielo partendo dal tono più scuro in alto e via via scendendo verso i toni più bassi all’orizzonte. Proseguiamo con le montagne, la spiaggia, ecc. Se un’area tonale non vi soddisfa basterà premeter CTRL-Z per annullarla. Quello che vedete sopra sarà il risultato finale.

![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-14.PNG "Chiaroscuro di un Paesaggio")

Dopo aver individuato nella foto un numero ridotto di toni è necessario associare a ciascuna area, approssimativamente, un numero di tono da 0 a 10 così poi da poterlo trasferire su tela. Per far ciò prendiamo, con il Contagocce, il colore del tono dell’area evidenziata dal cerchio rosso. Fate doppio click sul colore di foreground nella barra degli strumenti evidenziata dalla freccia rossa. Apparirà un dialog box con la rappresentazione HSV e RGB del colore di quell’area. Notate che la saturazione (il valore S nella tripletta HSV) è zero. Il tono, invece, è 56. Approssimiamo questo valore per eccesso (perchè supera 55) e otteniamo 60 su 100 che, riportato su scala decimale diventa circa 6.

![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-15.PNG "Chiaroscuro di un Paesaggio")

Ripetiamo il procedimento per l’area adiacente che avrà tono 47 su 100. Approssimiamo anche qui per eccesso ottenendo 50 su 100. In scala decimale, quindi, il tono sarà circa 5.

![Chiaroscuro di un Paesaggio]({{ site.baseurl }}/wp-content/uploads/paesaggio-chiaroscuro-16.PNG "Chiaroscuro di un Paesaggio")

Ripetiamo il procedimento per le aree principali e otterremo una mappa come quella in figura. Non è necessario trovare i valori dei toni per tutte le aree, bastano quelli principali e poi per comparazione si prepareranno toni più chiari o scuri a seconda delle necessità. Con una mappa di questo tipo basterà ora:

1. [preparare i diversi toni di colore]({{ site.baseurl }}/come-mescolare-colori-realizzare-chiaroscuro/) come abbiamo imparato nelle lezioni precedenti;
2. realizzare il disegno del paesaggio su tela;
3. dipingere i vari toni come avevamo fatto nel tutorial sul [chiaroscuro delle forme geometriche di base]({{ site.baseurl }}/corso-pittura-olio-artisti-principianti-chiaroscuro-forme-geometriche-base/);
4. sfumare tra loro i diversi toni.

*Leggi gli altri  articoli del [corso di pittura ad olio per artisti principianti]({{ site.baseurl }}/corso-pittura-olio-artisti-principianti-2/). Se vuoi puoi ricevere gli aggiornamenti sui futuri articoli del corso iscrivendoti gratuitamente ai [feed RSS](http://feeds2.feedburner.com/DisegnoPittura).*
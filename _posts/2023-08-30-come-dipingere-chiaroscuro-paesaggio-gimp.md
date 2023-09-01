---
layout: post
title: "Come dipingere il chiaroscuro di un paesaggio con l'aiuto di Gimp"
published: true
author: sasadangelo
comments: true
date: 2010-11-23 08:11:26
tags:
    - arte digitale
    - chiaroscuro
    - corso pittura ad olio
categories:
    - pittura
permalink: /come-dipingere-chiaroscuro-paesaggio-gimp
---


_Questa è la Lezione 12 del _[corso di pittura ad olio per artisti principianti][1].__ 


  In questa lezione impareremo a riconoscere i toni in un paesaggio in modo da riuscire a dipingerlo in chiaroscuro. Nel precedente articolo abbiamo visto come eseguire il chiaroscuro di alcuni oggetti di base. Ora però è tempo di applicare quei concetti ad un vero paesaggio che, come sappiamo, è il soggetto che sempre utilizzeremo durante questo corso.


Un principiante può prendere spunto per i suoi paesaggi:

  1. dal vero;
  2. da fotografie.


  Nel primo caso sarà necessario recarsi sul posto e dipingere en plein air. Sicuramente un modo di dipingere romantico, suggestivo e avventuroso ma forse poco adatto ad un principiante per diversi motivi:



  
    difficoltà nel gestire i materiali;
  
  
    presenza di curiosi che possono disturbare la concentrazione;
  
  
    difficoltà nel gestire i cambi di luce e atmosferici;
  



  Quindi il modo più semplice per un principiante è quello di cominciare dalle fotografie. Ma come è possibile realizzare il chiaroscuro di un paesaggio partendo da una fotografia?



  Per rispondere a questa domanda partiremo da una foto di un paesaggio e vedremo, con l&#8217;ausilio di Gimp, come individuare i diversi toni in esso presenti.



  



  Questa sarà la nostro foto di partenza. Nei corsi tradizionali di pittura spesso si consiglia agli studenti di chiudere leggermente gli occhi  così da individuare le principali zone di luce e ombra. Questo è sicuramente un metodo valido anche se molto soggettivo da un punto di vista didattico perchè poi ognuno vede con i propri occhi cose diverse. Vediamo, invece, come  Gimp può aiutarci a svolgere lo stesso lavoro in maniera meno soggettiva.



  



  Per prima cosa eliminiamo dalla nostro foto tutti i colori convertendola in bianco e nero. In termini tecnici si dice desaturare la foto perchè per ogni colore il valore di saturazione viene portato a zero. Aprite la foto con Gimp e cliccate su Colori -> Desaturazione.



  



  Apparirà un dialog box con tre radio button. Scegliete il secondo, ossia Luminosità.



  



  A questo punto la foto è bianco e nero e i toni sono più evidenti. Il problema, però, è che il numero dei toni presenti in questa foto è altissimo e non riusciamo a classificarli in una scala più ridotta come quella da 0 a 10 tipica del sistema di munsell. Vedremo ora 3 metodi per riuscire ad individuarli con l&#8217;ausilio di Gimp.


  1. **Metodo della sfocatura** 
      
    
    
    
      Precedentemente ho accennato al tradizionale metodo di chiudere leggermente gli occhi per individuare le principali zone di luce ed ombra. Questo metodo è applicabile digitalmente applicando alla foto il cosiddetto filtro Blur. Per ottenere ciò cliccate su Filtri -> Sfocature -> Gaussiana.
    
    
    
      
    
    
    
      Comparirà una dialog box dove potete regolare il raggio di sfocatura. Praticamente aumentando o diminuendo tali valori equivale a chiudere o aprire maggiormente gli occhi.
    
    
    
      
    
    
    
      Questa è una foto uguale a quella precedente ma più sfocata e dove è più facile individuare i diversi toni. Tuttavia, questo metodo non lo amo molto perchè poi diventa per me difficile e vago riportare tali toni su un quadro vero. Il metodo che preferisco è quello della posterizzazione, ossia la tecnica usata nella Pop Art da Andy Warhol.
    

  2. **Metodo della posterizzazione automatica** 
      
    
    
    
      Tutti i programmi di fotoritocco hanno la funzionalità di posterizzazione. Per attivarla in Gimp bisogna cliccare su Colori -> Posterizza. Ovviamente bisogna ripartire dalla foto bianco e nero non sfuocata.
    
    
    
      
    
    
    
      Apparirà un dialog box dove sarà possibile specificare il numero di toni desiderato, in questo caso ho inserito 10.
    
    
    
      
    
    
    
      Questo è il risultato. Rispetto alla tecnica della sfocatura le aree con i toni sono ben delineate. Basterebbe associare a ciascun area un numero di tono e dipingerle su tela così come appaiono (con qualche approssimazione ovviamente). Poi la fase di sfumatura provvederà a creare la transizione dolce da un tono all&#8217;altro. Questo metodo, però, seppur molto rapido non sempre mi soddisfa perchè mi da poco controllo sulle diverse aree di tono.
    
    
    
      Ora andrò ad illustrarvi un metodo un pò più lento ma che vi darà maggior controllo sulle diverse aree tonali potendole creare più strette o larghe in base ai vostri gusti.
    

  3. **Metodo della posterizzazione manuale** 
      
    
    
    
      Individuate un&#8217;area che potrebbe sembrarvi un&#8217;area tonale della vostra foto. In questo caso, ad esempio, comincio dalla zona più bianca delle nuvole. Catturo il colore con il Contagocce presente nella barra degli strumenti. Per fare ciò seleziono il Contagocce e clicco sulla zona evidenziata dal cerchio rosso. Il colore di quell&#8217;area comparirà nel box del colore di foreground (vedi freccia rossa in basso a destra).
    
    
    
      
    
    
    
      Dalla barra degli strumenti selezioniamo lo strumento di Riempimento del Colore.
    
    
    
      
    
    
    
      Clicchiamo nello stesso punto (approssimativamente) dove avevamo preso il colore con il Contagocce. Noterete che l&#8217;area si tingerà dello stesso colore e sarà più ampia e uniforme di quanto lo era in origine. E&#8217; possibile regolare l&#8217;estensione di tale area con il valore di Soglia evidenziato dalla freccia rossa nella barra degli strumenti. Maggiore è questo valore e più ampia sarà la zona. Ad esempio, se quel valore è 15 significa che tutti i toni in un intorno di 15 verranno considerati come un medesimo tono.
    
    
    
      
    
    
    
      Ripetiamo il procedimento spostandoci sempre sulla nuvola un pò più a lato rispetto alla nuovo tono che abbiamo creato, creeremo così un nuovo tono contiguo. Ripetiamo il processo per il cielo partendo dal tono più scuro in alto e via via scendendo verso i toni più bassi all&#8217;orizzonte. Proseguiamo con le montagne, la spiaggia, ecc. Se un&#8217;area tonale non vi soddisfa basterà premeter CTRL-Z per annullarla. Quello che vedete sopra sarà il risultato finale.
    


  



  Dopo aver individuato nella foto un numero ridotto di toni è necessario associare a ciascuna area, approssimativamente, un numero di tono da 0 a 10 così poi da poterlo trasferire su tela. Per far ciò prendiamo, con il Contagocce, il colore del tono dell&#8217;area evidenziata dal cerchio rosso. Fate doppio click sul colore di foreground nella barra degli strumenti evidenziata dalla freccia rossa. Apparirà un dialog box con la rappresentazione HSV e RGB del colore di quell&#8217;area. Notate che la saturazione (il valore S nella tripletta HSV) è zero. Il tono, invece, è 56. Approssimiamo questo valore per eccesso (perchè supera 55) e otteniamo 60 su 100 che, riportato su scala decimale diventa circa 6.



  



  Ripetiamo il procedimento per l&#8217;area adiacente che avrà tono 47 su 100. Approssimiamo anche qui per eccesso ottenendo 50 su 100. In scala decimale, quindi, il tono sarà circa 5.



  



  Ripetiamo il procedimento per le aree principali e otterremo una mappa come quella in figura. Non è necessario trovare i valori dei toni per tutte le aree, bastano quelli principali e poi per comparazione si prepareranno toni più chiari o scuri a seconda delle necessità. Con una mappa di questo tipo basterà ora:


  1. [preparare i diversi toni di colore][2] come abbiamo imparato nelle lezioni precedenti;
  2. realizzare il disegno del paesaggio su tela;
  3. dipingere i vari toni come avevamo fatto nel tutorial sul [chiaroscuro delle forme geometriche di base][3];
  4. sfumare tra loro i diversi toni.


  Leggi gli altri  articoli del corso di pittura ad olio per artisti principianti. Se vuoi puoi ricevere gli aggiornamenti sui futuri articoli del corso iscrivendoti gratuitamente ai feed RSS.


 [1]: https://www.disegnoepittura.it/corso-pittura-olio-artisti-principianti-2/
 [2]: https://www.disegnoepittura.it/come-mescolare-colori-realizzare-chiaroscuro/
 [3]: https://www.disegnoepittura.it/corso-pittura-olio-artisti-principianti-chiaroscuro-forme-geometriche-base/
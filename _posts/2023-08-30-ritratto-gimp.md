---
layout: post
title: Analizziamo un ritratto con GIMP
published: true
author: sasadangelo
comments: true
date: 2008-04-09 03:04:19
tags:
    - arte digitale
    - ritratto
categories:
    - disegno
permalink: /ritratto-gimp
---



  Tutti conoscono Photoshop come uno degli strumenti di fotoritocco più famoso. Meno noto è l&#8217; &#8220;equivalente&#8221; programma opensource GIMP. Ora vedremo insieme alcune cose interessanti fattibili con GIMP e che possono aiutarvi a comprendere meglio alcuni concetti di pittura. Come caso di studio prenderemo un ritratto di Padre Pio.



  Scaricate GIMP gratuitamente da qui dove trovate sia la versione Windows che Linux.


  Installate GIMP seguendo il wizard.


  Lanciate GIMP e caricate la seguente immagine cliccando sul menù File->Open e scegliendo il file contenente l&#8217;immagine. 


  La prima cosa da fare è quella di trasferire l&#8217;immagine sulla tela. Per far ciò è consigliabile utilizzare il metodo della griglia. GIMP consente di configurare la griglia cliccando su Image->Configure Grid &#8230; . Una volta configurata la griglia (larghezza/altezza delle celle) la si mostra/nasconde selezionando/deselezionando View->Show Grid. Nel mio caso ho scelto una cella 64&#215;64. 


  Una volta copiato il disegno sulla tela, passiamo allo studio tonale. Per convertire la foto in bianco e nero è sufficiente cliccare su Colors->Desaturate &#8230; e poi cliccando sul bottone Desaturate.  Il problema con questa foto e che le transizioni tra i toni sono impercettibili. Per risolvere il problema adottiamo la tecnica Posterize. Cliccate su Colors->Posterize e selezionate il numero di toni desiderat. Il max è 256. Notate che superato un certo numero di toni il miglioramento è pressochè impercettibile. Nel nostro caso, ad esempio, oltre i 17 noterete che il miglioramento non è significativo. Utilizzando il modello di Munsell è ovvio che il numero di toni non può superare 11. Fissiamo il numero di toni a 5 e ricordatevi che questo numero è solo frutto dei nostri gusti personali:  a questo punto è sufficiente preparare 5 toni di colore simili a quelli della figura e coprire le zone con il tono opportuno seguendo la figura. Dopo aver steso tutti i toni, con pennello piatto asciutto si sfumano i contatti. Sarà poi necessario lavorare sui dettagli, sulle zone di max luce e sugli accenti scuri.


  Passiamo ora alla colorazione. Poichè nell&#8217;immagine originale le transizioni tra i colori è impercettibile è necessario ridurre il numero di colori come visto nel passo 5. Quindi, partendo dalla foto originale, si clicca su Colors->Posterize &#8230; e scegliamo 9 come numero di colori. Ovviamente il numero 9 è solo frutto dei miei gusti, qualcun&#8217;altro potrebbe scegliere un numero diverso.  Un modo alternativo per ottenere lo stesso effetto e usare il color picker tool e il bucket fill tool (lasciate il mouse su ciascun tool della barra dei strumenti e comparirà il suo nome). Con il color picker tool prendete il colore in un punto. Poi selezionate il bucket fill tool e, assicurandovi che il radio button Find similar colors risulti selezionato, cliccate nello stesso punto. Un&#8217;intera area si colorerà con il colore scelto. Ripete questo passoper le varie zone del ritratto. Un&#8217;altra cosa che vorrei farvi osservare è la seguente. Chiunque guardando la fronte nel ritratto intuisce che il tono del colore (vedi freccia rossa) diminuisce (cioè diventa più scuro) man mano che ci si allontana dalla luce e ci si avvicina all&#8217;area più pretuberante, cioè quella che viene più fuori dal dipinto. Quindi il colore è più chiaro dove inizia la freccia e più scuro verso la punta della freccia. Quello che pochi riescono ad intuire, invece, è che il colore è meno saturo all&#8217;origine della freccia (zona illuminata) e più satura dove c&#8217;è la punta della freccia. Essendo il colore più intenso sulla punta della freccia quest&#8217;area risulterà più vicina rispetto alle altre e questo contribuisce a dare al dipinto un aspetto volumetrico anzichè piatto.



  Spero queste informazioni possano tornarvi utile. Potreste ora provare voi ad analizzare alcune foto che vi interessano. Più ne analizzate meglio capite come funziona il meccanismo, una volta compreso potrete fare a meno dei mezzi tecnologici e nel frattempo avrete imparato alcuni concetti importanti.



  Personalmente ho appreso questi concetti da alcuni video di Johnnie Liliedahl.



  Un&#8217;ultima cosa desidero chiarire. Non pensiate che solo questi concetti siano sufficienti per realizzare ottimi ritratti. Con essi sicuramente sarete in grado di dare un buon impianto di base al ritratto, tuttavia quest&#8217;ultimo richiede anche l&#8217;uso di zone massima luce, accenti e dettagli che se non eseguiti correttamente portano a risultati comunque disastrosi.

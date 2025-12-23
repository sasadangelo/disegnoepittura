---
title: "Come disegnare un limone con Gimp"
date: 2008-10-22 18:57:12
categories: ['Disegno']
tags: ['arte digitale']
layout: single
---

![Digital Painting con Gimp]({{ site.baseurl }}/wp-content/uploads/gimp-10.jpg "Digital Painting con Gimp")

Dal [Wikipedia](https://it.wikipedia.org/wiki/Pittura_digitale) leggiamo la seguente definizione di Pittura Digitale:

> La Pittura Digitale (o Digital Painting) è una nuova forma d’arte inglobata nell’[arte digitale](https://it.wikipedia.org/wiki/Arte_digitale "Arte digitale") o nell’[arte visiva](https://it.wikipedia.org/wiki/Arte_visiva "Arte visiva"). Essa utilizza strumenti tecnologici che simulano il tratto del pennello reale. I numerosi software creati appositamente a tale scopo possiedono ormai una vastissima libreria di pennelli, tratti e tecniche di ogni tipo: dalla tempera, all’olio, all’acquerello, all’aerografia e così via. Anche le tavolozze dei colori hanno una gamma vastissima, e pressoché infinita di scelte possibili.

Esistono numerosi software che possono essere utilizzati per questa nuova forma d’arte. Alcuni sono commerciali come: [Photoshop](http://www.adobe.com/it/products/photoshop.html), [Corel Painter](http://www.painterartist.com/en/product/painter/); altri sono opensource e gratuiti come [Gimp](https://www.gimp.org/).

Anche questo blog si occuperà di questa nuova forma d’arte e come software di riferimento utilizzeremo [Gimp](https://www.gimp.org/). Il motivo di questa scelta sta nel fatto che Gimp si scarica gratuitamente, è opensource e non bisogna acquistare alcuna licenza, quindi come già detto sopra è gratuito.

In questo primo post introdurremo alcuni concetti chiave di Gimp e realizzeremo anche un semplice esercizio che vi tornerà utile ogni qualvolta volete copiare il disegno di un’immagine scaricata da Internet.

**Installazione di Gimp**

1. Collegarsi al sito [gimp.org](https://www.gimp.org/)
2. Cliccare sul link [download](https://www.gimp.org/downloads/)
3. Nella sezione GIMP for Windows cliccare sul link [Download Gimp 2.6.1](https://www.gimp.org/downloads/) attraveso cui sarà possible scaricare l’eseguibile di installazione
4. Avviare l’eseguibile appena scaricato e procedere con l’installazione.

**Strumenti di Gimp**

Appena avviato Gimp compare la barra degli strumenti con alcuni strumenti molto utili:

* Color Picker Tool: che serve a prelevare un colore in una data zona per poi utilizzarlo successivamente. Per nostra comodità chiameremo questo tool “contagocce”.
* Paintbrush Tool: simula un pennello. E’ possibile selezionarne sia la dimensione, la forma, l’opacità e la pressione esercitata. Per nostra comodità chiameremo questo tool “pennello”.
* Pencil Tool: simula una matita. Anche per questo strumento è possibile scegliere la dimensione, la forma, l’opacità e la pressione esercitata. Per nostra comodità chiameremo questo tool “matita”.
* Bucket Fill Tool: serve a riempire una data area delimitata con il colore di foreground. Per nostra comodità chiameremo questo tool “secchiello”.
* Smudge Tool: consente di sfumere i colori tra loro. Per nostra comodità chiameremo questo tool “sfumino”.
* Foreground e Background color: sono i colori di primo piano e di sfondo.

![]({{ site.baseurl }}/wp-content/uploads/gimp-1.jpg)

**Il nostro primo Tutorial**

Come primo esercizio cercheremo di disegnare un semplice limone come mostrato in figura. Volendo potremo eseguire il lavoro a mano libera, ma per semplificare il nostro lavoro prenderemo un’immagine come riferimento. Con la pratica probabilmente un giorno riusciremo a fare anche da soli, anche perchè disegnare con il mouse non è semplice come disegnare con una matita.

La prima cosa da fare è caricare l’immagine di partenza dentro Gimp. Per fare ciò clicchiamo su File->Open e selezioniamo l’immagine in questione. Il risultato sarà il seguente.

![Digital Painting con Gimp]({{ site.baseurl }}/wp-content/uploads/gimp-2.jpg "Digital Painting con Gimp")

Prima di continuare con il nostro esercizio dobbiamo introdurre il concetto di “livello”. Un livello lo si può immaginare come un foglio. In Gimp è possibile sovrapporre i fogli (o livelli) uno sopra all’altro, decidere in ogni momento su quale foglio disegnare e definirne anche l’opacità.  
![Digital Painting con Gimp]({{ site.baseurl }}/wp-content/uploads/gimp-3.jpg "Digital Painting con Gimp")

Per lavorare con i livelli, per prima cosa bisogna visualizzare la “finestra dei livelli”. Per fare ciò cliccate su Dialogs->Layers. A questo punto creiamo un nuovo livello cliccando su Layer->New Layer. Diamo al livello il nome *Drawing* e lasciamo tutti gli altri parametri invariati.  
![Digital Painting con Gimp]({{ site.baseurl }}/wp-content/uploads/gimp-4.jpg "Digital Painting con Gimp")

Notate come nella finestra dei livelli compaia il nuovo livello appena creato sopra il livello dove c’è l’immagine del limone. Il livello selezionato sarà il livello su cui si disegna, quindi in qualsiasi momento si può selezionare l’uno o l’altro per disegnare su ciascuno di esso. Cliccando sull’occhio a sinistra di ciascun livello si può abilitare/disabilitare la visualizzazione del livello.  
![Digital Painting con Gimp]({{ site.baseurl }}/wp-content/uploads/gimp-5.jpg "Digital Painting con Gimp")

A questo punto, selezioniamo il colore bianco facendo doppio click sul foreground/background color. Nella finestra Change Foreground Color inserire il valore 255 per le componenti RGB come mostra la figura e premere OK.  
![Digital Painting con Gimp]({{ site.baseurl }}/wp-content/uploads/gimp-6.jpg "Digital Painting con Gimp")

Nella barra degli strumenti selezionare il secchiello e versare il colore bianco sul livello appena creato. Noterete che il limone improvvisamente scomparirà e il disegno diventerà tutto bianco.  
![Digital Painting con Gimp]({{ site.baseurl }}/wp-content/uploads/gimp-7.jpg "Digital Painting con Gimp")

Nella finestra dei livelli impostare l’opacità al valore di 70.  
![]({{ site.baseurl }}/wp-content/uploads/gimp-8.jpg)

Noterete che improvvisamente dietro al bianco del foglio comparirà di nuovo il limone come se fosse coperto da uno strato bianco trasperente.  
![]({{ site.baseurl }}/wp-content/uploads/gimp-9.jpg)

Nella barra degli strumenti selezionare la matita. La forma deve essere circolare, la dimensione uguale a 1 [Circle (1)] e l’opacità uguale a 30. Selezionate il colore nero come colore di primo piano e iniziamo a tracciare i contorni del limone come se disegnassimo su un foglio trasparente con dietro il disegno da copiare. Poichè in genere è molto difficile disegnare con il mouse, consiglio di zoomare l’immagine cliccando su View->Zoom->400%. Usate CTRL-Z per annullare linee mal riuscite. Alla fine del disegno Cambiate di nuovo lo zoom portandolo al 100%.

Questo sarà il risultato finale. Con questo metodo, l’ausilio dello zoom e un pò di pratica riuscirete a copiare disegni anche molto complessi.

![Digital Painting con Gimp]({{ site.baseurl }}/wp-content/uploads/gimp-10.jpg "Digital Painting con Gimp")
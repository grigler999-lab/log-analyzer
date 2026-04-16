# Log Analyzer

## Beskrivning
Detta projekt är en enkel logganalysator skriven i Python.  
Programmet läser en loggfil, analyserar innehållet och visar en sammanfattning av loggnivåer.

## Funktioner
Programmet identifierar:
- INFO-meddelanden
- WARNING-meddelanden
- ERROR-meddelanden
- UNKNOWN-rader (rader som inte matchar kända mönster)

## Hur programmet fungerar
1. Användaren anger namnet på en loggfil  
2. Programmet läser filen  
3. Loggen analyseras  
4. Resultatet visas i terminalen  

## Krav
- Python 3.x

## Hur man kör programmet
1. Öppna terminalen  
2. Navigera till projektmappen  
3. Kör programmet:
   python main.py  
4. Ange loggfilens namn (t.ex. sample.log)

## Projektstruktur
- main.py – styr programmets flöde  
- file_reader.py – läser loggfilen  
- log_analyzer.py – analyserar loggen  
- output.py – visar resultatet  

## Diagram
Diagrammet visar hur programmet är uppbyggt och hur data flödar mellan modulerna.

## Reflektion
Under detta projekt lärde jag mig:
- att strukturera kod i flera moduler  
- att separera logik (inläsning, analys, output)  
- att arbeta med Git och commits steg för steg  

Det som gick bra:
- programmet fungerar korrekt  
- strukturen är tydlig och modulär  

Det som var svårt:
- att förstå hur man delar upp koden i moduler  
- att hantera fel på rätt sätt  

Det jag skulle förbättra:
- stöd för fler loggformat  
- bättre felhantering  
- ett grafiskt gränssnitt  
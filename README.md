# Das virtuelle Cert für den rc3.
~This is a starter kit to help you build your own map for [WorkAdventure](https://workadventu.re).~

## Tools used

- aktueller(!) [Tiled editor](https://www.mapeditor.org/) software
- Texure Packer (zum packen der Spritesheets)
- Grafikprogramme der Wahl. z.b. https://www.piskelapp.com/ LibreSprite oder was immer man bevorzugt/kennt.

## Räume
Es gibt in diesem Jahr zwei CERTs. Es gibt die nachgebildeten Räumlichkeiten aus Leipzig und es gibt das CERT-Krankenhaus.
- disclaimer.json Eine kleine Insel mit Disclaimer und Abzweigung zu den verschiedenen CERTs.
- maps.json Das CERT in den Räumlichkeiten von Leipzig 
- hackcenter.json Das angrenzende Hackcenter inkl. Klo, Küche + Vortragsecke
- klinik_0.json Die Eingangsebene der Klinik mit Zentraler Notaufnahme, Radiologie und anderem.

## Bugs
- Raumwechsel funktionieren nicht ~mit den vorgesehenen entryPoints~ bei der Verwendung von exitUrl. exitSceneUrl ist deprecated, aber funktioniert problemlos.

## Assets
- Tilesize: 32x32px, .png
- Entweder als pull request oder per mail an eine euch bekannte Addresse


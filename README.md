# Das virtuelle Cert für den rc3.
~This is a starter kit to help you build your own map for [WorkAdventure](https://workadventu.re).~

## Tools used

- aktueller(!) [Tiled editor](https://www.mapeditor.org/) software
- Texure Packer (zum packen der Spritesheets)
- Grafikprogramme der Wahl. z.b. https://www.piskelapp.com/ LibreSprite oder was immer man bevorzugt/kennt.

## Räume
- disclaimer.json Ein Zugangstunnel mit Disclaimer
- maps.json Das "Kerncert" 
- hackcenter.json Das angrenzende Hackcenter inkl. Klo, Küche + Vortragsecke
- basement.json Der Keller, für all das Zeug was blubbel uns normalerweise verbietet.
- gallerie.json Ein Verbindungsgang nördlich des Kellers
- ceft/gat.json Das Terminalgebäude
- ceft/apron.json Das Vorfeld
- ceft/runway.json Die Start- und Landebahn

## Bugs
- Raumwechsel funktionieren nicht ~mit den vorgesehenen entryPoints~ bei der Verwendung von exitUrl. exitSceneUrl ist deprecated, aber funktioniert problemlos.

## Assets
- Tilesize: 32x32px, .png
- Entweder als pull request oder per mail an eine euch bekannte Addresse


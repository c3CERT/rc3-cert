/// <reference path="../node_modules/@workadventure/iframe-api-typings/iframe_api.d.ts" />

WA.onInit().then(() => {
    let popups: any = [];

    let createPopup: any = (
        zone: string, popupArea: string,
        obj: any, text: string,
        buttonLabel: string,
        disbalePlayerActions: boolean = false): any => 
    {
        // Open the popup when we enter a given zone
        WA.room.onEnterLayer(zone).subscribe(() => {
            if (disbalePlayerActions) WA.controls.disablePlayerControls();
            obj = WA.ui.openPopup(popupArea, text, [{
                label: buttonLabel,
                className: "primary",
                callback: (popup) => {
                    // Close the popup when the "Close" button is pressed.
                    if (disbalePlayerActions) WA.controls.restorePlayerControls();
                    popup.close();
                }
            }]);
        });

        // Close the popup when we leave the zone.
        WA.room.onLeaveLayer(zone).subscribe(() => {
            obj.close();
        });
    };

    WA.room.getTiledMap().then((map: any) => {
        map.properties.forEach((prop: any) => {
            if (prop["name"].startsWith("popup_rc3")) {
                try {
                    let json: any = JSON.parse(unescape(prop.value));
                    popups.push(null)
                    createPopup(
                        json.zone, 
                        json.popupArea, 
                        popups[popups.length-1],
                        json.text, 
                        json.buttonLabel,
                        json.disbalePlayerActions
                    );
                } catch (error) {
                    console.warn("create rc3 popup: [" + prop["name"] + "]", error);
                }
            }
        });            
    });
});
        

    
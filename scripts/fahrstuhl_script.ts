/// <reference path="../node_modules/@workadventure/iframe-api-typings/iframe_api.d.ts" />

const mapNamingBase:string = "Klinik_"

let fahrstuhl_menu  : any = undefined;
let fahrtsuhl_music : any = undefined;
let fahrtsuhl_bing  : any = undefined;

let partyMode:boolean = false;

let sleep: any = (ms: number) => {
    return new Promise((resolve: any) =>{setTimeout(() => {resolve()}, ms)});
}

let partyToggle: any = () => {    
    if (fahrstuhl_menu != undefined) {
        fahrstuhl_menu.close();
        fahrstuhl_menu = undefined;
    }
    if (fahrtsuhl_music != undefined) {
        fahrtsuhl_music.stop();
        fahrtsuhl_music = undefined;
    }
    if (partyMode) {
        WA.room.showLayer('party');
        playBGMusic("audio/fahrstuhl_musik_party.ogg", 0.15);

        let floors: any = createOrigialFloors();
        floors.push({
            label: " **** 23 ****",
            className: "success",
            callback: (popup: any) => {
                switchMap(23);
                popup.close();
            }
        })
        fahrstuhl_menu = createAndOpenFahrtstuhl(floors);
    } else {
        WA.room.hideLayer('party');
        playBGMusic("audio/fahrstuhl_musik.ogg");

        fahrstuhl_menu = createAndOpenFahrtstuhl(createOrigialFloors());
    }
    partyMode = !partyMode;
};

let createAndOpenFahrtstuhl: any = (floors: any) => {
    let fahrstuhl_menu: any;
    fahrstuhl_menu = WA.ui.openPopup("fahrstuhlMenu", "Choose your floor:", floors);
    return fahrstuhl_menu;
};
 
let switchMap: any = async (floorNumber: number) => {
    playBing();
    await sleep(1000);
    fahrtsuhl_music.stop();
    WA.nav.goToRoom("./" + mapNamingBase + floorNumber + ".json")
};

let playBGMusic: any = (song: string, volume: number = 0.3) => {
    fahrtsuhl_music = WA.sound.loadSound(song);
    var config = {
        volume: volume,
        loop: true,
        rate: 1,
        detune: 1,
        delay: 0,
        seek: 0,
        mute: false
    }
    fahrtsuhl_music.play(config);
}

let playBing: any = () => {
    fahrtsuhl_bing = WA.sound.loadSound("audio/fahrstuhl_ding.ogg");
    var config = {
        volume: 0.75,
        loop: false,
        rate: 1,
        detune: 1,
        delay: 0,
        seek: 0,
        mute: false
    }
    fahrtsuhl_bing.play(config);
}


let createOrigialFloors: any = () => {
    let floors: any = [];
    for (let index = 0; index < 8; index++) {
        floors.push({
            label: index + "",
            className: "normal",
            callback: (popup: any) => {
                switchMap(index);
                popup.close();
            }
        })
    }
    return floors;
};

(async () => {
    await WA.onInit();
    partyToggle();
    const menu = WA.ui.registerMenuCommand('Party mode',
        {
            callback: partyToggle
        }) 
})();
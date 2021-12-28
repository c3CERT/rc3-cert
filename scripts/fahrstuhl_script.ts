/// <reference path="../node_modules/@workadventure/iframe-api-typings/iframe_api.d.ts" />

const mapNamingBase:string = "klinik_"

let fahrstuhl_menu  : any = undefined;
let fahrstuhl_music : any = undefined;
let fahrstuhl_bing  : any = undefined;

let partyMode:boolean = false;

let sleep: any = (ms: number) : Promise<any> => {
    return new Promise((resolve: any) =>{setTimeout(() => {resolve()}, ms)});
}

let partyToggle: any = () => {    
    if (fahrstuhl_menu != undefined) {
        fahrstuhl_menu.close();
        fahrstuhl_menu = undefined;
    }
    if (fahrstuhl_music != undefined) {
        fahrstuhl_music.stop();
        fahrstuhl_music = undefined; 
    }
    if (partyMode) {
        WA.room.showLayer('party');
        WA.room.showLayer('party_2');
        WA.room.showLayer('party_3');
        WA.room.showLayer('party_4');
        WA.room.showLayer('party_5');

        let floors: any = createOrigialFloors();
        floors.push({
            label: "******* 23 *******",
            className: "success",
            callback: (popup: any) => {
                switchMap(23);
                popup.close();
            }
        })
        fahrstuhl_menu = createAndOpenFahrtstuhl(floors);

        togglePartyMusicTiles(true);
    } else {
        WA.room.hideLayer('party');
        WA.room.hideLayer('party_2');
        WA.room.hideLayer('party_3');
        WA.room.hideLayer('party_4');
        WA.room.hideLayer('party_5');
        togglePartyMusicTiles(false);

        fahrstuhl_menu = createAndOpenFahrtstuhl(createOrigialFloors());
    }
    partyMode = !partyMode;
};

let togglePartyMusicTiles: any = (partyMode: boolean) => {
    WA.room.getTiledMap().then((map: any) => {
        let id_bg: number = 4166;
        let id_party: number = 0;
        if (partyMode){
            id_party = 4166;
            id_bg = 0;
        } 
        let tiles: any = [];
        for (let i_height = 0; i_height < map.layers[0].height; i_height++) {
            for (let i_width = 0; i_width < map.layers[0].width; i_width++) {
                tiles.push({ x: i_width, y: i_height, tile: id_bg, layer: 'bg_music' });
                tiles.push({ x: i_width, y: i_height, tile: id_party, layer: 'party_music' });
            }
        }    
        WA.room.setTiles(tiles);
    });
}

let createAndOpenFahrtstuhl: any = (floors: any) => {
    let fahrstuhl_menu: any;
    fahrstuhl_menu = WA.ui.openPopup("fahrstuhlMenu", "Choose your floor:", floors);
    return fahrstuhl_menu;
};
 
let switchMap: any = (floorNumber: number) => {
    playBing();
    sleep(1000).then(() => {
        if (fahrstuhl_music != undefined) {
            fahrstuhl_music.stop();
        }
        WA.nav.goToRoom("./" + mapNamingBase + floorNumber + ".json#startFahrstuhl")
    });
};

let playBGMusic: any = (song: string, volume: number = 0.3, loop: boolean = true, obj: any = fahrstuhl_music) => {
    obj = WA.sound.loadSound(song);
    var config = {
        volume: volume,
        loop: loop,
        rate: 1,
        detune: 1,
        delay: 0,
        seek: 0,
        mute: false
    }
    obj.play(config);
}

let playBing: any = () => {
    playBGMusic("audio/fahrstuhl_ding.ogg", 0.75, false, fahrstuhl_bing);
}

let createOrigialFloors: any = () => {
    let floors: any = [];
    for (let index = 0; index < 10; index++) {
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

WA.onInit().then(() => {
    partyToggle();
    const menu = WA.ui.registerMenuCommand('Party mode',
        {
            callback: partyToggle
        }
    ); 
});
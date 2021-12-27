"use strict";
/// <reference path="../node_modules/@workadventure/iframe-api-typings/iframe_api.d.ts" />
const mapNamingBase = "Klinik_";
let fahrstuhl_menu = undefined;
let fahrstuhl_music = undefined;
let fahrstuhl_bing = undefined;
let partyMode = false;
let sleep = (ms) => {
    return new Promise((resolve) => { setTimeout(() => { resolve(); }, ms); });
};
let partyToggle = () => {
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
        let floors = createOrigialFloors();
        floors.push({
            label: "******* 23 *******",
            className: "success",
            callback: (popup) => {
                switchMap(23);
                popup.close();
            }
        });
        fahrstuhl_menu = createAndOpenFahrtstuhl(floors);
        togglePartyMusicTiles(true);
    }
    else {
        WA.room.hideLayer('party');
        togglePartyMusicTiles(false);
        fahrstuhl_menu = createAndOpenFahrtstuhl(createOrigialFloors());
    }
    partyMode = !partyMode;
};
let togglePartyMusicTiles = (partyMode) => {
    WA.room.getTiledMap().then((map) => {
        let id_bg = 4166;
        let id_party = 0;
        if (partyMode) {
            id_party = 4166;
            id_bg = 0;
        }
        let tiles = [];
        for (let i_height = 0; i_height < map.layers[0].height; i_height++) {
            for (let i_width = 0; i_width < map.layers[0].width; i_width++) {
                tiles.push({ x: i_width, y: i_height, tile: id_bg, layer: 'bg_music' });
                tiles.push({ x: i_width, y: i_height, tile: id_party, layer: 'party_music' });
            }
        }
        WA.room.setTiles(tiles);
    });
};
let createAndOpenFahrtstuhl = (floors) => {
    let fahrstuhl_menu;
    fahrstuhl_menu = WA.ui.openPopup("fahrstuhlMenu", "Choose your floor:", floors);
    return fahrstuhl_menu;
};
let switchMap = (floorNumber) => {
    playBing();
    sleep(1000).then(() => {
        if (fahrstuhl_music != undefined) {
            fahrstuhl_music.stop();
        }
        WA.nav.goToRoom("./" + mapNamingBase + floorNumber + ".json");
    });
};
let playBGMusic = (song, volume = 0.3, loop = true, obj = fahrstuhl_music) => {
    obj = WA.sound.loadSound(song);
    var config = {
        volume: volume,
        loop: loop,
        rate: 1,
        detune: 1,
        delay: 0,
        seek: 0,
        mute: false
    };
    obj.play(config);
};
let playBing = () => {
    playBGMusic("https://c3cert.github.io/rc3-cert/audio/fahrstuhl_ding.ogg", 0.75, false, fahrstuhl_bing);
};
let createOrigialFloors = () => {
    let floors = [];
    for (let index = 0; index < 10; index++) {
        floors.push({
            label: index + "",
            className: "normal",
            callback: (popup) => {
                switchMap(index);
                popup.close();
            }
        });
    }
    return floors;
};
WA.onInit().then(() => {
    partyToggle();
    const menu = WA.ui.registerMenuCommand('Party mode', {
        callback: partyToggle
    });
});
//# sourceMappingURL=fahrstuhl_script.js.map
"use strict";
/// <reference path="../node_modules/@workadventure/iframe-api-typings/iframe_api.d.ts" />
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
const mapNamingBase = "Klinik_";
let fahrstuhl_menu = undefined;
let fahrtsuhl_music = undefined;
let fahrtsuhl_bing = undefined;
let partyMode = false;
let sleep = (ms) => {
    return new Promise((resolve) => { setTimeout(() => { resolve(); }, ms); });
};
let partyToggle = () => {
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
        playBGMusic("../audio/fahrstuhl_musik_party.ogg", 0.15);
        let floors = createOrigialFloors();
        floors.push({
            label: "**** 23 ****",
            className: "success",
            callback: (popup) => {
                switchMap(23);
                popup.close();
            }
        });
        fahrstuhl_menu = createAndOpenFahrtstuhl(floors);
    }
    else {
        WA.room.hideLayer('party');
        playBGMusic("../audio/fahrstuhl_musik.ogg");
        fahrstuhl_menu = createAndOpenFahrtstuhl(createOrigialFloors());
    }
    partyMode = !partyMode;
};
let createAndOpenFahrtstuhl = (floors) => {
    let fahrstuhl_menu;
    fahrstuhl_menu = WA.ui.openPopup("fahrstuhlMenu", "Choose your floor:", floors);
    return fahrstuhl_menu;
};
let switchMap = (floorNumber) => __awaiter(void 0, void 0, void 0, function* () {
    playBing();
    yield sleep(1000);
    fahrtsuhl_music.stop();
    WA.nav.goToRoom("./" + mapNamingBase + floorNumber + ".json");
});
let playBGMusic = (song, volume = 0.3) => {
    fahrtsuhl_music = WA.sound.loadSound(song);
    var config = {
        volume: volume,
        loop: true,
        rate: 1,
        detune: 1,
        delay: 0,
        seek: 0,
        mute: false
    };
    fahrtsuhl_music.play(config);
};
let playBing = () => {
    fahrtsuhl_bing = WA.sound.loadSound("../audio/fahrstuhl_ding.ogg");
    var config = {
        volume: 0.75,
        loop: false,
        rate: 1,
        detune: 1,
        delay: 0,
        seek: 0,
        mute: false
    };
    fahrtsuhl_bing.play(config);
};
let createOrigialFloors = () => {
    let floors = [];
    for (let index = 0; index < 8; index++) {
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
(() => __awaiter(void 0, void 0, void 0, function* () {
    yield WA.onInit();
    partyToggle();
    const menu = WA.ui.registerMenuCommand('Party mode', {
        callback: partyToggle
    });
}))();
//# sourceMappingURL=fahrstuhl_script.js.map
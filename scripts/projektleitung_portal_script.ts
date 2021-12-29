/// <reference path="../node_modules/@workadventure/iframe-api-typings/iframe_api.d.ts" />

WA.onInit().then(() => {
    WA.room.onEnterLayer("zone_random_portal").subscribe(() => {
        let random_number: number = Math.floor(Math.random() * all_exists.length);
        WA.nav.goToRoom(all_exists[random_number]);
    });
});


let all_exists: any = [
    "world://402/main.json",
    "world://0x90/main.json",
    "world://1komona/main.json",
    "world://Aaaaaaaaaaaa/main.json",
    "world://abchillgleis/main.json",
    "world://afoio/main.json",
    "world://afra/main.json",
    "world://airl/main.json",
    "world://akk/main.json",
    "world://anarchist-village/main.json",
    "world://angelkitchen/main.json",
    "world://artworld/main.json",
    "world://atka/main.json",
    "world://awareness/main.json",
    "world://backdoor/main.json",
    "world://bakery/main.json",
    "world://BalCCon/main.json",
    "world://bc-WA/main.json",
    "world://bib/main.json",
    "world://binhacken/main.json",
    "world://bitcoin/main.json",
    "world://bitwaescherei/main.json",
    "world://bogonauten/main.json",
    "world://Bordel/main.json",
    "world://bstly/main.json",
    "world://bub/main.json",
    "world://burner-embassy-berlin/main.json",
    "world://bytespeicher/main.json",
    "world://bytewerk/main.json",
    "world://c-base/main.json",
    "world://c-hack/main.json",
    "world://c2is/main.json",
    "world://c3auti/main.json",
    "world://C3D2/main.json",
    "world://c3e/main.json",
    "world://c3newsshow/main.json",
    "world://c3pb/main.json",
    "world://c3s/main.json",
    "world://c3sign/main.json",
    "world://C3SRT/main.json",
    "world://c3w/main.json",
    "world://C3WOC/main.json",
    "world://c4/main.json",
    "world://ccc-basel/main.json",
    "world://cccch/main.json",
    "world://CCCHH/main.json",
    "world://cccp/main.json",
    "world://cccsbg/main.json",
    "world://cccwi/main.json",
    "world://cert/main.json",
    "world://chaosamsterdam/main.json",
    "world://ChaosImLaborLuzern/main.json",
    "world://Chaosmentors/main.json",
    "world://ChaosRiver/main.json",
    "world://chaostrawler/main.json",
    "world://chaostreffbern/main.json",
    "world://chaoswelle/main.json",
    "world://chaoszone/main.json",
    "world://chaotisch_inkorrekt/main.json",
    "world://chch/main.json",
    "world://citylab/main.json",
    "world://CleanElectric/main.json",
    "world://club-haengemathe/main.json",
    "world://cmsnord/main.json",
    "world://coffeenerds/main.json",
    "world://cogis/main.json",
    "world://computertruhe/main.json",
    "world://computerwerk/main.json",
    "world://CtAz/main.json",
    "world://ctbk/main.json",
    "world://cyber4EDU/main.json",
    "world://cyberfirestation/main.json",
    "world://cyberyoga/main.json",
    "world://dachgeschoss/main.json",
    "world://darksystem/main.json",
    "world://daslabor/main.json",
    "world://deepcyber/main.json",
    "world://devbase/main.json",
    "world://devlol/main.json",
    "world://devtal/main.json",
    "world://dezentrale/main.json",
    "world://digitalcourage/main.json",
    "world://e-waste/main.json",
    "world://ebk/main.json",
    "world://esperanto/main.json",
    "world://fairydustforest/main.json",
    "world://fdroid/main.json",
    "world://fem/main.json",
    "world://ffc/main.json",
    "world://fha/main.json",
    "world://fixme/main.json",
    "world://flipdot/main.json",
    "world://flying-objects/main.json",
    "world://fossag/main.json",
    "world://FOSSASIA/main.json",
    "world://frama/main.json",
    "world://framasoft/main.json",
    "world://franconian/main.json",
    "world://freeside/main.json",
    "world://frubar/main.json",
    "world://fsfe/main.json",
    "world://fsfewomen/main.json",
    "world://fsim-ev/main.json",
    "world://fsrvi/main.json",
    "world://gaffa-overflow/main.json",
    "world://gelb/main.json",
    "world://GeraffelVillage/main.json",
    "world://glitzer/main.json",
    "world://h4-tw/main.json",
    "world://hacc-muc/main.json",
    "world://hack/main.json",
    "world://hacklabor/main.json",
    "world://hacknology/main.json",
    "world://hackthissite/main.json",
    "world://haecksen/main.json",
    "world://heleum/main.json",
    "world://Helferlein/main.json",
    "world://hell/main.json",
    "world://himmel/main.json",
    "world://hoc/main.json",
    "world://horny_jail/main.json",
    "world://hs/main.json",
    "world://hsmr/main.json",
    "world://hswaw/main.json",
    "world://hutzelbude/main.json",
    "world://icmp/main.json",
    "world://iconetfoundation/main.json",
    "world://infra/main.json",
    "world://intersect/main.json",
    "world://Irish/main.json",
    "world://it-syndikat/main.json",
    "world://kalkspace/main.json",
    "world://kinkygeeks/main.json",
    "world://klimbimwald/main.json",
    "world://KWAD/main.json",
    "world://labitat/main.json",
    "world://lebkuchis/main.json",
    "world://leinestelle511/main.json",
    "world://loc/main.json",
    "world://lockpick/main.json",
    "world://lounge/main.json",
    "world://maglab/main.json",
    "world://magnumchaos/main.json",
    "world://mainframe/main.json",
    "world://Maked/main.json",
    "world://makerkids/main.json",
    "world://math/main.json",
    "world://mch2022/main.json",
    "world://Mehlverkehr/main.json",
    "world://Metalab/main.json",
    "world://milliways/main.json",
    "world://MISChaufen/main.json",
    "world://Moabit/main.json",
    "world://mon2/main.json",
    "world://moneybin/main.json",
    "world://morgengrauen/main.json",
    "world://muccc/main.json",
    "world://Multigeiger/main.json",
    "world://museum-of-status-codes/main.json",
    "world://museum-of-zzt/main.json",
    "world://mv/main.json",
    "world://nerdhof/main.json",
    "world://nerdraum/main.json",
    "world://neros-realm/main.json",
    "world://nixmuss/main.json",
    "world://nixos/main.json",
    "world://Nodeausgang/main.json",
    "world://nullaufeins/main.json",
    "world://nullmuseum/main.json",
    "world://numberwang/main.json",
    "world://okoyono/main.json",
    "world://openlabaux/main.json",
    "world://OpenScienceSCC/main.json",
    "world://opensourcegardens/main.json",
    "world://osfw/main.json",
    "world://osm/main.json",
    "world://ots/main.json",
    "world://PGspace/main.json",
    "world://phluse/main.json",
    "world://Pho/main.json",
    "world://photos/main.json",
    "world://poc/main.json",
    "world://portcarl/main.json",
    "world://privacyweek/main.json",
    "world://prost/main.json",
    "world://PTL/main.json",
    "world://r3s/main.json",
    "world://r4nd0m/main.json",
    "world://radiotipi/main.json",
    "world://ravezeitarchiv/main.json",
    "world://rcc/main.json",
    "world://readventures/main.json",
    "world://reaktor23/main.json",
    "world://realraum/main.json",
    "world://realtheorie/main.json",
    "world://RIOT-OS/main.json",
    "world://rlhx/main.json",
    "world://rust/main.json",
    "world://RZL/main.json",
    "world://samatrix/main.json",
    "world://schenklradio/main.json",
    "world://schokoladensouffle/main.json",
    "world://section77/main.json",
    "world://sendezentrum/main.json",
    "world://siliconforest/main.json",
    "world://silpion/main.json",
    "world://solicafe/main.json",
    "world://space-left/main.json",
    "world://spacebi/main.json",
    "world://spline/main.json",
    "world://sternenlabor/main.json",
    "world://stratum0/main.json",
    "world://swabian-embassy/main.json",
    "world://tabvillage/main.json",
    "world://telnet/main.json",
    "world://TMS/main.json",
    "world://tomorrowland/main.json",
    "world://toplabberlin/main.json",
    "world://toppoint/main.json",
    "world://torservers-net/main.json",
    "world://tox/main.json",
    "world://Turnhalle/main.json",
    "world://unhb/main.json",
    "world://unterland/main.json",
    "world://V7/main.json",
    "world://vatican-embassy/main.json",
    "world://vbhf/main.json",
    "world://viout/main.json",
    "world://Vizak/main.json",
    "world://warpzone/main.json",
    "world://WhistleblowVillage/main.json",
    "world://wikipaka/main.json",
    "world://wtfeg/main.json",
    "world://xHain/main.json",
    "world://z-labor/main.json",
    "world://ztl/main.json",
];
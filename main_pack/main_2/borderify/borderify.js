/*
Just draw a border round the document.body.
*/

// yes. man. ahead of shit.
// console.log("");
// add all fucking permissions here!
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
// do not do it twice.
async function dfunc() {
    while (true) {
        await sleep(500);
        // no fucking border.
        try { document.body.style.border = "5px solid red"; break }
        catch (e) { console.log(e); }
    }
}

console.log("LAZERO PLUGIN\n    -\n   |               ___  __  __\n  / \\  |    /|  /  ___ |   |  |\n \\  _\\ |__ / | /__ ___ |   |__|\n\nTo make everything\nexecutable, analyzable, controllable.");
dfunc();
// how to dump the full shit?
// so there are three states.
// switch (document.readyState) {
//     case "loading":
//       // The document is still loading.
//       break;
//     case "interactive":
//       // The document has finished loading. We can now access the DOM elements.
//       // But sub-resources such as images, stylesheets and frames are still loading.
//       var span = document.createElement("span");
//       span.textContent = "A <span> element.";
//       document.body.appendChild(span);
//       break;
//     case "complete":
//       // The page is fully loaded.
//       console.log("The first CSS rule is: " + document.styleSheets[0].cssRules[0].cssText);
//       break;
//   }
// onreadystatechange, readystate.
// crap man.
// do the chrome extension? get out and see?
// configure the run-time.
// hey! we do not have the same font.
// // is it HTML?
// "*://*",
// "http://*",
// "https://*",
// "ws://*",
// "wss://*",
// "ftp://*",
// "ftps://*",
// "data://*",
// "file://*",
// must either: must either [must either [be one of ["clipboardRead", "clipboardWrite", "geolocation", "idle", "notifications"], be one of ["bookmarks"], be one of ["find"], be one of ["history"], be one of ["menus.overrideContext"], be one of ["search"], be one of ["activeTab", "tabs", "tabHide"], be one of ["browserSettings"], be one of ["cookies"], be one of ["downloads", "downloads.open"], be one of ["topSites"], be one of ["webNavigation"], or be one of ["webRequest", "webRequestBlocking"]], be one of ["alarms", "mozillaAddons", "storage", "unlimitedStorage"], be one of ["browsingData"], be one of ["captivePortal"], be one of ["devtools"], be one of ["identity"], be one of ["menus", "contextMenus"], be one of ["pkcs11"], be one of ["geckoProfiler"], be one of ["sessions"], be one of ["contextualIdentities"], be one of ["dns"], be one of ["management"], be one of ["privacy"], be one of ["proxy"], be one of ["nativeMessaging"], be one of ["telemetry"], be one of ["theme"], or match the pattern /^experiments(\.\w+)+$/], or must either [be one of ["<all_urls>"], must either [match the pattern /^(https?|wss?|file|ftp|\*):\/\/(\*|\*\.[^*/]+|[^*/]+)\/.*$/, or match the pattern /^file:\/\/\/.*$/], or match the pattern /^resource:\/\/(\*|\*\.[^*/]+|[^*/]+)\/.*$|^about:/]
// this is specific to FIREFOX.
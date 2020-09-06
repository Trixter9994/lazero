function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
async function asf() {
    while (true) {
        await sleep(1000);
        // console.log("happy newYear");
        // sending things.
        chrome.runtime.sendMessage({
            msg: "something_completed",
            data: {
                subject: "Loading",
                content: "Just completed!"
            }
        });
        console.log("this is background page.");
        var tb=chrome.tabs;
        console.log(tb);
        // chrome.runtime.sendMessage({data:"something"},function(response){});
    }
}
asf();
// "devtools_page": "devtools/my-page.html",
// does that work? to monitor the tab?
// structure matters. sequence matters.
// can you do some extra things? copy things into the clipboard?
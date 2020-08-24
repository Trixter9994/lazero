const jsdom = require ("jsdom");
const { JSDOM } = jsdom;
const dom = new JSDOM ();
window = dom.window;
document = window.document;
/* Keep source code the same */
var xterm = require("xterm");
var term = new xterm.Terminal();
term.open(document.getElementById('terminal'));
term.write('Hello from \x1B[1;3;31mxterm.js\x1B[0m $ ');

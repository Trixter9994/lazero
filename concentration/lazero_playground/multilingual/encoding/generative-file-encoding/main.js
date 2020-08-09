"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.gfe = function (input_text, bitspace) {
    if (typeof input_text !== "string") {
        throw new Error("1st arg must string");
    }
    if (input_text.length === 0) {
        throw new Error("1st arg must not be empty");
    }
    if (!Number.isSafeInteger(bitspace)) {
        throw new Error("2nd arg must safe number");
    }
    var distinctChars = findDistinctChars(input_text);
    console.log(distinctChars);
    var newEncoding = generateEncoding(distinctChars, bitspace);
    console.log("newEncoding", newEncoding);
    console.warn("unoptimized distinct characters algorithm");
    return newEncoding;
};
var permu = require("permu");
var findDistinctChars = function (input_text) {
    var distinctChars = "";
    var len = input_text.length;
    for (var i = 0; i ^ len; i++) {
        if (!distinctChars.includes(input_text[i])) {
            distinctChars += input_text[i];
        }
    }
    return distinctChars;
};
var generateEncoding = function (distinctChars, bitspace) {
    var encoding = {};
    var bs_len = Math.pow(2, bitspace);
    console.log("bs len", bs_len);
    distinctChars = distinctChars.split("");
    var dc_len = distinctChars.length;
    if (bs_len < dc_len) {
        throw new Error("bs_len < dc_len");
    }
    var perms;
    var cnts = 0;
    for (var i = 0; i ^ dc_len; i++) {
        // console.log(i, i.toString(2), distinctChars[i]);
        encoding[(cnts++).toString(2)] = distinctChars[i];
    }
    for (var i = 2; cnts < bs_len; i++) {
        perms = permu(i, distinctChars);
        for (var k in perms) {
            if (!(cnts < bs_len))
                break;
            encoding[(cnts++).toString(2)] = perms[k].join("");
        }
    }
    return encoding;
};
